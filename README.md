# Malchemy

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
	- [Commit Messages](#commit-messages)
	- [Branch Names](#branch-names)
	- [Pull Requests](#pull-requests)
		- [Title](#title)
		- [Description](#description)
		- [Example Pull Request](#example-pr)
- [Developing Team](#developing-team)

## Overview

This is our UNIHACK hackathon project.

## Features

- feature 1
- feature 2

## Tech Stack

- **Backend**: Python, Flask, Flask-SocketIO
- **Frontend**: JavaScript, Socket.IO
- **Database**: SQLite, SQLAlchemy (ORM)
- **Cryptographic Libraries**: PyCryptodome (or PyCA/cryptography)
- **Authentication**: JSON Web Tokens (JWT) or server-side sessions

## Getting Started

1. Clone the repository: `git clone https://github.com/your-repo-url.git`
2. Navigate to the project directory: `cd secure-messaging-app`
3. Install the required Python packages: `pip install -r requirements.txt`
4. Run the application: `python app.py`
5. Access the application in your web browser at `https://localhost:5000`

## Contributing

Read the guidelines below to write good commit messages, branch names, and make pull requests that follow the conventions we will be using throughout the project.

### Commit Messages

- Capitalise the subject line.
- Do not end with a period.
- Use imperative mood, i.e. instead of *"Added ..."* write *"Add ..."*.
- Keep messages logical and relevant, do not write things like *"Please work"* or *"I hate frontend"*. To help decide the extent of this, imagine trying to access a point in the project 2 weeks ago, it would be better to have something like *"Add CSS for Navbar template"* or , so that we know from a glance what the commit is for.
- For more detailed messages, use `git commit -m <title> -m <description>`, however short and concise is still preferred.

### Branch Names
Make a branch using `git checkout -b <branch_name>`.
- Names fall under one of **4** categories
	- Minor Feature: `minor-FeatureName`
	- Major Feature: `major-FeatureName`
	- Patch: `patch-PatchName`
	- Miscellaneous: `name`
		- For example `documentation` for changing the README, or adding another markdown

### Pull Requests
*Summarised from [this article](https://namingconvention.org/git/pull-request-naming.html).*

#### Title
- Short and descriptive summary
- Should be capitalized and written in imperative present tense
- Do not end with period

#### Description
- Separated with a blank line from the subject
- Explain what, why, etc.
- Max 72 chars
- Each paragraph capitalized

#### Example Pull Request
```
This pull request is part of the work to make it easier for people to contribute to naming convention guides. One of the easiest way to make small changes would be using the Edit on Github button.

To achieve this, we needed to:
- Find the best Gitbook plugin which can do the work
- Integrate it in all the pages to redirect the user to the right page on GitHub for editing
- Make it visible on the page so users can notice it easily
```

## Developing Team
- Aqif
- [Devanshi Mirchandani](https://github.com/devanshimirchandani)
- Parth Bhargava
- Nasf
- Jenny

