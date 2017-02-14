def fun():
    print('Endless loop')

if __name__ == '__main__':
    while True:
        fun()
        answer=input('Do you want to exit (y)') 
        if answer == 'y':
            break   