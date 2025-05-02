import sys

def inspect_integer_size(value):
    size_bytes = sys.getsizeof(value)
    size_bits = size_bytes * 8
    digit_count = len(str(abs(value)))

    print(f"Integer: {value}")
    print(f"Size in bits: {size_bits}")
    print(f"Size in bytes: {size_bytes}")
    print(f"Theoretical minimum bits needed: {value.bit_length()}")
    print(f"Number of digits: {digit_count}")
    print("-" * 40)

integers_to_test = [
    42,         # Small integer
    1_000_000,  # Medium integer
    2 ** 30,    # Just over 1 billion
    2 ** 62,    # Large integer
    2 ** 100,   # Very large integer
    2 ** 1000,  # Enormous integer
    -42,        # Negative small integer
    -1_000_000  # Negative medium integer
]

if __name__ == "__main__":
    for value in integers_to_test:
        inspect_integer_size(value)