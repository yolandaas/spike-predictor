# spike-predictor

(c) Yolanda Shen 2021

## Goal

Build a HMM to predict COVID spike protein sequences

## Methods

1. Obtain COVID sequences from GISAID (n=646)
2. Pairwise align each sequence to the original COVID spike protein sequence (NCBI link below) via Smith-Waterman & bash in JupyterHub
3. Convert .water > .fasta (water_to_fasta.py)
4. Parse each .fasta for statistics to populate HMM transition matrices (get_stats.py)
5. Provide ancestor sequence and traverse HMM to predict descendant sequences (predict_seq.py)

NCBI link to spike protein sequence: https://www.ncbi.nlm.nih.gov/gene/43740568

## Slides
https://docs.google.com/presentation/d/1Lx5Aq6hIyBhkhd1DB0vQXvRA15tTOf-Nvnh0SYWEWic/edit?usp=sharing