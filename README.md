# employee_management_project
 # Employee Management System

## Overview
This project is an Employee Management System built using Django, a high-level Python web framework. The system allows for managing employee records, including creating, editing, viewing, and deleting employee details. It also includes user authentication to ensure that only authorized users can access and modify the data.

## Features
- User Authentication: Login and logout functionality.
- Employee Management: Create, read, update, and delete employee records.
- Templates: HTML templates for rendering views.
- Forms: Django forms for handling user input.

## Technologies Used
- **Programming Language**: Python
- **Web Framework**: Django
- **Database**: SQLite (default database for Django projects)
- **Frontend**: HTML, CSS, JavaScript

## Project Structure
- `employee_management/`: Main project directory containing settings and configuration files.
- `employees/`: App directory containing core functionality.
  - `admin.py`: Registers models with the Django admin site.
  - `forms.py`: Contains forms used in the application.
  - `models.py`: Defines the `Employee` model.
  - `templates/`: Contains HTML templates.
  - `urls.py`: Defines URL patterns for the app.
  - `views.py`: Contains view functions.
- `manage.py`: Command-line utility for interacting with the Django project.
- `media/`: Contains media files uploaded by users.
- `static/`: Contains static files like CSS, JavaScript, and images.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/SyedAbbas-02/employee_management_project.git
   cd employee_management_project
