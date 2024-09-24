'''
The rules for generating Collatz Sequence are:
If n is even:   n = n / 2
If n is odd:    n = 3n + 1
For example, if the starting number is 5 the sequence is:
5 -> 16 -> 8 -> 4 -> 2 -> 1
It has been proved for almost all integers, the repeated application of the above rule will result in a sequence that ends at 1.
Input format:
The input containing an integer 'n' which denotes the given number
Output format:
Print the numbers in the sequence and also print the number of times the rule has to be applied in order to reach 1.
Refer the sample output for formatting.
'''
def collatz_sequence(n):
    sequence = []
    steps = 0
    
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    
    sequence.append(1)  # Append the final 1 to the sequence
    
    print(" -> ".join(map(str, sequence)))
    print(f"Number of steps: {steps}")

# Example usage:
n = int(input("Enter a positive integer: "))
collatz_sequence(n)
'''
Enter a positive integer: 5
5 -> 16 -> 8 -> 4 -> 2 -> 1
Number of steps: 5
