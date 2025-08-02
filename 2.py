import random

print("📖Let's Learn Powers of 4!")
print("Here are the powers of 4 from 0 to 25:\n")

# Step 1: Show powers of 4
for i in range(26):
    print(f"4^{i} = {4 ** i}")

# Step 2: Random Quiz
print("\n Time for a Quick Quiz.")

# Generate 3 random questions 
for _ in range(4):
    exp = random.randint(0, 10)
    answer = int(input(f"What is 4 to the power of {exp}?"))

    if answer == 4 ** exp:
        print(f"☺️ ☺️ Correct! 4^{exp} = {4 ** exp}")
    else:
        print(f"😔 😢 😞Oops! The correct answer is {4 ** exp}")

print("\n 🎈🎊🎊Great job! Keep practising powers of 4!")