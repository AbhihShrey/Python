
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

#print("Original list %s" % bubble_list)
#sorted_list = bubble_sort(bubble_list)
#print("Sorted list %s" % sorted_list)


insertion_list = [1, 5, 7, 6, 2, 4, 3, 8, 9, 7, 5, 6, 4, 2, 3, 1]

def insertion_sort(insertion_list):
    #First loop, find the index of the smallest number and swap
    for i in range(len(insertion_list)):
        # Find the smallest number from i to end of list
        smallest_number = insertion_list[i]
        smallest_index = i
        for j in range(i + 1, len(insertion_list)):
            if smallest_number > insertion_list[j]:
                smallest_number = insertion_list[j]
                smallest_index = j
        # We now have the index where the smallest number is. Swap with i
        insertion_list[i], insertion_list[smallest_index] = insertion_list[smallest_index], insertion_list[i]

    return insertion_list

sorted_list = insertion_sort(insertion_list)
print(sorted_list)
