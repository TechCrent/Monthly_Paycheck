#Challenge 1.0

#write a python program that calculates the monthly paycheck of a
#salesperson at a local department store. Every salesperson has
#a base salary. The salesperson also receives a bonus at the end
#of each month, based on the following criteria: if the
#salesperson has been with the store for five years or less, the
#bonus is $10 for each year that he or she has worked there. If
#the salesperson has been with the store for more than five years,
#the bonus is $20 for each year that he or she has worked there.
#The salesperson can earn an additional bonus as follows: if the
#total sales made by the salesperson for the month are at least
#$5, 000 but less than $10,000, he or she receives a 3% commission
#on the sale. If the total sales made by the salesperson for the
#month are at least $10, 000, he or she receives a 6% commission
#on the sale.

#Variables
FirstBonus = 10
SecondBonus = 20

#Interface and Input
Salary = float(input ("Enter Your Salary: "))
NumOfYears = int(input("How Many Years Have You Been Working?: "))
TotalSales = float(input("Enter Your Total Sales For The Month: "))

#Calc for Monthly Bonus
if NumOfYears <= 5:
    MonthlyBonus = FirstBonus * NumOfYears
else:
    MonthlyBonus = SecondBonus * NumOfYears

#Calc for Additional Bonus
if TotalSales >= 5000 and TotalSales < 10000:
    AdditionalBonus = 0.03 * TotalSales
elif TotalSales >= 10000:
    AdditionalBonus = 0.06 * TotalSales
else:
    AdditionalBonus = 0

#Calc for Total Bonus and Paycheck
TotalBonus = MonthlyBonus + AdditionalBonus
TotalPaycheck = Salary + TotalBonus

#Calc for Total Paycheck
print("Good Work This Month!")
print("Your Monthly Bonus is: $", MonthlyBonus)
print("Your Additional Bonus is: $", AdditionalBonus)
print("Your Total Bonus is: $", TotalBonus)
print("Your Total Paycheck is: $", TotalPaycheck)
print("Thank You For Working With Us!")
#End of Program.






