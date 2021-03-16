# Hướng dẫn sử dụng chương trình

Cài đặt Arduino IDE

Cài đặt thư viện `src/4107_123450-1520995731-0-dht11.zip` trong Arduino IDE.

Mở code `src/dht11.ino` trong Arduino IDE.

Cắm chân dữ liệu của DHT11 vào chân số 8 của Arduino.
Cắm chân Vcc của DHT11 vào 5V, GND vào GND của Arduino.

Nạp code lên Arduino.

Chạy lần lượt các lệnh sau trên các Terminal khác nhau:

```
$ roscore
```

```
$ rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=9600
```

```
$ rosrun IoTPrj listener.py
```

Lấy được dữ liệu loại `Float32` tương ứng là nhiệt độ, độ ẩm đọc được.

Tuấn cần viết thêm các hàm thực hiện các hành động trong file `scripts/listener.py`.
