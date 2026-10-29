def to_binary(n):
    return format(n & 255, '08b')


def signed_value(n):
    if n >= 128:
        return n - 256
    return n


def calculate(a, b):
    print("\nFirst number:", a, "=", to_binary(a))
    print("Second number:", b, "=", to_binary(b))

    result = (a - b) & 255

    print("Subtraction:", to_binary(a), "-", to_binary(b))
    print("Result in binary:", to_binary(result))
    print("Result in decimal:", signed_value(result))

    actual = a - b
    overflow = actual < -128 or actual > 127

    print("Overflow:", overflow)


print("a) 45 - (+19)")
calculate(45, 19)

print("\nb) (-35) - (-12)")
calculate(-35, -12)
