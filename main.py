import cv2
import os

directory = 'splashes'
possibleAnswers = []
needleImage = cv2.imread('needle.png', cv2.COLOR_BGR2GRAY)


for filename in os.listdir(directory):

    currentSplash = cv2.imread('splashes/' + filename, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(currentSplash, needleImage, cv2.TM_CCOEFF_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    print(filename + ' tested!')
    if maxVal > .7:
        print(maxVal)
        possibleAnswers.append(filename, + " value:"+  maxVal + 100 + "%")
        


print(possibleAnswers)


