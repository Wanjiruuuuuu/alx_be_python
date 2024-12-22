#Welcome to match case calculator 

try:


    num1 = (float(input("Enter the first number: ")))
    num2 = (float(input("Enter the second number: ")))

    #Choose operation

    operation = (input("Choose the operation (+, -, *, /): "))

    match operation :
         case "+" :
              result = num1 + num2
              print("The result is", result)

         case  "-" :
              result =  num1 - num2 
              print("The result is", result)

         case  "*" :
              result = num1 * num2 
              print("The result is", result)

         case  "/" :
              if num2 == 0:
                   print("cannot be divided by zero.")
              else:
                   result = num1 / num2 
                   print("The result is", result)
         case _:
              print("Invalid operation. Please choose one of the operations given")

except ValueError:
     print("Invalid input. please enter valid numbers.")
         




        









