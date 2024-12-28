def sum_of_numbers(numbers):
    return sum(numbers)

numbers={1,2,3,4}
print(sum_of_numbers(numbers))




def is_prime(number):
    if number <= 1:
       return False
    for i in range(1,int(number ** 0.5)+1):
       if number % i == 0 :
           return False
    return True
number=int(input("put any nymber that you want: "))
print(is_prime(number))



def count_vowls(string):
    vowls="aeiou"
    return sum(1 for char in string.lower()if char in vowls)
string= str(input("put any string here please : "))
print(count_vowls(string))



def factorial(n):
    if n < 0:
        return "factorial does not exist for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    

def reverse_string(strings):
    return strings[::-1]
strings =input("put any string i will reverse it: ")
print(reverse_string(strings))


def find_max(numbers):
    return max(numbers)
numbers=input("put any numbers here :")
print(max(numbers))

def celsius_to_fahrenheit(celsius):
    return(celsius * 9/5)+32
celsius=input("put it her celcius to fahrenheit:")
print(celsius_to_fahrenheit(celsius))
