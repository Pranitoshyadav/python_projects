grade = {
    "Ram" : 80,
    "Sita" : 70,
    "Rohan" : 40,
    "Ahvhis" : 90,
    "Pranitosh" : 95
}

for i in range(1):
   total_grade = int((grade["Pranitosh"] + grade["Ahvhis"] + grade["Rohan"] + grade["Sita"] + grade["Ram"])/5)
   print("The avrage grade is : ", total_grade)
   print("The minimum grade is : ", int(min(total_grade)))
   print("the maxumum grade is : ", int(max(total_grade)))

