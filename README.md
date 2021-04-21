# EHR_analysis
## setup instructions
`ehr_analysis` includes 6 functions: `upload_patients`, `upload_labs`, `get_patientInfo`, `get_labData`, `num_older_than` and `sick_patients`.

`upload_patients` uploads patients files to the provided url.

`upload_labs` uploads labs files to the provided url.

`get_patientInfo` returns patient infomation according to given ID.

`get_labData` returns lab data according to given ID.

`num_older_than` returns the number of patients whose ages are older than the input age.

`sick_patients` returns the IDs of the sick patients.

## examples
* uploading patients and labs files by providing URLs
```bash
> curl -X POST http://localhost/patients -d "{\"url\": \"http://biostat821.colab.duke.edu/patients.txt\"}"
> curl -X POST http://localhost/labs -d "{\"url\": \"http://biostat821.colab.duke.edu/labs.txt\"}"
```

* accessing specific patients by providing their ids
  ```bash
  > curl -X GET http://localhost/patients/FB2ABB23-C9D0-4D09-8464-49BF0B982F0F
  {
    "gender": "Male",
    "DOB": "1947-12-28 02:45:40.547",
    "race": "Unknown",
    "marital_status": "Married",
    "language": "Icelandic",
    "population_percentage_below_poverty": 18.08
  }
  ```

* accessing labs belonging to each patient
  ```bash
  > curl -X GET http://localhost/patients/FB2ABB23-C9D0-4D09-8464-49BF0B982F0F/labs
  [
    {
      "admission_id": 1,
      "name": "URINALYSIS: RED BLOOD CELLS",
      "value": 3.1,
      "units": "rbc/hpf",
      "datetime": "1968-10-07 14:41:30.843"
    },
    ...
  ]
  ```

* other analytics capabilities
  ```bash
  > curl -X GET http://localhost/num_older_than?age=51.2
  54
  > curl -X GET http://localhost/sick_patients?lab_name=METABOLIC%3A%20ALBUMIN&operator=%3C&lab_value=4.0
  ["FB2ABB23-C9D0-4D09-8464-49BF0B982F0F", "64182B95-EB72-4E2B-BE77-8050B71498CE"]
