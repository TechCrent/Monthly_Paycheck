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
first_bonus = 10
second_bonus = 20

#Interface and Input
salary = float(input ("Enter Your Salary: "))
num_of_years = int(input("How Many Years Have You Been Working?: "))
total_sales = float(input("Enter Your Total Sales For The Month: "))

#Calc for Monthly Bonus
if num_of_years <= 5:
    monthly_bonus = first_bonus * num_of_years
else:
    monthly_bonus = second_bonus * num_of_years

#Calc for Additional Bonus
if 5000 <= total_sales < 10000:
    additional_bonus = 0.03 * total_sales
elif total_sales >= 10000:
    additional_bonus = 0.06 * total_sales
else:
    additional_bonus = 0

#Calc for Total Bonus and Paycheck
total_bonus = monthly_bonus + additional_bonus
total_paycheck = salary + total_bonus

#Calc for Total Paycheck
print("Good Work This Month!")
print(f"Your Monthly Bonus is: ${monthly_bonus:.2f}")
print(f"Your Additional Bonus is: ${additional_bonus:.2f}")
print(f"Your Total Bonus is: ${total_bonus:.2f}")
print(f"Your Total Paycheck is: ${total_paycheck:.2f}")
print("Thank You For Working With Us!")
#End of Program.






