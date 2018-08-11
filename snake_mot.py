#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 23:34:05 2018

@author: root
"""

import cv2 as cv
import numpy as np
import sys
import random
import time

img=np.zeros((700,1370,3),dtype=np.uint8)
r,c,_=img.shape
img.fill(255)
x=0
y=0
x_sp=20
k=0


def motion(img,face_cascade,k):
    
    
    
    
    
    
#    gray = fgbg.apply(img)
    
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    cv.rectangle(img,(125,20),(225,120),(0,0,0),2)
    cv.rectangle(img,(50,150),(150,250),(0,0,0),2)
    cv.rectangle(img,(200,150),(300,250),(0,0,0),2)
    cv.rectangle(img,(125,270),(225,370),(0,0,0),2)
    cv.rectangle(img,(350,10),(600,470),(0,0,0),3)
    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        if x>=125 and x+w<=225 and y >=20 and y+h<=120  :
            k=119
            print("yes")
            break
        if x>=50 and x+w<=150 and y >=150 and y+h<=250  :
            k=97
            print("yes")
            break
        if x>=200 and x+w<=300 and y >=150 and y+h<=250  :
            k=100
            print("yes")
            break
        if x>=125 and x+w<=225 and y >=270 and y+h<=360  :
            k=115
            print("yes")
            break
            
        
       
    cv.imshow('img',img)
    
    return k

#fuctions

#work
def initg(img,x,y,x_sp,k,d):
    rx,ry=random.randint(1,65)*20,random.randint(1,32)*20
    cv.rectangle(img,(rx,ry),(20+rx,20+ry),(0,255,0),-1)
    cv.rectangle(img,(0+(x*x_sp),0+(y*x_sp)),(20+(x*x_sp),20+(y*x_sp)),(0,255,0),-1)
    face_cascade = cv.CascadeClassifier('aGest.xml')
    vid=cv.VideoCapture(1)  
    
    f=1
    total=0
    ti=time.time()
    
    while(f):
        
        img.fill(255)
        cv.rectangle(img,(rx,ry),(20+rx,20+ry),(255,0,0),-1)
        a=cv.waitKey(d)    
        
        p,i=vid.read()
        k=motion(i,face_cascade,k)
        
        if a!=-1:
            k=a
        if x in range(69) and y in range(34):
            
            
            if k == 119:
                y=y-1
      
            elif k == 97:
                x=x-1
     
            elif k == 115:
                y=y+1
    
            elif k == 100:
                x=x+1
            
      
            else:
                pass;
            if a==27:
                break;
        else:
            if x>=69:
                x=0
            elif x<0:
                x=68
            elif y>=34:
                y=0
            else:
                y=33    
        
        
        
        
        
        print(x,y)
        print(0+(x*x_sp),0+(y*x_sp),20+(x*x_sp),20+(y*x_sp))    
        cv.rectangle(img,(0+(x*x_sp),0+(y*x_sp)),(20+(x*x_sp),20+(y*x_sp)),(0,255,0),-1)
        if rx==x*x_sp and ry==y*x_sp:
            total+=1
            rx,ry=random.randint(1,65)*20,random.randint(1,32)*20
        cv.putText(img,str(total),(1250,200), font, 1,(0,0,0),2,cv.LINE_AA)
        cv.putText(img,"time :"+" " +str(int(time.time()-ti)),(1150,650), font, 1,(0,0,0),2,cv.LINE_AA)
        cv.imshow("Wolfgang\'s Snake",img)
        if time.time()-ti>=61:
            f=0
    cv.rectangle(img,(0,r//2-(100)),(1370,r//2+(100)),(110,40,150),-1)

    cv.putText(img,'Total : '+str(total),(c//2-(250),r//2), font, 2.5,(255,255,255),2,cv.LINE_AA)
    cv.putText(img,'Wanna Play Again?? Press "y" Else "n" ',(c//2-(300),r//2+80), font, 1,(0,200,255),2,cv.LINE_AA)
    cv.imshow("Wolfgang\'s Snake",img)
    vid.release()
    cv.destroyWindow("img")
   
    k3=cv.waitKey(0)
    return k3
    



#Start

d=40
font = cv.FONT_HERSHEY_SIMPLEX
cv.rectangle(img,(380,100),(1000,200),(200,200,200),-1)
cv.putText(img,'Kiddo!!!',(580,180), font, 1.5,(0,0,0),2,cv.LINE_AA)
cv.rectangle(img,(0,r//2-(100)),(1370,r//2+(100)),(110,40,150),-1)

cv.putText(img,'Wolfgang\'s Snake',(c//2-(350),r//2), font, 2.5,(255,255,255),2,cv.LINE_AA)
cv.putText(img,'Time Limit :- 60 sec',(c//2-(200),r//2+80), font, 1,(255,255,255),2,cv.LINE_AA)
cv.putText(img,'y to Start | Esc to Exit ',(c//2-(350),580), font, 2,(0,0,255),2,cv.LINE_AA)
cv.putText(img,'              1 :- Kiddo | 2 :- Man | 3:- Legend ',(c//2-(500),650), font, 1,(0,125,255),2,cv.LINE_AA)



while(1):
    
    cv.imshow("Wolfgang\'s Snake",img)
    k1=cv.waitKey(1)
    if k1==121:
        
        break;
    if k1==49:
        cv.rectangle(img,(380,100),(1000,200),(200,200,200),-1)
        cv.putText(img,'Kiddo!!!',(580,180), font, 1.5,(0,0,0),2,cv.LINE_AA)
        d=40
    if k1==50:
        cv.rectangle(img,(380,100),(1000,200),(125,125,125),-1)
        cv.putText(img,'Men!!!',(580,180), font, 1.5,(0,0,0),2,cv.LINE_AA)
        d=20
    if k1==51:
        cv.rectangle(img,(380,100),(1000,200),(50,50,50),-1)
        cv.putText(img,'Legend!!!',(580,180), font, 1.5,(250,250,250),2,cv.LINE_AA)
        d=10
    if k1==27:
        cv.destroyAllWindows()
        sys.exit()

img.fill(255)

#main
f2=1

while(f2):
    t=initg(img,x,y,x_sp,k,d)
    if t==121:
        f2=1
    else:
        f2=0
        

cv.destroyAllWindows()
    
    
    
    
