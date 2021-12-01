# Author: Yolanda Shen
# November - December 2021

import csv


#########################
#      PARAMETERS       #
#########################

# global parameters
bases = {"A": 0, "C": 1, "T": 2, "G": 3, "-": 4}
states = {"I": 0, "D": 1, "M": 2}


# HMM rate tensor as layers, row = s-1, col = s
A_tensor = [[0] * 3 for _ in range(3)]
C_tensor = [[0] * 3 for _ in range(3)]
T_tensor = [[0] * 3 for _ in range(3)]
G_tensor = [[0] * 3 for _ in range(3)]

tensor_dict = {"A": A_tensor, "C": C_tensor, "T": T_tensor, "G": G_tensor}

# transition residue tensors, row = y, col = x
Qi_tensor = [0] * 4
Qm_tensor = [[0] * 4 for _ in range(4)]


#########################
#     FILE READING      #
#########################

def get_align(file):
    f = open(file, "r")
    desc = ""
    anc = ""

    i = 0
    for line in f:

        if line[0] == ">":
            i += 1
        
        elif i == 1:
            desc += line
        
        elif i == 2:
            anc += line

    return desc, anc


#########################
#      PROCESSING       #
#########################

def process_align(pair_align_file):
    # obtain anc and desc
    anc, desc = get_align(pair_align_file)
    anc = anc.replace("\n", "")
    desc = desc.replace("\n", "")

    # parameters
    align_len = len(anc)
    prev_s = None
    s = None
    
    for i in range(align_len):

        anc_residue = anc[i] 
        desc_residue = desc[i]

        # ensure first bp is match
        if i == 0:
            assert anc_residue != "-"
            assert desc_residue != "-"
        
        # ins
        if anc_residue == "-":
            assert desc_residue != "-"
            # count_ins(desc_residue, s)
            s = "I"
            
        # del
        elif desc_residue == "-":
            #count_del(anc_residue, s)
            s = "D"

        # match
        else:
            s = "M"
        
        if prev_s:
            print(i, anc_residue, desc_residue, prev_s, s)
            fill_hmm(prev_s, s, desc_residue, anc_residue)
        
        prev_s = s
        s = None
    
    return None


def fill_hmm(prev_s, s, x, y):
    x_int = bases[x]
    y_int = bases[y]
    s_int = states[s]
    prev_s_int = states[prev_s]

    assert 0 <= s_int <= 2

    # ins
    if s_int == 0:
        for t in tensor_dict.values():
            t[prev_s_int][0] += 1
        Qi_tensor[x_int] += 1

    # del
    elif s_int == 1:
        tensor = tensor_dict[y]
        tensor[prev_s_int][s_int] += 1
    
    # match
    elif s_int == 2:
        tensor = tensor_dict[y]
        tensor[prev_s_int][s_int] += 1
        Qm_tensor[y_int][x_int] += 1

    return None

    

#########################
#        TENSORS        #
#########################


def calc_tensor_rate(tensor):
    new_tensor = []

    if type(tensor[0]) != list:
        tensor = [tensor]

    for row in tensor:
        new_tensor += [[x/sum(row) if sum(row) > 0 else x for x in row]]
    return new_tensor


#### FIXME
def write_tensor(tensor_name, tensor):
    tensor_file = "./tensors"
    with open(f"{tensor_file}/{tensor_name}.csv", "w", newline="") as f:
        write = csv.writer(f)
        write.writerows(tensor)

    return None 


def print_tensor(name=None, t=[]):
    if name:
        print(name)
    for line in t:
        print(line)
    print("\n")