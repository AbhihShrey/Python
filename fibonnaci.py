num = int(input("Enter any number greater than 0: "))

#Creating numbers to start with and sum
num1 = 0
num2 = 1
sum = 0
#Algorithm to add first number and sum
def fibonnaci_sequence(num, num1, num2, sum):
    if num < 0:
        print("Please enter a number greater than 0: ")
    else:
        for i in range(0, num):
            #Changing the variables so it ads the next numbers -- the sum and num2
            num1 = num2
            num2 = sum
            sum = num1 + num2
            print(sum)
            
    return sum

result = fibonnaci_sequence(num, num1, num2, sum)
print("Your final result is", result)