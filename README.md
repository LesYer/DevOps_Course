# DevOps_Course
Tasks from DevOps Course

## Contributors
* Oleksii Yermolin

## Usage
1. Clone repository `https://github.com/LesYer/DevOps_Course.git`
2. Create virtual enviroment `python -m venv venv`
3. Activate virtual enviroment:
    * Windows: `venv\Scripts\activate`
    * Unix-like: `source venv/bin/activate` 

### Plain install with sqlite database
4. Install all dependencies `pip install -r requirements.txt`
5. Run gunicorn server `python3 app.py`


###Preparing enviroment and install Jenkins on server

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install default-jre sudo apt-get install default-jdk
sudo apt-get install wget wget -q -O - http://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update
sudo apt-get install jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins

###Intall any program on server jenkins

sudo apt-get install git
git --version
sudo apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
apt-cache policy docker-ce
sudo systemctl status docker
sudo chmod 666 /var/run/docker.sock
sudo cat /var/lib/jenkins/secrets/initialAdminPassword

###Docker instalation

chmod +x docker_install.sh
./docker_install.sh
docker-compose up

========
