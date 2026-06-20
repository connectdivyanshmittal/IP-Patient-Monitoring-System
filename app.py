from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

def get_latest_data():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM patients
    ORDER BY id DESC
    LIMIT 20
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/api/data")
def api_data():
    rows = get_latest_data()

    data = []

    for row in rows:
        data.append({
            "id": row[0],
            "patient": row[1],
            "hr": row[2],
            "spo2": row[3],
            "temp": row[4],
            "time": row[5]
        })

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)