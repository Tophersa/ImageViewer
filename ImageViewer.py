# Image Viewer Window
# Mukhotho Vhonani Christopher
# 19 May 2021

# importing tkinter and Pillow 
from tkinter  import *
from PIL import Image, ImageTk

# defining root
viewer = Tk()
viewer.title('ImageViewer by Mukhotho Vhonani')


# sourcing images
img1 = ImageTk.PhotoImage(Image.open('images/img1.png'))
img2 = ImageTk.PhotoImage(Image.open('images/img2.jpg'))
img3 = ImageTk.PhotoImage(Image.open('images/img3.jpg'))
img4 = ImageTk.PhotoImage(Image.open('images/img4.jpg'))
img5 = ImageTk.PhotoImage(Image.open('images/img5.jpg'))
img6 = ImageTk.PhotoImage(Image.open('images/img6.jpg'))


# Listing images
imageList = [img1, img2, img3, img4, img5, img6]

# Placing image
labelin = Label(image=img1)
labelin.grid(row= 0, column=0, columnspan=3)


# Next button function
def next(imageNo):
    global labelin
    global nextButton
    global backButton
    
    labelin.grid_forget()
    labelin = Label(image=imageList[imageNo-1])
    nextButton = Button(viewer, text=">>", command= lambda: next(imageNo + 1))
    backButton = Button(viewer, text="<<", command= lambda: back(imageNo - 1))

    # Disable next button if current image is the last image
    if imageNo == 6:
        nextButton = Button(viewer, text=">>", state=DISABLED)

    labelin.grid(row= 0, column=0, columnspan=3)
    backButton.grid(row=1, column=0)
    nextButton.grid(row=1, column=2)

    
# Back button function
def back(imageNo):
    global labelin
    global backButton
    global nextButton

    labelin.grid_forget()
    labelin = Label(image=imageList[imageNo-1])
    nextButton = Button(viewer, text=">>", command= lambda: next(imageNo + 1))
    backButton = Button(viewer, text="<<", command= lambda: back(imageNo - 1))

    # Disable back button if current image is the last image
    if imageNo == 1:
        backButton = Button(viewer, text="<<", state=DISABLED)

    labelin.grid(row= 0, column=0, columnspan=3)
    backButton.grid(row=1, column=0)
    nextButton.grid(row=1, column=2)


# Creating buttons
backButton = Button(viewer, text="<<", command= lambda: back)
exitButton = Button(viewer, text="Exit", command=viewer.quit)
nextButton = Button(viewer, text=">>", command= lambda: next(2))

# Placing buttons
backButton.grid(row=1, column=0)
exitButton.grid(row=1, column=1)
nextButton.grid(row=1, column=2)

# Calling image viewer window
viewer.mainloop()