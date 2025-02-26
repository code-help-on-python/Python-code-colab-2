import string, os, random


def random_pass():
    while True:
        lenght = input('How long(min-8)')
        if lenght.isdigit():
            lenght = int(lenght)
            break
        else:
            print('enter digit:')
            continue
    random.seed = (os.urandom(1024))
    chars = string.ascii_letters + string.digits + '!@#$%^&*'
    password = ''.join(random.choice(chars) for i in range(lenght + 1))
    print(password)


random_pass()
