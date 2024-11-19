from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    old_fruits = [
        {"name": "apples", "quantity": 3},
            {"name": "oranges", "quantity": 2},
            {"name": "strawberries", "quantity": 6}
    ]

    fruits = []
    for fruit in old_fruits:
       curr = fruit["name"][0]
       if curr.lower() == 'o' and fruit["quantity"] < 3:
           fruits.append(fruit)

    return render_template("index.html", fruits=fruits)
