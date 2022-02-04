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

When the virtual environment is activated and you are placed in the folder where the main file is located, launch the program with the command:
```
(myenv) $ python3 manage.py runserver
```

Then a window will appear to select your file with shares. Once the program is finished, the recommended investment appears in the console but is also available in a text file.
This text file is located in the same place as your data. The data directory provides examples of input and output data.

🗒️ *Note: Depending on the installation of python it is possible that the `python3` command is not recognized under windows. In this case, you will have to replace `python3` by `python`.*