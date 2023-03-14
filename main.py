import cv2
import os

directory = 'splashes'
possibleAnswers = []
needleImage = cv2.imread('needle.png', cv2.COLOR_BGR2GRAY)


for filename in os.listdir(directory):

    currentSplash = cv2.imread('splashes/' + filename, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(currentSplash, needleImage, cv2.TM_CCOEFF_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    print(str(filename) + " value:"+  str(maxVal * 100) + "%")
    if maxVal > .7:
        print(str(filename) + " value:"+  str(maxVal + 100) + "%")
        possibleAnswers.append(str(filename) + " value:"+  str(maxVal * 100) + "%")
        


print(possibleAnswers)


