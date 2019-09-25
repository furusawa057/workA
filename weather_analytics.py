def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]
    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    add_temp = 0

    for data in weather_information:
        add_temp += (data['temperature'])

    average_temp = add_temp / len(weather_information)
    print(average_temp)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    osaka_station = []
    for data in weather_information:
        if data['prefecture'] == '大阪府':
            osaka_station.append(data['station'])
    print(f"{osaka_station[0]},{osaka_station[1]},{osaka_station[2]}")

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    add_temp_f = 0
    i = 0
    for data in weather_information:
        if data['prefecture'] == '福岡県':
            add_temp_f += data['temperature']
            i += 1

    average_temp_f = add_temp_f / i
    print(average_temp_f)


if __name__ == '__main__':
    main()
