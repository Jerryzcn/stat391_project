# -*- coding: utf-8 -*-
"""
Created on Mon Jun 09 00:15:23 2014

@author: Jerry
"""

import data_processor as dp
from feature_selection import Features
from knn import KNN

def train_and_test():
    training_data = dp.read_data('dataset/splice-Xtrain.dat', 'dataset/splice-Ytrain.dat')
    test_data = dp.read_data('dataset/test40.txt', 'dataset/ytest40.txt')
    feature = Features()
    dp.remove_ambiguous_entry_plus(training_data)
    training_set = feature.amino_acid_count(training_data)
    test_set = feature.amino_acid_count(test_data)
    
    k_nearest_neighbors = KNN(training_set, 22)
    
    error_count = 0
    for index in range(len(test_set)):
        feature_vector, correct_class = test_set[index]
        prediction = k_nearest_neighbors.predict_codon_manhattan(feature_vector, k_nearest_neighbors.no_weight)
        if  prediction != correct_class:
            error_count += 1
        print prediction, correct_class
    error_rate = float(error_count)/len(test_set)
    print 'error rate:', error_rate
    
if __name__ == '__main__':
    train_and_test()
