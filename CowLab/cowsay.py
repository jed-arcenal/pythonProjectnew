from heifer_generator import HeiferGenerator
import sys


# a list of cow object

def list_cows(cows):
    cow_list = ""
    count = 0
    for x in cows:
        cow_list += cows[count].name
        cow_list += " "
        count += 1
    return cow_list


def find_cow(name, cows):
    for x in cows:
        if name == x.name:
            return x

    # iterate through
    # cows[i].name == name
    # return cows[i]


if __name__ == "__main__":

    cows = HeiferGenerator.get_cows()
    # cows[0].name, cows[0].image

    # list out all the command line arguments

    args = sys.argv
    # print(args)
    if args[1] == '-l':
        print(f"Cows available: {list_cows(cows)}")

    elif args[1] == '-n':
        mes = args[3:]
        name = args[2]
        if find_cow(name, cows):
            print_cow = find_cow(name, cows)
            print(" ".join(mes))
            print(print_cow.get_image())
        else:
            print(f"Could not find {name} cow!")


        # find the specific cow based on the name
        # print out the message

    else:
        mes = args[1:]
        print(" ".join(mes))
        print(cows[0].get_image())

    # print(cows[0].name)
    # print(cows[0].image)
