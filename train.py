# -*- coding: utf-8 -*-
"""
Created on Sat Jun 07 15:18:19 2014

@author: Jerry
"""
import data_processor as dp

def train():
    training_data = dp.read_data('../dataset/splice-Xtrain.dat','../dataset/splice-Ytrain.dat')
    training_set, validation_set = dp.read_training_val_set('../dataset/train.txt', '../dataset/val.txt')
        
    
        
    return 0

def generate_train_val():
    training_data = dp.read_data('../dataset/splice-Xtrain.dat','../dataset/splice-Ytrain.dat')
    dp.generate_training_val_set(len(training_data), '../dataset/train.txt', '../dataset/val.txt')
    

if __name__ == '__main__':
    #generate_train_val()
    train()