""" load data and conduct data analysis"""
from datetime import datetime

## Initialization
def load_patients(filename):
    '''The computational complexity of initialization is O(n)'''
    if not isinstance(filename,str):
        raise IOError(f"{filename} is not a string.")
    try:
        with open(filename,'r') as f:
            patients=dict()
            lines=f.readlines()[1:]
            for line in lines:
                words=line.strip().split('\t')
                ID=words[0]
                birthday=datetime.strptime(words[2], "%Y-%m-%d %H:%M:%S.%f")
                patients[f"{ID}"]={"Birthday":birthday}
        return patients
    except:
        raise IOError(f"{filename} has wrong format.")

def load_labs(filename):
    if not isinstance(filename,str):
        raise IOError(f"{filename} is not a string.")
    try:
        with open(filename,'r') as f:
            patients_record=[]
            lines=f.readlines()[1:]
            for line in lines:
                words=line.strip().split('\t')
                PatientID=words[0]
                LabName=words[2]
                LabValue=words[3]
                LabDateTime=datetime.strptime(words[5], "%Y-%m-%d %H:%M:%S.%f")
                record=(PatientID,LabName,LabValue,LabDateTime)
                patients_record.append(record)
        return patients_record
    except:
        raise IOError(f"{filename} has wrong format.")
## Capabilities
### Old patients

def num_older_than(patient,age):
    '''the compuatational complexity of old_patient function at runtime is O(n)'''
    if not isinstance(patient,dict):
        raise TypeError(f"{patient} is not a dictionary.")
    if not isinstance(age, (int,float)):
        raise TypeError(f"{age} should be integer or float.")
    try:
        now = datetime.now() 
        sum=0
        for key,value in patient.items():
            birthday = value['Birthday']
            ages = round(((now - birthday).days)/365,1)
            if ages > age:
                sum+=1
        return sum
    except:
        raise IOError(f"{patient} has wrong format.")

### Sick patients

def sick_patients(labs, lab, gt_lt, value):
    '''The compuatational complexity of sick_patient function at runtime is O(n)'''
    if not isinstance(labs,list):
        raise TypeError(f"{labs} is not a list.")
    if not isinstance(lab,str):
        raise TypeError(f"{lab} is not a string.")
    if not isinstance(gt_lt,str):
        raise TypeError(f"{gt_lt} is not a string.")
    if not isinstance(value, (int,float)):
        raise TypeError(f"{value} should be integer or float.")
    try:
        PatientsList=[]    
        for record_tuple in labs:
            if record_tuple[1] == lab:
                criteria= record_tuple[2]+gt_lt+str(value)
                if eval(criteria) == True:
                    PatientsList.append(record_tuple[0])
        return list(set(PatientsList))
    except:
        raise IOError(f"{labs} has wrong format.")

def first_admission_age(patients,labs,PatientID):
    if not isinstance(patients,dict):
        raise TypeError(f"{patients} is not a dictionary.")
    if not isinstance(labs,list):
        raise TypeError(f"{labs} is not a list.")
    if not isinstance(PatientID,str):
        raise TypeError(f"{PatientID} is not a string.")
    try:
        birthday = patients[f'{PatientID}']['Birthday']
        AgeList = []
        for record_tuple in labs:
            if record_tuple[0] == PatientID:
                age = round(((record_tuple[3]-birthday).days)/365,1)
                AgeList.append(age)
        return min(AgeList)
    except:
        raise IOError("Input data have wrong formats.")
        
if __name__ == "__main__":
    patients = load_patients("PatientCorePopulatedTable.txt")
    print(num_older_than(patients,51.2))
    # print(len(patients))
    labs=load_labs("LabsCorePopulatedTable.txt")
    # print(len(labs))
    print(sick_patients(labs,"METABOLIC: ALBUMIN", ">", 4.0))
    print(first_admission_age(patients,labs,"1A8791E3-A61C-455A-8DEE-763EB90C9B2C"))
