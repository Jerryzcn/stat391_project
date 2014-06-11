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
            
    def _convert_to_amino(self, codon):
        if codon in ['TTT','TTC']:
            return 'Phe'
        if codon in ['TTA','TTG','CTT','CTC','CTA','CTG']:
            return 'Leu'
        if codon in ['ATT','ATC','ATA']:
            return 'lle'
        if codon in ['ATG']:
            return 'Met'
        if codon in ['GTT','GTC','GTA','GTG']:
            return 'Val'
        if codon in ['TCT','TCC','TCA','TCG','ATG','AGC']:
            return 'Ser'
        if codon in ['CCT','CCC','CCA','CCG']:
            return 'Pro'
        if codon in ['ACT','ACC','ACA','ACG']:
            return 'Thr'
        if codon in ['GCT','GCC','GCA','GCG']:
            return 'Ala'
        if codon in ['TAT', 'TAC']:
            return 'Tyr'
        if codon in ['TAA', 'TGA', 'TAG']:
            return 'STOP'
        if codon in ['CAT', 'CAC']:
            return 'His'
        if codon in ['CAA', 'CAG']:
            return 'Gln'
        if codon in ['AAT', 'AAC']:
            return 'Asn'
        if codon in ['AAA', 'AAG']:
            return 'Lys'
        if codon in ['GAT', 'GAC']:
            return 'Asp'
        if codon in ['GAA', 'GAG']:            
            return 'Glu'
        if codon in ['TGT, TGC']:
            return 'Cys'
        if codon in ['TGG']:
            return 'Trp'
        if codon in ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']:
            return 'Arg'
        if codon in ['GGT', 'GGC', 'GGA', 'GGG']:
            return 'Gly'
            
    def simple(self, data):
        training_data = []
        for dna_seq, label in data:
            tmp = []
            for base in dna_seq:
                tmp.append(self._convert_base(base))
            training_data.append((tmp, label))
        return training_data
        
    def codon_count(self, data):
        training_data = []
        for dna_seq_simple, label in data:
            feature = {}
            for i in range(len(dna_seq_simple)):
                bases = dna_seq_simple
                if i > 57:
                    break
                if (bases[i]+bases[i+1]+bases[i+2]) in feature:
                    feature[bases[i]+bases[i+1]+bases[i+2]] += 1
                else:
                    feature[bases[i]+bases[i+1]+bases[i+2]] = 1
            
            training_data.append((feature, label))
        return training_data
        
    def amino_acid_count(self, data):
        training_data = []
        for dna_seq_simple, label in data:
            feature = {}
            j = 0
            for i in range(len(dna_seq_simple)):
                bases = dna_seq_simple
                if j > 57:
                    break
                amino_acid = self._convert_to_amino(bases[j]+bases[j+1]+bases[j+2])
                if (amino_acid) in feature:
                    feature[amino_acid] += 1
                else:
                    feature[amino_acid] = 1
                j += 3
            
            training_data.append((feature, label))
        return training_data