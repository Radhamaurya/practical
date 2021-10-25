#Using Data Set (a), perform following task
# a. Create a function to increase the basic of all person with 10%.
# b. Create a function to filter records leaving in Ahmedabad.

data = {
101 : {'personal':{'name':'ABC', 'city':'Ahmedabad'},
'salary':{'basic':5000, 'allowance':500, 'deductions': 50}},
102 : {'personal':{'name':'ABC', 'city':'Delhi'},
'salary':{'basic':7000, 'allowance':700, 'deductions': 70}},
103 : {'personal':{'name':'DEF', 'city':'Ahmedabad'},
'salary':{'basic':4000, 'allowance':400, 'deductions': 40}},
104 : {'personal':{'name':'GHI', 'city':'Ahmedabad'},
'salary':{'basic':2000, 'allowance':200, 'deductions': 20}},
105 : {'personal':{'name':'DEF', 'city':'Delhi'},
'salary':{'basic':1000, 'allowance':100, 'deductions': 10}
}}

# a. Create a function to increase the basic of all person with 10%.


# b. Create a function to filter records leaving in Ahmedabad.

def number_of_emp_ahm(data):
    i = 0;
    for k in data:
    
       if('Ahmedabad' in data[k]):
         i= i + 1
         i.append(data[k][0])
    return i
    
    
    
count = number_of_emp_ahm(data)
print("Total Number of Empolyees in Ahmedabad is : ", count)


