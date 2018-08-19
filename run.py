from flask import Flask, render_template, url_for, request
from form import Contact

app = Flask(__name__)
app.config['SECRET_KEY'] = '3421043ec1282e6a6c6d7e5e273d644f'

@app.route('/')
def index():
	return render_template('index.html', title='Home | E-Commerce')

@app.route('/products')
def products():
	return render_template('products.html', title='products | E-Commerce')


@app.route('/about')
def about():
	return render_template('about.html', title='About Us | E-Commerce')


@app.route('/contact', methods=('GET', 'POST'))
def contact():
	form = Contact()
	if form.validate_on_submit():
		return "hello"
		#return render_template('contact.html', title='contact Us | E-Commerce', form=form)
	else:
		return "i don't work"

if __name__ == '__main__':
	app.run(debug=True)