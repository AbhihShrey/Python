def reversestr(string):
    result = ""
    for i in string:
        result = i + result
    return result


string = "racecar"
final_result = reversestr(string)
print(reversestr(string))


def palindrome(reversestr):
    if string == final_result:
        print("This is a palindrome!")
    else:
        print("This is not a palindrome.")


palindrome(reversestr)
