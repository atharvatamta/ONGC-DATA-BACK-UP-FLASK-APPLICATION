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
