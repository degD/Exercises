
import random as rd
from math import factorial as fact

def permutations_rd(s):
    """
    Generate permutations of s using pseudo-random operations.
    Assumes s is a string.
    Returns a list containing all permutations.
    """
    numerator = fact(len(s))
    denominator = 1
    
    c_dict = {}
    for c in s:
        
        if c in c_dict:
            c_dict[c] += 1
        else:
            c_dict[c] = 1
            
        denominator *= c_dict[c]
        
    num_of_perm = numerator / denominator
    
    permutations = set()
    while len(permutations) < num_of_perm:
        
        s_list = list(s)
        rd.shuffle(s_list)
        permutations.add(''.join(s_list))
        
    return list(permutations)
