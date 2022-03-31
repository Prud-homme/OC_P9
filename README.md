# LITReview

## Menu

* [Installation](#installation-and-execution-using-venv-and-pip)
* [Features for users](#features-for-users)

## Installation and execution using venv and pip

⚠️ Git and Python 3.8+ must be installed first.

1. Clone this repository using `$ git clone https://github.com/Prud-homme/OC_P9.git` (you can also download the code [as a zip file](https://github.com/Prud-homme/OC_P9/archive/refs/heads/main.zip))
2. Move to the OC_P9 root folder with `$ cd OC_P9`
3. Create a virtual environment for the project with 
    * `$ python -m venv env` on windows
    * `$ python3 -m venv env` on macos or linux
4. Activate the virtual environment with 
    * `$ env\Scripts\activate` on windows
    * `$ source env/bin/activate` on macos or linux
5. Install project dependencies with `$ pip3 install -r requirements.txt`
6. Run the server with
    * `$ python manage.py runserver` on windows
    * `$ python3 manage.py runserver` on macos or linux

When the server is running after step 6 of the procedure, the Web App can be launch from the URL: [http://localhost:8000](http://localhost:8000 "LitReview Web App").

Steps 1-3 and 5 are only required for initial installation. For subsequent launches of the Web App, you only have to execute steps 4 and 6 from the root folder of the project.

🗒️ *Notes:*

* *To reset the database you can delete db.sqlite3 file and run `$ python manage.py migrate` to create a new empty database*
* *To disable the virtual environment, run: `$ deactivate`.*


## Features for users

* Log in and sign up - the site should not be accessible to a non-logged-in user.
* View a feed containing the latest tickets and reviews from users that they follow ordered by time with the latest first.
* Create new tickets requesting a review on a book/article.
* Create reviews as a response to tickets.
* Create reviews not in response to a ticket.  As part of a one-step process, the user will create a ticket and then a review responding to their own ticket.
* Be able to view, edit, and delete their own tickets and reviews,
* Follow other users by entering their username,
* View who they follow and unfollow whoever they want. 

## Flake8

Flake8 helps prevent things like syntax errors, typos, bad formatting, incorrect style, etc.
By using it on my code, I make sure I'm following the PEP8 standard.

The report is generated in the *flake-report* folder under the name *index.html*. To open the report open the *index.html* file with a web browser.
