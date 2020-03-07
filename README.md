# Probabilistic Context-Free Grammar (PCFG)
Implement Probabilistic Context-Free Grammar in python

## Context-Free Grammar (CFG)
Context Free Grammar (CFG) is a certain type of formal grammar, which is represented by V → w, where V is a non-terminal symbol and w is a string consisting of terminals or non-terminals. For example, CFG is expressed as S → NP VP or N → king. 

Context-free means that it can substitute strings for variables regardless of the context.       
CFG consists of a list of rules, a set of terminals and a set of non-terminals.

A context free grammar G is defined by the 4 tuple.   
G = (N, ∑, R, S) where N stands for the set of non-terminal symbols or variables, ∑ stands for the set of terminal symbols, R stands for the set of rules or productions and S stands for the designated start symbol and the member of N. 

CFG is frequently applied to Natural Language Processing (NLP) because it is powerful to describe the syntax of programming languages and simple to allow the construction of efficient parsing algorithms.

CFG is sometimes called as Phrase Structure Grammars (PSG) or Backus-Naur Form (BNF).

## The problem of CFG
Even though CFG is widely used in NLP, it has critical limitation.  
It can generate the ambiguity. One sentence can have many possible trees. 

Humans can choose the most proper tree based on their linguistic knowledge. However, computer just parses the sentence and it does not know which tree is the best output.

For example, the sentence “I saw the man with the telescope” can have two interpretations.   
First, I saw the man by using the telescope. Second, I saw the man who had the telescope. Computer cannot choose the more proper interpretation. Disambiguation is regarded as the most difficult and important task in NLP. 

## The advent of PCFG
Thus, CFG introduced the probability to solve the ambiguity problem. It is called as Probabilistic CFG (PCFG). 

Similar to CFG, A probabilistic context-free grammar is defined by 5 tuple G = (M,T,R,S,P), where M stands for the set of non-terminal symbols, T stands for the set of terminal symbols, R stands for the set of rules or productions, S stands for the start symbol and P stands for the set of probabilities on the rules. 

PCFG counts all the number of CFG rules and calculates each probability. Thus, PCFG needs the training data to calculate the probabilities. The more parse trees training data has, the better performance level PCFG shows. 

In this study, I made a model calculating the probabilities using Python
