# -*- coding: utf-8 -*-
"""
Created on Fri Jun 06 23:46:32 2014

K-Nearest Neighbors classifier.

@author: Jerry
"""

import heapq
import numpy as np

class KNN:
    def __init__(self, training_set, k):
        self.k = k
        self.instances = training_set
    
    def predict(self, features):
        neighbor_distance = []
        for instance in self.instances:
            distance = 0
            for feature in features:
                for instance_feature in instance[0]:
                    if feature[0] != instance_feature[0]:
                        distance += 1
            neighbor_distance.append((distance, instance[1]))
        k_nearest_neighbors = heapq.nsmallest(self.k, neighbor_distance)
        dna_class = [0,0,0]
        print k_nearest_neighbors
        for neighbor in k_nearest_neighbors:
            dna_class[neighbor[1]] += 1
        return np.argmax(dna_class)