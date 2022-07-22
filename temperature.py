list1 = [2, 5, 6, 7]

conversion_celsius = [((9/5)*temperature + 32) for temperature in list1]

print(conversion_celsius)

list2 = [83, 75, 101, 97]

conversion_farenheit = [((temp - 32) * 5/9) for temp in list2]

print(conversion_farenheit)
