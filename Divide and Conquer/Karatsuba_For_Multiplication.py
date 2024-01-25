def karatsuba(num1, num2):
    if len(str(num1)) == 1 or len(str(num2)) == 1:
        return num1 * num2
    else:
        n = max(len(str(num1)), len(str(num2)))
        n_2 = n//2

        a = num1 // 10**n_2
        b = num1 % 10**n_2
        c = num2 // 10**n_2
        d = num2 % 10**n_2

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ab_cd = karatsuba((a+b), (c+d)) - ac - bd

        return (ac * 10**(n_2*2)) + (ab_cd * 10**n_2) + bd


num1 = 4852173
num2 = 54128
print(karatsuba(num1, num2))