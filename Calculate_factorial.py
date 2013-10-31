def factorial(n):
    count = 1
    var = 1
    if n < 2:
        return 1
    else:
        while count != n+1:
            var *= count
            count += 1
        return var

print factorial(6)