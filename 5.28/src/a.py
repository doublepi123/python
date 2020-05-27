from PIL import Image
import matplotlib.pyplot as plt
import os
def main():
    src = Image.open("src.jpg")
    src = src.convert('L')
    # src = src.rotate(-1.05)
    # src.save("a.jpg")
    unit = (28,28)
    x1 = 0
    y1 = 0
    x2 = 80
    y2 = 79
    w = x2 - x1
    h = y2 - y1
    for j in range(10):
        x = x1
        y = y1
        for i in range(10):
            box=(x,y,x+w,y+h)
            now=src.crop(box)
            now = now.resize(unit)
            now.save(str(i)+ "-"+chr(ord('a')+j)+'-41824307.png')
            x += w
        y1 += h


if __name__ == "__main__":
    main()