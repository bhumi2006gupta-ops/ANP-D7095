
'''MOVIE TICKET ELIGIBLE'''
# Taking age as an input
age= int(input("Enter the age : "))
#Validating the age of a costumer
if age<0:
    exit("Age must be positive ")
if(age>=18):
    print("Eligible to watch a movie ")
else:
    print("Not Eligible to watch a movie")        
