#!/bin/bash

git clone https://github.com/alex-shmukler/SCE-2018-Elections.git
cd SCE-2018-Elections
sudo easy_install pip
sudo pip install -r requirements.txt
python db_create.py
sudo nohup python run.py &
