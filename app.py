from flask import Flask, render_template, request, redirect, session, url_for
#vulnerability #3, generating a random secret key for CSRF protection
from flask_wtf import CSRFProtect
import psycopg2
from config import DB_CONFIG, SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY


def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cur = conn.cursor()
        #fix to vulnerability #1
        cur.execute("SELECT id, password FROM users WHERE username = %s", (username,))
        user = cur.fetchone()

        cur.close()
        conn.close()

        if user and password == user[1]:
            session["user_id"] = user[0]
            return redirect(url_for("dashboard"))

        return "Invalid credentials", 401

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    #vulnerability #4, setting debug to False for production to prevent executing code
    app.run(debug=False)

