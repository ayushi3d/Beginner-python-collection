import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&"
length=int(input("enter length: "))
pswd = ""

for a in range(length):
    pswd+=random.choice(chars)
print(pswd)
save_choice = input("\nDo you want to save this password to a file? (yes/no): ").strip().lower()

if save_choice in ['yes', 'y']:
    with open("password.txt", "a") as file:
        file.write(pswd + "\n")
    print("✅ Password saved to 'password.txt'")
else:
    print("❌ Password not saved.")