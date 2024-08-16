def fibonacci(n):
    fib_sequence=[0,1]
    if n==0:
        return []
    elif n==1:
        return [0]
    while len(fib_sequence)< n:
        fib_sequence.append(fib_sequence[-1]+fib_sequence[-2])
    return fib_sequence
num_terms=10
print(f"fibonacci sequence with(num_terms)terms:")
print(fibonacci(num_terms))
