'''
Write a program to determine whether 'n' is a factorial number or not. Factorial of a number is the product of all positive numbers from 1 to 'n'.
Input format:
The input containing an integer 'n' which denotes the given number.
Output format:
If the given number is factorial, print "Yes". Otherwise, print "No".
Refer the sample output for formatting.
'''
def is_factorial(n):
    if n < 0:
        return False  # Factorial is not defined for negative numbers
    factorial = 1
    i = 1
    while factorial < n:
        i += 1
        factorial *= i
    return factorial == n
n = int(input("Enter a number: "))
if is_factorial(n):
    print("Yes")
else:
    print("No")
'''
Enter a number: 6
yes
