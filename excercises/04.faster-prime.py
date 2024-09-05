import timeit


def allPrimesUpTo(num):
    # Initialize a boolean array "sieve" with True values
    sieve = [True] * (num + 1)
    # 0 and 1 are not prime numbers
    sieve[0] = sieve[1] = False

    # Loop's ending condition is i * i <= num
    for i in range(2, int(num**0.5) + 1):
        if sieve[i]:
            # Mark multiples of i as non-prime
            for j in range(i * i, num + 1, i):
                sieve[j] = False

    # Collect all prime numbers
    return [i for i in range(num + 1) if sieve[i]]


def test_prime_function(func, num, iterations=1000):
    # Measure the execution time of the function
    time_taken = timeit.timeit(lambda: func(num), number=iterations)
    # Return average time per iteration
    return time_taken / iterations


# Test cases: different upper limits for prime calculation
test_cases = [100, 200, 500, 1000]

# Print table header
print(f"{'Range':<10}{'Time (seconds)':<20}{'Number of Primes':<20}")
print("-" * 50)

for case in test_cases:
    # Measure execution time
    time_taken = test_prime_function(allPrimesUpTo, case)
    # Calculate primes
    primes = allPrimesUpTo(case)
    # Print results: range, time taken, and number of primes found
    print(f"1 to {case:<5}{time_taken:<20.6f}{len(primes):<20}")

# Print all prime numbers up to 200
print("\nPrime numbers up to 200:")
print(allPrimesUpTo(200))
