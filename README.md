# 🚀 General Purpose Starter App

A ready-to-use web application starter template with a Vue.js + Bootstrap 5 frontend and Flask + Flask-RESTful backend. Designed to save time and kickstart development.

---

## 🌟 Features

- Vue 3 with Bootstrap 5 UI
- Flask backend with RESTful API (Flask-RESTful)
- User authentication (login/signup pages pre-built)
- Modular structure for easy expansion
- Basic user models and database schema (SQLite by default)
- Responsive design

---

## 🛠 Tech Stack

**Frontend:**

- Vue 3
- Bootstrap 5
- Vue Router

**Backend:**

- Flask
- Flask-RESTful
- SQLAlchemy (ORM)
- SQLite (easy local development)

---

## 📁 Folder Structure
starter-app/
├── backend/
│ ├── app.py # Flask app entry point
│ ├── models.py # SQLAlchemy models (User, Role, etc.)
│ ├── resources/ # API routes using Flask-RESTful
│ ├── db.sqlite # SQLite DB file
│ └── init.py (if using app factory)
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── views/ # Home, About, Login, Signup
│ │ └── components/ # Navbar, form components
│ └── main.js # Vue entry point
├── README.md
└── requirements.txt # Python dependencies

---

# 🚀 Getting Started

## 1. Clone the Repo
```
git clone https://github.com/yourusername/starter-app.git
cd starter-app
```

## 2. Backend Setup (Flask)
```
cd backend
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows
pip install -r ../requirements.txt
python app.py  # Runs the Flask API
```

## 3. Frontend Setup (Vue)
```
cd ../frontend
npm install
npm run serve
```

## 4. Genrate Secret Values
```
def generate_secure_string(length=120):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

# Generate and print
print("SECRET_KEY =", generate_secure_string())
print("SECURITY_PASSWORD_SALT =", generate_secure_string())
```

## 5. Setting Up .env variables
####  Create a `.env` file in the root of your project with this content:
```
# Security
SECRET_KEY=your_very_secret_key_here
SECURITY_PASSWORD_SALT=your_salt_value_here

# Mail
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-gmail
MAIL_PASSWORD=your gmail-app password not you actual gmail password create secondary password 
MAIL_DEFAULT_SENDER=your-gmail
```

## 6. Install the `python-dotenv` package if you haven't:
```
pip install python-dotenv
```

## 7. Access `.env` variables
```
from dotenv import load_dotenv
import os

load_dotenv()  # Load from .env file in the current directory

print(os.getenv("APP_SECRET_KEY"))
```
