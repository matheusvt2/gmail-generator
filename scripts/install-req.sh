sudo apt update
sudo apt upgrade -y
cat  os-requirements.txt | xargs sudo apt install -y
sudo pip3 install -r requirements.txt