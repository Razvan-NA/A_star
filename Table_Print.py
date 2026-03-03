from termcolor import colored
def print_table(table):
    print(colored("-+-+-", color="grey"))
    for j in range(3):
        print(colored("|", color="grey"), end="")
        for i in range(3):
            index = j * 3 + i
            if table[index] == index+1:
                print(colored(table[index],color="green"), end="")
            else:
                print(colored(table[index], color="red"), end="")
        print(colored("|", color="grey"),)
    print(colored("-+-+-", color="grey"))