# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home():

#     applications = [
#         ("IBM", "ASE", "23-06-2026", "Applied"),
#         ("Infosys", "SE", "20-06-2026", "Rejected")
#     ]

#     return render_template(
#         "index.html",
#         applications=applications
#     )

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, render_template

from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():

    conn = sqlite3.connect("data/database.db")

    cursor = conn.cursor()

    cursor.execute("SELECT id, company, role, date_applied, status FROM applications")

    applications = cursor.fetchall()

    conn.close()

    return render_template(
        "index.html",
        applications=applications
    )


@app.route("/add", methods=["GET", "POST"])
def add_application():

    if request.method == "POST":
        id = request.form["id"]
        company = request.form["company"]
        role = request.form["role"]
        date_applied = request.form["date_applied"]
        status = request.form["status"]
        notes = request.form["notes"]

        conn = sqlite3.connect("data/database.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO applications
        (id, company, role, date_applied, status, notes)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (id, company, role, date_applied, status, notes))

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add.html")

@app.route("/delete/<int:id>")
def delete_application(id):

    conn = sqlite3.connect("data/database.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM applications WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_application(id):

    conn = sqlite3.connect("data/database.db")
    cursor = conn.cursor()

    if request.method == "POST":

        company = request.form["company"]
        role = request.form["role"]
        date_applied = request.form["date_applied"]
        status = request.form["status"]
        notes = request.form["notes"]

        cursor.execute("""
        UPDATE applications
        SET company=?,
            role=?,
            date_applied=?,
            status=?,
            notes=?
        WHERE id=?
        """, (
            company,
            role,
            date_applied,
            status,
            notes,
            id
        ))

        conn.commit()
        conn.close()

        return redirect("/")

    cursor.execute(
        "SELECT * FROM applications WHERE id=?",
        (id,)
    )

    app_data = cursor.fetchone()

    conn.close()

    return render_template(
        "edit.html",
        app=app_data
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)