from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leather_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    # photo_product = db.Column(db.String(80), unique=True, nullable=False)
    color = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(400), unique=True, nullable=False)
    stock = db.Column(db.Integer, unique=True, nullable=False)
    rating = db.Column(db.Integer, unique=True, nullable=False)
    price = db.Column(db.Integer, unique=True, nullable=False)
    review = db.Column(db.String(300), unique=True, nullable=False)

    def __repr__(self):
        return self.title

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/delivery')
def delivery():
    return render_template('delivery.html')

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method=='POST':
        title = request.form['title']
        price = request.form['price']
        color = request.form['color']
        description = request.form['description']
        stock = request.form['stock']
        rating = request.form['rating']
        review = request.form['review']

        item = Product(title=title, price=price, color=color, description=description, stock=stock, rating=rating, review=review)
        try:
            
            db.session.add(item)
            db.session.commit()
            print('lllllll')
            return redirect('/')
        except:
            return 'Произошла ошибка'

    else:
        return render_template('create.html')






if __name__=="__main__":
    app.run(debug=True)