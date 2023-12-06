# JotBot

> THE Online Note App

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#installation)
- [Usage](#usage)
- [Technologies](#technology)
- [Acknowledgments](#acknowledgments)

## Introduction

- This application allows users to create notes without the unnecessary clutter or distraction.
- We wrote this no-fuss application in the hopes it encourages more people to "jot" down their ideas!

## Features

- Create, Edit, Delete and Save notes
- Change profile information for personal experience
- Hide timestamps for added privacy

## Requirements

### Functional

- Users must be able to create an account using email and password [Natalie]
- Users must be able to create a new note [Natalie]
- Users must be able to edit an existing note [Natalie]
- Users must be able to delete notes [Natalie]
- Users must be able to bold, italicize, and underline text [Novel]
- Users must be able to save their notes [Novel]
- Users must be able to log out of their account [Natalie]
- Users must be able to update their profile name [Natalie]
- Connect with an External API\* [Novel]
- User must be able to turn timestamp visibility on and off [Novel]
- Users must have the ability to permanently delete their account [Jaclyn]
- User must have the ability to search notes [Jaclyn]

### Non-Functional

- Multilingual Support\* [Jaclyn and Natalie]

## Setup

To set up the application, initiate the cloning process by copying the repository link and executing "git clone" in the terminal. After cloning, navigate to the “131project” directory, then go into the "jotbot" subdirectory. Execute the command "python3 run.py" to run the application.

## Usage

Once the application is running, navigate to the registration page to create your account. One must create an account using a username, email, and password. After creating an account, the user's data will be stored in the database. The application will bring the user back to the login page, where they will be prompted for their login information. If login information is found in the database, the user will be brought to the JotBot’s homepage. On the homepage, users can create a new note with a title and content and modify existing notes by selecting the note they wish to update and saving their changes. All notes will be timestamped when they are created or edited, and users can choose to make those timestamps visible or hidden. Users can initiate a search to find specific notes quickly within the “Search” feature. Within “Profile,” users can update their profile name and birthday by clicking "Edit Profile" or delete their account by clicking "Delete Account." Within each note, users have the ability to remove unwanted notes permanently by clicking ”Delete”. For text formatting, users can bold, italicize, or underline text, as well as change text size and font while creating or editing a note. After each edit, users must “Save” their notes to ensure changes are stored securely. Manage your account by logging out to secure your data. To log out of the application, the user will click “Logout”.

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
