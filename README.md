# font-decoder

字体解密工具-通过图片处理与ocr识别手段将字体的映射字典生成出来

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />

<p align="center">
  <a href="https://github.com/hjdhnx/font-decoder/">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">font-decoder 字体解密专家</h3>
  <p align="center">
    字体解密专家去快速开始你的项目！
    <br />
    <a href="https://github.com/hjdhnx/font-decoder"><strong>探索本项目的文档 »</strong></a>
    <br />
    <br />
    <a href="https://github.com/hjdhnx/font-decoder">查看Demo</a>
    ·
    <a href="https://github.com/hjdhnx/font-decoder/issues">报告Bug</a>
    ·
    <a href="https://github.com/hjdhnx/font-decoder/issues">提出新特性</a>
  </p>

</p>


本篇README.md面向开发者

## 目录

- [上手指南](#上手指南)
    - [开发前的配置要求](#开发前的配置要求)
    - [安装步骤](#安装步骤)
- [文件目录说明](#文件目录说明)
- [开发的架构](#开发的架构)
- [部署](#部署)
- [使用到的框架](#使用到的框架)
- [贡献者](#贡献者)
    - [如何参与开源项目](#如何参与开源项目)
- [版本控制](#版本控制)
- [作者](#作者)
- [鸣谢](#鸣谢)

### 上手指南

代码拉下来后 `pip install -r requirements.txt`然后运行主文件`main.py`即可

###### 开发前的配置要求

1. windows 10/11
2. python 3.8.8
3. `pyinstaller -F main.py -p F:\python\mypython\font-decoder\Lib\site-packages`
4. `python manage.py build` `python manage.py build-pro` `python builder.py`
5. `font-decoder.exe -p dc027189e0ba4cd.woff2` `font-decoder-pro.exe -abp dc027189e0ba4cd.woff2`

###### **安装步骤**

1. Get a free API Key at [https://github.com/hjdhnx/font-decoder](https://github.com/hjdhnx/font-decoder)
2. Clone the repo

```sh
git clone https://github.com/hjdhnx/font-decoder.git
```

### 文件目录说明

eg:

```
filetree 
├── README.md
├── LICENSE
├── requirements.txt
├── manage.py
├── main.py
├── main.spec
├── main_pro.spec
├── onnxruntime.dll
├── onnxruntime_providers_shared.dll
├── charsets.json
├── common.onnx
├── common_old.onnx
├── /images/
│  ├── logo.ico
│  ├── logo.png
├── /test_ocr/
├── /test_font/
│  ├── dc027189e0ba4cd.woff2

```

### 开发的架构

请阅读[ARCHITECTURE.md](https://github.com/hjdhnx/font-decoder/blob/master/ARCHITECTURE.md) 查阅为该项目的架构。

### 部署

暂无

### 使用到的框架

- [ddddocr](https://github.com/sml2h3/ddddocr)

### 已知的问题

不支持识别区分大写字母，大写字母也会被识别成小写字母

### 贡献者

请阅读**CONTRIBUTING.md** 查阅为该项目做出贡献的开发者。

#### 如何参与开源项目

贡献使开源社区成为一个学习、激励和创造的绝佳场所。你所作的任何贡献都是**非常感谢**的。

1. Fork the Project
2. Create your Feature Branch (`git checkout -b hjdhnx/font-decoder`)
3. Commit your Changes (`git commit -m 'Add some font-decoder Feature'`)
4. Push to the Branch (`git push origin hjdhnx/font-decoder`)
5. Open a Pull Request

### 版本控制

该项目使用Git进行版本管理。您可以在repository参看当前可用版本。

### 作者

256161887@qq.com
CSDN:https://blog.csdn.net/qq_32394351
知乎:不通周天不改名 &ensp; qq:256161887

*您也可以在贡献者名单中参看所有参与该项目的开发者。*

### 版权说明

该项目签署了MIT 授权许可，详情请参阅 [LICENSE.txt](https://github.com/hjdhnx/font-decoder/blob/master/LICENSE.txt)

### 鸣谢

- [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
- [Img Shields](https://shields.io)
- [Choose an Open Source License](https://choosealicense.com)
- [GitHub Pages](https://pages.github.com)
- [Animate.css](https://daneden.github.io/animate.css)
- [xxxxxxxxxxxxxx](https://connoratherton.com/loaders)
- [ddddocr](https://ddddocr.com/)

<!-- links -->

[your-project-path]:hjdhnx/font-decoder

[contributors-shield]: https://img.shields.io/github/contributors/hjdhnx/font-decoder.svg?style=flat-square

[contributors-url]: https://github.com/hjdhnx/font-decoder/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/hjdhnx/font-decoder.svg?style=flat-square

[forks-url]: https://github.com/hjdhnx/font-decoder/network/members

[stars-shield]: https://img.shields.io/github/stars/hjdhnx/font-decoder.svg?style=flat-square

[stars-url]: https://github.com/hjdhnx/font-decoder/stargazers

[issues-shield]: https://img.shields.io/github/issues/hjdhnx/font-decoder.svg?style=flat-square

[issues-url]: https://img.shields.io/github/issues/hjdhnx/font-decoder.svg

[license-shield]: https://img.shields.io/github/license/hjdhnx/font-decoder.svg?style=flat-square

[license-url]: https://github.com/hjdhnx/font-decoder/blob/master/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/shaojintian

[ddddocr打包exe教程]:https://zhuanlan.zhihu.com/p/456894600?utm_id=0




