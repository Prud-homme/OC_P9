# LITReview


## Menu

* [Program setup](#program-setup)
* [Program execution](#program-execution)

## Program setup

### Creation of a virtual environment

**On Windows**
```
$ python3 -m venv c:\path\to\myenv
$ myenv\Scripts\activate.bat
```

**On Unix or MacOS**
```
$ python3 -m venv /path/to/myenv
$ source myenv/bin/activate
```

**To install packages from the requirements.txt file**
```
(myenv) $ pip3 install -r requirements.txt
```

**To disable the virtual environment, run:**
```
(myenv) $ deactivate
```

## Program execution

When the virtual environment is activated and you are placed in the root folder, launch the program with the command:
```
(myenv) $ python3 manage.py runserver
```
To access the application, launch a web browser and navigate to *localhost:8000*

🗒️ *Note: Depending on the installation of python it is possible that the `python3` command is not recognized under windows. In this case, you will have to replace `python3` by `python`.*
