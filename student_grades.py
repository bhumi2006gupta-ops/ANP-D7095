''' STUDENT GRADES'''
m = int(input("Enter the marks of Maths: "))
e = int(input("Enter the marks of English: "))
s = int(input("Enter the marks of Science: "))
h = int(input("Enter the marks of Hindi: "))
sst = int(input("Enter the marks of Social Studies: "))
Total_marks= (m+e+s+h+sst)
total_perc=(((Total_marks)/500)*100)
print("Total Percentage :", (total_perc))
#Validating grade
if total_perc<0:
    exit("Student marks cannot be negative:")
elif total_perc>=90:
    print("Grade A")
elif total_perc>=75 and total_perc<=89:
    print("Grade B")
elif total_perc>= 50 and total_perc<= 74:
    print("Grade C ")
else:
    print("Grade F")    