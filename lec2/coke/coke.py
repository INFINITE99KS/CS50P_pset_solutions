def main():
    change_due = 50
    while change_due > 0:
        print(f"Amount Due: {change_due}")
        take_coins = int(input("Insert Coin: "))
        if take_coins == 25 or take_coins == 10 or take_coins == 50 or take_coins == 5:
            change_due -= take_coins
    if change_due >= 0:
        print(f"Change Owed: {change_due}")
    else:
        print(f"Change Owed: {-change_due}")
main()
