"""
basic flask app that serves a webpage
"""
from flask import Flask, render_template, request
from read_file import read_csv, read_json

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == "json":
        if not product_id:
            return render_template('product_display.html', products=read_json('products.json'))

        product = read_json('products.json', product_id)
        if product and not isinstance(product, str):
            return render_template('product_display.html', products=product)

        return render_template('product_display.html', error="Product not found")
    
    elif source == "csv":
        if not product_id:
            return render_template('product_display.html', products=read_csv('products.csv'))
        
        product = read_csv('products.csv', product_id)
        if product and not isinstance(product, str):
            return render_template('product_display.html', products=product)

        return render_template('product_display.html', error="Product not found")
    
    else:
        return render_template('product_display.html', error="Wrong source")

if __name__ == '__main__':
    app.run(debug=True, port=5000)