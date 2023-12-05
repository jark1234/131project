# JotBot

> THE Online Note App

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup](#installation)
- [Usage](#usage)
- [Technologies](#technology)
- [Acknowledgments](#acknowledgments)

## Introduction

- This application allows users to create notes without the unnecessary clutter or distraction.
- We wrote this no-fuss application in the hopes it encourages more people to "jot" down their ideas!

## Features

- Create, Edit, Delete and Save notes
- Edit interface for personalization

## Setup

To set up the application, initiate the cloning process by copying the repository link and executing "git clone" in the terminal. After cloning, navigate to the “131project” directory, then go into the "jotbot" subdirectory. Execute the command "python3 run.py" to run the application.

## Usage

Once the application is running, navigate to the registration page to create your account. One must create an account using an email and password. After creating an account, the user's data will be stored in the database. The application will bring the user back to the login where they will be prompted for their login information. If login information is found in the database, the user will be brought to the JotBot’s homepage. On the homepage, users can create a new note with a title and content and modify existing notes by selecting the note they wish to update and saving their changes. All notes will be timestamped when they are created. Users can initiate a search with regular expressions or category filters to find specific notes quickly within the “Search” feature. Within “Settings,” users can personalize their interface by choosing between dark and light modes, or update their profile name. To edit a profile name, users will click “edit profile name” before making desired changes and saving them. To edit the mode setting, the user will click “mode” and choose between “light” or “dark”. Within each note, users have the ability to remove unwanted notes permanently by clicking ”Delete”. For text formatting, users can bold, italicize, or underline text, as well as change text size and font while creating or editing a note. After each edit, users must “Save” their notes to ensure changes are stored securely. If one would like to secure their note with a password for added privacy, they will click "Secure with Password" within the open note. The user will be prompted for a password to secure the note. Manage your account by logging out to secure your data, access the profile settings to update your profile name, or permanently delete your account if needed or desired. To log out of the application, the user will click “Logout”. To delete an account, click “Delete Account”.

## Technologies

- IDE (Ubuntu and VSCode)
- Python3.11
- SQLAlchemy
- Flask
- Quill
- HTML
- CSS
- Flask-login
- Flask-wtf
- Flask-wtforms
- Flask-sqlalchemy
- Werkzeug
- Json

## Acknowledgments

- Jaclyn Turner (@jark1234) - lead
- Novel Alam (@Novel-Alam)
- Natalie Kao (@nataliekao03)
- Iskandar Daoud (@iskandardaoud)
