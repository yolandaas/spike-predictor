# Author: Yolanda Shen
# November 2021

import csv


#########################
#      PARAMETERS       #
#########################

# global parameters
bases = {"A": 0, "C": 1, "T": 2, "G": 3, "-": 4}
states = {"I": 0, "D": 1, "M": 2}


# state rate tensors, row = y, col = s
"FIXME: write to csv or to txt"
insRate_tensor = [0] * 3
delRate_tensor = [[0] * 3 for _ in range(4)]
matchRate_tensor = [[0] * 3 for _ in range(4)]

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
    s = None
    
    for i in range(align_len):

        anc_residue = anc[i] 
        desc_residue = desc[i]

        # print(i, anc_residue, desc_residue)

        # ensure first bp is match
        if i == 0:
            assert anc_residue != "-"
            assert desc_residue != "-"
        
        # ins
        if anc_residue == "-":
            assert desc_residue != "-"
            count_ins(desc_residue, s)
            s = "I"
            
        # del
        elif desc_residue == "-":
            count_del(anc_residue, s)
            s = "D"

        # match
        else:
            if s is not None:
                count_match(desc_residue, anc_residue, s)
            s = "M"
    
    return None


def count_ins(x, s):
    x_int = bases[x]
    s_int = states[s]
    insRate_tensor[s_int] += 1
    Qi_tensor[x_int] += 1
    return None


def count_del(y, s):
    y_int = bases[y]
    s_int = states[s]
    delRate_tensor[y_int][s_int] += 1
    return None


def count_match(x, y, s):
    x_int = bases[x]
    y_int = bases[y]
    s_int = states[s]
    matchRate_tensor[y_int][s_int] += 1
    Qm_tensor[y_int][x_int] += 1
    return None


#########################
#        TENSORS        #
#########################


#### FIXME
def calc_tensor_rate(tensor):
    return


#### FIXME
def write_tensors():
    return None 


def print_tensor(name=None, t=[]):
    if name:
        print(name)
    for line in t:
        print(line)
    print("\n")


process_align("./fastas/myseq0_align_2021-09-11.fasta")
print_tensor("insRate\n", insRate_tensor)
print_tensor("delRate\n", delRate_tensor)
print_tensor("matchRate\n", matchRate_tensor)
print_tensor("Qi\n", Qi_tensor)
print_tensor("Qm\n", Qm_tensor)
