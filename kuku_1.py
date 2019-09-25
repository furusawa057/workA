def main():

    numbers = range(1, 10)

    for i in numbers:
        for j in numbers:
            print(f'{i*j} ', end="")
        print('\n')


if __name__ == '__main__':
    main()
