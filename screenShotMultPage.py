import pyautogui
import time
import pyscreenshot as ImageGrab
import img2pdf

# pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

upper_x = 1410
upper_y = 101

lower_x = 2157
lower_y = 1028

next_page_x = 2130
next_page_y = 547

number_pages = 760

# list of image files to convert to pdf
imageFiles = []

for i in range(number_pages):
    img = imageFiles.append("img{}.png".format(i+1))

    # grab the screen shot
    im = ImageGrab.grab(bbox = (upper_x, upper_y,lower_x, lower_y))

    # save the png images
    im.save("img{}.png".format(i+1))

    # go to the next page button and click
    pyautogui.click(next_page_x, next_page_y) 

    # sleep to give time for page to load
    time.sleep(3)
    
with open("securityPlusGuide.pdf","wb") as f:
    f.write(img2pdf.convert(imageFiles))


    



