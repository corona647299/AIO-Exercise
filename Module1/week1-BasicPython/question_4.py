def factorial(k):
    if k == 0 or k == 1:
        return 1
    result = 1
    for i in range(2, k + 1):
        result *= i
    return result

def approx_sin(x, n):
    sin_x = 0
    for i in range(n):
        approx = ((-1)**i * x**(2*i + 1)) / factorial(2*i + 1)
        sin_x += approx
    return sin_x

def approx_cos(x, n):
    cos_x = 0
    for i in range(n):
        approx = ((-1)**i * x**(2*i)) / factorial(2*i)
        cos_x += approx
    return cos_x

def approx_sinh(x, n):
    sinh_x = 0
    for i in range(n):
        approx = (x**(2*i + 1)) / factorial(2*i + 1)
        sinh_x += approx
    return sinh_x

def approx_cosh(x, n):
    cosh_x = 0
    for i in range(n):
        approx = (x**(2*i)) / factorial(2*i)
        cosh_x += approx
    return cosh_x

if __name__ == "__main__":
# Ví dụ sử dụng các hàm với x và n
    x = float(input("Enter x (in radians): "))
    n = int(input("Enter n (number of terms): "))

    if n <= 0:
        print("n must be a positive integer")
    else:
        print(f"sin({x}) ≈ {approx_sin(x, n)}")
        print(f"cos({x}) ≈ {approx_cos(x, n)}")
        print(f"sinh({x}) ≈ {approx_sinh(x, n)}")
        print(f"cosh({x}) ≈ {approx_cosh(x, n)}")
