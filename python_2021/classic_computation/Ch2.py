# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 12:00:58 2021

@author: WB
"""


### CH2: Searching problems
### DNA search:
from enum import IntEnum
# IntEnum VS Enum ---> IntEnum: subclass of integer, Enum: not a subclass of integer
# IntEnum : can use comparison operator
gene_set = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
print(gene_set)
print(gene_set['A'])
for gene in gene_set:
    print(gene)
    print("Integer mapping of this gene is {}".format(gene))
# Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]  type alias for codons
# Gene = List[Codon]   type alias for gene
# Gene string: string of ACGT
    
# Convert Gene to Condon(3 Nucleotide) --> string to tuple
def gene_to_condon(string):
    print(len(string))
    if len(string)<3:
        return "No Condon"
    condon_list = []
    for i in range(0,len(string)-2,3):
        condon = (gene_set[string[i]],gene_set[string[i+1]],gene_set[string[i+2]])
        condon_list.append(condon)
    return condon_list
test_gene = gene_to_condon('ACGTCGATGCATCGAA')
print(test_gene)
print(len(test_gene))

def linear_search_condon(condon, gene):
    for i in range(gene):
        if gene[i]==condon:
            return i
    return "Not Found"

def binary_search_condon(condon, gene):
    high = len(gene)-1
    low = 0
    middle = (high + low)//2
    sample = gene
    while  len(sample)>1:
        if gene[middle]==condon:
            return True
        elif condon>gene[middle]:
            #high = middle
            low = middle+1
            sample = sample[middle+1:]
            middle = (high + low)//2
            
        elif condon<gene[middle]:
            high = middle -1
            sample = sample[:middle]
            middle = (high + low)//2
    return False

test_gene =[(gene_set['G'],gene_set['C'],gene_set['T']),(gene_set['C'],gene_set['T'],gene_set['A']),(gene_set['A'],gene_set['T'],gene_set['G'])] 
print(test_gene)
print(type(test_gene))
test_gene.sort()
print(test_gene)
print(gene_set['A'] > gene_set['C'])


### Maze Problem        
#test = [['','x','x'],['x','x', ''],['','','']]
#print(test)
from enum import Enum
from typing import NamedTuple

# This is the basic building block for the maze
class Cell(str, Enum):
    empty = ''
    block = 'X'
    start = 'S'
    end = 'E'
    path = '*'

# Use tuple to name the location   
class Mazelocation(NamedTuple):
    ## How this work??
    colum: int
    row: int

loc1 = Mazelocation(0,0)
print(loc1.colum)   
print([[Cell.empty for i in range(10)]])

class Maze:
    def __init__(self, rows=10, colums=10, sparsness=0.2,start=Mazelocation(0,0),end= Mazelocation(9,9)):
        self.rows = rows
        self.coluns =colums
        self.sparsness = sparsness
        self.start = start
        self.end = end
        
