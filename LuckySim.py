from Symbol import Symbol  # name, odds, pay5, pay4, pay3, pay2
from WeightedChoice import WeightedChoice
from pprint import pprint
import operator
import random
import statistics

symWild = Symbol(
    "Wild",
    10,
    3000,
    400,
    35,
    0
)
symDog = Symbol(
    "Dog",
    30,
    1500,
    300,
    25,
    0
)
symDragon = Symbol(
    "Dragon",
    30,
    600,
    200,
    25,
    0
)
symCat = Symbol(
    "Cat",
    30,
    400,
    100,
    15,
    0
)
symFish = Symbol(
    "Fish",
    30,
    300,
    100,
    10,
    0
)
symFan = Symbol(
    "Fan",
    30,
    250,
    140,
    10,
    0
)
symAce = Symbol(
    "Ace",
    40,
    200,
    100,
    10,
    0
)
symKing = Symbol(
    "King",
    40,
    200,
    100,
    10,
    0
)
symQueen = Symbol(
    "Queen",
    40,
    200,
    100,
    10,
    0
)
symJack = Symbol(
    "Jack",
    40,
    100,
    50,
    5,
    0
)
symTen = Symbol(
    "Ten",
    40,
    100,
    40,
    5,
    0
)
symBonus = Symbol(
    "Bonus",
    10,
    0,
    0,
    0,
    0
)

symbolList = []
symbolList.extend((symWild,
                   symDog,
                   symDragon,
                   symCat,
                   symFish,
                   symFan,
                   symAce,
                   symKing,
                   symQueen,
                   symJack,
                   symTen,
                   symBonus)
                  )
weightedChoice = WeightedChoice(symbolList)

reel = [[Symbol for i in range(5)] for j in range(3)]

# pretty print the slot result for debug purposes
# s = [[str(e.name) for e in row] for row in reel]
# lens = [max(map(len, col)) for col in zip(*s)]
# fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
# table = [fmt.format(*row) for row in s]
# print('\n'.join(table))


def populate_lines(func_reel):
    func_lines = []

    # add all lines to list
    func_lines.append([func_reel[1][0], func_reel[1][1], func_reel[1][2], func_reel[1][3], func_reel[1][4]])  # Line 1
    func_lines.append([func_reel[0][0], func_reel[0][1], func_reel[0][2], func_reel[0][3], func_reel[0][4]])  # Line 2
    func_lines.append([func_reel[2][0], func_reel[2][1], func_reel[2][2], func_reel[2][3], func_reel[2][4]])  # Line 3
    func_lines.append([func_reel[0][0], func_reel[1][1], func_reel[2][2], func_reel[1][3], func_reel[0][4]])  # Line 4
    func_lines.append([func_reel[2][0], func_reel[1][1], func_reel[0][2], func_reel[1][3], func_reel[2][4]])  # Line 5
    func_lines.append([func_reel[1][0], func_reel[0][1], func_reel[1][2], func_reel[0][3], func_reel[1][4]])  # Line 6
    func_lines.append([func_reel[1][0], func_reel[2][1], func_reel[1][2], func_reel[2][3], func_reel[1][4]])  # Line 7
    func_lines.append([func_reel[0][0], func_reel[0][1], func_reel[1][2], func_reel[2][3], func_reel[2][4]])  # Line 8
    func_lines.append([func_reel[2][0], func_reel[2][1], func_reel[1][2], func_reel[0][3], func_reel[0][4]])  # Line 9
    func_lines.append([func_reel[1][0], func_reel[2][1], func_reel[1][2], func_reel[0][3], func_reel[1][4]])  # Line 10
    func_lines.append([func_reel[1][0], func_reel[0][1], func_reel[1][2], func_reel[2][3], func_reel[1][4]])  # Line 11
    func_lines.append([func_reel[0][0], func_reel[1][1], func_reel[1][2], func_reel[1][3], func_reel[0][4]])  # Line 12
    func_lines.append([func_reel[2][0], func_reel[1][1], func_reel[1][2], func_reel[1][3], func_reel[2][4]])  # Line 13
    func_lines.append([func_reel[0][0], func_reel[1][1], func_reel[0][2], func_reel[1][3], func_reel[0][4]])  # Line 14
    func_lines.append([func_reel[2][0], func_reel[1][1], func_reel[2][2], func_reel[1][3], func_reel[2][4]])  # Line 15
    func_lines.append([func_reel[1][0], func_reel[1][1], func_reel[0][2], func_reel[1][3], func_reel[1][4]])  # Line 16
    func_lines.append([func_reel[1][0], func_reel[1][1], func_reel[2][2], func_reel[1][3], func_reel[1][4]])  # Line 17
    func_lines.append([func_reel[0][0], func_reel[0][1], func_reel[2][2], func_reel[0][3], func_reel[0][4]])  # Line 18
    func_lines.append([func_reel[2][0], func_reel[2][1], func_reel[0][2], func_reel[2][3], func_reel[2][4]])  # Line 19
    func_lines.append([func_reel[0][0], func_reel[2][1], func_reel[2][2], func_reel[2][3], func_reel[0][4]])  # Line 20
    
    return func_lines


print('\n')

# fill reel with random symbols based on percentage chance
for i in range(len(reel)):
    for j in range(len(reel[i])):
        reel[i][j] = weightedChoice.next()


# TODO: Fix bug: When line starts with wild it only counts the first 2 symbols
def countlist(line):
    wins = []
    win = []
    count = 1
    wildcount = 0
    symbol = line[0]
    # Avoid IndexError for  random_list[i+1]
    for s in range(0, 1):                      # iterate only from first symbol (before we were going through every symbol, but lines only pay left to right)
        # print(line[s].name)
        win.clear()
        hasWilds = False
        win.append(line[s])                         # start new potential win with current symbol
        for i in range(s+1, len(line)):             # iterate all symbols left after the current one we are on
            # print(line[i].name)
            if ((line[i].name == win[0].name) or    # next symbol matches current win check
                    (line[i].name == "Wild")):             # next symbol is wild
                win.append((line[i]))                 # append symbol or wild to current win
            elif ((win[0].name == 'Wild' and             # Special case when multiple wilds are in a row
                  line[i].name != 'Wild') or
                  line[i].name == win[-1].name):              # since we need to add wilds count plus another win
                containssymbol = False
                for x in win:
                    if x.name != 'Wild':
                        containssymbol = True
                if containssymbol == False or line[i].name == win[-1].name:
                    win.append(line[i])                 # for wilds + the trailing symbol
                    hasWilds = True
                else:
                    break
            else:
                break
        if len(win) > 1 and hasWilds is False:
            wins.append((win[0].name, len(win), win[0].getprize(len(win))))  # append win to wins list
        elif len(win) > 1 and hasWilds is True:
            for x in win:
                if x.name != 'Wild':
                    wins.append((x.name, len(win), x.getprize(len(win))))  # append win to wins list

    wins.sort(key=operator.itemgetter(2), reverse=True)
    return wins


def getBonusWin(bonusWheelSpins):
    if bonusWheelSpins > 5:
        bonusWheelSpins = 5
    totBonusWin = 0
    freeSpins = 5
    multiplier = 1
    millArrows = 1
    expandWild = False

    bonusItems = ['Coins_500',
                  'ExpandWild',
                  'FreeSpins_2',
                  'Coins_3000',
                  'Multiplier_1',
                  'Coins_2000',
                  'MillArrow_1',
                  'FreeSpins_10',
                  'MillSpins_1',
                  'Coins_1000',
                  'Multiplier_2',
                  'FreeSpins_5',
                  ]

    i = 1
    while i < bonusWheelSpins:
        curWinIndex = random.randint(0, len(bonusItems) - 1)
        for x in range(0, millArrows):
            curWinIndex = curWinIndex - (x * 2) % 12
            # print(curWinIndex)
            curWin = bonusItems[-12].split('_')
            if curWin[0] == 'Coins':
                totBonusWin += int(curWin[1])
            elif curWin[0] == 'FreeSpins':
                freeSpins += int(curWin[1])
            elif curWin[0] == 'Multiplier':
                multiplier += int(curWin[1])
            elif curWin[0] == 'MillSpins':
                bonusWheelSpins += int(curWin[1])
            elif curWin[0] == 'MillArrow':
                millArrows += int(curWin[1])
            elif curWin[0] == 'ExpandWild':
                expandWild = True

        bonusWheelSpins -= 1

        # do free spins with multiplier
        for fs in range(0, freeSpins):
            # fill reel with random symbols based on percentage chance
            for i in range(len(reel)):
                for j in range(len(reel[i])):
                    reel[i][j] = weightedChoice.next()

            lines = []

            # add all lines to list
            lines.append([reel[1][0], reel[1][1], reel[1][2], reel[1][3], reel[1][4]])  # Line 1
            lines.append([reel[0][0], reel[0][1], reel[0][2], reel[0][3], reel[0][4]])  # Line 2
            lines.append([reel[2][0], reel[2][1], reel[2][2], reel[2][3], reel[2][4]])  # Line 3
            lines.append([reel[0][0], reel[1][1], reel[2][2], reel[1][3], reel[0][4]])  # Line 4
            lines.append([reel[2][0], reel[1][1], reel[0][2], reel[1][3], reel[2][4]])  # Line 5
            lines.append([reel[1][0], reel[0][1], reel[1][2], reel[0][3], reel[1][4]])  # Line 6
            lines.append([reel[1][0], reel[2][1], reel[1][2], reel[2][3], reel[1][4]])  # Line 7
            lines.append([reel[0][0], reel[0][1], reel[1][2], reel[2][3], reel[2][4]])  # Line 8
            lines.append([reel[2][0], reel[2][1], reel[1][2], reel[0][3], reel[0][4]])  # Line 9
            lines.append([reel[1][0], reel[2][1], reel[1][2], reel[0][3], reel[1][4]])  # Line 10
            lines.append([reel[1][0], reel[0][1], reel[1][2], reel[2][3], reel[1][4]])  # Line 11
            lines.append([reel[0][0], reel[1][1], reel[1][2], reel[1][3], reel[0][4]])  # Line 12
            lines.append([reel[2][0], reel[1][1], reel[1][2], reel[1][3], reel[2][4]])  # Line 13
            lines.append([reel[0][0], reel[1][1], reel[0][2], reel[1][3], reel[0][4]])  # Line 14
            lines.append([reel[2][0], reel[1][1], reel[2][2], reel[1][3], reel[2][4]])  # Line 15
            lines.append([reel[1][0], reel[1][1], reel[0][2], reel[1][3], reel[1][4]])  # Line 16
            lines.append([reel[1][0], reel[1][1], reel[2][2], reel[1][3], reel[1][4]])  # Line 17
            lines.append([reel[0][0], reel[0][1], reel[2][2], reel[0][3], reel[0][4]])  # Line 18
            lines.append([reel[2][0], reel[2][1], reel[0][2], reel[2][3], reel[2][4]])  # Line 19
            lines.append([reel[0][0], reel[2][1], reel[2][2], reel[2][3], reel[0][4]])  # Line 20

            # TODO: Expand wild
            for line in range(len(lines)):
                if len(countlist(lines[line])) > 0:
                    win = countlist(lines[line])[0]
                    # print('Line ' + str(line+1) + ': ')
                    # print(win)
                    totBonusWin += (int((bet / 20) * win[2] * multiplier))

    # print('Bonus Win: ' + str(totBonusWin))
    return totBonusWin


def testWin(testBet):
    test_win_total = 0
    test_win = 0
    test_balance = 56000

    # Game paid ???? on a 1000 coin bet.
    # TODO: Fix wild algorithm. This scenario detects lines of 3 tens instead of 5.
    test_reel = [[symWild, symTen, symWild, symTen, symWild],
                 [symWild, symTen, symWild, symTen, symWild],
                 [symWild, symTen, symWild, symTen, symWild]]

    # add all lines to list
    test_lines = populate_lines(test_reel)
    test_win_total = 0

    for test_line in range(len(test_lines)):
        if len(countlist(test_lines[test_line])) > 0:
            test_win = countlist(test_lines[test_line])[0]
            print('Test Line Win: ' + str(test_win) + (str((testBet / 20) * test_win[2])))
            test_win_total += (int((testBet / 20) * test_win[2]))

    print('Test reel total - ????:' + str(test_win_total))
    print("")

    # 1. Game paid 0 on a 1000 coin bet.
    test_reel = [[symJack, symDragon, symAce, symTen, symCat],
                 [symTen, symJack, symTen, symBonus, symDragon],
                 [symFan, symFish, symDragon, symDragon, symKing]]

    # add all lines to list
    test_lines = populate_lines(test_reel)
    test_win_total = 0

    for test_line in range(len(test_lines)):
        if len(countlist(test_lines[test_line])) > 0:
            test_win = countlist(test_lines[test_line])[0]
            print('Test Line Win: ' + str(test_win) + (str((testBet / 20) * test_win[2])))
            test_win_total += (int((testBet / 20) * test_win[2]))

    test_balance -= 1000
    test_balance += test_win_total
    print('Test reel total - 0:' + str(test_win_total))
    print("Balance: " + str(test_balance))
    print("")

    # 2. Game paid 500 on a 1000 coin bet.
    test_reel = [[symTen, symTen, symTen, symQueen, symQueen],
                 [symQueen, symKing, symFan, symDragon, symKing],
                 [symAce, symJack, symFish, symBonus, symJack]]

    # add all lines to list
    test_lines = populate_lines(test_reel)
    test_win_total = 0

    for test_line in range(len(test_lines)):
        if len(countlist(test_lines[test_line])) > 0:
            test_win = countlist(test_lines[test_line])[0]
            print('Test Line Win: ' + str(test_win) + (str((testBet / 20) * test_win[2])))
            test_win_total += (int((testBet / 20) * test_win[2]))

    test_balance -= 1000
    test_balance += test_win_total
    print('Test reel total - 0:' + str(test_win_total))
    print("Balance: " + str(test_balance))
    print("")

    # 3. Game paid 4750 on a 1000 coin bet.
    test_reel = [[symKing, symFan, symAce, symTen, symDragon],
                 [symTen, symQueen, symJack, symJack, symDragon],
                 [symQueen, symWild, symQueen, symQueen, symFish]]

    # add all lines to list
    test_lines = populate_lines(test_reel)
    test_win_total = 0

    for test_line in range(len(test_lines)):
        if len(countlist(test_lines[test_line])) > 0:
            test_win = countlist(test_lines[test_line])[0]
            print('Test Line Win: ' + str(test_win) + (str((testBet / 20) * test_win[2])))
            test_win_total += (int((testBet / 20) * test_win[2]))

    test_balance -= 1000
    test_balance += test_win_total
    print('Test reel total - 4750:' + str(test_win_total))
    print("Balance: " + str(test_balance)) # 58750 -> 62500
    print("")


testWin(1000)

bet = 5000
users = []
usersCount = 1000
totWinAllUsers = 0
totBetAllPlayers = 0
totSpinsAllPlayers = 0
totHitsAllPlayers = 0

for u in range(usersCount):
    balance = 100000
    for i in range(1000):
        balance -= bet
        totBetAllPlayers += bet
        totSpinsAllPlayers += 1
        winTotal = 0
        # fill reel with random symbols based on percentage chance
        for i in range(len(reel)):
            for j in range(len(reel[i])):
                reel[i][j] = weightedChoice.next()

        lines = []

        # add all lines to list
        lines.append([reel[1][0], reel[1][1], reel[1][2], reel[1][3], reel[1][4]])  # Line 1
        lines.append([reel[0][0], reel[0][1], reel[0][2], reel[0][3], reel[0][4]])  # Line 2
        lines.append([reel[2][0], reel[2][1], reel[2][2], reel[2][3], reel[2][4]])  # Line 3
        lines.append([reel[0][0], reel[1][1], reel[2][2], reel[1][3], reel[0][4]])  # Line 4
        lines.append([reel[2][0], reel[1][1], reel[0][2], reel[1][3], reel[2][4]])  # Line 5
        lines.append([reel[1][0], reel[0][1], reel[1][2], reel[0][3], reel[1][4]])  # Line 6
        lines.append([reel[1][0], reel[2][1], reel[1][2], reel[2][3], reel[1][4]])  # Line 7
        lines.append([reel[0][0], reel[0][1], reel[1][2], reel[2][3], reel[2][4]])  # Line 8
        lines.append([reel[2][0], reel[2][1], reel[1][2], reel[0][3], reel[0][4]])  # Line 9
        lines.append([reel[1][0], reel[2][1], reel[1][2], reel[0][3], reel[1][4]])  # Line 10
        lines.append([reel[1][0], reel[0][1], reel[1][2], reel[2][3], reel[1][4]])  # Line 11
        lines.append([reel[0][0], reel[1][1], reel[1][2], reel[1][3], reel[0][4]])  # Line 12
        lines.append([reel[2][0], reel[1][1], reel[1][2], reel[1][3], reel[2][4]])  # Line 13
        lines.append([reel[0][0], reel[1][1], reel[0][2], reel[1][3], reel[0][4]])  # Line 14
        lines.append([reel[2][0], reel[1][1], reel[2][2], reel[1][3], reel[2][4]])  # Line 15
        lines.append([reel[1][0], reel[1][1], reel[0][2], reel[1][3], reel[1][4]])  # Line 16
        lines.append([reel[1][0], reel[1][1], reel[2][2], reel[1][3], reel[1][4]])  # Line 17
        lines.append([reel[0][0], reel[0][1], reel[2][2], reel[0][3], reel[0][4]])  # Line 18
        lines.append([reel[2][0], reel[2][1], reel[0][2], reel[2][3], reel[2][4]])  # Line 19
        lines.append([reel[0][0], reel[2][1], reel[2][2], reel[2][3], reel[0][4]])  # Line 20

        # pretty print the slot result for debug purposes
        # s = [[str(e.name) for e in row] for row in reel]
        # lens = [max(map(len, col)) for col in zip(*s)]
        # fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        # table = [fmt.format(*row) for row in s]
        # print('\n'.join(table))
        # print("")

        for line in range(len(lines)):
            if len(countlist(lines[line])) > 0:
                win = countlist(lines[line])[0]
                # print('Line ' + str(line+1) + ': ')
                # print(win)
                # print("Line win: " + str(int((bet / 20) * win[2])))
                winTotal += (int((bet / 20) * win[2]))


        # print("Won: " + str(winTotal))
        # print("")

        # check for bonus win
        bonusCount = 0
        for i in range(len(reel)):
            for j in range(len(reel[i])):
                if reel[i][j].name == 'Bonus': bonusCount += 1

        if bonusCount >= 3:
            bonusWin = getBonusWin(bonusCount)
            # print(bonusWin)
            winTotal += bonusWin

        balance += winTotal
        # print("Balance: " + str(balance))
        if winTotal > 0:
            totHitsAllPlayers += 1

        totWinAllUsers += winTotal

        if balance <= 0:
            balance = 0
            break

    users.append(balance)
    # print(str(balance))

print('After 1000 spins per user: ')
print(str(sum(i <= 0 for i in users)) + ' users went to 0 coins')
print(str(len(list(x for x in users if 1000 <= x <= 10000))) + ' users ended between 1,000 and 10,000 coins')
print(str(len(list(x for x in users if 10001 <= x <= 100000))) + ' users ended between 10,000 and 100,000 coins')
print(str(len(list(x for x in users if 100001 <= x <= 1000000))) + ' users ended between 100,001 and 1,000,000 coins')
print(str(len(list(x for x in users if 1000000 <= x))) + ' users ended higher than 1,000,000 coins')

totStartingCoins = 100000 * usersCount
totEndingCoins = sum(users)
print('RTP: ' + str((totWinAllUsers / totBetAllPlayers) * 100))
print('Hit Frequency: ' + str((totHitsAllPlayers / totSpinsAllPlayers) * 100))


