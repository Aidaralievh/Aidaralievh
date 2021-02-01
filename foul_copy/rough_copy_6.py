


time = int(input('Enter a number: '))


def con_sec_to_hour():
    print(f'{time // 3600}:{time // 60}:{time % 60}')
    if time == 60:
        return time = 0


con_sec_to_hour()