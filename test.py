from brain import handle

print("JARVIS text mode ON (exit likho band karne ke liye)\n")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
    print("JARVIS:", handle(user))