def multiply(a, b):
    return(a*b)

def multiplication_table(n):
    table = ''
    for i in range(1, n+1):
        table += "{} times {} is {}\n".format(n, i, multiply(n, i))
    return(table.strip())

def print_multiplication_table(n):
    print(multiplication_table(n))

def print_twelve_times():
    print_multiplication_table(12)

def add(a, b):
    return(a+b)
