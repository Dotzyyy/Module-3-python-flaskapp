# python-flask-app
Flask Blog
Render Url: https://fullstack-python-flask-app.onrender.com/
Github Url: https://github.com/Dotzyyy/Module-3-python-flaskapp

## Concept

This app was made to act as an online blog where users can register for an account and sign into the blog with the home page also serving as the user feed. As there was no SQL used in this project, it was mainly dummy data that was utilised. Some of the finctionality such as the dark mode/ light mode and reveal info sections were items I wished to improve on since the last project.

### Languages and Technology Used

Featured Languages:

* HTML5

* CSS3

* JavaScript

* Python3

Featured Technologies:

* Bootstrap 

* Flask

* Render (For deploying the app)

### Features

There are few features making use of python and javascript:

* On all pages there is a dark mode/ light mode option present on the navbar

* The navbar shrinks down to a sidebar when the screen becomes small. It is contained in a 3 lined icon.

* There is a 'smooth scroll' icon on the index page which scrolls down to the bottom of the page.

* Two forms are processed using python and imported flask validators for fields such as 'username' 'email' and 'password'.

* The about page containes a faq area with 'accordians' that reveal/hide infro when clicked




### Future Updates

The biggest feature I would love to implement in the future is an account database using SQL wherby we can store a user's login details and profile details.

## How to Deploy/Access

### Step 1:

One of three options:

* Upload the project folder to your own github.

* Clone this git repository at https://github.com/Dotzyyy/Module-3-python-flaskapp

* Access via the provided URL https://fullstack-python-flask-app.onrender.com/

### Step 2:
    
    Create an account on https://render.com/

### Step 3:

    Link your github account

### Step 4:

   Once logged in and on the main dashboard, select "New" > "Web Service".

### Step 5:

    Connect to this repository or a clone of it

### Step 6:

On the following form, ensure that:

* You select an appropriate name for the web service

* Select your closest region (Frankfurt for Europe)

* Branch should be 'main'

* Make sure not to change any of the pre-loaded flask options such as 'build command'

* Start Command '$ gunicorn app:app' (make sure 'Flask' and 'Gunicorn' is listed in requirements.txt)

* Select Instance Type 'free

### Step 7:

Use the provided Url to access the website!:

    https://fullstack-python-flask-app.onrender.com/






