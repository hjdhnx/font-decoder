#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : main.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/10/10

import json
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from ddddocr import DdddOcr
from PIL import Image
import os
import sys
import argparse
import shutil
import time
import requests
import hashlib
import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import warnings
import traceback

# 关闭警告
warnings.filterwarnings("ignore")
requests.packages.urllib3.disable_warnings()

VERSION = '1.0.0 2024 1010'
# 创建一个锁
lock = threading.Lock()


def print_with_lock(message):
    # 获取锁
    with lock:
        print(message)
        # 打印完毕后释放锁，以便其他线程继续打印


def md5(text):
    return hashlib.md5(text.encode(encoding='UTF-8')).hexdigest()


def get_online_font(font_path):
    headers = {
        'user-agent': 'Mozilla/5.0',
    }
    # pathname = str(int(time.time() * (10 ** 7)))
    print_with_lock(f'start download {font_path}')
    r = requests.get(font_path, headers=headers, verify=False)
    font_dir = os.path.join(os.path.dirname(__file__), 'test_font')
    font_path = os.path.join(font_dir, md5(font_path) + '.woff2')
    with open(font_path, 'wb') as f:
        f.write(r.content)
    print_with_lock(f'download success to {font_path}')
    return font_path


def get_single_font(fkey, fvalue, font, svg_path, png_path):
    ret = {fvalue.lower(): {}}
    global ocr
    try:
        # print(f'font dict key:{fkey},value:{fvalue}')
        with lock:
            pen = SVGPathPen(font.getGlyphSet())
            font.getGlyphSet()[fvalue].draw(pen)
            xMin, xMax, yMin, yMax = font['head'].xMin, font['head'].xMax, font['head'].yMin, font['head'].yMax
        height1 = (yMax - yMin)
        width1 = (xMax - xMin)
        r = width1 / 100
        svg1 = f'<svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="{xMin} {yMin} {width1} {height1}"><g transform="matrix(0.6 0 0 -0.6 {xMin + width1 * 0.2} {yMin + yMax - height1 * 0.2})"><path stroke = "black" fill = "black" d="{pen.getCommands()}"/></g></svg>'
        svg_file = os.path.join(svg_path, f'{fvalue}.svg')
        png_file = os.path.join(png_path, f'{fvalue}.png')
        with open(svg_file, 'w+', encoding='utf-8') as f:
            f.write(svg1)
        drawing = svg2rlg(svg_file)
        renderPM.drawToFile(drawing, png_file, fmt='PNG')
        img = Image.open(png_file)
        img.thumbnail((100, int(height1 / r)))
        img.save(png_file, 'png')

        with open(png_file, 'rb') as f:
            text1 = ocr.classification(f.read())
            print_with_lock(f'font dict key:{fkey},value:{fvalue},ocr result:{text1}')
            if text1 != None and text1 != '':
                ret[fvalue.lower()] = {'unicode_hex': hex(int(fkey)), 'int': fkey, 'char': text1[:1]}
        print_with_lock(f'ret:{ret}')
        return ret
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        print_with_lock(f'error happend: {e}')
        return ret


def covert_dict1(ret_dict: dict):
    dict1 = {}
    for key, value in ret_dict.items():
        dict1[str(value['int'])] = value['char']
    return dict1


def covert_dict2(ret_dict: dict):
    dict1 = covert_dict1(ret_dict)
    dict1_keys = dict1.keys()
    from_int = int(min(dict1_keys))
    to_int = int(max(dict1_keys))
    dict2_value = []
    for i in range(from_int, to_int + 1):
        if str(i) in dict1_keys:
            dict2_value.append(dict1[str(i)])
        else:
            dict2_value.append('?')

    return dict2_value


def get_font_dict(font_path, remove_temp=False, max_workers=16):
    if font_path.startswith('http'):
        try:
            font_path = get_online_font(font_path)
        except Exception as e:
            sys.exit(f'{e}')
    pathname = os.path.basename(font_path).split('.')[0]
    file_dir = os.path.dirname(__file__)
    dict_path = os.path.join(file_dir, 'output.json')
    dict_path1 = os.path.join(file_dir, 'output1.json')
    dict_path2 = os.path.join(file_dir, 'output2.json')
    svg_path = os.path.join(pathname, 'svg')
    png_path = os.path.join(pathname, 'png')
    os.makedirs(svg_path, exist_ok=True)
    os.makedirs(png_path, exist_ok=True)
    font = TTFont(font_path)
    charsdict = font.getBestCmap()
    print(charsdict)
    ret_dict = {}
    items = charsdict.items()
    # 单线程用法
    # for fkey, fvalue in items:
    #     ret = get_single_font(fkey, fvalue, font, svg_path, png_path)
    #     ret_dict.update(ret)

    # 线程池用法
    results = []
    with ThreadPoolExecutor(max_workers=min(len(items), max_workers)) as pool:
        # 构造一个列表，循环向线程池内submit提交执行的方法
        tasks = [pool.submit(get_single_font, fkey, fvalue, font, svg_path, png_path) for fkey, fvalue in items]
        try:
            pool.shutdown(wait=True)  # 线程数等待所有线程结束，这里 卡住主线程
            results = [task.result() for task in tasks]
        except Exception as e:
            print(f'multi get_single_font error:{e}')
    for ret in results:
        ret_dict.update(ret)

    dict_value = json.dumps(ret_dict, ensure_ascii=False, indent=4)
    with open(dict_path, mode='w+', encoding='utf-8') as f:
        f.write(dict_value)

    dict_value1 = covert_dict1(ret_dict)
    dict_value1 = json.dumps(dict_value1, ensure_ascii=False, indent=4)
    with open(dict_path1, mode='w+', encoding='utf-8') as f:
        f.write(dict_value1)

    dict_value2 = covert_dict2(ret_dict)
    dict_value2 = json.dumps(dict_value2, ensure_ascii=False, indent=4)
    with open(dict_path2, mode='w+', encoding='utf-8') as f:
        f.write(dict_value2)

    if remove_temp:
        shutil.rmtree(pathname)
    return ret_dict


def arguments():
    parser = argparse.ArgumentParser(description="decode font file to dict and export image files")
    # parser.add_argument("-p", '--path', type=str,default="./test_font/dc027189e0ba4cd.woff2", help=f"woff file path")
    parser.add_argument("-p", '--path', type=str, help=f"woff file path")
    parser.add_argument("-v", '--version', action='store_true', help=f"show app version")
    parser.add_argument("-r", '--remove', action='store_true', help=f"remove temp files after run")

    args = parser.parse_args()
    if args.version:
        print(f'version:{VERSION}')
    return args


def main(path=''):
    args = arguments()
    path = args.path or path
    if path and (os.path.exists(path) or path.startswith('http')):
        t1 = time.time()
        model_path = os.path.join(os.path.dirname(__file__), './common.onnx')
        charsets_path = os.path.join(os.path.dirname(__file__), './charsets.json')
        # ocr = DdddOcr(import_onnx_path=model_path,charsets_path=charsets_path)
        global ocr
        ocr = DdddOcr()
        print(get_font_dict(path, args.remove))
        t2 = time.time()
        print(f'cost: {round(t2 - t1, 2)} s')


if __name__ == '__main__':
    # main('test_font/dc027189e0ba4cd.woff2')
    # main('https://lf6-awef.bytetos.com/obj/awesome-font/c/dc027189e0ba4cd-500.woff2')
    # main('https://lf6-awef.bytetos.com/obj/awesome-font/c/dc027189e0ba4cd-700.woff2')
    main()
