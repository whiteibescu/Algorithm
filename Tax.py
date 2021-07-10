t = int (input())
for _ in range(t):
    n = int(input())

    coinnum = 0
    coins = [50000, 10000, 5000, 1000, 500, 100]

    for coin in coins:
        coinnum += n//coin
        n %= coin
    print(coinnum)




















