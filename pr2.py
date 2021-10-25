#Write a program to print the following pattern
#    *
#   * *
#  * * *
# * * * *


num = int(input("enter the number of row:"))
for i in range(1,num+1):
    print("  "*(num-i)+" *  "*i)

