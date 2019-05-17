"""
Code Challenge
  Name: 
    Image Processing using PIL
  Filename: 
    imgprocess.py
  Problem Statement:
    Given an image, perform image processing operations. 

    Keep only one output image i.e perform all tasks on the same image (override) 
    and print only the name of your output image with extension name in the end of your program. 

    Take the Image name from User (Handle the extension for image file name in your code)
    
    The image processing features to be provided by your code are:

        a.     Greyscale
        b.     Rotate_90 (Rotate the given image file by 90 clockwise)
        c.     Crop (Center) (size = 160(W), 204(H))
        d.     Thumbnail – Generate the thumbnail of the given image (size = 75, 75)
    
"""
from PIL import Image

input1=raw_input("Enter name of file>")
input1=input1 + ".jpg"
img = Image.open(input1)
print("a.     Greyscale")
print("b.      Rotate_90 (Rotate the given image file by 90 clockwise")
print("c.     Crop (Center) (size = 160(W), 204(H)")
print("d.     Thumbnail – Generate the thumbnail of the given image (size = 75, 75")
while True:
    ch1=raw_input("enter your choice>").lower()
    if(not ch1):
        break
    if(ch1 == 'a'):
        img.convert('LA')
        img.save('greyscale.jpg')
    elif(ch1 == 'b'):
        image_rotate=img.transpose(Image.ROTATE_90)
        image_rotate.save('image_rotate.jpg')
    elif(ch1 == 'c'):
        wid,hgh=img.size
        l=(wid-160)/2
        r=(hgh-204)/2
        w=(wid+160)/2
        h=(hgh+204)/2
        crop_img=img.crop(box=(l,r,w,h))
        crop_img.save('crop_img.jpg')
    elif(ch1 == 'd'):
        img.thumbnail((75, 75))
        print(img.width, img.height)
        img.save('thumb_sample1.jpg')
    else:
        print('invalid choice')
        continue


