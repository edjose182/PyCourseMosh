import requests

from pdf2txt import convert, Converter

response = requests.get("http://google.com")
print(response)

obj_converter = Converter()

obj_converter.text_upload()

convert("C:/pdf2convert.pdf")