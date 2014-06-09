# -*- coding: utf-8 -*-
"""
Created on Sat Jun 07 16:38:56 2014

@author: Jerry
"""

class Features:
    """
    A = 0
    T = 1
    G = 2
    C = 3
    (D = 4)
    (N = 5)
    (S = 6)
    (R = 7)
    """    
    def _convert_base(self, base):
        if base == 'A':
            return [0]
        elif base == 'T':
            return [1]
        elif base == 'G':
            return [2]
        elif base == 'C':
            return [3]
        elif base == 'D':
            return [0,1,2]
        elif base == 'N':
            return [0,1,2,3]
        elif base == 'S':
            return [2,3]
        else:
            return [0,2]
            
    def simple(self, data):
        training_data = []
        for dna_seq, label in data:
            tmp = []
            for base in dna_seq:
                tmp.append(self._convert_base(base))
            training_data.append((tmp, label))
        return training_data
        
    def codon(self, data):
        return 0
        
    def amino_acid(self, data):
        return 0