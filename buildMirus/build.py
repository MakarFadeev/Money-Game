from PIL import Image
import platform,os
icon=Image.open("icons.iconset/icon.png","r")
if platform.system()=='Darwin':
    icon.save("Mirus.icns","ICNS")
    os.system('pyinstaller game.py -i Mirus.icns --noconsole --noconfirm')
else:
    icon.save("Mirus.ico", "ICO")
    os.system('pyinstaller game.py -i Mirus.ico --noconsole --noconfirm')