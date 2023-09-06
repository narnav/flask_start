from flask import Flask, render_template, request

app = Flask(__name__)

products=["cola","milk","pizza","xl","blue","xxllllllll"]
cart=[]

@app.route('/index')
def index():
    cart.append(products[int(request.args.get('selected'))])
    return render_template("index.html",prods=products,cart=cart)

if __name__ == '__main__':
    app.run(debug=True)