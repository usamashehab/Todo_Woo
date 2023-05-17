# TODO Application

## Features

1.User Registration: Users can create a new account by providing their email address and password.
2.User Login: Registered users can log in using their credentials to access their personalized todo lists.
3.Create New Todo: Users can add new tasks to their list, providing a title and description.
4.Mark as Important: Users can mark specific todos as important to prioritize them.
5.Update Todo: Users can modify the details of their existing todos, such as the title, description, and importance.
6.Delete Todo: Users can remove completed or unwanted todos from their list.

## Installation

To install and run this project locally, follow these steps:

1. Clone the repository:

```bash
$ git clone https://github.com/usamashehab/Todo_Woo.git
```

2. Change into the project directory:

```bash
$ cd Todo_Woo
```

3. Install the required dependencies:

```bash
$ pip install -r requirements.txt
```

4. Create the database tables:

```bash
$ python manage.py migrate
```

5. Start the development server:

```bash
$ python manage.py runserver
```

6. Open a web browser and navigate to `http://localhost:8000` to access the application.

## Usage

1.Register a new account by providing your email address and password.
2.Log in using your credentials to access your personalized todo list.
3.Add new todos by providing a title and description.
4.Mark important todos to prioritize them.
5.Update the details of existing todos as needed.
6.Delete completed or unwanted todos from your list.

## Acknowledgements

- The Django documentation: https://docs.djangoproject.com/en/3.2/
- Bootstrap: https://getbootstrap.com/
