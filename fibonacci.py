# Fibonacci numbers function
def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1 # Values of fibonacci

    for _ in range(n):
        fibonacci_sequence.append(a)  # Add number to sequence
        a, b = b, a + b  # Update numbers in list

    return fibonacci_sequence

def main():
    # Ask user for input
    n = int(input("Enter a number n to know its corresponding Fibonacci numbers: "))
    
    # Generate Fibonacci numbers assigned
    fibonacci_numbers = generate_fibonacci(n)

    print("The first", n, "Fibonacci numbers are:", fibonacci_numbers)

# Run and check main program
if __name__ == "__main__":
    main()

