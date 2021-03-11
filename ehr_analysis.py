""" load data and conduct data analysis"""
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd


class Patient:
    """Patient."""

    def __init__(self, ID, sex, DOB, race):
        """Initalize."""
        self.ID = ID
        self.sex = sex
        self.DOB = DOB
        self.race = race

    @property
    def age(self):
        """Calculate patient's age."""
        now = datetime.now()
        birthday = self.DOB
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
        """Plotting."""
        if not isinstance(LabName, str):
            raise ValueError(f"{LabName} is not a string.")
        if not isinstance(Filename, str):
            raise ValueError(f"{Filename} is not a string.")
        rec = dict()
        with open("LabsCorePopulatedTable.txt", "r") as f:
            lines = f.readlines()[1:]
            rec["LabName"] = []
            rec["LabValue"] = []
            rec["LabUnit"] = []
            rec["LabDateTime"] = []
            for line in lines:
                words = line.strip().split("\t")
                if words[0] == self.ID:
                    rec["LabName"].append(words[2])
                    rec["LabValue"].append(float(words[3]))
                    rec["LabUnit"].append(words[4])
                    DateTime = datetime.strptime(words[5], "%Y-%m-%d %H:%M:%S.%f")
                    rec["LabDateTime"].append(DateTime)
            patient_rec = pd.DataFrame(rec)
            plot_data = patient_rec.loc[patient_rec["LabName"] == LabName]
            x = plot_data["LabDateTime"]
            y = plot_data["LabValue"]
        plt.scatter(x, y)
        plt.title(f"{self.ID}: {LabName}")
        plt.xlabel("Time")
        plt.ylabel(f"{LabName}")
        plt.savefig(Filename)


class Observation:
    """Observation values."""

    def __init__(self, ID, LabName, LabValue, LabUnit, LabDateTime):
        """Initalize."""
        self.ID = ID
        self.LabName = LabName
        self.LabValue = LabValue
        self.LabUnit = LabUnit
        self.LabDateTime = LabDateTime


if __name__ == "__main__":
    ID = [
        "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
        "6E70D84D-C75F-477C-BC37-9177C3698C66",
    ]
    patient = []
    with open("PatientCorePopulatedTable.txt", "r") as f:
        lines = f.readlines()[1:]
        for line in lines:
            words = line.strip().split("\t")
            for i in range(0, len(ID)):
                if words[0] == ID[i]:
                    sex = words[1]
                    DOB = datetime.strptime(words[2], "%Y-%m-%d %H:%M:%S.%f")
                    race = words[3]
                    patient.append(Patient(ID[i], sex, DOB, race))

    record = []
    with open("LabsCorePopulatedTable.txt", "r") as f:
        lines = f.readlines()[1:]
        for i in range(0, len(ID)):
            LabName = []
            LabValue = []
            LabUnit = []
            LabDateTime = []
            for line in lines:
                words = line.strip().split("\t")
                if words[0] == ID[i]:
                    LabName.append(words[2])
                    LabValue.append(float(words[3]))
                    LabUnit.append(words[4])
                    DateTime = datetime.strptime(words[5], "%Y-%m-%d %H:%M:%S.%f")
                    LabDateTime.append(DateTime)
            Record = Observation(ID, LabName, LabValue, LabUnit, LabDateTime)
            record.append(Record)

    # print(patient[0].age)
    # print(patient[1].age)
    # print(patient[1].__gt__(40.0))
    # print(len(record[1].LabValue))
    # print(record[0].LabDateTime)
    # patient[0].plot("URINALYSIS: PH", "ph_over_time.png")
