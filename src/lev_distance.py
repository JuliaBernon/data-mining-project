### Compute the Levenshtein distance for lists of string ###

def levenshtein_distance_list(l1, l2):
    """
    Compute the Levenshtein distance between two lists of strings.
    
    l1 : List[str]
    l2 : List[str]
    
    levenshtein_distance_list(l1, l2) -> int
    """

    d =[[0 for _ in range(len(l2) + 1)] for _ in range(len(l1) + 1)]
    for i in range(len(l1) + 1):
        d[i][0] = i
    for j in range(len(l2) + 1):
        d[0][j] = j

    for i in range(1, len(l1) + 1):
        for j in range(1, len(l2) + 1):

            if l1[i - 1] == l2[j - 1]:
                cost = 0
            else:
                cost = 1

            d[i][j] = min(d[i - 1][j] + 1,    # deletion  
                          d[i][j - 1] + 1,      # insertion
                          d[i - 1][j - 1] + cost) # substitution
    
    return d[len(l1)][len(l2)]

## test
# l1 = ["a", "b", "c"]
# l2 = ["a", "b", "c", "d"]
# print(levenshtein_distance_list(l1, l2))