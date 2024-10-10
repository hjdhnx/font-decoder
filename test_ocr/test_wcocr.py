import wcocr
import os

wechat_path = r"D:\soft\WeChat\[3.9.2.20]"
wechatocr_path = os.getenv("APPDATA") + r"\Tencent\WeChat\XPlugin\Plugins\WeChatOCR\7045\extracted\WeChatOCR.exe"
wcocr.init(wechatocr_path, wechat_path)
result = wcocr.ocr("test.png")
# print(result)
ret = result['ocr_response'][0]['text']
print(ret)
