#!/bin/bash
#git clone https://github.com/denstiny/Terslation.git
sudo cp translation/fanyi.sh /bin/terlat
sudo chmod +x /bin/terlat
sudo mkdir /usr/local/src/fanyi && sudo chmod +777 /usr/local/src/fanyi
sudo cp translation/fanyi.py /usr/local/src/fanyi/fanyi.py
echo "Before the installation is complete, run, please make sure that wh
ether have dependence"
echo "There is no problem, please press enter to continue..."
read str
