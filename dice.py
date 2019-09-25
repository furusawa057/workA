import random


def main():
    surface = int(input('サイコロの面の数は？：'))
    trytime = int(input('何回振りますか？：'))

    dice_result = []

    for num in range(trytime):
        dice_number = random.randint(1, surface)
        dice_result.append(dice_number)
    print(dice_result)


if __name__ == '__main__':
    main()
