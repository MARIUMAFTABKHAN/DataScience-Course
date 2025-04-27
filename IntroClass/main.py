
# name="MARIUM"
# age=25
# height=5.2
# programmer=False
#
# print("Name: "+name)
# print("Age: ",age)
# print("Height: ",height)
# print("Programmer: ",programmer)
#
#
# print("*"*5)
#
# a=type(name)
# print(a)
#
# b=type(age)
# print(b)
#
# c=type(height)
# print(c)
#
# d=type(programmer)
# print(d)
#
# from playsound import playsound
# playsound("audio/Saans.mp3")
#
# from playsound import playsound
# playsound(r"audio/smp3.mp3"

# from playsound import playsound
# playsound(r"C:\Users\BLC\PycharmProjects\IntroClass\audio\smp3.mp3")

# import pygame
# pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load("audio/Saans.mp3")
# pygame.mixer.music.play()
# input("Press Enter to stop playback...")
# pygame.mixer.music.stop()

# Importing pygame module
import pygame
from pygame.locals import *

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Rectangle Drawing")

# Fill the scree with white color
window.fill((255, 255, 255))

# Using draw.rect module of
# pygame to draw the outlined rectangle
pygame.draw.rect(window, (0, 0, 255),
                 [100, 100, 400, 100], 2)

# Draws the surface object to the screen.
pygame.display.update()
# Add a loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()

# from rembg import remove
# from PIL import Image
#
# input_path="audio/tom-and-jerry.jpg"
# output_path="audio/c1.png"
# myinput=Image.open(input_path)
# output=remove(myinput)
# output.save(output_path)


# import pyshorteners
# long_url=input("Enter your long url")
# type_tiny=pyshorteners.Shortener()
# short_url=type_tiny.tinyurl.short(long_url)
# print("Short url here: ",short_url)

# from pdf2docx import Converter
# pdf_file="audio/AbdulRafay_CV_2025 (1).pdf"
# docx_file="audio/docsfile.docx"
# newfile=Converter(pdf_file)
# newfile.convert(docx_file)
# newfile.close()

import calendar

# create the object
html_cal = calendar.HTMLCalendar(firstweekday=0)
year = 2022
month = 3
print(html_cal.formatmonth(year, month))

yy=2024
mm=4

print(calendar.month(yy,mm))

print(calendar.calendar(yy))

# importing calendar module
# from calendar import Calendar
#
# obj = Calendar()
#
# # iterating with itermonthdates
# for day in obj.itermonthdates(2018, 9):
#     print(day)