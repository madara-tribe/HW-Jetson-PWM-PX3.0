#/bin/sh
# git clone from source
git clone https://github.com/NVIDIA/jetson-gpio.git
cd jetson-gpio
sudo python3 setup.py install

# create group and add user
sudo groupadd -f -r gpio
sudo usermod -a -G gpio <ユーザー名>

# add udev rule
sudo cp lib/python/Jetson/GPIO/99-gpio.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && sudo udevadm trigger
sudo reboot
