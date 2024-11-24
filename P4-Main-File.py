# A QR code generator
import qrcode

input_1 = input(
    "Write the massage or URL that you\nwant to show in this qrcode: ")
input_2 = input("Write the name of the file and\n'.png' at the end of name: ")
img = qrcode.make(input)
img.save(input_2)
