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

#### Setup the development environment
```
$ virtualenv venv
$ . venv/bin/activate
```

#### Install Flask
```
$ pip install flask
$ pip freeze > requirements.txt
```

#### Create a simple Flask Application
Save the following Python code in a file called app.py.

```Python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

if __name__ == "__main__":
  app.run()

```

#### Run the Flask Application
```
$ python app.py
```

Open http://localhost:5000 in your browser, and you sould see the "Hello World!" response.

## Useful Resources

#### SheCanCodeIT Slack Channel
* Join http://shecancodeit.slack.com
* Go to #projectwork channel





