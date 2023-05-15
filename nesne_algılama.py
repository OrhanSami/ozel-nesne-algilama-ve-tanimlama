from dataclasses import dataclass
import cv2 

fullbody_cascade = cv2.CascadeClassifier(f"{cv2.data.haarcascades}haarcascade_fullbody.xml") # tam vucut
body_cascade = cv2.CascadeClassifier(f"{cv2.data.haarcascades}haarcascade_upperbody.xml") #üst vucut
#face_cascade = cv2.CascadeClassifier(f"{cv2.data.haarcascades}haarcascade_frontalface_default.xml") #yüz 
#eye_cascade = cv2.CascadeClassifier(f"{cv2.data.haarcascades}haarcascade_eye.xml") #göz
#smile_cascade = cv2.CascadeClassifier(f"{cv2.data.haarcascades}haarcascade_smile.xml") #ağız
özel_xml_dosyası_cascade = cv2.CascadeClassifier(f"{cv2.data.haarcascades}özel_xml_dosyası.xml")


def detect(gray ,frame):
    fullbodys =fullbody_cascade.detectMultiScale(gray, 1.1, 3)
    for (fx,fy,fw,fh) in fullbodys:
        cv2.reactangle(frame , (fx,fy), (fx+fw,fy+fh), (131,32,133) ,7)
    return frame
def detect(gray ,frame): 
    bodys =body_cascade.detectMultiScale(gray, 1.1, 3) #vucut için okuma
    for (bx,by,bw,bh) in bodys:
        cv2.rectangle(frame , (bx,by), (bx+bw,by+bh), (237,40,142) ,5) #vucudu kutu içine al
        #roi_gray = gray[ by:by+bh ,bx:bx+bw ]
        #roi_color = frame[ by:by+bh ,bx:bx+bw ]

        faces =face_cascade.detectMultiScale(gray, 1.3, 5) #vucut bulursa yüzü algılaması için 
        for (x,y ,w ,h) in faces : # her yüz için tanıma yapıyor döngü 
            cv2.rectangle(frame , (x,y), (x+w ,y+h) , (255,0,0) ,2 ) # yüzün çevresine dikdörtgen çiz 
            roi_gray = gray[ y:y+h ,x:x+w ] # 
            roi_color = frame[y:y+h ,x:x+w ]#
            
           #eyes =eye_cascade.detectMultiScale(roi_gray, 1.1, 3)# bulunan yüz içerisinde göz tespit et
            #for (ex,ey,ew,eh) in eyes : #her yüz için bunu yapıyor 
                #cv2.rectangle(roi_color , (ex, ey) , (ex+ew , ey+eh),(0,255,0),2) # gözün etrafına dikdörtgen çiz
                
            #smile = smile_cascade.detectMultiScale(roi_gray, 1.7, 22) 
            #for (ix,iy,iw,ih) in smile :#  
                #cv2.rectangle(roi_color , (ix,iy) , (ix+iw , iy+ih), (0,0,255),2) 
    
    gokleren =gokleren_cascade.detectMultiScale(gray, 1.1, 3)
    for (gx,gy,gw,gh) in gokleren:
        cv2.reactangle(frame , (gx,gy), (gx+gw,gy+gh), (431,42,433) ,12)
    
    
    
    return frame # baştan detect fonksiyonuna dönüyor 

capture = cv2.VideoCapture(1) # kamerayı aç
while True : #sonsuz döngü oluşturuyoruz 
     _, frame =capture.read() # son resmi okut
     gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY) # resmi gri yap
     canvas =detect(gray,frame)# fonksiyonumuza 2 parametre yolluyoruza
     cv2.imshow('video',canvas)# kamera çıktısını al
     if cv2.waitKey(1) & 0xFF == ord('q'): #klavyeden tuşa basarsak 
            break # döngü duruyor
capture.release() # kamerayı kapa
cv2.destroyAllWindows() # tüm kodu sonlandı
print('çalışıyor') 