/*
 * Publish DHT11 data to ROS topic
 * temperature: sensor_msgs/Temperature
 * humidity: sensor_msgs/RelativeHumidity
 * 
 * Author: Thanh-Tung Ngo + Viet-Thang Tran 
 * 
 */

//Add ROS library
#include <ros.h>
#include <ros/time.h>
#include <std_msgs/Float32.h>
// #include <std_msgs/Bool.h>

#include<DHT.h> //DHT11 library

ros::NodeHandle nh; //Declare node

void messageCb( const std_msgs::Float32& toggle_msg){
  digitalWrite(13, HIGH-digitalRead(13));   // blink the led
}



//Declare messages
std_msgs::Float32 temp_msg;
std_msgs::Float32 humid_msg;

//Declare publishers
ros::Publisher pub_temp("/temperature", &temp_msg);
ros::Publisher pub_humid("/humidity", &humid_msg);

//Declare subscribers
ros::Subscriber<std_msgs::Float32> sub("/alert", &messageCb );

const int DHTPIN = 8;       //Read DHT11 data from pin 8 on Arduino circuit
const int DHTTYPE = DHT11;  //Declare sensor type (DHT11/DHT22)
 
DHT dht(DHTPIN, DHTTYPE); 
 
void setup() {
  pinMode(13, OUTPUT);
  
  nh.initNode(); //Init ROS node

  nh.advertise(pub_temp);
  nh.advertise(pub_humid);

  nh.subscribe(sub);

  Serial.begin(9600);
  dht.begin();         // Khởi động cảm biến
}
 
void loop() {
  float h = dht.readHumidity();    //Đọc độ ẩm
  float t = dht.readTemperature(); //Đọc nhiệt độ

  temp_msg.data = t;
  humid_msg.data = h;
  
  pub_temp.publish(&temp_msg);
  pub_humid.publish(&humid_msg);
  
  Serial.print("Nhiet do: ");
  Serial.println(t);               //Xuất nhiệt độ
  Serial.print("Do am: ");
  Serial.println(h);               //Xuất độ ẩm
  
  Serial.println();                //Xuống hàng
  delay(10);

  nh.spinOnce();
}
