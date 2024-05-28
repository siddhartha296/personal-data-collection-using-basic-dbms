from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for storing form data
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.phone}', '{self.address}')"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']

        # Wrap the database operations inside app.app_context()
        with app.app_context():
            new_user = User(name=name, email=email, phone=phone, address=address)
            db.session.add(new_user)
            db.session.commit()

        return redirect(url_for('index'))

#if __name__ == '__main__':
    # Create database tables before running the app
#    with app.app_context():
#        db.create_all()
#    app.run(debug=True)
