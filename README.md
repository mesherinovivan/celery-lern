[![codecov](https://codecov.io/gl/AdviNow/orchestration-engine/branch/development/graph/badge.svg?token=2ZauC4cRE0)](https://codecov.io/gl/AdviNow/orchestration-engine) | [![pipeline status](https://gitlab.com/AdviNow/orchestration-engine/badges/development/pipeline.svg)](https://gitlab.com/AdviNow/orchestration-engine/commits/development)


# Orchestration Engine

This service handles communication and storage of data between the Kiosk, the Doctor App, the Diagnostic Engine, the Treatment Engine, and third party integrations..

To clone run:
```shell
$ git clone git@gitlab.com:AdviNow/orchestration-engine.git
```

---

## Local deploy instructions
The Orchestration Engine has system requirements that are not compatible with Windows. Supported operating systems are Linux and Mac. If you are running Windows use a virtual machine with any linux distro preferrably CentOS or Ubuntu.

### Prerequisites
In order to get the system running locally, we must install the appropriate development tools and Python >= 3.6

### Summarized instructions

1) You need to install libxmlsec1-dev and pkg-config for xml crypto algorithms. In ubuntu-based distributives you can simply use 
```shell
$ sudo apt install pkg-config libxmlsec1-dev
```

2) create and activate virtulalenv and other apt packages:
```shell
$ sudo apt-get install python3-venv
$ sudo apt install -y apt-utils pkg-config libxmlsec1-dev openssh-client gettext libgettextpo-dev
$ sudo mkdir /var/log/orchestration_engine/
$ sudo chmod 777 /var/log/orchestration_engine/
```

3) activate the virtulalenv
```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
```

4) Make sure you have access to the following repos:

- https://gitlab.com/AdviNow/orchestration-engine-db

- https://gitlab.com/AdviNow/oe-json-map

- https://gitlab.com/AdviNow/pdf_generator

- https://gitlab.com/AdviNow/pdf_generator

5) Install pip packages
```shell
$ pip install restricted_pkg
$ pip install -r requirements/tests.txt
```

Note: If there are any other bugs you find please report it so that we can keep this document upto date.

6) Check to see if you are able to run it locally
```shell
$ python3 manage.py migrate
$ python3 manage.py runserver 0.0.0.0:8000 
Go to any browser and check to see if you are able to open the admin login page: http://localhost:8000/advinowadmin
```

7) You can also run some tests with right arguments from command line (This might take a long time)
```shell
$ python3 manage.py test <arguments>
```
I just want to add a new line here to try out something fancy!

### Docker run:

Build image for oe2 project, for wich you need actual ssh keys to git lab, you have to specify path to keys in environment file,
deafult path is ~/.ssh/id_rsa
`docker-compose -f docker/docker-compose.local.yml up`
