from flask import Flask, render_template, request

app = Flask(__name__)

users=[
    {"user":"waga","email":"waga@gmail.com"},
    {"user":"baga","email":"baga@gmail.com"},
    {"user":"gaga","email":"gaga@gmail.com"}
]


@app.route('/index')
def index():
    # print(users[0]["email"])
    clr = request.args.get('clr')
    selected_user = request.args.get('selected')
    return render_template("index.html",clr=clr,users=users,selected_user=selected_user)

    

if __name__ == '__main__':
    app.run(debug=True)
