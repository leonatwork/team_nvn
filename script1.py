import cv2
import numpy as np
import math



capture = cv2.VideoCapture(0)


while(capture.isOpened()):
    # read image
    ret, img = capture.read()

    # get hand data from the rectangle sub window on the screen
    cv2.rectangle(img, (300,300), (100,100), (0,255,0),0)
    crop_img = img[100:300, 100:300]

    # convert to grayscale
    grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

    # applying gaussian blur
    value = (35, 35)
    blurred = cv2.GaussianBlur(grey, value, 0)

    # thresholdin: Otsu's Binarization method
    _, thresh1 = cv2.threshold(blurred, 127, 255,
                               cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    image, contours, hierarchy = cv2.findContours(thresh1.copy(), \
        cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # find contour with max area
    cnt = max(contours, key = lambda x: cv2.contourArea(x))

    # finding convex hull
    hull = cv2.convexHull(cnt)

    # finding convex hull
    hull = cv2.convexHull(cnt, returnPoints=False)

    # finding convexity defects
    defects = cv2.convexityDefects(cnt, hull)
    count_defects = 0
    cv2.drawContours(thresh1, contours, -1, (0, 255, 0), 3)

    # applying Cosine Rule to find angle for all defects (between fingers)
    # with angle > 90 degrees and ignore defects
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]

        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])

        # find length of all sides of triangle
        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)

        # apply cosine rule here
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57

        # ignore angles > 90 and highlight rest with red dots
        if angle <= 90:
            count_defects += 1
            cv2.circle(crop_img, far, 1, [0,255,0], -1)
        dist = cv2.pointPolygonTest(cnt,far,True)
        # draw a line from start to end i.e. the convex points (finger tips)
        #cv2.line(crop_img,start, end, [255,255,255], 2)
        #cv2.circle(crop_img,far,5,[0,255,255],-1)








    # define actions required
    if count_defects == 1:
        cv2.putText(img,"Scissor", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        str="Scissor"
        file = open("testfile.txt","w")
        file.write("Scissor")
        file.close()
    elif count_defects == 3:
        cv2.putText(img,"Paper", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        str="Paper"
        file = open("testfile.txt","w")
        file.write("Paper")
        file.close()
    elif count_defects == 4:
        cv2.putText(img,"Paper", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        str="Paper"
        file = open("testfile.txt","w")
        file.write("Paper")
        file.close()
    elif count_defects == 0:
        cv2.putText(img, "Rock", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        str="Rock"
        file = open("testfile.txt","w")
        file.write("Rock")
        file.close()
    else:
        cv2.putText(img,"Scissor", (50, 50),\
                    cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        str="Scissor"
        file = open("testfile.txt","w")
        file.write("Scissor")
        file.close()
    cv2.imshow('Gesture', img)




    # show appropriate images in windows




    k = cv2.waitKey(10)
    if k == 27:
        break