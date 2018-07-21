from PIL import Pillow


def posterizer(c):
    if c >= 0 and c <= 63:
        return 50
    elif c >= 64 and c <= 127:
        return 100
    elif c >= 128 and c <= 191:
        return 150
    elif c >= 192 and c <= 255:
        return 200

def solarizer(n):
    if n < 128:
        return 255 - n
    else:
        return n

def remove_red(name):
    img = Image.open(name)
    pixels = [(0,b,g) for (r,g,b) in img.getdata()]
    img.putdata(pixels)
    img.save("not_red_devil.jpg")

def invert_color():
    img = Image.open(name)
    pixels = [(255-r,255-g,255-b) for (r,g,b) in img.getdata()]
    img.putdata(pixels)
    img.save("invert_devil.jpg")

def darken_color(name):
    img = Image.open(name)
    pixels = [(int(0.75 * r),int(0.75 * g),int(0.75 * b)) for (r,g,b) in img.getdata()]
    img.putdata(pixels)
    img.save("dark_devil.jpg")

def lighten_color(name):
    img = Image.open(name)
    pixels = [(int(1.25 * r),int(1.25 * g),int(1.25 * b)) for (r,g,b) in img.getdata()]
    img.putdata(pixels)
    img.save(name)

def greyscale(name):
    img = Image.open(name)
    pixels = [(int((r+g+b)/3),int((r+g+b)/3),int((r+g+b)/3)) for (r,g,b) in img.getdata()]
    img.putdata(pixels)
    img.save("grey_devil.jpg")

def posterize(name):
    img = Image.open(name)
    pixels = [(posterizer(r),posterizer(g),posterizer(b)) for (r,g,b) in img.getdata()]
    img.putdata(pixels)
    img.save("posterized_devil.jpg")

def solarize(name):
    img = Image.open(name)
    pixels = [(solarizer(r),solarizer(g),solarizer(b)) for (r,g,b) in img.getdata()]
    img.putdata(pixels)
    img.save("solarized_" + name)

Choice = input("Enter the Editing system you wnat to use: 1.Remove Red 2.Invert Color 3.Darken Color 4.Lighten Color 5.Greyscale 6.Posterize 7.Solarize:  ")
if Choice == "1":
    remove_red(input("Enter filename:  "))
elif Choice == "2":
    invert_color(input("Enter filename:  "))
elif Choice == "3":
    darken_color(input("Enter filename:  "))
elif Choice == "4":
    lighten_color(input("Enter filename:  "))
elif Choice == "5":
    greyscale(input("Enter filename:  "))
elif Choice == "6":
    posterize(input("Enter filename:  "))
elif Choice == "7":
    solarize(input("Enter filename:  "))
