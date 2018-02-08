import cv2
import numpy as np
import math
import random
import time

capture = cv2.VideoCapture(0)

k = 0
comp_move = [" "," "," "," "," "]
user_move = [" "," "," "," "," "]
for i in range(5):
    rand_num = random.randint(1,3)
    if rand_num == 1:
        comp_move[k] = "Rock"
    elif rand_num == 2:
        comp_move[k] = "Paper"
    elif rand_num == 3:
        comp_move[k] = "Scissor"
    k = k + 1

print("/********************************************************/\n")
print("                   Rock-Paper-Scissor                   \n")
print("/********************************************************/\n")
k = 0
for i in range(5):
    print(comp_move[k])
    k = k + 1
print("--------")

# Score variables initialization
scUser = 0
scComp = 0

flag = 0

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
    elif count_defects == 3:
        cv2.putText(img,"Paper", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    elif count_defects == 4:
        cv2.putText(img,"Paper", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    elif count_defects == 0:
        cv2.putText(img, "Rock", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    else:
        cv2.putText(img,"Scissor", (50, 50),\
                    cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    cv2.putText(img,comp_move[0], (300, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    cv2.putText(img,comp_move[1], (300, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    cv2.putText(img,comp_move[2], (300, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        #time.sleep(2)
    cv2.imshow('Gesture', img)


    if flag==1:
        print("---Welcome---\n")
        k=0
        for i in range(5):
            print("Make your play\n")
            choice='a'
            while(choice!='y'):
                if count_defects == 1:
                    move="Scissor"
                elif count_defects == 3:
                    move="Paper"
                elif count_defects == 4:
                    move="Paper"
                elif count_defects == 0:
                    move="Rock"
                else:
                    move="Scissor"
                print("Your move : "+move)
                choice = input("\nPress Y if its correct : ")
                if choice=='y':
                    user_move[k]=move
                    k = k+1
        k = 0
        for i in range(5):
            print(user_move[k])
            k = k + 1
    if flag==0:
        flag=1
    else:
        flag=0

    # show appropriate images in windows




    k = cv2.waitKey(10)
    if k == 27:
        break



# k = 0
# user_move = [" "," "," "," "," "]
# for i in range(5):
#     if count_defects == 1:
#         user_move[k]="Scissor"
#     elif count_defects == 3:
#         user_move[k]="Paper"
#     elif count_defects == 4:
#         user_move[k]="Paper"
#     elif count_defects == 0:
#         user_move[k]="Rock"
#     else:
#         user_move[k]="Scissor"
#     k = k + 1
#     time.sleep(1)


# k = 0
# for i in range(5):
#     print(user_move[k])
#     k = k + 1

# k=0
# for i in range(5):
#     if user_move[k]=="Scissor" and comp_move[k]=="Rock":
#         scComp = scComp + 1
#     elif user_move[k]=="Scissor" and comp_move[k]=="Paper":
#         scUser = scUser + 1
#     elif user_move[k]=="Rock" and comp_move[k]=="Paper":
#         scComp = scComp + 1
#     elif user_move[k]=="Rock" and comp_move[k]=="Scissor":
#         scUser = scUser + 1
#     elif user_move[k]=="Paper" and comp_move[k]=="Scissor":
#         scComp = scComp + 1
#     elif user_move[k]=="Paper" and comp_move[k]=="Rock":
#         scUser = scUser + 1
#     k = k + 1

# print("-----------")


# if scUser<scComp:
#     print("You lose")
# else:
#     print("You win")
