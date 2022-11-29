# Write a program that detects even numbers and diplay how many even numbers are

user_input = input("Please insert a number: ")
even_num_count  = 0
for i in range(1,int(user_input)):
    if i%2 == 0:
        print(i)
        even_num_count +=1
print(f"We have {even_num_count} even numbers")