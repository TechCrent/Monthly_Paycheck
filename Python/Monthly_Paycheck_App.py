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

#imports
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QMessageBox, QVBoxLayout
)

#Variables
first_bonus = 10
second_bonus = 20

#Interface and Input
#Function for calculation and output(Still learning functions)
def calculate_bonus():
    try:
        salary = float(salary_input.text())
        num_of_years = int(years_input.text())
        total_sales = float(sales_input.text())

        #Calc for Monthly Bonus
        #Unchanged
        if num_of_years <= 5:
            monthly_bonus = first_bonus * num_of_years
        else:
            monthly_bonus = second_bonus * num_of_years

        #Calc for Additional Bonus
        #Unchanged
        if 5000 <= total_sales < 10000:
            additional_bonus = 0.03 * total_sales
        elif total_sales >= 10000:
            additional_bonus = 0.06 * total_sales
        else:
            additional_bonus = 0

        #Calc for Total Bonus and Paycheck
        #unchanged
        total_bonus = monthly_bonus + additional_bonus
        total_paycheck = salary + total_bonus

        #Calc for Total Paycheck
        #Changes to Output
        msg = QMessageBox()
        msg.setWindowTitle("Salary Result")
        msg.setText(
            f"Good Work This Month!\n"
            f"Your Monthly Bonus is: ${monthly_bonus:.2f}\n"
            f"Your Additional Bonus is: ${additional_bonus:.2f}\n"
            f"Your Total Bonus is: ${total_bonus:.2f}\n"
            f"Your Total Paycheck is: ${total_paycheck:.2f}\n"
            "Thank You For Working With Us!"
        )
        msg.exec_()
    except ValueError:
        error = QMessageBox()
        error.setWindowTitle("Input Error")
        error.setText("Please enter valid numbers in all fields.")
        error.exec_()

#GUI Setup
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Monthly Paycheck Calculator")

#Labels and Inputs
salary_label =QLabel("Enter Your Salary:")
salary_input = QLineEdit()

years_label = QLabel("How Many Years Have You Been Working?")
years_input = QLineEdit()

sales_label = QLabel("Enter Your Total Sales For The Month:")
sales_input = QLineEdit()

#Button
calc_button: QPushButton = QPushButton("Calculate")
calc_button.clicked.connect(calculate_bonus)

#Layout
layout =QVBoxLayout()
layout.addWidget(salary_label)
layout.addWidget(salary_input)
layout.addWidget(years_label)
layout.addWidget(years_input)
layout.addWidget(sales_label)
layout.addWidget(sales_input)
layout.addWidget(calc_button)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
#End of Program.






