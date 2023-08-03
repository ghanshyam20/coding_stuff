import random

def generate_random_number():
    return random.randint(1, 100)

def check_guess(guess, target):
    if guess < target:
        return "Too low!"
    elif guess > target:
        return "Too high!"
    else:
        return "Congratulations! You guessed the number!"

if __name__ == "__main__":
    target_number = generate_random_number()

    while True:
        user_guess = int(input("Guess the number (1-100): "))
        result = check_guess(user_guess, target_number)
        print(result)
        if result == "Congratulations! You guessed the number!":
            break
