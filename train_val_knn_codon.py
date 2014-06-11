# -*- coding: utf-8 -*-
"""
Created on Mon Jun 09 17:54:23 2014

@author: Jerry
"""


import data_processor as dp
import numpy as np
from feature_selection import Features
from knn import KNN

def train_and_val():
    training_data = dp.read_data('dataset/splice-Xtrain.dat', 'dataset/splice-Ytrain.dat')
    training_set_indices, validation_set_indices = dp.read_training_val_set('dataset/train.txt', 'dataset/val.txt')
    feature = Features()
    features_labels_pair = feature.amino_acid_count(training_data)
    training_set = []
    for index in training_set_indices:
        training_set.append(features_labels_pair[index])
    
    dp.remove_ambiguous_entry_plus(training_set)
    k_nn = KNN(training_set, 23)
    
    confusion_matrix = np.zeros([3,3])
    correct = 0.0
    total = 0.0
    
    validation_set = []
    for index in validation_set_indices:
        validation_set.append(features_labels_pair[index])
    
    dp.remove_ambiguous_entry_plus(validation_set)
    for feature_vector, correct_class in validation_set: 
        prediction = k_nn.predict_codon_manhattan(feature_vector, k_nn.no_weight)
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
        #print prediction, correct_class
    print confusion_matrix      
    print correct/total     
    
def generate_train_val():
    training_data = dp.read_data('dataset/splice-Xtrain.dat','dataset/splice-Ytrain.dat')
    dp.generate_training_val_set(len(training_data), 'dataset/train.txt', 'dataset/val.txt')
    

if __name__ == '__main__':
    #generate_train_val()
    train_and_val()
