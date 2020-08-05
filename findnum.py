import random, time
print('Start program')
time.sleep(1)
print('Welcome to game: Number?')
time.sleep(1)
print('Can you find my number? From 1 to 100!')
number = random.randint(1, 100)
time.sleep(1)
print('Well done? All right! Now try to find that number')
while True:
    ans = int(input('Enter your number: '))
    if ans > number:
        print('My number less!')
    if ans < number:
        print('My number more!')
    if ans == number:
        print('Well done! Wanna do it again? y/n')
        ex = input().lower()
        if ex == 'n':
            break
        else:
            number = random.randint(1, 100)
print('Well played! See you later!')