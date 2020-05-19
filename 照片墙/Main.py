from PIL import Image
import os
#背景图片位置
Background_image = '1.png'

#其他源图片目录
SRC = 'photo/'

Bg = Image.open(Background_image)
#创建一张空图大小与背景图片一致
w,h = Bg.size
new_img = Image.new('RGB',(w,h),'#FFFFFF')
Pt_Set = []
unit = 60
x_i = w // unit
y_i = h // unit

#读取照片源文件
for i in os.listdir(SRC):
    if(i.endswith('.jpg')):
        try:
            print('正在打开'+i)
            Pt_Set.append(Image.open(SRC+i))
        except:
            print('打开'+SRC+i+'错误')
pt_len = len(Pt_Set)
x = 0
y = 0
#将每一张照片贴在新建的图片上
for i in range(x_i*y_i):
    now = Pt_Set[i%pt_len].resize((unit,unit))
    new_img.paste(now,(x*unit,y*unit))
    x += 1
    if x == x_i:
        x = 0
        y += 1
#将背景贴在图片表面
new_img.paste(Bg,(0,0),Bg)
new_img.save("output.png")

