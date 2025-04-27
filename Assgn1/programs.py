import datetime

# 1. Count even numbers from 1 to 100
def count_even_numbers():
    even_numbers = [i for i in range(1, 101) if i % 2 == 0]
    print(f"\nEven numbers from 1 to 100: {len(even_numbers)}")
    # Optional: print(even_numbers)

# 2. Leap years from your birth year to current year
def leap_years_from_birth(birth_year):
    current_year = datetime.datetime.now().year
    leap_years = [year for year in range(birth_year, current_year + 1)
                  if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))]
    print(f"\nLeap years from {birth_year} to {current_year}:")
    print(leap_years)

# 3. Check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

# 4. Factorial of a number
def factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

# Main Program
def main():
    count_even_numbers()

    # Leap years
    birth_year = int(input("\nEnter your birth year: "))
    leap_years_from_birth(birth_year)

    # Prime check
    prime_check = int(input("\nEnter a number to check if it's prime: "))
    if is_prime(prime_check):
        print(f"{prime_check} is a prime number.")
    else:
        print(f"{prime_check} is not a prime number.")

    # Factorial
    fact_input = int(input("\nEnter a number to find its factorial: "))
    print(f"Factorial of {fact_input} is {factorial(fact_input)}")

if __name__ == "__main__":
    main()
