import json
import subprocess

def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}

script_path = 'git.sh'
file_path = 'Data/games_list.json'
data = load_data(file_path)

def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def add_game(console, game_name):
    data[console].append(game_name)

def remove_game(console, game_name):
    if game_name in data[console]:
        data[console].remove(game_name)
        print(f"{game_name} removed from {console} list.")
    else:
        print(f"{game_name} not found in {console} list.")

def show_games():
    for console, games in data.items():
        print(f"{console} games:")
        for game in games:
            print(f" - {game}")
        print()

def sort_json(data):
    temp = data.items()
    data = {key: sorted(value) for key, value in temp}

    return data


while True:
    print("\nOptions:")
    print("1. Add game")
    print("2. Remove game")
    print("3. Show games")
    print("4. Sort JSON")
    print("5. Save and exit")

    choice = input("Choose an option (1/2/3/4): ")

    if choice == '1':
        console = input("Enter console (e.g., PS4, PS5): ")
        game_name = input("Enter game name: ")
        add_game(console, game_name)

    elif choice == '2':
        show_games()
        console = input("Enter console (e.g., PS4, PS5): ")
        game_name = input("Enter game name to remove: ")
        remove_game(console, game_name)

    elif choice == '3':
        show_games()

    elif choice == '4':
        data = sort_json(data)

    elif choice == '5':
        save_data(file_path, data)
        print("Data saved. Commiting...")
        try:
            subprocess.run(['bash', script_path], check=True)
            print("Bash script executed successfully.")
        except subprocess.CalledProcessError:
            print("Error: Bash script execution failed.")
        break

    else:
        print("Invalid choice. Please choose a valid option.")
