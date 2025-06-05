/*
Challenge 1.0

write a c++ program that calculates the monthly paycheck of a
salesperson at a local department store. Every salesperson has
a base salary. The salesperson also receives a bonus at the end
of each month, based on the following criteria: if the
salesperson has been with the store for five years or less, the
bonus is $10 for each year that he or she has worked there. If
the salesperson has been with the store for more than five years,
the bonus is $20 for each year that he or she has worked there.
The salesperson can earn an additional bonus as follows: if the
total sales made by the salesperson for the month are at least
$5, 000 but less than $10,000, he or she receives a 3% commission
on the sale. If the total sales made by the salesperson for the
month are at least $10, 000, he or she receives a 6% commission
on the sale.
*/

#include <iostream>
#include <iomanip>

int main() {
    //Variables used in the Code
    //Base salary for the Salesman
    float baseSalary;
    //New salary after adding all Bonus
    float newSalary;
    //Total Sales made at the end of the month
    float totalSales;
    //Additional Bonus gained from the commission
    float addSalary = 0.0;
    //Number of Years the salesman has worked
    int numOfYears;
    //Monthly bonus calculated based on year
    float monthlyBonus = 0.0;

    //Bonus depending on conditions
    float firstBonus = 10;
    float secondBonus = 20;

    //Interface
    std::cout << "Enter Your Salary: ";
    std::cin >> baseSalary;
    std::cout << "How Many Years Have You Been Working?: ";
    std::cin >> numOfYears;
    std::cout << "Enter Your Total Sales For The Month: ";
    std::cin >> totalSales;


    //PayCheck calculation for monthly bonus
    if (numOfYears <= 5){
        monthlyBonus = firstBonus * numOfYears;
        newSalary = baseSalary + monthlyBonus;
    }else{
        monthlyBonus = secondBonus * numOfYears;
        newSalary= baseSalary + monthlyBonus;
    }

    //PayCheck calculation for additional commission bonus
    if (totalSales >= 5000 && totalSales < 10000){
        addSalary = totalSales * (3.0/100.0);
        newSalary += addSalary;
    }else if(totalSales >= 10000){
        addSalary = totalSales * (6.0/100.0);
        newSalary += addSalary;
    }

    //Printing Out PayCheck
    //Details
    std::cout << "Good Work This Month!" << std::endl;
    std::cout << "Your bonus for this month is: $" << monthlyBonus << std::endl;
    std::cout << "Your additional bonus for this month is: $" << addSalary << std::endl;
    //Actual Check
    std::cout << "Your Paycheck is: $" << newSalary << std::endl;


    return 0;
}
