# Flask Hangman Game Website

Welcome to the Flask Hangman Game website! This project allows you to play the classic Hangman game online. The website includes user registration, login, password recovery, profile management, and a variety of word topics to challenge your vocabulary.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)

## Features

- **User Registration and Confirmation**: Users can register for an account and receive a confirmation email to activate their account.
- **Login and Authentication**: Secure login system with authentication and session management.
- **Password Recovery**: Forgot your password? No problem. Users can reset their password by receiving a recovery link via email.
- **Word Topics**: Choose from various word topics to play Hangman with words related to that topic.
- **Profile Management**: Users can change their name, email address, and password in their profile settings.
- **Profile Picture**: Customize your profile with a profile picture.
- **Status Updates**: Users can view their own status or the statuses of all players.

## Getting Started

Follow these steps to set up and run the Flask Hangman Game website on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/Danas544/baigiamas_hangman.git
   cd baigiamas_hangman/compose
   docker-compose build
   docker-compose up
   docker-compose exec database psql -U user -d postgres
   CREATE DATABASE hangman;
   \q
   docker-compose down
   docker-compose up




