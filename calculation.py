def getsum(data):
    amount = 0
    for num in data:
        amount += num
    return amount


def getmax(data):
    maximum = data[0]
    for i in range(len(data) - 1):
        if (maximum >= data[i + 1]):
            maximum = maximum
        else:
            maximum = data[i + 1]
    return maximum


def getmin(data):
    minimum = data[0]
    for i in range(len(data) - 1):
        if (minimum < data[i + 1]):
            minimum = minimum
        else:
            minimum = data[i + 1]
    return minimum


def getave(data):
    amount = 0
    for num in data:
        amount += num
    average = int(amount / len(data))

    return average


def main():
    data = input('データを入力してください(スペース区切り) >').split()
    for i in range(len(data)):
        data[i] = int(data[i])

    print(data)

    print(getsum(data))
    print(getmax(data))
    print(getmin(data))
    print(getave(data))


if __name__ == '__main__':
    main()
