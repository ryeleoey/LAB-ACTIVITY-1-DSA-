import random

BOTTLE_ART = r"""
        _____
                                          ██████                                        
                                        ██░░░░░░██                                      
                                      ██░░   ░▓▓░░██                                    
                                      ██░░░░░░▓▓░░██                                    
                                      ██░░▓▓▓▓▓▓░░██                                    
                                        ██░░░░░░██                                      
                                        ██▓▓▓▓▓▓██                                      
                                    ████░░░░░░░░░░████                                  
                                ████▓▓░░░░░░░░░░░░░░▓▓████                              
                              ████░░░░░░░░░░░░░░░░░░░░░░████                            
                            ██░░▓▓░░░░░░░░░░░░░░░░░░░░░░▓▓░░██                          
                            ██░░░░▓▓▓▓░░░░░░░░░░░░░░▓▓▓▓░░░░██                          
                            ██  ░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▒▒██                          
                            ██░░    ░░░░░░░░░░░░░░░░░░▒▒▒▒░░██                          
                              ██░░░░              ▒▒▒▒░░░░██                            
                              ██████░░░░░░░░░░░░░░░░░░██████                            
                            ██░░  ░░██████████████████▒▒▒▒▒▒██                          
                            ██  ░░░░░░░░  ░░░░░░  ░░░░░░░░▒▒██                          
                            ██  ░░▒▒▒▒░░░░      ░░░░▒▒▒▒░░▒▒██                          
                            ██  ▒▒░░░░▒▒░░░░  ░░░░▒▒░░░░  ▒▒██                          
                            ██  ▒▒░░░░░░  ░░░░░░▒▒░░░░░░  ▒▒██                          
                            ██  ▒▒░░░░░░  ░░░░░░▒▒░░░░░░  ▒▒██                          
                            ██  ▒▒░░░░░░  ░░░░░░▒▒░░░░░░  ▒▒██                          
                            ██  ▒▒░░░░░░  ░░░░░░▒▒░░░░░░  ▒▒██                          
                            ██  ▒▒░░░░░░  ░░░░░░▒▒░░░░░░  ▒▒██                          
                            ██░░░░      ░░░░▒▒░░░░      ░░▒▒██                          
                              ██▒▒░░░░░░░░▒▒▒▒▒▒░░░░░░░░▒▒██                            
                                ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████                              
                                    ██████████████████                                  
"""

def get_interior_spaces(art):
    lines = art.split("\n")
    positions = []
    for row, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
        start = len(line) - len(line.lstrip())
        end = start + len(stripped)
        for col in range(start, end):
            if line[col] == " ":
                positions.append((row, col))
    return positions


def bottle_with_stars(quotes, max_stars=25):
    positions = get_interior_spaces(BOTTLE_ART)
    num_stars = min(len(quotes), max_stars, len(positions))

    star_rng = random.Random(len(quotes))
    chosen = star_rng.sample(positions, num_stars)

    lines = [list(line) for line in BOTTLE_ART.split("\n")]
    for row, col in chosen:
        lines[row][col] = "★"
    return "\n".join("".join(line) for line in lines)

def create_starter_quotes():
    return [
        "Just because it's hard doesn't mean you can't do it.",
        "Push yourself, because no one else is going to do it for you.",
        "Great things never come from comfort zones.",
        "Dream it. Wish it. Do it.",
        "Success doesn't just find you. You have to go out and get it.",
        "Little things make big days.",
        "You are capable of amazing things.",
        "You don't have to be perfect to be amazing.",
        "Small things is still a progress.",
        "Take a deep breath, you've got this.",
    ]

def add_quote(quotes):
    new_quote = input("\nType a motivational quote to add to the bottle: ").strip()
    if new_quote == "":
        print("Empty quote was not added.")
        return
    quotes.append(new_quote)
    print(f'"{new_quote}" was dropped into the bottle!')
    

def display_all_quotes(quotes):
    print(bottle_with_stars(quotes))
    print(f"--- {len(quotes)} Quote(s) in the Bottle ---")
    for i in range(len(quotes)):
        print(f"  [{i}] \"{quotes[i]}\"")


def shake_bottle(quotes):
    if not quotes:
        print("\nThe bottle is empty! Add a quote first.")
        return
    print("\nShaking the bottle... ")
    print(bottle_with_stars(quotes))
    chosen = random.choice(quotes)
    print(f' "{chosen}" ')

def search_quotes(quotes, keyword):
    matches = []
    for i in range(len(quotes)):
        if keyword.lower() in quotes[i].lower():
            matches.append((i, quotes[i]))
    return matches

def edit_quote(quotes, index, new_text):
    quotes[index] = new_text

def total_characters(quotes):
    total = 0
    for i in range(len(quotes)):
        total += len(quotes[i])
    return total


def average_length(quotes):
    if not quotes:
        return 0
    return total_characters(quotes) / len(quotes)


def shortest_quote(quotes):
    shortest = quotes[0]
    for i in range(len(quotes)):
        if len(quotes[i]) < len(shortest):
            shortest = quotes[i]
    return shortest


def longest_quote(quotes):
    longest = quotes[0]
    for i in range(len(quotes)):
        if len(quotes[i]) > len(longest):
            longest = quotes[i]
    return longest


def print_menu():
    print("\n===== MOTIVATIONAL QUOTES IN A BOTTLE =====")
    print("1. Add a quote to the bottle")
    print("2. Shake the bottle (get a random quote)")
    print("3. Display all quotes in the bottle")
    print("4. Search quotes by keyword")
    print("5. Edit (update) a quote")
    print("6. Show total characters across all quotes")
    print("7. Show average quote length")
    print("8. Show shortest quote")
    print("9. Show longest quote")
    print("0. Exit")


def main():
    quotes = create_starter_quotes()
    print("Welcome! You found a bottle full of motivational quotes.")
    print(bottle_with_stars(quotes))

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_quote(quotes)

        elif choice == "2":
            shake_bottle(quotes)

        elif choice == "3":
            display_all_quotes(quotes)

        elif choice == "4":
            keyword = input("Enter a keyword to search for: ").strip()
            results = search_quotes(quotes, keyword)
            if results:
                print(f"\nFound {len(results)} quote(s) containing '{keyword}':")
                for idx, text in results:
                    print(f'  [{idx}] "{text}"')
            else:
                print(f"No quote contains '{keyword}'.")

        elif choice == "5":
            if not quotes:
                print("The bottle is empty. Nothing to edit.")
                continue
            display_all_quotes(quotes)
            try:
                idx = int(input("\nEnter the index number of the quote to edit: "))
                if 0 <= idx < len(quotes):
                    new_text = input("Enter the new quote text: ").strip()
                    if new_text:
                        edit_quote(quotes, idx, new_text)
                        print("Quote updated successfully.")
                    else:
                        print("Empty text — quote left unchanged.")
                else:
                    print("Index out of range.")
            except ValueError:
                print("Invalid input.")

        elif choice == "6":
            print(f"\nTotal characters across all quotes: {total_characters(quotes)}")

        elif choice == "7":
            print(f"\nAverage quote length: {average_length(quotes):.1f} characters")

        elif choice == "8":
            sq = shortest_quote(quotes)
            print(f'\nShortest quote ({len(sq)} characters): "{sq}"')

        elif choice == "9":
            lq = longest_quote(quotes)
            print(f'\nLongest quote ({len(lq)} characters): "{lq}"')

        elif choice == "0":
            print("\nThanks for shaking the bottle. Stay motivated!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()