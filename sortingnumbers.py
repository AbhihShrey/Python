'''
numbers = []
x = int(input("How many numbers?: "))

for i in range(x):
    y = int(input("Pick your number: "))
    numbers.append(y)

def bubble_sort(numbers):
    x = len(numbers)
    for i in range(x):
        for e in range(i+1,x):
            if numbers[i] > numbers[e]:
                value = numbers[i]
                numbers[i] = numbers[e]
                numbers[e] = value
    print(numbers)
    
bubble_sort(numbers)
'''

#Create a list
bubble_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def bubble_sort(bubble_list):
    #   - Create a while loop and break when swapping is over
    while True:
        swapping = False
        for i in range(len(bubble_list)-1):
            #Cool swapping algorithm short cut
            if bubble_list[i] > bubble_list[i + 1]:
                bubble_list[i], bubble_list[i+1] = bubble_list[i + 1], bubble_list[i]
                swapping = True
        #If there is no more swapping to do, then stop the program
        if swapping == False:
            break

    #Print the final list
    return bubble_list

print("Original list %s" % bubble_list)
sorted_list = bubble_sort(bubble_list)
print("Sorted list %s" % sorted_list)


