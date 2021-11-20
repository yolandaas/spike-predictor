<script type="text/javascript"
        src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

## Notation

y = prev anc bp  
z = curr anc bp  
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
  
Matrices will be 4x3, with row i being the previous base, and col j being the previous state

***
## Insertion

P(is insertion, inserted bp | prev anc bp, prev state)

P(is insertion | prev anc bp, prev state) * P(inserted bp | is insertion)  
-- may make it also consider len of ins/del  

$P(I\:|\:y,\:s)\:*\:P(x\:|\:I)$  

$insRate(y,\:s)\:*\:Q_i(y \rightarrow x)$


<br/>

***
## Deletion

P(is deletion | prev anc bp, prev state)  
-- may make it also consider len of ins/del  

$P(D | y, s)$  

$delRate(y, s)$
  

<br/>

***
## Match
P(is match, match bp | prev anc bp, prev state)

P(is match | prev anc bp, prev state) * P(match bp | is match)  

$P(M\:|\:y,\:s)\:*\:P(x\:|\:M)$  

$matchRate(y,\:s)\:*\:Q_m(y \rightarrow x)$


## Notes
- 1000-5000 sequences  
- begin with like 10 for proof of concept