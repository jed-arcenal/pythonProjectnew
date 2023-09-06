from pakudex import Pakudex

pakudex = Pakudex(capacity=5)

if __name__ == "__main__":
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:
        user_capacity = (input("Enter max capacity of the Pakudex: "))
        if user_capacity.isnumeric() and int(user_capacity) > 0:
            user_capacity = int(user_capacity)
            break
        else:
            print("Please enter a valid size.")
            continue
    pakudex.capacity = user_capacity

    # pakudex.capacity = int(input("Enter max capacity of the Pakudex: "))
    print(f"The Pakudex can hold {pakudex.capacity} species of Pakuri.")

    while True:
        print()
        print("Pakudex Main Menu")
        print("-----------------")
        print("1. List Pakuri")
        print("2. Show Pakuri")
        print("3. Add Pakuri")
        print("4. Evolve Pakuri")
        print("5. Sort Pakuri")
        print("6. Exit")
        print()
        try:

            user_input = int(input("What would you like to do? "))
        except:
            print("Unrecognized menu selection!")
            continue

        if user_input == 1:
            if pakudex.get_species_array() is None:
                print("No Pakuri in Pakudex yet!")
            else:
                print("Pakuri In Pakudex: ")
                count = 1
                for x in pakudex.get_species_array():
                    x = str(x)
                    print(f"{count}. {x}")
                    count += 1

        elif user_input == 2:
            species = input(f"Enter the name of the species to display: \n")
            if pakudex.get_stats(species):
                [attack, defense, speed] = pakudex.get_stats(species)
                print(f"Species: {species}")
                print(f"Attack: {attack}")
                print(f"Defense: {defense}")
                print(f"Speed: {speed}")
            else:
                print("Error: No such Pakuri!")
        elif user_input == 3:
            if pakudex.get_size() == pakudex.capacity:
                print("Error: Pakudex is full!")
                continue
            species = input("Enter the name of the species to add: ")
            if pakudex.add_pakuri(species):
                print(f"Pakuri species {species} successfully added!")

        elif user_input == 4:
            species = input("Enter the name of the species to evolve: ")
            if pakudex.evolve_species(species):
                print(f"{species} has evolved!")
            else:
                print(f"Error: No such Pakuri!")


        elif user_input == 5:
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")

        elif user_input == 6:
            print("Thanks for using Pakudex! Bye!")
            break
        else:
            print("Unrecognized menu selection!")
