# 06 April 2025

# Choose your own adventure game!

print("You awaken in a mysterious forest with no memory of how you got there.")

# First choice
print("Path A: Deeper into forest")
print("Path B: Follow the path out")
first_choice = input("Explore deeper into the forest OR follow a small path that seems to lead out? ").lower()

if first_choice == 'a':
    print("You discover an ancient temple!")
    path_forest = input("Enter the temple OR circle around it? ").lower()
    
    if path_forest == 'enter':
        print("You face a puzzle/riddle challenge")
        print("You solved the puzzle and found a treasure, but remain lost (bittersweet ending)")
    elif path_forest == 'circle':
        print("You find a hidden cave entrance")
        print("You lost in the hidden cave and get trapped in the forest forever (bad ending)")
else:
    print("You reach a river crossing!")
    exit_path = input("Build a raft OR search for a bridge? ")
    
    if exit_path == 'raft':
        print("You navigate dangerous rapids and managed to escape the forest and return home (good ending)")
    elif exit_path == 'bridge':
        print("You encounter a troll/guardian and successfully defeat it. Becoming the new guardian of the forest (secret ending)")
