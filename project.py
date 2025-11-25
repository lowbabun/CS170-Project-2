import random

def rando(features):
    return round(random.uniform(20.0,80.0),1)

def backward_elimination(features):


    curr_set = list(range(0,features))
    best_overall = rando(curr_set)
    print("\nUsing no features and “random” evaluation, I get an accuracy of "
          f"{rando([])}%")
    print("\nBeginning search.\n")

    while len(curr_set)>1:
        feature_to_remove = -1
        best_so_far = 0

        for feature in curr_set:
            temp_set = [x for x in curr_set if x != feature]
            score = rando(temp_set)
            print(f"Using features {temp_set} accuracy is {score}%")

            if score>best_so_far:
                best_so_far = score
                feature_to_remove = feature
        
        temp_set = [x for x in curr_set if x != feature_to_remove]
        print(f"\nFeature set {temp_set} was best, accuracy is {best_so_far}%\n")

        if best_so_far<best_overall:
            print("Warning, Accuracy has decreased!")
        
        curr_set.remove(feature_to_remove)
        best_overall = max(best_overall, best_so_far)

    print(f"Finished search!! The best feature subset is {curr_set}"
          f" with accuracy of {best_overall}%")


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