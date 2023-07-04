![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome to Tic Tac Toe!

This is a simple game of Tic Tac Toe that you can play in your browser. It is built using Python.

Users are asked to enter their name and then choose whether they want to be X or O. The game will then begin.
## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

## Resources
- [Tic Tac Toe Tutorial](https://www.askpython.com/python/examples/tic-tac-toe-using-python)
- [Google sheet API setup](http://ai2.appinventor.mit.edu/reference/other/googlesheets-api-setup.html)