def collatz_conjecture(n):
    count = 0
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    print(n)
    print("Steps:", count)

# Test the code
n = int(input("Enter a natural number: "))
collatz_conjecture(n)