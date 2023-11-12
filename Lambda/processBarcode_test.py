import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

def readBarcode(img):
    barcodes = decode(img)
    if not barcodes:
        print("No barcode detected")
    else:
        for barcode in barcodes:
            if barcode.data!="":
                print(barcode.data.decode('utf-8'))

while 1:
    ret, frame = cap.read()
    if not ret:
        print("Unable to capture video")
        break
    readBarcode(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
