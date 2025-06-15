decimal = input("Enter a decimal number: ")
def decimal_to_binary(n):
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary or "0" 
 
binary_number = decimal_to_binary(int(decimal))
print(f"Binary number: {binary_number}")    

while True:
    decimal = input("Enter a decimal number (or 'q' to quit): ")
    if decimal.lower() == 'q':
        break
    if not decimal.isdigit():
        print("Please enter a valid non-negative integer.")
        continue
    binary_number = decimal_to_binary(int(decimal))
    print(f"Binary number: {binary_number}")    