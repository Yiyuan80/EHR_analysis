# EHR_analysis
## setup instructions
`ehr_analysis` includes 5 modules: load_patients, load_labs, num_older_than,  sick_patients, first_admission_age.

`load_patients(filename)`: reads patients' information and returns a dictionary that includes patients' ID and birthday. `filename` shoule be a string.

`load_labs(filename)`: reads patients' lab record and returns a list that includes patients' ID, lab name, lab value and lab date time. `filename` shoule be a string.

`num_older_than(patient,age)`: returns the number of patients older than a given age (in years). `patient` should be a dictionary. `age` should be integer or float.

`sick_patients(labs, lab, gt_lt, value)`: returns a (unique) list of patients who have a given test with value above (">") or below ("<") a given level. `labs` should be a list. `lab` and `gt_lt` should be string type. `value` should be integer or float.

`first_admission_age(patients,labs,PatientID)`: computes the age at first admission of any given patient. `patients` should be a dictionary. `labs` should be a list. `PatientID` should be a string.

## examples
```python
>> patients = load_patients("PatientCorePopulatedTable.txt")

>>labs = load_labs("LabsCorePopulatedTable.txt")

>> num_older_than(patients, 51.2)
75

>> sick_patients(labs,"METABOLIC: ALBUMIN", ">", 4.0)
['C54B5AAD-98E8-472D-BAA0-638D9F3BD024', '69B5D2A0-12FD-46EF-A5FF-B29C4BAFBE49',...]

>>first_admission_age(patients,labs,"1A8791E3-A61C-455A-8DEE-763EB90C9B2C")
18.9
```
## testing instructions
To test your functions, you need to add test function in `test_ehr_analysis.py` and use pytest.