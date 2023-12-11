def fibonacci_range(start, end):
    fibonacci_series = []
    a, b = 0, 1
    while a <= end:
        if a >= start:
            fibonacci_series.append(a)
        a, b = b, a + b
    return fibonacci_series

start_num = int(input("Enter the starting number of the range: "))
end_num = int(input("Enter the ending number of the range: "))

fibonacci_range_list = fibonacci_range(start_num, end_num)
print("Fibonacci series within the given range:", fibonacci_range_list)
