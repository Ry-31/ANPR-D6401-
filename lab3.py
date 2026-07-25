

def guess_no():
    rn = random.randint(1, 10)
    max_attempts = 3

    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Attempt {attempt}/{max_attempts}: Guess a number (1-10): "))

        if guess == rn:
            print("🎉 Congratulations! You won.")
            break
        elif guess > rn:
            print("Your guess is greater.")
        else:
            print("Your guess is smaller.")
    else:
        print("❌ You have used all your attempts.")
        print("The correct number was:", rn)

guess_no()