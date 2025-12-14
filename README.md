# Grocery Shop

A Django-based e-commerce website for grocery shopping.

## Features

- User authentication (signup, login, logout)
- Product catalog with categories
- Search and filter functionality
- Shopping cart
- Checkout process
- Admin panel for product management

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your browser

## Admin Panel

Access the admin panel at http://127.0.0.1:8000/admin/ using your superuser credentials to manage products and categories. 



created by Kritika
