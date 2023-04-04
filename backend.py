from flask import Flask, render_template, request, session, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)


app.config['MONGO_URI'] = 'mongodb://localhost:27017/bike_selling_website'
mongo = PyMongo(app)


app.secret_key = 'bike selling website'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bikes')
def bikes():
    bikes = mongo.db.bikes.find()
    return render_template('bikes.html', bikes=bikes)

@app.route('/bikes/<id>')
def bike(id):
    bike = mongo.db.bikes.find_one({'_id': ObjectId(id)})
    return render_template('bike.html', bike=bike)

@app.route('/add_bike', methods=['GET', 'POST'])
def add_bike():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        image = request.form['image']

        mongo.db.bikes.insert_one({
            'name': name,
            'description': description,
            'price': price,
            'image': image
        })

        return redirect(url_for('bikes'))
    else:
        return render_template('add_bike.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']})
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({
                'username': request.form['username'],
                'password': hashpass
            })
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            return 'That username already exists!'
    else:
        return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'username': request.form['username']})
        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('index'))
            else:
                return 'Invalid username/password combination'
        else:
            return 'Invalid username/password combination'
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

# Start server
if __name__ == '__main__':
    app.run(debug=True)
