# TaskMaster - Django Task Management System

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

A comprehensive task management web application built with Django that helps you organize, track, and manage your tasks efficiently.

## Features

- **User Authentication**: Secure login/logout functionality with Django's built-in auth system
- **Task Management**: Create, view, and manage tasks with detailed information
- **Status Tracking**: Monitor task progress with status indicators (Pending, In Progress, Completed)
- **Responsive Design**: Clean and user-friendly interface
- **Admin Panel**: Full-featured Django admin interface for managing data

## Project Structure

```
taskmaster/
├── manage.py
├── taskmaster/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── homepage.html
│   │   └── tasks/
│   │       ├── task_list.html
│   │       ├── task_detail.html
│   │       └── task_form.html
│   ├── static/
│   │   └── tasks/
│   │       └── style.css
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── db.sqlite3
```

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Srprajapat/TaskMaster.git
   cd TaskMaster
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django pillow
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:8000`

## Usage

1. **Homepage**: Visit the root URL to see the welcome page
2. **Authentication**: Use `/accounts/login/` to log in and `/accounts/logout/` to log out
3. **Task List**: View all tasks at `/tasks/`
4. **Task Details**: View individual task details at `/tasks/<task_id>/`
5. **Create Task**: Add new tasks at `/tasks/create/`
6. **Admin Panel**: Access the admin interface at `/admin/` (requires superuser privileges)

## Customization

### Adding New Task Status Options

Edit the `STATUS_CHOICES` in `tasks/models.py`:

```python
STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
    ('On Hold', 'On Hold'),  # Add new status
]
```

### Modifying Styling

Edit the CSS file at `tasks/static/tasks/style.css` to customize the appearance:

```css
/* Example customization */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    max-width: 1200px;
    margin: 0 auto;
    background-color: #f8f9fa;
}
```

### Adding New Fields to Tasks

Edit the `Task` model in `tasks/models.py`:

```python
class Task(models.Model):
    # Existing fields...
    estimated_hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

Then create and run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## API Endpoints

The application currently uses traditional Django views. To add a REST API:

1. Install Django REST Framework: `pip install djangorestframework`
2. Add `'rest_framework'` to `INSTALLED_APPS` in `settings.py`
3. Create serializers for models
4. Implement API views

## Deployment

### For Production Deployment

1. **Set DEBUG to False** in `settings.py`:
   ```python
   DEBUG = False
   ```

2. **Configure allowed hosts**:
   ```python
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   ```

3. **Set up a production database** (PostgreSQL recommended):
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'mydatabase',
           'USER': 'mydatabaseuser',
           'PASSWORD': 'mypassword',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

4. **Collect static files**:
   ```bash
   python manage.py collectstatic
   ```

5. **Use a production WSGI server** (e.g., Gunicorn):
   ```bash
   pip install gunicorn
   gunicorn taskmaster.wsgi:application
   ```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions:

1. Check the Django documentation at https://docs.djangoproject.com/
2. Search existing issues on GitHub
3. Create a new issue with detailed information about your problem

## Acknowledgments

- Built with the Django Web Framework
- Icons provided by [Font Awesome](https://fontawesome.com/)