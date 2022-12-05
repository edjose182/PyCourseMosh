def fizzbuzz(input):

    message = ""

    message += "Fizz" if int(input) %3 == 0 else "" 
    message += "Buzz" if int(input) %5 == 0 else ""

    if message == "":
        message = input
    
    print(message)

value = int(input("Introduce a number: "))

fizzbuzz(value)