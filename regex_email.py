import re


def run():
    email_pattern = re.compile(r'^[a-z0-9_]+@[a-z]{1,10}\.[a-z]{2,10}$')

    email = input('Enter an email: ').strip()

    if email_pattern.match(email):
        print('Valid')
    else:
        print('Invalid')


if __name__ == '__main__':
    run()
