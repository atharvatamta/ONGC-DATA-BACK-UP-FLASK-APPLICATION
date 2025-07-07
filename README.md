# ONGC Digital Backup System

A web application built using **Flask** to digitize and manage ONGC’s physical backup register entries. The system provides role-based access for users and admins, enabling secure and efficient data entry and review.

---

## 🔐 Login Credentials (Demo)

| Role  | Username | Password  |
|-------|----------|-----------|
| Admin | admin    | password  |
| User  | user     | password  |

---

## ✅ Features

- Clean Bootstrap-based card UI
- Submit new backup entries (date, type, tape number, batch, remarks)
- View and search all entries
- Role-based login:
  - **User** can submit and view entries
  - **Admin** can view, update, and delete entries
- Session-based access control

---

## ⚙️ Technologies Used

- **Backend:** Python, Flask, Flask-SQLAlchemy
- **Frontend:** HTML5, CSS (Bootstrap), JavaScript
- **Database:** SQLite

---

## 🛠 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/ongc-flask-app.git
   cd ongc-flask-app

2. **Create Virtual Environmnet**
   ```bash
    python3 -m venv venv
    source venv/bin/activate

3. **Install Requirements:**
   ```bash
   pip install -r requirements.txt

4. **Run the app and open it in browser(use command+click for macos):**
   ```bash
    python app.py
   http://127.0.0.1:5000
  you can also change the port number I have used the default port number as 5000 feel free to use any port number but change it in the app.py first

## File structure 
```bash
ONGC FLASK APP/
  │
  ├── static/               # Static files
  │   ├── styles.css
  │   ├── search.js
  │   └── ongc-logo.png
  │
  ├── templates/            # HTML templates
  │   ├── login.html
  │   ├── index.html
  │   ├── entries.html
  │   └── entriesadmin.html
  │
  ├── app.py                # Main Flask application
  ├── requirements.txt      # Dependency list
  ├── backupdata.db         # SQLite DB
  └── .gitignore


