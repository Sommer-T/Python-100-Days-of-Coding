print("Welcome to your Day 3 Python Sprint Card.")
print("Let's turn today's practice into proof.\n")

name = input("What is your name? ").strip().title()
topic = input("What Python topic are you practicing today? ").strip().title()
tiny_win = input("What is your tiny win today? ").strip()
revisit = input("What concept do you want to revisit? ").strip().title()
confidence = input("Confidence today, from 1 to 10? ").strip()

name = name or "Python Learner"
topic = topic or "Strings + Formatting"
tiny_win = tiny_win or "I showed up and practiced."
revisit = revisit or "String Slicing"
confidence = confidence or "1"

first_initial = name[0].upper()
topic_preview = topic[:12]
proof_sentence = f"{name} is practicing {topic} one clear rep at a time."

print("\n" + "=" * 40)
print("DAY 3 PYTHON SPRINT CARD")
print("=" * 40)
print(f"Coder: {name}")
print(f"Initial: {first_initial}")
print(f"Topic: {topic}")
print(f"Topic Preview: {topic_preview}")
print(f"Tiny Win: {tiny_win}")
print(f"Revisit: {revisit}")
print(f"Confidence: {confidence}/10")
print(f"Proof: {proof_sentence}")
print("=" * 40)
