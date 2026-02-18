print("Hello I am your friendly AI chat bot")
name = input("\nWhat's your name? ")
print(f"It is a plesure to meet you {name}")

day = input("\nHow was your day?").lower()

if "good" in day or "great" in day:
    print("I am glad to hear that")
elif "bad" in day or "sad" in day:
    print("Hope you have a better day")
else:
    print("I understand. Its hard sometimes, hope you have a better day")
    
work = input("did you do anything new today?")
print(f"\nI hope you will have a better day, {work}")

if "yes" in work or "yeah" in work:
    print("Wow!, I hope it was great")
elif "no" in work or "not" in work:
    print("Hope you do aomething New tommrow")
else:
    print("Hope you do smoething next time")

print(f"\nIt was great talking to you {name}, goodbye")