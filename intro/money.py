# reviewer: anan.
def money(cash):
    bills = {200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    for note in bills.keys():
        if cash // note == 0:
            continue
        bills[note] = cash // note
        cash %= note
        print(f'{bills[note]} {note}s')


for i in range(1, 1000, 150):
    print(f'Initial amount: {i}. result:')
    money(i)
