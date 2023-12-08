#! /usr/bin/env python3

# 12 red cubes, 13 green cubes, and 14 blue cubes
cbs_in_bag = {'red':12, 'green':13, 'blue':14}

lines = ['']
fname = 'games_test.txt'
# fname = 'input'
games = ['']
reveals = []
reveals2 = [[{'blank':0}]]
games_sum = 0
games_ok = []


# MAIN ------------------------------------------------------------------
if __name__ == "__main__":
    with open(fname, 'r') as f:
        for line in f.readlines():
            lines.append(line.strip())

    # test
    # print(lines)
    # print("3-rd game:", lines[3])

    for line in lines[1:]:
        line = line.replace(", ", "|").replace("; ", "|")
        games.append(line.split(": ")[1])

    for game in games:
        reveals.append(game.split("|"))
    # print(reveals)

    rindex = 1
    for reveal in reveals[1:]:
        reveals2.append([])
        for el in reveal:
            el_dels = el.split(", ")[0]
            kvs = el_dels.split(" ")
            k = kvs[1]
            v = int(kvs[0])
            pick = {k:v}
            reveals2[rindex].append(pick)
        rindex += 1

    # print(reveals2)

    gindex = 1
    for game in reveals2[1:]:
        print(f"game-{gindex}  : {game}")
        greens = []
        reds = []
        blues = []
        for el in game:
            if list(el.keys())[0] == 'green':
                greens.append(el['green'])
            if list(el.keys())[0] == 'red':
                reds.append(el['red'])
            if list(el.keys())[0] == 'blue':
                blues.append(el['blue'])
        elsum = max(greens) * max(reds) * max(blues)
        games_sum += elsum
        print(f"game-{gindex}  : greens: {greens} | reds: {reds} | blues: {blues}")
        print(f"maximums: greens: {max(greens)} | reds: {max(reds)} | blues: {max(blues)}")

        print("---")
        gindex += 1


    print(games_sum)

