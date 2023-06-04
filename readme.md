
# Customer Management System

The Customer Management System is a Django-based web application that allows you to create and manage customer records. It provides functionality to create new customers, update existing customer details, and perform user authentication for login.

![image](https://github.com/AnujCtrl/Darwin-assignment/assets/63535089/48cfce2c-c32f-42e3-b99e-bb017491e76f)


## Features

- User Registration: Create new customer accounts with a unique username, password, email, mobile number, name, and address.
- User Authentication: Allow registered customers to log in to access their account.
- Customer Management: View, update, and delete customer records.
- Email Notifications: Send welcome emails to newly registered customers containing their user ID.
- Validation: Perform validation checks on user inputs, including email format, username format, mobile number format, and password strength.

## Prerequisites

Make sure you have the following requirements installed:

- Python 3.x
- Django 3.x
- Django REST framework (if applicable)
- Other dependencies specified in the project's `requirements.txt` file (if any)

## Installation

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/your-username/customer-management-system.git
   ```

2. Change to the project directory:

   ```
   cd customer-management-system
   ```

3. Install the project dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```
   python manage.py migrate
   ```

## Usage

1. Start the development server:

   ```
   python manage.py runserver
   ```

   Also run smtp server for sending email locally:

   ```
   python -m smtpd -n -c DebuggingServer localhost:1025
   ```

2. Access the web application in your browser at `http://localhost:8000/frontend/test_api/`.

3. Use the provided forms to create new customers, log in to existing customer accounts, and manage customer records.

## Configuration

The project's configuration can be found in the Django project settings file (`settings.py`). You can modify settings such as database configuration, email settings, static file paths, and more in this file.

## Contributing

Contributions to the Customer Management System are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

The Customer Management System is for an assignment and not intended to use commercially.

## Acknowledgements

- [Django](https://www.djangoproject.com/) - The web framework used in this project.
- [Django REST framework](https://www.django-rest-framework.org/) - A powerful and flexible toolkit for building Web APIs.
- [Bootstrap](https://getbootstrap.com/) - A popular CSS framework used for styling the web application.
