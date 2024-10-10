#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : test_wechat_ocr.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/10/11

import hashlib
import os
import json
import time
# pip install wechat-ocr
from wechat_ocr.ocr_manager import OcrManager, OCR_MAX_TASK_ID

wechat_ocr_dir = r"C:\Users\dashen\AppData\Roaming\Tencent\WeChat\XPlugin\Plugins\WeChatOCR\7045\extracted\WeChatOCR.exe"
wechat_dir = r"D:\soft\WeChat\[3.9.2.20]"
ocr_manager = OcrManager(wechat_dir)
ocr_cache = {}


def md5(text):
    return hashlib.md5(text.encode(encoding='UTF-8')).hexdigest()


def ocr_result_callback(img_path: str, results: dict):
    ret = results['ocrResult'][0]['text']
    global ocr_cache
    key = md5(os.path.abspath(img_path))
    ocr_cache[key] = ret
    result_file = os.path.basename(img_path) + ".json"
    print(f"识别成功，img_path: {img_path}, result_file: {result_file},ret:{ret}")
    with open(result_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(results, ensure_ascii=False, indent=2))


def ocr_start():
    global ocr_manager
    # 设置WeChatOcr目录
    ocr_manager.SetExePath(wechat_ocr_dir)
    # 设置微信所在路径
    ocr_manager.SetUsrLibDir(wechat_dir)
    # 设置ocr识别结果的回调函数
    ocr_manager.SetOcrResultCallback(ocr_result_callback)
    # 启动ocr服务
    ocr_manager.StartWeChatOCR()


def ocr_end():
    global ocr_manager
    ocr_manager.KillWeChatOCR()


def ocr_img(img_path):
    global ocr_manager
    global ocr_cache
    # 开始识别图片
    ocr_manager.DoOCRTask(img_path)
    time.sleep(0.5)
    while ocr_manager.m_task_id.qsize() != OCR_MAX_TASK_ID:
        pass
    # 识别输出结果
    print(ocr_cache)
    key = md5(os.path.abspath(img_path))
    return ocr_cache[key]


def main():
    ocr_start()
    ret = ocr_img('test.png')
    ret1 = ocr_img('gid58356.png')
    print('ret:', ret)
    print('ret1:', ret1)
    ocr_end()


if __name__ == "__main__":
    main()
