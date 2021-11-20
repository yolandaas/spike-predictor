# Author: Yolanda Shen
# November 2021

import csv


# global parameters
bases = {"A": 0, "C": 1, "T": 2, "G": 3}
states = {"I": 0, "D": 1, "M": 2}


# state rate tensors, row = y, col = s
"FIXME: write to csv or to txt"
insRate_tensor = []
delRate_tensor = []
matchRate_tensor = []


# transition residue tensors, row = y, col = x
Qi_tensor = []
Qm_tensor = []


def init_tensors():
    # FIXME set proper tension size and shape
    # currently all 2dim 
    return


def process_align(pair_align_file):

    # open pairwise alignment
    pair_align = open(pair_align_file, "r").split("\n")
    assert len(pair_align) == 2

    # obtain anc and desc
    anc = pair_align[0]
    desc = pair_align[1]

    # parameters
    align_len = len(anc)
    s = None
    y = None
    "FIXME: track len in place of state, or in addition to (?)"
    
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
            count_ins(desc_residue, y, s)
            s = "I"
            
        # del
        elif desc_residue == "-":
            count_del(y, s)
            s = "D"

        # match
        else:
            count_del(desc_residue, y, s)
            s = "M"

        y = anc_residue
    
    return


def count_ins(x, y, s):
    y_int = bases[y]
    s_int = states[s]
    delRate_tensor[y_int][s_int] += 1
    Qi_tensor[y][x] += 1
    return


def count_del(y, s):
    y_int = bases[y]
    s_int = states[s]
    insRate_tensor[y_int][s_int] += 1
    return


def count_match(x, y, s):
    y_int = bases[y]
    s_int = states[s]
    matchRate_tensor[y_int][s_int] += 1
    Qm_tensor[y][x] += 1
    return


def write_tensors():
    return
