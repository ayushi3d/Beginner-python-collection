import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "❌ Cannot divide by zero"
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def modulus(x, y):
    return x % y

def sin_deg(x):
    return math.sin(math.radians(x))

def cos_deg(x):
    return math.cos(math.radians(x))

def tan_deg(x):
    return math.tan(math.radians(x))


print("\n Scientific Calculator Menu")
print("-----------------------------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power (x^y)")
print("6. Square Root")
print("7. Modulus (x % y)")
print("8. Sine (in degrees)")
print("9. Cosine (in degrees)")
print("10. Tangent (in degrees)")

choice = input("\nEnter choice (1-10): ")

if choice in ['1', '2', '3', '4', '5', '7']:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if choice == '1':
        result = add(x, y)
    elif choice == '2':
        result = subtract(x, y)
    elif choice == '3':
        result = multiply(x, y)
    elif choice == '4':
        result = divide(x, y)
    elif choice == '5':
        result = power(x, y)
    elif choice == '7':
        result = modulus(x, y)

elif choice == '6':
    x = float(input("Enter number: "))
    result = sqrt(x)

elif choice in ['8', '9', '10']:
    angle = float(input("Enter angle in degrees: "))
    if choice == '8':
        result = sin_deg(angle)
    elif choice == '9':
        result = cos_deg(angle)
    elif choice == '10':
        result = tan_deg(angle)
else:
    result = "❌ Invalid choice"

print(f"\n✅ Result: {result}")
