#! /usr/bin/env python3

# 12 red cubes, 13 green cubes, and 14 blue cubes
cbs_in_bag = {'red':12, 'green':13, 'blue':14}

lines = ['']
fname = 'games_test.txt'
games = [[]]
reveals = []



# MAIN ------------------------------------------------------------------
if __name__ == "__main__":
    with open(fname, 'r') as f:
        for line in f.readlines():
            lines.append(line.strip())

    # test
    # print(lines)
    # print("3-rd game:", lines[3])

    for line in lines[1:]:
        # print(line)
        games.append((line.split(": ")[1]).split("; "))

    print(games)

