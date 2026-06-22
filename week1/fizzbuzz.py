def fizzbuzz():
    # range(1, 101) starts at 1 and ends exactly at 100
    for a in range(1, 101):
        # 1. Check the combined condition first (a % 15 == 0 works too!)
        if a % 3 == 0 and a % 5 == 0:
            print("FizzBuzz")
        # 2. Check individual conditions only if the first one fails
        elif a % 3 == 0:
            print("Fizz")
        elif a % 5 == 0:
            print("Buzz")
        # 3. Print the number if it's not divisible by 3 or 5
        else:
            print(a)

fizzbuzz()
