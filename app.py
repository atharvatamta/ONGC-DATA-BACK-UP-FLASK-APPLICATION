from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from flask import flash  # at top



app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure key

# DB Setup
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'backupdata.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# DB Model
class BackupEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    tape = db.Column(db.String(50), nullable=False)
    batch = db.Column(db.String(50), nullable=False)
    remarks = db.Column(db.Text, nullable=True)

# Login route (default landing page)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            session['user'] = username
            return redirect(url_for('index'))
        return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

# Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# Protected entry form
@app.route('/index')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

# Submit form
@app.route('/submit', methods=['POST'])
def submit():
    if 'user' not in session:
        return redirect(url_for('login'))

    date = request.form['date']
    type_ = request.form['type']
    tape = request.form['tape']
    batch = request.form['batch']
    remarks = request.form['remarks']

    new_entry = BackupEntry(date=date, type=type_, tape=tape, batch=batch, remarks=remarks)
    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for('index'))

# View entries
@app.route('/entries')
def entries():
    if 'user' not in session:
        return redirect(url_for('login'))

    q = request.args.get('q', '').lower()
    if q:
        results = BackupEntry.query.filter(
            BackupEntry.type.ilike(f"%{q}%") |
            BackupEntry.tape.ilike(f"%{q}%") |
            BackupEntry.batch.ilike(f"%{q}%") |
            BackupEntry.remarks.ilike(f"%{q}%")
        ).all()
    else:
        results = BackupEntry.query.all()
    return render_template('entries.html', entries=results)

# AJAX search
@app.route('/search')
def search():
    q = request.args.get('q', '')
    results = BackupEntry.query.filter(
        BackupEntry.type.ilike(f"%{q}%") |
        BackupEntry.tape.ilike(f"%{q}%") |
        BackupEntry.batch.ilike(f"%{q}%") |
        BackupEntry.remarks.ilike(f"%{q}%")
    ).all()
    return jsonify([
        {
            'id': entry.id,
            'date': entry.date,
            'type': entry.type,
            'tape': entry.tape,
            'batch': entry.batch,
            'remarks': entry.remarks
        } for entry in results
    ])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
