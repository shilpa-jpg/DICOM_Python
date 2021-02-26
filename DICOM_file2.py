import os
import pydicom
from datetime import datetime
import matplotlib.pyplot as plt


def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)


date = datetime.today().strftime('%Y%m%d')
time = datetime.today().strftime('%H%M%S')
print("Current Date:" + str(date))
print("Current Time:" + str(time))

# code to read whole folder
folder = (".\\cube_dicom_files")
for root, dirs, files in os.walk(folder):
    for file in files:
        if ".dcm" in file:
            print("Reading list of files:" +str(file))


# ******************************* Code to read single file ************************************
# file = (".\\cube_dicom_files\image0.dcm")
# ds = pydicom.dcmread(file)
# print("Dataset", ds)

# ********************************* Code to display image ****************************************
# plt.imshow(ds.pixel_array, plt.cm.bone)
# plt.show()

# PatientName = ds["PatientName"]
# PatientSex = ds["PatientSex"]
# ContentDate = ds["ContentDate"]
# ContentTime = ds["ContentTime"]
# PatientBirthDate = ds["PatientBirthDate"]
#
# PatientName.value = "John"
# PatientSex.value = "MALE"
# ContentDate.value = date
# ContentTime.value = time
#
# PatientBirthDate = datetime.strptime(PatientBirthDate.value, '%Y%m%d').strftime('%Y-%m-%d')
# date = str(datetime.today().strftime('%Y-%m-%d'))
# d = days_between(date, PatientBirthDate)
# print("Days_between current date and PatientBirthDate: ", d)
#
# age = str(int(round(d / 365, 1)))
# ds.add_new([0x0010, 0x1010], 'AS', age)
# print("+++++++++++++++++++ after changing ++++++++++++++++++++++++++++++")
# print(ds)
# ds.save_as('C:\\Users\\shilp\\DICOM_file\\out.dcm')
