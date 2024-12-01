import random

a = ['apple', 'orenge', 'banana']

word = random.choice(a)



dash = ['_'] * len(word)
print(dash)

chance = 5
while chance > 0:
    print("\ncurrent Word: ", ' '.join(dash))
    text = input('Enter the word : ')
    if text in word:
        for i, char in enumerate(word):
            if char == text:
                dash[i] = text
    else:
        chance -=1
        print("balance chance",chance)

print(dash)