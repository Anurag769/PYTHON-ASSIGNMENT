
#Q No.1
print('ANSWER 1.') 
# taking 3 numbers from user 
number1 = float(input("Enter 1st No = "))
number2 = float(input("Enter 2nd No = "))
number3 = float(input("Enter 3rd No = "))
# finding average of these 3 numbers entered by users
sum = number1+number2+number3
print(sum/3)

# Q No.2
print('ANSWER 2.')
# taking input of gross income(a) and no.of dependent(b) from user
a = int(input("Enter Your Gross Income (in nearest integer) = "))
b = int(input("Enter No. Of Dependent = "))
# $10,000 stndard deduction(c)
c = 10000
# Total dependent deduction(d) as per $3000 on each dependent
d = 3000*b
# Calculating Taxable Income(e) with all data entered
# taxable income = gross income-standard deduction-total dependent deduction 
e = a-c-d 
# Calculating Tax as per tax rate(20%)
# tax = taxable income * tax rate(20%) 
tax = e*(0.2)
# printing final output
print("Your Total Income Tax is : ",tax) 

# Q No.3
print('ANSWER 3.')
# taking all the inputs from the user as mentioned in question 
sid = int(input("Your SID : "))
name = input("Your Name : ")
print("For Male (M),For Female(F),For Unknown(U)")
gender = input("Your Gender : ")
coursename = input("Your Course Name : ")
cgpa = float(input("Your CGPA : "))
# making list of all the details entered by user and then printing it
list = [sid,name,gender,coursename,cgpa]
print(list)

# Q No.4
print('ANSWER 4.')
print("Enter marks of 5 students")
# taking input of marks from 5 students where s1 represent student 1 and so on....
s1 = float(input())
s2 = float(input())
s3 = float(input())
s4 = float(input())
s5 = float(input())
# making a list of all inputs and then sorting it
list = [s1,s2,s3,s4,s5]
list.sort()
# then printing final output
print(list)

# Q No.5
print('ANSWER 5.A')
# list of colours
list = ['Red','Green','White','Black','Pink','Yellow']
print(list)
# part a = removing 4th element (black) from list and printing final output (list)
del list[3]
print(list)
print('ANSWER 5.B')
# list of colours
list = ['Red','Green','White','Black','Pink','Yellow']
print(list)
# part b = removing black and pink and removing it with purple and then printing it 
list[3]=list[4]='Purple'
print(list)




