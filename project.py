import random

def rando(features):
    return round(random.uniform(20.0,80.0),1)

def backward_elimination(features):
    print("not implemented yet")

def forward_selection(features):
    print("not implemented yet")


def main():
    print("Welcome to Chao Wei and Ryans Feature Selection Algorithm")
    n = input("Please enter total number of features:")
    print("Type the number of the algorithm you want to run.")
    print("1. Forward Selection"
          "\n2. Backward Elimination"
          "\n3. Chao and Ryan’s Special Algorithm.")
    choice = int(input())


    if(choice == 1):
        forward_selection(n)
    elif(choice == 2):
        backward_elimination(n)
    else:
        print("Chao and Ryan's Special Algorithm is not yet implemented.")
main()