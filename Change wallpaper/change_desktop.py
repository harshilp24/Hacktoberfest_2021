import ctypes
import time

img0 = r"C:\Users\Kapadia\Desktop\Project1\img\img0.jpg"
img1 = r"C:\Users\Kapadia\Desktop\Project1\img\img1.jpg"
img2 = r"C:\Users\Kapadia\Desktop\Project1\img\img2.jpg"
img3 = r"C:\Users\Kapadia\Desktop\Project1\img\img3.jpg"
img4 = r"C:\Users\Kapadia\Desktop\Project1\img\img4.jpg"
img5 = r"C:\Users\Kapadia\Desktop\Project1\img\img5.jpg"
img6 = r"C:\Users\Kapadia\Desktop\Project1\img\img6.jpg"
img7 = r"C:\Users\Kapadia\Desktop\Project1\img\img7.jpg"
img8 = r"C:\Users\Kapadia\Desktop\Project1\img\img8.jpg"
img9 = r"C:\Users\Kapadia\Desktop\Project1\img\img9.jpg"
img10 = r"C:\Users\Kapadia\Desktop\Project1\img\img10.jpg"

images = [img0, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10]

for n in range(11):
    print("Current Wallpaper is: ",n)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(10, 0 , images[n], 0)