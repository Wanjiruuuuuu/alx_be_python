#Generating a multiplication table
#Prompt user input

number = int(input("Enter a number to see its multiplication table:"))

#Start loop to generate multiplication table for number

for i in range(1,11):
    product =  number * i
    print(f"{number}*{i}={product}")



