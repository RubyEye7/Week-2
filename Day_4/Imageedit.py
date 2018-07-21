from PIL import Image
from PIL import ImageFilter


def denoiser3(r,g,b):
    if r == 255:
        if g == 255 and b == 255:
            return (0,0,0)
        elif g == 0 and b == 0:
            return (0,0,0)
    else:
        return (r,g,b)

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
    img.save("solarized_devil.jpg")

def denoise():
    img = Image.open("iron-puzzle.png")
    pixels = [(int(r * 10),0,0,a) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    img.save("solved_iron_puzzle.png")

def denoise2():
    img = Image.open("copper-puzzle.png")
    pixels = [(0,int(g * 20),int(b * 20),a) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    img.save("solved_copper_puzzle.png")

def denoise3():
    img = Image.open("copper-puzzle.png")
    pixels = [denoiser3(r,g,b) for (r,g,b) in img.getdata()]
    img.putdata(pixels)
    img.save("solved_copper_puzzle.png")


Choice = input("Enter the Editing system you wnat to use: 1.Remove Red 2.Invert Color 3.Darken Color 4.Lighten Color 5.Greyscale 6.Posterize 7.Solarize 8.Denoise:  ")
if Choice == "1":
    remove_red()
elif Choice == "2":
    invert_color()
elif Choice == "3":
    darken_color()
elif Choice == "4":
    lighten_color()
elif Choice == "5":
    greyscale()
elif Choice == "6":
    posterize()
elif Choice == "7":
    solarize()
elif Choice == "8":
    Secondary = input("Denoise 1, 2, or 3:  ")
    if Secondary == "1":
        denoise()
    elif Secondary == "2":
        denoise2()
    elif Secondary == "3":
        denoise3()
