import json
import sys

name = sys.argv[1]
action = sys.argv[2]
console = sys.argv[3]

with open("games.json", "r") as file:
    games = json.load(file)

console_games = games[console]
if action == "remove":
    for i in range(len(console_games)):
        if console_games[i]["name"] == name:
            console_games.pop(i)
elif action == "add":
    if console == "PS4":
        new_data = {
            "name": name,
            "price": None,
            "price plus": None,
            "best price": None,
            "base price": None
        }
    else:
        new_data = {
            "name": name,
            "price": None,
            "best price": None,
            "base price": None,
        }
    console_games.append(new_data)

with open("games.json", "w") as file:
    json.dump(games, file, indent=2, separators=(',', ': '))