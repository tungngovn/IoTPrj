import Adafruit_DHT
import RPi.GPIO as GPIO
import time

# Adafruit_DHT ho tro nhieu loai cam bien DHT, o day dung DHT11 nen chon cam bien  DHT11
chon_cam_bien = Adafruit_DHT.DHT11

GPIO.setmode(GPIO.BCM)

# chan DATA duoc noi vao chan GPIO25 cua PI
pin_sensor = 25

print ("RASPI.VN Demo cam bien do am DHT 11");

while(1):
   # Doc Do am va Nhiet do tu cam bien thong qua thu vien Adafruit_DHT
   # Ham read_retry se doc gia tri Do am va Nhiet do cua cam bien
   # neu khong thanh cong se thu 15 lan, moi lan cach nhau 2 giay.
   do_am, nhiet_do = Adafruit_DHT.read_retry(chon_cam_bien, pin_sensor);
   
   # Kiem tra gia tri tra ve tu cam bien (do _am va nhiet_do) khac NULL
   if do_am is not None and nhiet_do is not None:
     print ("NNhiet Do = {0:0.1f}  Do Am = {1:0.1f}\n").format(nhiet_do, do_am);
     print ("RASPI.VN cho 2 giay de tiep tuc do ...\n");
     time.sleep(2)
   else:
     # Loi :(
     print("Loi khong the doc tu cam bien DHT11 :(\n")import Adafruit_DHT