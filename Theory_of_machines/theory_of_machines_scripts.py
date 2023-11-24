def dof(l, j, h=0):
    """
        l = links
        j = joints
        h = higher pairs
    """
    print("The degree of freedom is: ", (3 * (l - 1) - 2 * j - h))

def crank_rocker(s, l, p, q, n=1):
    """
        Defines the type of the mechanism.
        n is just the place of the shortest link.
            1 -> adjacent to fixed link
            2 -> the fixed link
            3 -> opposite to the fixed link
    """
    if (s + l) <= (p + q):
        if n == 1: ## s is adjacent to fixed link
            print("The mechanism is: Crank-rocker")
        elif n == 2: ## s is the fixed link
            print("The mechanism is: dobule crank")
        elif n == 3: ## s is opposite to the link
            print("The mechanism is: Double-rocker")
        if (s + l) == (p + q): ## the special case
            print("\tLinks are collinear")
    else: ## s can be anywhere (value of n doesn't matter)
        print("No complete revolution (Triple rocker)")