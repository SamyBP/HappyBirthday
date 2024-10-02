# HappyBirthday

## Description

HappyBirthday is a personal project to help automate sending Happy Birthday messages to your phone contacts
It uses the Google Contacts API to fetch your contacts and WhatsApp API to send a personalized Happy Birthday message when one of your contacts celebrate theirs birthday

## Prerequisites 

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