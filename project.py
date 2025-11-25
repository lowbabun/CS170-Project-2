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
    features = int(features)
    current_set = []

    # Score with no features testing empty set
    base_acc = rando(current_set)
    print(f"Using no features and “random” evaluation, I get an accuracy of {base_acc}%")
    print("Beginning search.")

    best_subset = current_set.copy()   
    best_score = base_acc              

    # Add one feature at each level of the search tree
    for level in range(1, features + 1):

        feature_to_add = None
        level_best_accuracy = -1

        # Test each feature not in current_set
        for feature in range(1, features + 1):
            if feature not in current_set:
                trial = current_set + [feature]
                acc = rando(trial)
                print(f"Using feature(s) {trial} accuracy is {acc}%")

                if acc > level_best_accuracy:
                    level_best_accuracy = acc
                    feature_to_add = feature

        # Add the best feature found at each level of the tree
        if feature_to_add is not None:
            new_set = current_set + [feature_to_add]

            if level_best_accuracy < best_score:
                print("(Warning, Accuracy has decreased!)")

            print(f"Feature set {new_set} was best, accuracy is {level_best_accuracy}%")

            current_set = new_set

            # Store the best subset
            if level_best_accuracy > best_score:
                best_score = level_best_accuracy
                best_subset = new_set.copy()

    print(f"Finished search!! The best feature subset is {best_subset}, "
          f"which has an accuracy of {best_score}%")



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