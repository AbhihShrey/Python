string = "This is WAR"


def string_checking(string):
    word = input("Choose your word: ")
    if word in string:
        print("This word is in the string!")
    else:
        print("This word is not in the string")


string_checking(string)
