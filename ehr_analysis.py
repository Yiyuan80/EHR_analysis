import sqlite3
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import urllib.request
from datetime import datetime

APP = FastAPI()

patient = sqlite3.connect("biostat821.db")
cursor = patient.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS PatientInfo(ID TEXT, SEX TEXT, DOB DATE, RACE TEXT, MaritalStatus TEXT, LANGUAGE TEXT, PercentageBelowPoverty NUMERIC)"
)
cursor.execute(
    "CREATE TABLE IF NOT EXISTS LabInfo(ID TEXT, AdmissionId INTERGER, LabName TEXT, LabValue DECIMAL, LabUnit TEXT, LabDateTime DATE)"
)
patient.commit()
patient.close()


class URL(BaseModel):
    url: str


class Lab(BaseModel):
    lab_name: str
    lab_value: float


@APP.post("/patients")
def upload_patients(link: URL):
    """Upload patients files by providing URLs."""
    with urllib.request.urlopen(link.url) as response:
        patient_data = []
        for line in response:
            line = line.decode("utf-8")
            row = line.strip("\r\n").replace("\t", ",")
            item = row.split(",")
            patient_data.append(item)
    patient = sqlite3.connect("biostat821.db")
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO patient_data VALUES (?, ?, ?, ?, ?, ?, ?)", patient_data
    )
    patient.commit()
    patient.close()
    return "Patient data uploaded."


@APP.post("/labs")
def upload_labs(link: URL):
    """Upload labs files by providing URLs."""
    with urllib.request.urlopen(link.url) as response:
        lab_data = []
        for line in response:
            line = line.decode("utf-8")
            row = line.strip("\r\n").replace("\t", ",")
            item = row.split(",")
            lab_data.append(item)
    patient = sqlite3.connect("biostat821.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO lab_data VALUES (?, ?, ?, ?, ?, ?)", lab_data)
    patient.commit()
    patient.close()
    return "Lab data uploaded."


@APP.get("/patients/{id}")
def get_patientInfo(id: str):
    """Return patient infomation according to given ID."""
    patient = sqlite3.connect("biostat821.db")
    cursor = patient.cursor()
    cursor.execute("SELECT * FROM PatientInfo where ID='{id}'")
    results = cursor.fetchone()
    if results is None:
        raise HTTPException(404, f"{id} does not exit.")
    cursor.close()
    patinetInfo = {
        "ID": results[0],
        "Sex": results[1],
        "DateOfBirth": results[2],
        "Race": results[3],
        "MaritalStatus": results[4],
        "Language": results[5],
    }
    return patinetInfo


@APP.get("/patients/{id}/labs")
def get_labData(id: str):
    """Return lab data according to given ID."""
    patient = sqlite3.connect("biostat821.db")
    cursor = patient.cursor()
    cursor.execute("SELECT * FROM LabInfo where ID='{id}'")
    results = []
    for line in cursor.fetchall():
        results.append(
            {
                "ID": line[1],
                "LabName": line[2],
                "Labvalue": line[3],
                "Labunits": line[4],
                "Labdatetime": line[5],
            }
        )
    patient.close()
    return results


@APP.get("/num_older_than")
def num_older_than(age: float) -> int:
    """Return the number of patients whose ages are older than the input age."""
    try:
        float(age)
    except ValueError:
        print("'{age}' is not a number.")
    patient = sqlite3.connect("biostat821.db")
    cursor = patient.cursor()
    cursor.execute("SELECT DOB FROM PatientInfo")
    now = datetime.now()
    sum = 0
    for line in cursor.fetchall()[1:]:
        DOB = datetime.strptime(line[0], "%Y-%m-%d %H:%M:%S.%f")
        ages = round(((now - birthday).days) / 365, 1)
        if ages > age:
            sum += 1
    patient.close()
    return sum


@APP.get("/sick_patients")
def sick_patients(lab_name: str, operator: str, lab_value: float):
    """Return the IDs of the sick patients."""
    if not isinstance(lab_name, str):
        raise TypeError(f"{lab_name} is not a str.")
    if operator == "<" or operator == ">":
        pass
    else:
        print("The input operator is invalid.")
        return False
    if not isinstance(lab_value, float):
        raise TypeError(f"{lab_value} is not a float.")
    patient = sqlite3.connect("biostat821.db")
    cursor = patient.cursor()
    cursor.execute(f"SELECT ID, LabValue FROM LabInfo WHERE LabName='{lab_name}'")
    sick_patients = []
    for line in cursor.fetchall():
        if operator == "<":
            if line[1] < lab_value:
                sick_patients.append(line[0])
        else:
            if line[1] > lab_value:
                sick_patients.append(line[0])
    patient.close()
    return list(set(sick_patients))
