# -*- coding: utf-8 -*-
"""
Created on Fri Jun 06 21:24:55 2014

Proejct dataset reader

@author: Jerry
"""

import numpy as np
from random import shuffle

"""
Provided helper methods to process the dataset
"""

def read_data(dna_data_file, labels_file):
    """
    Reads training files.
    Returns training_data, a list of tuples contains training data and labels.
    """
    print 'reading dna data...'
    dna_data = np.genfromtxt(dna_data_file, dtype='str', delimiter='\n')
    print 'reading labels...'
    labels = np.genfromtxt(labels_file, dtype='int', delimiter='\n')
    
    if len(dna_data) != len(labels):
        raise StandardError('ERROR: training data and training labels have different length')
        
    training_data = []
    for i in range(len(dna_data)):
        sample = (dna_data[i], labels[i])
        training_data.append(sample)
    
    return training_data
        
def generate_training_val_set(training_data_size, training_file, validation_file):
    """
    Randomly generates training and validation set using the training data 
    and save them to file. Training data are split in 4:1 ratio. 4 being training
    set and 1 being validation set
    """
    
    training_index = range(training_data_size)
    print 'shuffle index'
    shuffle(training_index)
    training_set = []
    validation_set= []
    print 'generate training set'
    for i in range(int(0.8 * training_data_size)):
        training_set.append(training_index[i])
    print 'generate validation set'
    for i in range(int(0.8 * training_data_size), training_data_size):
        validation_set.append(training_index[i])
    
    print 'saving files...'
    np.savetxt(training_file, training_set, fmt='%d', delimiter='\n')
    np.savetxt(validation_file, validation_set, fmt='%d', delimiter='\n')
    
    return (training_set, validation_set)

def read_training_val_set(training_file, validation_file):
    training_set = np.genfromtxt(training_file, dtype='int', delimiter='\n')
    validation_set = np.genfromtxt(validation_file, dtype='int', delimiter='\n')
    return (training_set, validation_set)