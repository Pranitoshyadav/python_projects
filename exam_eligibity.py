
# 1) Ask the student if they had a medical cause and store the answer in `medical_cause`.

# (Also clean the input so it becomes either 'Y' or 'N'.)

# 2) If `medical_cause` is 'Y':

# - Print that the student is allowed to attend the exam.

# 3) Otherwise (medical_cause is 'N'):

# a) Ask for the student’s attendance percentage and store it in `atten`.

# b) If `atten` is 75 or more:

# - Print "Allowed"

# c) Else:

# - Print "Not allowed"
meducal_cause = input("enter a medical cause (type yes(Y) or no(N)) : ")

if meducal_cause == "Y" :
    print("you are allowed in the test")
else :
    atten = int(input("enter your attendence percentage : "))

    if atten >= 75:
        print("allowed")
    else :
        print("Not allowed")