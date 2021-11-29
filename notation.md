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
  
Matrices will be 4x3, with row i being the previous base, and col j being the previous state

***
## Insertion

P(is insertion, inserted bp | prev anc bp, prev state)

P(is insertion | prev anc bp, prev state) * P(inserted bp | is insertion, prev anc bp, prev state)  

ins bp is independent of prev state so we take that out  
insertion state and ins bp is independent of current ancestor bp, so it is also removed from both

$P(I\:|\:y)\:*\:P(x\:|\:I)$  

$insRate(y,\:s)\:*\:Q_i(x)$

<br/>

***
## Deletion

P(is deletion | prev anc bp, prev state)  

$P(D | y, s)$  

$delRate(y, s)$
  

<br/>

***
## Match
P(is match, match bp | prev anc bp, prev state)

P(is match | prev anc bp, prev state) * P(match bp | is match, prev anc bp, prev state)  

match bp is independent of prev state so we take that out  

$P(M\:|\:y,\:s)\:*\:P(x\:|\:M,\:y)$  

$matchRate(y,\:s)\:*\:Q_m(y \rightarrow x)$


## Notes
- 1000-5000 sequences  