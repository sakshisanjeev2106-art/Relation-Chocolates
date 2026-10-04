from flask import Flask, render_template

app = Flask(__name__)
WHATSAPP_NUMBER = "919043682788"

@app.route("/")
def home():
    return render_template(
        "index.html",
        active_page="home",
    )

@app.route("/menu")
def menu():
    return render_template(
        "menu.html",
        active_page="menu",
        whatsapp_number=WHATSAPP_NUMBER,
    )

@app.route("/contact")
def contact():
    return render_template("contact.html", active_page="contact")

if __name__ == "__main__":
    app.run(debug=True)
