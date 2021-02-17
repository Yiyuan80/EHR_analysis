from datetime import datetime
from ehr_analysis import load_patients,load_labs,num_older_than, sick_patients,first_admission_age

def test_load_patients():
    """Test load_patients()."""
    result = load_patients("PatientCorePopulatedTable.txt")
    assert len(result) == 100

def test_load_labs():
    """Test load_labs()."""
    result = load_labs("LabsCorePopulatedTable.txt")
    assert len(result) == 111483

def test_num_older_than():
    """Test num_older_than()."""
    patient = {
        "a": {"Birthday": datetime.strptime("2020-02-09 00:00:00.00", "%Y-%m-%d %H:%M:%S.%f")},
        "b": {"Birthday": datetime.strptime("1920-02-09 00:00:00.00", "%Y-%m-%d %H:%M:%S.%f")},
        "c": {"Birthday": datetime.strptime("1920-02-09 00:00:00.00", "%Y-%m-%d %H:%M:%S.%f")},
    }
    assert num_older_than(patient, 50) == 2

def test_sick_patients():
    """Test sick_patients()."""
    labs_data = [
        ("Bob", "URINALYSIS: PH", "4.9"),
        ("Bob", "URINALYSIS: PH", "5.2"),
        ("Stacy", "URINALYSIS: PH", "4.2"),
    ]
    result = sick_patients(labs_data, "URINALYSIS: PH", ">", 4.5)
    assert result[0] == "Bob"

def test_first_adimission_age():
    """Test first_adimission_age()."""
    patient = {
        "a": {"Birthday": datetime.strptime("1987-02-09 00:00:00.00", "%Y-%m-%d %H:%M:%S.%f")},
        "b": {"Birthday": datetime.strptime("1998-08-01 00:00:00.00", "%Y-%m-%d %H:%M:%S.%f")},
        "c": {"Birthday": datetime.strptime("1990-03-19 00:00:00.00", "%Y-%m-%d %H:%M:%S.%f")},
    }
    labs_data = [
        ("a", "URINALYSIS: PH", "4.9",datetime.strptime("2009-02-09 00:00:00.00", "%Y-%m-%d %H:%M:%S.%f")),
        ("b", "URINALYSIS: PH", "5.2",datetime.strptime("2018-08-09 00:00:00.00", "%Y-%m-%d %H:%M:%S.%f")),
        ("c", "URINALYSIS: PH", "4.2",datetime.strptime("2019-09-09 00:00:00.00", "%Y-%m-%d %H:%M:%S.%f")),
    ]
    result = first_admission_age(patient,labs_data,"b")
    assert result == 20