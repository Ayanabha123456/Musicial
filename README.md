[<img src="https://img.shields.io/badge/Bootstrap-Frontend-important.svg?logo=Bootstrap">](<LINK>)
[<img src="https://img.shields.io/badge/JavaScript-Frontend-important.svg?logo=Javascript">](<LINK>)
[<img src="https://img.shields.io/badge/Django-Backend-important.svg?logo=Django">](<LINK>)
[<img src="https://img.shields.io/badge/SQLite-Database-important.svg?logo=SQLite">](<LINK>)


<h1 align="center" style="font-size:60px;">Musicial</h1>

Musicial is a social media website based on photos and music developed using Django and Bootstrap.

# Technologies
<img src="https://getbootstrap.com/docs/5.3/assets/brand/bootstrap-logo-shadow.png" width="50">
<img src="https://i.postimg.cc/2SMpQnnq/django-logo.png" width="50" height="30">
<br>

# Prerequisites
* Install [Anaconda Navigator](https://www.anaconda.com/download)
* Clone/Download the repository
* Open the Anaconda prompt terminal

# How to run application?
* Perform the upcoming operations in the terminal
* Navigate to the drive where you downloaded the repository (e.g - D drive)
```bash
D:
```
* Create a virtual environment for the application with python enabled
```bash
conda create -n musicial python=3.7.5
```
* Activate the virtual environment
```bash
conda activate musicial
```
* Install Django
```bash
conda install django==2.1.5
```
* Install Pillow
```bash
conda install pillow
```
* Navigate to Musicial/ITECH
```bash
cd Musicial/ITECH
```
* Make your migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
* Create a new superuser
```bash
python manage.py createsuperuser
```

* Start the application server
```bash
python manage.py runserver
```
* The website can now be accessed via the following link: http://127.0.0.1:8000/musicial

# Video Demo
![image](https://github.com/Ayanabha123456/Musicial/assets/42903837/a4b56fd4-d45c-4e46-8194-67bc843add99)
Click the [link](https://drive.google.com/file/d/19RoVmnCe5YTaSK9hpIa23uYrfm_MCRXn/view?usp=sharing) to watch a demonstration of the website
