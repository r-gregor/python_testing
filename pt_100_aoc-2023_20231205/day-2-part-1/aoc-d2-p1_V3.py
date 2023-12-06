#! /usr/bin/env python3

# 12 red cubes, 13 green cubes, and 14 blue cubes
cbs_in_bag = {'red':12, 'green':13, 'blue':14}

lines = ['']
# fname = 'games_test.txt'
fname = 'input'
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

    gindex = 1
    for game in reveals2[1:]:
        print(f"game-{gindex}: {game}")
        for el in game:
            for k in el.keys():
                if el[k] > cbs_in_bag[k]:
                    games_ok.append(0)
                    break
            else:
                continue
            break
        else:
            games_ok.append(1)
            gindex += 1

    print(games_ok)

    for i in range(len(games_ok)):
        add = (i + 1) * games_ok[i]
        games_sum += add

    print(games_sum)

