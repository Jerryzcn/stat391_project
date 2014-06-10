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
    
    def predict_diff_bases(self, features, weight_fn):
        neighbor_distance = []
        for instance in self.instances:
            distance = 0
            for i in range(len(features)):
                if features[i][0] != instance[0][i][0]:
                    distance += 1
            neighbor_distance.append((distance, instance[1]))
        k_nearest_neighbors = heapq.nsmallest(self.k, neighbor_distance)
        dna_class = [0,0,0]
        print k_nearest_neighbors
        for neighbor in k_nearest_neighbors:
            dna_class[neighbor[1]] += weight_fn(neighbor[0])
        return np.argmax(dna_class)
        
    def predict_codon_manhattan(self, features, weight_fn):
        neighbor_distance = []
        for instance in self.instances:
            distance = 0
            for feature in features:
                if feature in instance[0]:
                    distance += np.abs(features[feature]-instance[0][feature])
                else:
                    distance += features[feature]
            for instance_feature in instance[0]:
                if instance_feature not in features:
                    distance += instance[0][instance_feature]
            neighbor_distance.append((distance, instance[1]))
        k_nearest_neighbors = heapq.nsmallest(self.k, neighbor_distance)
        dna_class = [0,0,0]
        print k_nearest_neighbors
        for neighbor in k_nearest_neighbors:
            dna_class[neighbor[1]] += weight_fn(neighbor[0])
        return np.argmax(dna_class)
    
    def predict_codon_euclidean(self, features, weight_fn):
        neighbor_distance = []
        for instance in self.instances:
            distance = 0
            for feature in features:
                if feature in instance[0]:
                    distance += (features[feature]-instance[0][feature])**2
                else:
                    distance += features[feature]**2
            for instance_feature in instance[0]:
                if instance_feature not in features:
                    distance += instance[0][instance_feature]**2
            neighbor_distance.append((np.sqrt(distance), instance[1]))
        k_nearest_neighbors = heapq.nsmallest(self.k, neighbor_distance)
        dna_class = [0,0,0]
        print k_nearest_neighbors
        for neighbor in k_nearest_neighbors:
            dna_class[neighbor[1]] += weight_fn(neighbor[0])
        return np.argmax(dna_class)    
    
    def no_weight(self, distance):
        return distance

    def inverse_dis_weight(self, distance):
        return 1.0/distance
    
    def linear_weight(self, distance):
        return 60 - distance

    def quadratic_weight(self, distance):
        return 360 - distance**2
