# EHR_analysis
## setup instructions
`ehr_analysis` includes 2 classes: `Patient` and `Observation`.

`Patient` is oriented towards patient's basic information. It has 1 instance atrributes: ID. It also includes 4 properties: `sex`, `DOB`, `race`, `age`, and 3 functions: `__gt__`, `__lt__` and `plot`.

`Patient.sex` returns patient's sex and it is a property.

`Patient.DOB` returns patient's birthday and it is a property.

`Patient.race` returns patient's race and it is a property.

`Patient.age` calculates the patient's age in float and it is a property.

`Patient.__gt__(value)` returns whether the patient's age is greater than the input value. The input `value` should be a float.

`Patient.__lt__(value)` returns whether the patient's age is less than the input value. The input argument `value` should be a float.

`Patient.plot(LabName, Filename)` plots the patient's lab value over time and saves the image as the input filename. The input arguments `LabName` and `Filename` should be strings.

`Observation` is oriented towards patient's lab record. It has 1 instance atrributes: ID and 4 properties: `LabName`, `LabValue`, `LabUnit`, `LabDateTime`.

## examples
```python
>> patient1 = Patient("1A8791E3-A61C-455A-8DEE-763EB90C9B2C")
>> patient1.sex
Male

>> patient1.race
Asian

>> patient1.age
47.7

>> patient1.sex__lt__(50.0)
True

>> Patient().plot("URINALYSIS: PH", "ph_over_time.png")
```

## testing instructions
`test_ehr_analysis.py` includes 2 functions to test `Patient` and `Observation`: `test_Patient` and `test_Observation`. To test your functions in the two classes, you need to add test function in `test_ehr_analysis.py` and run `pytest test_ehr_analysis.py` in your terminal.