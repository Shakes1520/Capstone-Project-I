#The program that allows the user to access two different calculators, the home loan and investment calculator.

#Math library
import math

#Showing the user what the program does 
print("\n")
print("Choose either 'investment' or 'bond' from the menu below to proceed :\n")
print("investment  - to calculate the amount of interest youl'll earn on interest")
print("bond        - to calculate the amount you'll have to pay on a home loan ")

#Prompting the user to make a choice about the type of calculations he wants to be performed
calculator=input("Please make a choice :")

#Make decision on which calculator to be used 
if calculator=="Investment" or calculator=="investment" or calculator=="INVESTMENT":

#Prompt the user t enter the principal amount, interest rate, investment period and the type of calculation to be done
     princ_amount=input("Please enter your deposit amount\t\t\t:") 
     inter_rate  =input("Please enter the interest rate percentage \t\t:")
     invest_period=input("Please enter the number of years tou planning to invest :")
     interest_type=input("What type of interest do you want simple or compound\t:")

#Converting the user prompted character variables to float data type and calculating the interest 
     inter_rate=float(inter_rate)
     princ_amount=float(princ_amount)
     inter_rate=inter_rate/100
     invest_period=float(invest_period)

#Making a decision to based on the user input, as to which calculations to do
     if  interest_type=="simple" or interest_type=="Simple" or interest_type=="SIMPLE":

#Calculating the simple interest
       simp_total_Amount=princ_amount*(1+inter_rate*invest_period)

#Displaying the calculated total amount of the simple interest
       print(f"The total amount of the simple interest is\t\t: {simp_total_Amount}")

#Compound decision making and total amount of compound interest calculations 
     elif interest_type=="compound" or interest_type=="Compound" or interest_type=="COMPOUND":

#Calculating the compound interest
       comp_total_Amount=princ_amount*(1+inter_rate)**invest_period

#Displaying the calculated total amount of the compound interest
       print("The compounded amount is \t\t\t\t:",format(comp_total_Amount,'.2f'))

#The bond repayment data capturing, variable declariation, conversion and display
elif calculator=="bond" or calculator=="Bond" or calculator=="BOND": 

#user prompting,declariation, storage and conversion of bond variables 
     present_value=float(input("Please enter the present value of the  house \t\t:"))
     bon_inter_rate=float(input("Please enter the monthly interest  rate \t\t:"))
     repay_period=int(input("Please enter the number of monthly payback period\t:"))

#Converting the interest percentage
     bon_inter_rate=bon_inter_rate/100

#breaking the bond repayment formula into two simplest form for accurate calculations 
     first_part=bon_inter_rate*present_value
     second_part=(1-(1+bon_inter_rate)**(-repay_period))

#The final bond repayment calculation and displaying the monthly bond repayment
     repayment=first_part/second_part
     print("The monthly repayment is\t\t\t\t:",format(repayment,'.2f'))

#The message to be displayed when an invalid input has been made
else:
     print("Invalid input!! please try again")
    

