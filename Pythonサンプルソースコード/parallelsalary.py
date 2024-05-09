from func_salary import calcsalary
import sys
args = sys.argv

salaries = (int(args[1]), int(args[2]), int(args[3]))

for salary in salaries:
    
    pay_tax = calcsalary(salary)
    print("給与:"+ str(salary)+ "、支給額:"+ str(pay_tax[0]) + "、税額:" + str(pay_tax[1]))