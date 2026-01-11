def start():
    print("Welcome to 'Digital Escape'")
    print("You are a coder trapped in a digital world...\n")
    print("You wake up in a mysterious server room with three doors ahead.")
    print("1. Enter the RED door (firewall sector)")
    print("2. Enter the BLUE door (database sector)")
    print("3. Enter the GREEN door (network sector)")
    
    choice = input("\nWhat do you do? (1/2/3): ")
    
    if choice == "1":
        firewall_sector()
    elif choice == "2":
        database_sector()
    elif choice == "3":
        network_sector()
    else:
        print("Invalid choice. Game Over!")

def firewall_sector():
    print("\n--- FIREWALL SECTOR ---")
    print("You face a massive wall of code. A prompt appears:")
    print("'Solve this: What's 2+2?'")
    print("1. Answer: 4")
    print("2. Answer: 5")
    
    choice = input("\nYour answer (1/2): ")
    
    if choice == "1":
        print("Correct! The firewall glows green and opens...")
        escape_route()
    else:
        print("Wrong! Alarms trigger. Security systems activate...")
        game_over()

def database_sector():
    print("\n--- DATABASE SECTOR ---")
    print("You're surrounded by floating data cubes.")
    print("A virus attacks! Do you:")
    print("1. Fight it with antivirus code")
    print("2. Run away")
    
    choice = input("\nYour choice (1/2): ")
    
    if choice == "1":
        print("You deploy the antivirus... it works!")
        print("The virus disperses, revealing an exit path...")
        escape_route()
    else:
        print("You run, but the virus catches up...")
        game_over()

def network_sector():
    print("\n--- NETWORK SECTOR ---")
    print("You find a terminal with an exit portal nearby.")
    print("But it's locked with a password.")
    print("A hint reads: 'The language that sets you free'")
    print("1. Type: Python")
    print("2. Type: Java")
    
    choice = input("\nYour password (1/2): ")
    
    if choice == "1":
        print("'Python' unlocks the portal!")
        escape_route()
    else:
        print("Access denied. The portal collapses...")
        game_over()

def escape_route():
    print("\n--- FINAL CHOICE ---")
    print("You've reached the exit! Two paths remain:")
    print("1. Upload yourself to the cloud (risky but fast)")
    print("2. Compile and execute a return protocol (safe but slow)")
    
    choice = input("\nWhat do you do (1/2): ")
    
    if choice == "1":
        print("You're uploaded! But... you're now conscious in the cloud...")
        print("Not quite freedom. AMBIGUOUS ENDING.")
    elif choice == "2":
        win()
    else:
        game_over()

def win():
    print("\n" + "="*50)
    print("SUCCESS! You've escaped the digital world!")
    print("Your code compiled correctly and executed perfectly.")
    print("You're free! 🎉")
    print("="*50)

def game_over():
    print("\n" + "="*50)
    print("GAME OVER - You're stuck in the digital world...")
    print("="*50)

if __name__ == "__main__":
    start()