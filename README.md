# 🍽️ The Recipe Cloud App

**The Recipe Cloud** is a modern, stylish, and interactive recipe management application built with **Django**, **Bootstrap**, and custom **CSS** for a sleek and seamless user experience. Users can **add, edit, view, and delete recipes**, with authentication and dynamic UI enhancements.

---

## 🌟 Key Features

🔐 **User Authentication:** Secure login, registration, and profile management.

📝 **Recipe Management:** Full CRUD (Create, Read, Update, Delete) functionality for recipes.

🎨 **Sleek UI:** A responsive and interactive user interface powered by Bootstrap and custom CSS.

🃏 **Card-Based Layout:** Beautifully designed recipe cards with smooth animations.

🗂️ **Database Support:** Supports both PostgreSQL (for production) and SQLite (for development).

📋 **Enhanced Forms:** Stylish and user-friendly forms using Django Crispy Forms.

🌐 **Responsive Design:** Optimized for all devices, from desktops to mobile phones.

---

## 🚀 Live Demo

Check out the **live version** of the app:

🔗 https://the-recipe-cloud.onrender.com/

---

## 🛠️ Installation & Setup

Follow these steps to set up **The Recipe Cloud** on your local machine:

1️⃣ **Clone the Repository**

git clone https://github.com/MahadevBalla/The-Recipe-Cloud
cd The-Recipe-Cloud

2️⃣ **Create a Virtual Environment & Install Dependencies**

python -m venv env
source env/bin/activate # On Windows: env\Scripts\activate
pip install -r requirements.txt

3️⃣ **Apply Migrations & Run the Server**

python manage.py migrate
python manage.py runserver

4️⃣ **Access the App**

Open your browser and navigate to:
🌐 http://127.0.0.1:8000/

---

## 🛠️ Tech Stack

**Backend:** Django

**Frontend:** Bootstrap, Custom CSS

**Database:** PostgreSQL, SQLite

**Forms:** Django Crispy Forms

**Deployment:** Render

---

## 📂 Project Structure

The-Recipe-Cloud/

├── manage.py # Django management script

├── requirements.txt # Project dependencies

├── runtime.txt # Specifies Python version for deployment

├── env/ # Virtual environment (ignored in version control)

├── recipes/ # Main Django app for recipe management

│ ├── migrations/ # Database migrations

│ ├── static/ # Static files (CSS, images)

│ ├── templates/ # HTML templates for recipes

│ ├── models.py # Database models for recipes

│ ├── views.py # Views for recipe management

│ ├── urls.py # URL routes for recipes

│ └── ... # Other app-specific files

├── users/ # Django app for user authentication

│ ├── migrations/ # Database migrations

│ ├── templates/ # HTML templates for authentication

│ ├── forms.py # User registration and login forms

│ ├── views.py # Views for authentication

│ └── ... # Other app-specific files

├── config/ # Django project settings

│ ├── settings.py # Project settings (e.g., database, static files)

│ ├── urls.py # Main URL routing for the project

│ └── ... # Other project-specific files

└── README.md # Project documentation
