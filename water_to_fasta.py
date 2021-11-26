import re

# Author: Yolanda Shen
# November 2021


# TODO: CONVERT TO FUNCTIONS AND MAKE IT INTO A LOOP

# read from alignment
alignment_folder = "./alignments"
file_name = "myseq0_align"
path = f"{alignment_folder}/{file_name}.fa"
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

def write_fasta(file_name, anc_name, anc, desc_name, desc):
    f = open(f"./fastas/{file_name}_{desc_name}.fasta", "w")
    f.write(f">{anc_name}\n{anc}\n>{desc_name}\n{desc}")
    f.close()

write_fasta(file_name, anc_name, anc, desc_name, desc)