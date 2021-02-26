# Add support to calculate the patient age based on the PatientBirthDate and 
# StudyDate (including error handling for invalid BirthDate
#  (i.e. in the future or more than 100 years old) and handling for leap year)

from datetime import datetime
import pydicom


def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)


file = ".\\different_birthdate_dicom_files\image10_28021985.dcm"
ds = pydicom.read_file(file)
print("Dataset", ds)

PatientBirthDate = ds["PatientBirthDate"]
PatientBirthDate = datetime.strptime(PatientBirthDate.value, '%Y%m%d').strftime('%Y-%m-%d')
date = str(datetime.today().strftime('%Y-%m-%d'))
d = days_between(date, PatientBirthDate)
print("Days_between current date and PatientBirthDate: ", d)

try:
    year = PatientBirthDate[0:4]
    age = str(int(round(d / 365, 1)))
    if int(age) <= 100 or year % 100 == 0:
        ds.add_new([0x0010, 0x1010], 'AS', age)
        print(ds)
        print("Patient age is valid and not in a leap year:", age, str(year))

except Exception as InvalidAge:
    age = str(int(round(d / 366, 1)))
    if int(age) > 100 or year % 4 == 0 and year % 100 != 0:
        print("Patient age is not valid or in leap year", InvalidAge, age, str(year))
