#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : builder.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/10/11

import os
from manage import build, build_pro


def main():
    build()
    build_pro()
    # os.system('python manage.py build')
    # os.system('python manage.py build-pro')


if __name__ == '__main__':
    main()
