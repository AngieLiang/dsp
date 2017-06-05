import random
N = random.randrange(100)
num = input('Input a number:')
if int(num) == N:
    print('That is the answer!')
if int(num) > N:
    print('Too High')
if int(num) < N:
    print('Too Low')


