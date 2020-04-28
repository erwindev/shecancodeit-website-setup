# SheCanCodeIt Web Setup

This is a sample application that will be used to teach SheCanCodeIT members how to build a web application using Python and Flask.

## Get Started
#### Install Python 3
* [Windows](https://realpython.com/installing-python/#windows)
* [MacOSX](https://realpython.com/installing-python/#macos-mac-os-x)

#### Install Pip
* [Windows](https://www.liquidweb.com/kb/install-pip-windows/)
* [Mac](https://www.shellhacks.com/python-install-pip-mac-ubuntu-centos/)

#### Install Vistual Studio Code
* [Visual Studio Code](https://code.visualstudio.com/)

#### Install Git 
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

#### Install Virtualenv (Globally)
```
$ pip install virtualenv
```

#### Setup the development environment(Linux & MacOS)
```
$ virtualenv venv
$ . venv/bin/activate
```

#### Setup the development environment(Windows)
```
$ virtualenv venv
$ .\venv\Scripts\activate
```


#### Install the application
```
$ pip install -r requirements.txt
```

#### Run the Flask Application
```
$ flask db upgrade
$ flask run
```

Open http://localhost:5000

#### Changes to any model object (i.e. UserModel)
If you make any change to any model object, you will need to apply those changes to the database. 
```
$ flask db migrate -m 'comment here'
$ flask db upgrade
```

#### SheCanCodeIT Slack Channel
* Join http://shecancodeit.slack.com
* Go to #projectwork channel




