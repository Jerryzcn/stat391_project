# -*- coding: utf-8 -*-
"""
Created on Mon Jun 09 00:15:23 2014

@author: Jerry
"""

import data_processor as dp
import numpy as np
from feature_selection import Features
from knn import KNN

def train_and_test():
    training_data = dp.read_data('dataset/splice-Xtrain.dat', 'dataset/splice-Ytrain.dat')
    test_data = dp.read_data('dataset/test40.txt', 'dataset/ytest40.txt')
    feature = Features()
    dp.remove_ambiguous_entry_plus(training_data)
    training_set = feature.amino_acid_count(training_data)
    test_set = feature.amino_acid_count(test_data)
    
    k_nearest_neighbors = KNN(training_set, 21)
    
    confusion_matrix = np.zeros([3,3])
    correct = 0.0
    total = 0.0
    
    for index in range(len(test_set)):
        feature_vector, correct_class = test_set[index]
        prediction = k_nearest_neighbors.predict_codon_manhattan(feature_vector, k_nearest_neighbors.no_weight)
        total += 1
        if prediction == correct_class:
            correct += 1
        if prediction == 0 and correct_class == 0:
            confusion_matrix[0,0] += 1
        if  prediction == 0 and correct_class == 1:
            confusion_matrix[0,1] += 1
        if  prediction == 0 and correct_class == 2:
            confusion_matrix[0,2] += 1
        if  prediction == 1 and correct_class == 0:
            confusion_matrix[1,0] += 1
        if  prediction == 1 and correct_class == 1:
            confusion_matrix[1,1] += 1
        if  prediction == 1 and correct_class == 2:
            confusion_matrix[1,2] += 1
        if  prediction == 2 and correct_class == 0:
            confusion_matrix[2,0] += 1
        if  prediction == 2 and correct_class == 1:
            confusion_matrix[2,1] += 1
        if  prediction == 2 and correct_class == 2:
            confusion_matrix[2,2] += 1  
    
    print confusion_matrix      
    print correct/total
    
if __name__ == '__main__':
    train_and_test()
