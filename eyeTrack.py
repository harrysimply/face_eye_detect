# coding=utf-8
import cv2
import time
'''
基于opencv和QT的瞳孔精确检测程序
https://blog.csdn.net/zyx1990412/article/details/51219076

基于QT和opencv的瞳孔定位及跟踪程序
https://blog.csdn.net/zyx1990412/article/details/51254127
'''
def eyeDetect():
    #eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    #lefteye_cascade =cv2.CascadeClassifier('/home/hx-104b/眼动追踪/haarcascade_lefteye_2splits.xml')
    camera = cv2.VideoCapture(0)
    while (True):
        stime = time.time()
        ret, frame = camera.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            #得到位置信息x,y,w,h
            eyes = eye_cascade.detectMultiScale(gray, 1.1, 8, 0 , (30, 30))
            face = face_cascade.detectMultiScale(gray, 1.1, 5, 0 , (40, 40))

            #3. double scaleFactor=1.1：这个是每次缩小图像的比例，默认是1.1
            # 4. minNeighbors=3：匹配成功所需要的周围矩形框的数目，每一个特征匹配到的区域都是一个矩形框，只有多个矩形框同时存在的时候，才认为是匹配成功，比如人脸，这个默认值是3。
            # 5. flags=0：可以取如下这些值：
            # CASCADE_DO_CANNY_PRUNING=1, 利用canny边缘检测来排除一些边缘很少或者很多的图像区域
            # CASCADE_SCALE_IMAGE=2, 正常比例检测
            # CASCADE_FIND_BIGGEST_OBJECT=4, 只检测最大的物体
            # CASCADE_DO_ROUGH_SEARCH=8 初略的检测
            # 6. minObjectSize maxObjectSize：匹配物体的大小范围


            print (eyes)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            for (ex, ey, ew, eh) in face:
                cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)

            cv2.imshow('VideoFaceDetect', frame)
            #print ("{:.1f} fps".format(1/(time.time()-stime)))
            k = cv2.waitKey(1)
            if k == ord("q"):
                    break
    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    eyeDetect()