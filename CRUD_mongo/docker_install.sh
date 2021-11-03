#!/bin/bash

sudo apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common -y
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
apt-cache policy docker-ce
sudo systemctl status docker
sudo chmod 666 /var/run/docker.sock
sudo apt install docker-compose -y
docker-compose build
