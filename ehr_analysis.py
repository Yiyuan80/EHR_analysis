""" load data and conduct data analysis"""
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

# load data
patientData = sqlite3.connect("patient.db")
curPatient = patientData.cursor()
curPatient.execute(
    "CREATE TABLE IF NOT EXISTS PatientInfo(ID TEXT, SEX TEXT, DOB DATE, RACE TEXT)"
)
with open("PatientCorePopulatedTable.txt", "r") as f:
    lines = f.readlines()[1:]
    for line in lines:
        words = line.strip().split("\t")
        curPatient.execute("INSERT INTO PatientInfo VALUES (?, ?, ?, ?)", words[0:4])
curPatient.execute("CREATE INDEX PatientID ON PatientInfo(ID)")
patientData.commit()


labData = sqlite3.connect("lab.db")
curLab = labData.cursor()
curLab.execute(
    "CREATE TABLE IF NOT EXISTS PatientLab(ID TEXT, AdmissionId INTERGER, LabName TEXT, LabValue DECIMAL, LabUnit TEXT, LabDateTime DATE)"
)
with open("LabsCorePopulatedTable.txt", "r") as f:
    lines = f.readlines()[1:]
    for line in lines:
        words = line.strip().split("\t")
        # for i in range(0, len(lines)):
        curLab.execute("INSERT INTO PatientLab VALUES (?, ?, ?, ?, ?, ?)", words[0:6])
curLab.execute("CREATE INDEX PatinetID ON PatientLab(ID)")
labData.commit()


class Patient:
    """Patient."""

    def __init__(self, ID):
        """Initalize."""
        self.ID = ID

    @property
    def sex(self):
        """
        Return patient's sex.

        O(log(N))
        """
        curPatient.execute(
            f"SELECT PatientInfo.SEX FROM PatientInfo WHERE PatientInfo.ID == '{self.ID}'"
        )
        return curPatient.fetchone()[0]

    @property
    def DOB(self):
        """
        Return patient's birthday.

        O(log(N))
        """
        curPatient.execute(
            f"SELECT PatientInfo.DOB FROM PatientInfo WHERE PatientInfo.ID == '{self.ID}'"
        )
        return curPatient.fetchone()[0]

    @property
    def race(self):
        """
        Return patient's race.

        O(log(N))
        """
        curPatient.execute(
            f"SELECT PatientInfo.RACE FROM PatientInfo WHERE PatientInfo.ID == '{self.ID}'"
        )
        return curPatient.fetchone()[0]

    @property
    def age(self):
        """
        Calculate patient's age.

        O(log(N))
        """
        now = datetime.now()
        birthday = datetime.strptime(self.DOB, "%Y-%m-%d %H:%M:%S.%f")
        Age = round(((now - birthday).days) / 365, 1)
        return Age

    def __lt__(self, value):
        """Less than."""
        if not isinstance(value, float):
            raise ValueError(f"{value} is not a float.")
        if self.age < value:
            return True
        return False

    def __gt__(self, value):
        """greater than."""
        if not isinstance(value, float):
            raise ValueError(f"{value} is not a float.")
        if self.age > value:
            return True
        return False

    def plot(self, LabName, Filename):
        """
        Plotting.

        O(Nlog(N))
        """
        if not isinstance(LabName, str):
            raise ValueError(f"{LabName} is not a string.")
        if not isinstance(Filename, str):
            raise ValueError(f"{Filename} is not a string.")
        Value = []
        DateTime = []
        LabValue = curLab.execute(
            f"SELECT PatientLab.LabValue From PatientLab WHERE PatientLab.ID == '{self.ID}' and PatientLab.LabName == '{LabName}'"
        ).fetchall()
        for i in LabValue:
            Value.append(i[0])
        LabDateTime = curLab.execute(
            f"SELECT PatientLab.LabDateTime From PatientLab WHERE PatientLab.ID == '{self.ID}' and PatientLab.LabName == '{LabName}'"
        ).fetchall()
        for i in LabDateTime:
            DateTime.append(datetime.strptime(i[0], "%Y-%m-%d %H:%M:%S.%f"))
        plt.scatter(DateTime, Value)
        plt.title(f"{self.ID}: {LabName}")
        plt.xlabel("Time")
        plt.ylabel(f"{LabName}")
        plt.savefig(Filename)


class Observation:
    """Observation values."""

    def __init__(self, ID):
        """Initalize."""
        self.ID = ID

    @property
    def LabName(self):
        """
        Return patient's LabName.

        O(log(N))
        """
        curLab.execute(
            f"SELECT PatientLab.LabName FROM PatientLab WHERE PatientLab.ID == '{self.ID}'"
        )
        return curLab.fetchall()[0]

    @property
    def LabValue(self):
        """
        Return patient's LabValue.

        O(log(N))
        """
        curLab.execute(
            f"SELECT PatientLab.LabValue FROM PatientLab WHERE PatientLab.ID == '{self.ID}'"
        )
        return curLab.fetchall()

    @property
    def LabUnit(self):
        """
        Return patient's LabUnit.

        O(log(N))
        """
        curLab.execute(
            f"SELECT PatientLab.LabUnit FROM PatientLab WHERE PatientLab.ID == '{self.ID}'"
        )
        return curLab.fetchall()

    @property
    def LabDateTime(self):
        """
        Return patient's LabDateTime.

        O(log(N))
        """
        curLab.execute(
            f"SELECT PatientLab.LabDateTime FROM PatientLab WHERE PatientLab.ID == '{self.ID}'"
        )
        return curLab.fetchall()


# if __name__ == "__main__":
#     ID = "1A8791E3-A61C-455A-8DEE-763EB90C9B2C"
#     patient1 = Patient(ID)
#     patient1.plot("URINALYSIS: PH", "ph_over_time.png")
#     print(patient1.sex)
#     print(patient1.DOB)
#     print(patient1.race)
#     print(patient1.age)
#     print(patient1.__lt__(50.0))
#     observation1 = Observation(ID)
#     print(len(observation1.LabValue))
#     print(observation1.LabUnit[0][0])
