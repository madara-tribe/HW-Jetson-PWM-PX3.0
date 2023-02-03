# Jetson Nano PWM as HW Prototype

# abstract

Jetson's PWM(Pulse Width Modulation) to move 2 Servomortor with multi-thread.

```sh
- JetPack > 4.6
- python3 3.6.9
- opencv 4.1.2
- Servo mortor :  TowerPro SG-90, 
```

<b>Jetson Nano and 2 Serbo mortor</b>

<img src="https://user-images.githubusercontent.com/48679574/211758179-abc3911f-4c45-4318-9de4-2c95f379bbd9.jpg" width="650" height="400"/>

# Adafruit-PCA9685 (PWM controller)

It can control multi-servo motor (maximum is 16). and script don't need multithread process.

<img src="https://user-images.githubusercontent.com/48679574/216533582-243f2e2c-19d7-4bae-bfee-6245f2e5709d.jpg" width="800" height="400"/>


# Setup

```zsh
# rewrite user name and install GPIO
sudo bash setup/install_gpio.sh

# setup pins for servo PWM
sudo bash setup/setpwm.sh

# Adafruit-PCA9685
pip3 install Adafruit_PCA9685
# i2cdetect -y -r 1
# rewrite I2C.py file
vi ~/.local/lib/python3.6/site-packages/Adafruit_GPIO/I2C.py
```


# References
- [jetson-gpio](https://github.com/NVIDIA/jetson-gpio/tree/master/samples)
- [Jetson Nano の 2 つのハードウェア PWM を使用してみた](https://qiita.com/kitazaki/items/2c9deb912f11106d1215)
- [jetson_nano_grove](https://github.com/kitazaki/jetson_nano_grove)
