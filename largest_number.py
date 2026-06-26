
amt_1= int(input("Enter the first amount: "))
amt_2= int(input("Enter the second amount: "))
amt_3= int(input("Enter the third amount: "))
if amt_1>=amt_2 and amt_1>=amt_3:
  print("The first amount is largest. ")
elif amt_2>=amt_1 and  amt_2>=amt_3:
  print("The Second amount is largest. ")
elif amt_3 >=amt_1 and amt_3>=amt_2:
  print("The Third amount is largest. ")
else:
  print("Error")