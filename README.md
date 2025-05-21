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
git clone https://github.com/vivek-0115/App_stater.git
```

## 2. Backend Setup (Flask)
```
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

