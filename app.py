from flask import Flask, render_template, request

app = Flask(__name__)

products=["cola","milk","pizza","xl","blue","xxl"]


@app.route('/index')
def index():
    return render_template("index.html",prods=products)

    

if __name__ == '__main__':
    app.run(debug=True)
