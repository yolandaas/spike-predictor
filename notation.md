<script type="text/javascript"
        src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

## Notation

y = curr anc bp  
x = descendant bp (inserted or matched)  

s = prev state  

I = ins  
D = del  
M = match  

<br/>

## Values (for tensors)

#### Base Pairs
A = 0  
C = 1  
T = 2  
G = 3  
  
I = 0  
D = 1  
M = 2  
  
Matrices will be 3x3, with row i being the previous base, and col j being the previous state

***
## Insertion

P(is insertion, inserted bp | prev anc bp, prev state)

P(is insertion | prev anc bp, prev state) * P(inserted bp | is insertion, prev anc bp, prev state)  

ins bp is independent of prev state so we take that out  
insertion state and ins bp is independent of current ancestor bp, so it is also removed from both

$P(I\:|\:y)\:*\:P(x\:|\:I)$  

<br/>

***
## Deletion

P(is deletion | prev anc bp, prev state)  

$P(D | y, s)$  
  

<br/>

***
## Match
P(is match, match bp | prev anc bp, prev state)

P(is match | prev anc bp, prev state) * P(match bp | is match, prev anc bp, prev state)  

match bp is independent of prev state so we take that out  

$P(M\:|\:y,\:s)\:*\:P(x\:|\:M,\:y)$  


## bash commands

`awk 'BEGIN {n_seq=0;} /^>/ {if(n_seq%1==0){file=sprintf("raw_fasta/myseq%d.fa",n_seq);} print >> file; n_seq++; next;} { print >> file; }' < gisaid_hcov-19_2021_12_02_02.fasta`  

`for i in {0..645}; do echo ${i}; water -asequence gene.fna -bsequence raw_fasta/myseq${i}.fa -gapopen 10.0 -gapextend 0.5 -outfile aligned/myseq${i}_align.water; done`