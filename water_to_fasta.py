# Author: Yolanda Shen
# November - December 2021

import re
import os


def convert_files(alignment_folder):   
    for file in os.listdir(alignment_folder):
        convert_file(alignment_folder, file)


def convert_file(alignment_folder, file_name):
    path = f"{alignment_folder}/{file_name}"
    file = open(path, "r")
    f = file.read()

    # COVID reference sequence name
    anc_name = "21563-25384"
    desc_name = re.search("# 2: .*", f).group().split("# 2: ")[1]


    f_by_line = f.split("\n")
    sequences = [line for line in f_by_line if len(line)>0 and line[0]!="#"]

    anc = ""
    desc = ""

    for line in sequences:
        if anc_name==line[:len(anc_name)]:
            anc += re.search("([ACTG]+-*[ACTG]*)|([ACTG]*-*[ACTG]+)", line).group()
        elif desc_name==line[:len(desc_name)]:
            desc += re.search("([ACTG]+-*[ACTG]*)|([ACTG]*-*[ACTG]+)", line).group()

    # print(anc)
    # print(desc)
    write_fasta(file_name, anc_name, anc, desc_name, desc)


def write_fasta(file_name, anc_name, anc, desc_name, desc):
    file_name = file_name.split(".")[0]
    f = open(f"./fastas/{file_name}_{desc_name}.fasta", "w")
    f.write(f">{anc_name}\n{anc}\n>{desc_name}\n{desc}")
    f.close()
