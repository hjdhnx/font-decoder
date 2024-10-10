#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : test_ocr_D.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/10/11

from PIL import Image
from ddddocr import DdddOcr
import unittest
import string
import easyocr
import pytesseract
# import muggle_ocr
from pyocr import pyocr

ocr = DdddOcr(show_ad=False, beta=True)
reader = easyocr.Reader(['en'], gpu=True)
# sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.OCR)
# 创建OCR工具
tool = pyocr.get_available_tools()[0]


class TestOcr(unittest.TestCase):
    def test_ocr_d(self):
        with open('test.png', 'rb') as f:
            ocr.set_ranges(2)
            text1 = ocr.classification(f.read())
            ret = text1[:1]
            # 全部大小写字母
            if ret in string.ascii_letters:
                print('ret:', ret)
                ret1 = reader.readtext('test.png', detail=0)
                print('ret1:', ret1)
                ret2 = pytesseract.image_to_string('test.png')
                print('ret2:', ret2)
                # ret3 = sdk.predict(image_bytes=f.read())
                # print('ret3:',ret3)
                ret3 = tool.image_to_string(Image.open('test.png'), lang='eng')
                print('ret3:', ret3)
            self.assertEqual(ret, 'D')


if __name__ == '__main__':
    unittest.main()
