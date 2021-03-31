from datetime import datetime
from ehr_analysis import Patient, Observation


def test_Patient():
    """Test Patient."""
    ID = "1A8791E3-A61C-455A-8DEE-763EB90C9B2C"
    patient1 = Patient(ID)
    assert patient1.sex == "Male"
    assert patient1.race == "Asian"
    assert patient1.age == 47.7
    assert patient1.__lt__(50.0)


def test_Observation():
    """Test Observation."""
    ID = "1A8791E3-A61C-455A-8DEE-763EB90C9B2C"
    observation1 = Observation(ID)
    assert len(observation1.LabValue) == 803
    assert observation1.LabUnit[0][0] == "rbc/hpf"
