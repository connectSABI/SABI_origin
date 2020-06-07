# SABI_origin

* Note: Use command prompt terminal and not powershell

## Getting Started
* Install virtualenvwrapper-win with the following command
	* pip install virtualenvwrapper-win
* Make virtual environment for the project
	* mkvirtualenv sabi
* Activate environment every time before working on project using the command
	* workon sabi
* Install requirements from requirements.txt
	* pip install -r requirements

## Setting up mailer
* Login to your gmail account in a browser
* Allow application to send mails from your google account
	* Go to myaccount.google.com/lesssecureapps
	* Turn on whatever is shown
	* Accept if google sends a warning email
	* Go to accounts.google.com/DisplayUnlockCaptcha
	* Click continue and do whatever it asks
* Setup environment variable for username and password
	* Run setVariables.py and enter required fields
	* If your email and password is shown as output then variables are set

## Setting up database
* To be added
