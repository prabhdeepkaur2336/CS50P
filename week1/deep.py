user_input=input("What is the answer to the Great question of life, the Universe and everything? ").lower().strip()

if user_input in ["42","forty two","forty-two"]:
    print("Yes")
else:
    print("No")