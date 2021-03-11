from datetime import datetime
from ehr_analysis import Patient, Observation


def test_Patient():
    """Test Patient."""
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
    assert patient[0].sex == "Male"
    assert patient[0].race == "White"
    assert patient[0].age == 42.2
    assert patient[0].__lt__(patient[1].age)
    assert patient[1].__gt__(40.0)


def test_Observation():
    """Test Observation."""
    ID = [
        "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
        "6E70D84D-C75F-477C-BC37-9177C3698C66",
    ]
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
    assert len(record[0].LabDateTime) == 803
    assert len(record[1].LabValue) == 1529
