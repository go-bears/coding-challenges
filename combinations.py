"""
    Define NumScores(A,B):

        If A=0 and B=0, return 1
        Else If A<0 or B<0, return 0
        Else If A<25 and B<25, return NumScores(A-1,B) + NumScores(A,B-1)
        Else If |A-B|>1, return 0
        Else return NumScores(A-1,B) + NumScores(A,B-1)

"""

def num_scores(a_score, b_score):

    if a_score == 0 and b_score == 0:
        return 1
    elif a_score < 0 or b_score < 0:
        return 0
    elif a_score < 25 and b_score < 25:
        return num_scores(a_score - 1, b_score)+num_scores(a_score,b_score-1)

    # elif abs(a_score - b_score) > 1:
    #     return 0
    else:
        return num_scores(a_score - 1, b_score)+num_scores(a_score,b_score-1)

# print num_scores(3,25)


def n_choose_k(a_score, b_score):
    """
    Function to find combinations of score sequences
    of a volleyball game, using n choose k combinations formula
    """

    # import module for factorial function
    import math

    # validation for edge cases
    if a_score < 1 or b_score < 1 or \
    a_score > 25 or b_score > 25:
        return

    # assign larger score to value a
    if b_score > a_score:
        a = b_score-1
        b = a_score

    # assigns a_score to a variable a
    if a_score > b_score:

        # game ends with team A winning, so final sequence is 
        # known. Subtract 1 possible combination possibility
        a = a_score - 1
        b = b_score

    # in a volleyball game, team a must win by 2 points
    if b_score < (a_score - 2):

        # n = number of total possiblity combinations for total score between team A and team B
        n = math.factorial(a+b)

        # k = number of valid possibilities for where b team scores 3 points
        k = math.factorial(a) * math.factorial(b)
        
        # sequences = n choose k possibilities 
        sequences =  n/k

        return sequences

print n_choose_k(25, 3)