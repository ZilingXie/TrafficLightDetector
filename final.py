from ShapeDetector import ShapeDetector
from colorlabeler import ColorLabeler
import cv2

image = cv2.imread("C:\Users\Ziling Xie\OneDrive\Shape/3.jpg")

blurrimage = cv2.GaussianBlur(image, (5, 5), 0)
lab = cv2.cvtColor(blurrimage, cv2.COLOR_BGR2LAB)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
cnts, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

sd = ShapeDetector()
cl = ColorLabeler()

for c in cnts:
  
  
    shape = sd.detect(c)
    color = cl.label(lab, c)
    text = "{} {}".format(color, shape)
    textT = "It's a Traffic Light"
    textR = "Red Light, STOP!"
    textG = "Green Light, Go!"
    textY = "Yellow Light, Slow!"
    countb = 0
    if(text == "red circle"):
        
            #cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            #cv2.putText(image, textR, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
        print(textR)
        
            
    elif(text == "green circle"):
       
            #cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            #cv2.putText(image, textG, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
        print(textG)
  

    elif(text == "yellow circle"):
       
            #cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            #cv2.putText(image, textY, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
        print(textY)
     

    '''elif(text == "black rectangle"):
        
            #cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            #cv2.putText(image, textT, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
        if(countb == 0):
            print(textT)
            countb+=1
        else:
            pass
   
    else:
        pass'''
            
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    #cv2.putText(image, text, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
    
	
cv2.imshow("Image", image)
cv2.waitKey(0)
