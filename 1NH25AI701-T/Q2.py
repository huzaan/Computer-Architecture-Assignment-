def rol(value, count):
    for i in range(count):
        msb = (value >> 7) & 1
        value = ((value << 1) | msb) & 255
        print("Step", i + 1, ":", format(value, '08b'))
    return value


def rcl(value, count, carry):
    for i in range(count):
        msb = (value >> 7) & 1
        value = ((value << 1) | carry) & 255
        carry = msb
        print("Step", i + 1, ":", format(value, '08b'),
              "Carry:", carry)
    return value, carry


number = int('10110110', 2)

print("a) Rotate Left Without Carry (ROL)")
print("Original:", format(number, '08b'))
result = rol(number, 2)
print("Final result:", format(result, '08b'))

print("\nb) Rotate Left With Carry (RCL)")
print("Original:", format(number, '08b'))
carry = 0
print("Initial carry:", carry)
result, carry = rcl(number, 2, carry)
print("Final result:", format(result, '08b'))
print("Final carry:", carry)