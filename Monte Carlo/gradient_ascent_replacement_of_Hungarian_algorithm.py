import numpy as np
import random

ep_input = [[   7,  53, 183, 439, 863, 497, 383, 563,  79, 973, 287,  63, 343, 169, 583 ],
    [ 627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913 ],
    [ 447, 283, 463,  29,  23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743 ],
    [ 217, 623,   3, 399, 853, 407, 103, 983,  89, 463, 290, 516, 212, 462, 350 ],
    [ 960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350 ],
    [ 870, 456, 192, 162, 593, 473, 915,  45, 989, 873, 823, 965, 425, 329, 803 ],
    [ 973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326 ],
    [ 322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601,  95, 973 ],
    [ 445, 721,  11, 525, 473,  65, 511, 164, 138, 672,  18, 428, 154, 448, 848 ],
    [ 414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198 ],
    [ 184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390 ],
    [ 821, 461, 843, 513,  17, 901, 711, 993, 293, 157, 274,  94, 192, 156, 574 ],
    [  34, 124,   4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699 ],
    [ 815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107 ],
    [ 813, 883, 451, 509, 615,  77, 281, 613, 459, 205, 380, 274, 302,  35, 805 ]]

#assertion purposes
def are_equal(b,c):
    n = len(b)
    for i in range(n):
        if b[i] != c[i]:
            return False
    return True


def flip_entries_in_arr(arr, flip):
    (i,j) = flip
    assert(0<= min(i,j) < len(arr))
    arr[i], arr[j] = arr[j], arr[i]


def get_random_permutation(n):
    arr = np.arange(n)
    for i in range(1,n):
        j = random.randint(0,i) #inclusive
        flip_entries_in_arr(arr, (i, j))
    return arr

def get_permuation_score(perm, matrix):
    n = len(perm)
    assert(n==len(matrix) and n==len(matrix[0]))
    score = 0
    for i in range(n):
        score += matrix[i][perm[i]]
    return score

#this does not change perm
def get_permuation_score_with_flip(perm, matrix, flip): 
    old_perm = perm.copy()
    flip_entries_in_arr(perm, flip) #this changes perm
    new_score = get_permuation_score(perm, matrix)
    flip_entries_in_arr(perm, flip) #this reverts the change to perm
    assert(are_equal(perm, old_perm))
    return new_score


def ascent_to_best_flip(perm, matrix, score, flip_list):
    assert(score == get_permuation_score(perm, matrix))
    best_score = score
    best_flip = (0,0)

    for flip in flip_list:
        new_score = get_permuation_score_with_flip(perm, matrix, flip)
        if new_score > best_score:
            best_score = new_score
            best_flip = flip

    flip_entries_in_arr(perm, best_flip) #changes perm using best flip found
    assert(best_score == get_permuation_score(perm, matrix))
    return best_score


def get_random_flip_list(n, flip_list_length):
    flip_list = []
    for _ in range(flip_list_length):
        i = random.randint(1,n-1) #inclusive
        j = random.randint(0,i-1)
        flip_list.append((i,j))
    return flip_list


def gradient_ascent(perm, matrix, score):
    assert(score == get_permuation_score(perm, matrix))
    n = len(perm)

    new_score = ascent_to_best_flip(perm, matrix, score, get_random_flip_list(n,10))
    if new_score > score:
        return gradient_ascent(perm, matrix, new_score)

    assert(score == get_permuation_score(perm, matrix))
    new_score = ascent_to_best_flip(perm, matrix, score, [(i,j) for i in range(1,n) for j in range(i)])

    if new_score > score:
        return gradient_ascent(perm, matrix, new_score)

    #reached local maxima!
    return score


def random_gradient_ascent_trial(matrix):
    n = len(matrix)
    perm = get_random_permutation(n)
    return gradient_ascent(perm, matrix, get_permuation_score(perm,matrix))

max_=0
for _ in range(40):
    curr = random_gradient_ascent_trial(ep_input)
    max_ = max(max_,curr)
    #print(curr)

print("\n\n")
print(max_)
