greeting = input("Enter greeting:").strip().lower()

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h") or greeting != "hello ":
    print("$20")
else:
    print("$100")
