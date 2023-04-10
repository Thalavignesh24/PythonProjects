import qrcode

data=input("Enter the data/url: ")

imageExt=input("Enter the imageExt: ")

scannerName=input("Enter the scannerName: ")

path='QrcodeScanner/'

image=qrcode.QRCode(version=1,box_size=20,border=1)

image.add_data(data)

image.make(fit=True)

img=image.make_image(fill_color='red',back_color='black')

img.save(path+scannerName+'.'+imageExt)



