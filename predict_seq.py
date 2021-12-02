# author Yolanda Shen
# November - December 2021

import csv
from random import seed, choices

# global parameters
bases = {"A": 0, "C": 1, "T": 2, "G": 3, "-": 4}
rev_bases = {0: 'A', 1: 'C', 2: 'T', 3: 'G', 4: '-'}
states = {"I": 0, "D": 1, "M": 2}
rev_states = {0: 'I', 1: 'D', 2: 'M'}
rnd = 134
seed(rnd)

# tensors
def read_tensor(file):
    file = f"./tensors/{file}.csv"
    with open(file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

A_rate_tensor = read_tensor("A_rate")
C_rate_tensor= read_tensor("C_rate")
T_rate_tensor = read_tensor("T_rate")
G_rate_tensor = read_tensor("G_rate")
Qi_rate_tensor = read_tensor("Qi_rate")[0]
Qm_rate_tensor = read_tensor("Qm_rate")

tensor_dict = {"A": A_rate_tensor, "C": C_rate_tensor, "T": T_rate_tensor, "G": G_rate_tensor}
state_dict = {"M": "|", "S": "*", "I": "^", "D": "-"}

def simulate(anc, n=1, p=False):
    descs = []
    muts = []
    for i in range(n):
        if p:
            print(anc)
        desc, mut = generate_descendant(anc)
        descs += [desc]
        muts += [mut]
        if p:
            print(str.join("", mut))
            print(desc)
    
    return descs, muts


def generate_descendant(ancestor):
    descendant = ancestor[0]
    prev_s = "M"
    mutations=["|"]
    i = 1
    while i < len(ancestor):
        y = ancestor[i]
        s = next_state(prev_s, y)
        x = next_base(s, y)
        descendant += x

        if s == "M" and y != x:
            mutations += [state_dict["S"]]
        else:
            mutations += [state_dict[s]]
        
        if s != "I":
            i += 1

        prev_s = s
    return descendant, str.join("", mutations)


def next_state(prev_s, y):
    prev_s_int = states[prev_s]
    tensor = tensor_dict[y]
    probs = [int(x) for x in tensor[prev_s_int]]
    s = choices([0, 1, 2], weights=probs, k=1)[0]
    return rev_states[s]


def next_base(s, y):
    y_int = bases[y]

    if s == "M":
        probs = [int(x) for x in Qm_rate_tensor[y_int]]
        x = choices([0, 1, 2, 3], weights=probs)[0]
        return rev_bases[x]
    elif s == "I":
        probs = [int(x) for x in Qi_rate_tensor]
        x = choices([0, 1, 2, 3], weights=probs)[0]
        return rev_bases[x]
    else:
        return "-"