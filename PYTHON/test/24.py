import qrcode

data = "https://gemini.google.com/app?hl=ko"

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qrcode.png")
print("my_qrcode.png 파일로 저장되었습니다!")