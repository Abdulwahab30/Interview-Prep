def primecheck(num):
    # Prime numbers must be strictly greater than 1
    if num > 1:
        # Loop through potential divisors starting from 2 up to (num - 1)
        for i in range(2, num):
            # Check if 'i' divides 'num' perfectly with no remainder
            if num % i == 0:
                print("Not Prime")
                break  # Exit the loop immediately because we found a factor
        else:
            # This 'else' belongs to the 'for' loop, NOT the 'if' statement.
            # It only runs if the loop finishes completely without hitting the 'break'.
            print("prime")

    else:
        # Handles edge cases where num is 1, 0, or negative numbers
        print("Number less than 1")

# Test the function
primecheck(12)