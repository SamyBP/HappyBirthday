# HappyBirthday

## Description

HappyBirthday is a personal project to help automate sending Happy Birthday messages to your phone contacts
It uses the Google Contacts API to fetch your contacts and PyWhatKit to send a personalized Happy Birthday message when one of your contacts celebrate theirs birthday
The script will first fetch your contacts, retrieving the contact names, birthdays and phoneNumbers
By default the script will only check for the first birthday and phone number saved for any of your contacts and send the Happy Birthday message 
if the contact celebrates his birthday.

## Prerequisites 

* Have python 3.11.* installed
* Go to **Google Cloud Console** and create a new project
* Enable **Google People API** from **API & Services > Library**
* Create credentials: Choose OAuth Client ID and for client type choose Desktop Application
  * Download the client-secret-{generated_id} into the project root dir and rename it to client-secret.json

## Setup

* Create a virtual environment:

      python -m venv .venv

* Activate the virtual environment:

      .venv\Scripts\activate

* Install the libraries:

      pip install -r requirements.txt

* Creat a .env and enter your Happy Birthday message:

      MESSAGE_TO_SEND="La Multi Ani!!"

## Usage

* Run the script:

      python main.py