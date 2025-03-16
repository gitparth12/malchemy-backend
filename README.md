# Flask API Project

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

This is a Flask-based backend application that serves API endpoints for malchemy.

## Features

- REST API endpoints to fetch and process data
- JSON responses for seamless frontend integration
- Modular Flask structure for maintainability

## Tech Stack

- **Backend**: Flask, Python
- **Frontend**: TypeScript, React, TailwindCSS

## Getting Started

1. Clone the repository:  
   ```sh
   git clone https://github.com/gitparth12/malchemy-backend.git
   ```
2. Navigate to the project directory  
3. Create a virtual environment and activate it:  
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
4. Install the required Python packages:  
   ```sh
   pip install -r requirements.txt
   ```
5. Run the Flask application:  
   ```sh
   python src/app.py
   ```
6. Access the API at:  
   ```
   http://localhost:5000
   ```

## Contributing

Read the guidelines below to ensure consistency in commit messages, branch names, and pull requests.

### Commit Messages

- Capitalize the subject line.
- Do not end with a period.
- Use imperative mood, e.g., *"Add endpoint for fetching user data"* instead of *"Added..."*.
- Keep messages clear and relevant.
- For detailed messages, use:  
  ```sh
  git commit -m "Title" -m "Description"
  ```

### Branch Names

Branches should follow one of these categories:

- **Feature**: `feature-<name>` (e.g., `feature-authentication`)
- **Fix**: `fix-<name>` (e.g., `fix-api-response`)
- **Refactor**: `refactor-<name>` (e.g., `refactor-logging`)
- **Docs**: `docs-<name>` (e.g., `docs-readme-update`)

Create a branch using:
```sh
git checkout -b <branch_name>
```

### Pull Requests

#### Title
- Short and descriptive summary
- Capitalized and written in imperative present tense
- No period at the end

#### Description
- Separate from the title with a blank line
- Explain what and why the changes were made
- Keep lines under 72 characters

#### Example Pull Request
```
This pull request adds a new API endpoint for retrieving user details.

To implement this, we:
- Created a new route in `src/api.py`
- Added authentication checks for secure access
- Updated documentation with usage instructions
```

## Developing Team
- Aqif
- Devanshi
- Parth
- Nasif
- Jenny
