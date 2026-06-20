import sqlite3
import random
import time

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

patients = [
    "Patient 1",
    "Patient 2",
    "Patient 3"
]

while True:

    for patient in patients:

        hr = random.randint(70,110)
        spo2 = random.randint(92,99)
        temp = round(random.uniform(36.0,38.5),1)

        cursor.execute("""
        INSERT INTO patients
        (patient_name,heart_rate,spo2,temperature)
        VALUES (?,?,?,?)
        """,
        (patient,hr,spo2,temp))

        conn.commit()

        print(patient, hr, spo2, temp)

    time.sleep(2)