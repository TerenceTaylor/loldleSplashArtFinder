from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import cv2
import os

directory = 'splashes'
possibleAnswers = []

class GUIObject:
    

    def __init__(self, master):
        self.master = master
        master.title("Loldle Splash Cheater")

        self.topFrame = Frame()
        self.topFrame.pack(side= TOP)

        self.openButton = Button(self.topFrame, text="Open", command=self.open)
        self.openButton.pack(side = LEFT)

        self.fileNameLabel = Label(self.topFrame)
        self.fileNameLabel.pack(side= RIGHT)

        self.image1Label = Label()
        self.image1Label.pack()




    def open(self):
        self.image1Label.destroy()
        needleImagePath = filedialog.askopenfilename(initialdir= "C:/Users/drtig/Desktop/loldleCheat", 
                                            title= "Select File",
                                            filetypes= (("PNG files", "*.png"), ("all files", "*.*"))
                                            )
        


        image1 = ImageTk.PhotoImage(Image.open(needleImagePath))
        

        self.image1Label = Label(image=image1)
        self.image1Label.pack()
        root.update()



        needleImage = cv2.imread(needleImagePath, cv2.COLOR_BGR2GRAY)
        for filename in os.listdir(directory):
            global image2
            image2 = ImageTk.PhotoImage(Image.open('splashes/' + filename))
            self.image1Label.config(image = image2)
            root.update()
            currentSplash = cv2.imread('splashes/' + filename, cv2.COLOR_BGR2GRAY)

            result = cv2.matchTemplate(currentSplash, needleImage, cv2.TM_CCOEFF_NORMED)



            minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)

            #Print and display the file currently being checked + % accuracy
            print(str(filename) + " value:"+  str(maxVal * 100) + "%")
            self.fileNameLabel.config(text= str(filename) + " value:"+  str(maxVal * 100) + "%")
            if maxVal > .7:
                print(str(filename) + " value:"+  str(maxVal * 100) + "%")
                possibleAnswers.append(str(filename) + " value:"+  str(maxVal * 100) + "%")

                topLeft = maxLoc
                bottomRight = (topLeft[0] + needleImage.shape[1], topLeft[1] + needleImage.shape[0])

                #Draw Rectangle and convert to tkimage to display
                cv2.rectangle(currentSplash, topLeft, bottomRight, color=(0,255,0), thickness= 2, lineType= cv2.LINE_4)
                blue,green,red = cv2.split(currentSplash)
                img = cv2.merge((red,green,blue))
                im = Image.fromarray(img)
                global imgtk
                imgtk = ImageTk.PhotoImage(image=im)
                self.image1Label.config(image=imgtk)

                #image1Label.destroy()


                break
        


root = Tk()
gui = GUIObject(root)
root.mainloop()

