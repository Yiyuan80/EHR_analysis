# EHR_analysis
## setup instructions
`ehr_analysis` includes 2 classes: `Patient` and `Observation`.

`Patient` is oriented towards patient's basic information. It has 4 instance atrributes: ID, sex, DOB, race. It also includes 4 functions: `age`, `__gt__`, `__lt__` and `plot`.

`Patient.age` calculates the patient's age in float and it is a property.

`Patient.__gt__(value)` returns whether the patient's age is greater than the input value. The input `value` should be a float.

`Patient.__lt__(value)` returns whether the patient's age is less than the input value. The input argument `value` should be a float.

`Patient.plot(LabName, Filename)` plots the patient's lab value over time and saves the image as the input filename. The input arguments `LabName` and `Filename` should be strings.

`Observation` is oriented towards patient's lab record. It has 5 instance atrributes: ID, LabName, LabValue, LabUnit, LabDateTime.

## examples
```python
>> Patient("1A8791E3-A61C-455A-8DEE-763EB90C9B2C", 'Male', datetime.strptime('1979-01-04 05:45:29.580000', "%Y-%m-%d %H:%M:%S.%f"), 'White').age
42.2

>> Patient("1A8791E3-A61C-455A-8DEE-763EB90C9B2C", 'Male', datetime.strptime('1979-01-04 05:45:29.580000', "%Y-%m-%d %H:%M:%S.%f"), 'White').__gt__(40.0)
True

>> Patient("1A8791E3-A61C-455A-8DEE-763EB90C9B2C", 'Male', datetime.strptime('1979-01-04 05:45:29.580000', "%Y-%m-%d %H:%M:%S.%f"), 'White').__lt__(40.0)
False

>> Patient().plot("URINALYSIS: PH", "ph_over_time.png")
```

## testing instructions
`test_ehr_analysis.py` includes 2 functions to test `Patient` and `Observation`: `test_Patient` and `test_Observation`. To test your functions in the two classes, you need to add test function in `test_ehr_analysis.py` and run `pytest test_ehr_analysis.py` in your terminal.