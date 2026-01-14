from random_num_gen import generate_rand_int
from calc import add, subtract, multiply, divide, power, modulus

def operations():
    sum = add(x, y)
    difference = subtract(x, y)
    product = multiply(x, y)
    quotient = round(divide(x, y),2)
    exp = power(x, y)
    mod = modulus(x, y)

    print(f"Chosen random numbers: x={x}, y={y}")

    print(f"Addition: {x} + {y} = {sum}")
    print(f"Subtraction: {x} - {y} = {difference}")
    print(f"Multiplication: {x} * {y} = {product}")
    print(f"Division: {x} / {y} = {quotient}")
    print(f"Exponentiation: {x} ** {y} = {exp}")
    print(f"Modulus: {x} % {y} = {mod}")

x = generate_rand_int(1, 10)
y = generate_rand_int(1, 10)


if __name__ == "__main__":
    operations()