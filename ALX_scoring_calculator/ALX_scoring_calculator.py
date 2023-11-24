"""
    Calculates the final score percentage or Score in current project or both
"""
def final_score(current, number_of_projects, *added_projects):
    """
        Calculates the worst and best case of your situation and the actual case you've entered

        parameters:
            'current' is your percentage
            'number_of_projects' is your completed projects
            'added_projects' is the integer (score) per each added future project
    """
    print("Worst case: ", round(current * number_of_projects / (number_of_projects + len(added_projects)), 2))
    print("Best Case: ", round((current * number_of_projects + 200 * len(added_projects)) / (number_of_projects + len(added_projects)), 2))
    print("Final score: ", round((current * number_of_projects + sum(added_projects)) / (number_of_projects + len(added_projects)) ,2))

def worst_score(current, number_of_projects, total_projects):
    """
        Calculates the abandoned projects starting from your current score and tells you if you are safe or not.

        parameters:
            'current' is your current score
            'number_of_projects' are your completed projects
            'total_projects' are the total number of projects including the completed ones
    """
    total = current * number_of_projects / total_projects
    print("Worst score is gonna be: ", total)
    if total < 70:
        print("you need {} more to get 70!!".format(round((70 * total_projects - current * number_of_projects), 2)))
    else:
        print("You're safe! you can relax now!")