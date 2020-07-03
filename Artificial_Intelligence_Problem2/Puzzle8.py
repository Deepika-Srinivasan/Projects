#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Puzzle 8 problem.
This module includes:
     - Puzzle 8 problem definition
     - Search Tree
     - hash table implementation
     - 5 Examples of increasing complexity
"""

# //Deepika Srinivasan
# // 700693073
# //Certificate of Authenticity: “I certify that the codes/answers of this assignment are entirely my own work.”

from collections import deque
import random


NO_MOVE =-1
NULL = -1

# definition of the Puzzle 8 problem
class Puzzle8_Problem:
    initial_state=''
    move_cost=1
    end_state=(1,2,3,4,5,6,7,8,0) #defines end state
    valid_moves=[
         [NO_MOVE,3,NO_MOVE,1],
         [NO_MOVE,4,0,2],
         [NO_MOVE,5,1,NO_MOVE],
         [0,6,NO_MOVE,4],
         [1,7,3,5],
         [2,8,4,NO_MOVE],
         [3,NO_MOVE,NO_MOVE,7],
         [4,NO_MOVE,6,8],
         [5,NO_MOVE,7,NO_MOVE]
         ]

    def __init__(self, init_state=(1,2,3,4,5,6,7,8,0)):
        self.initial_state=init_state

    def shuffle_state(self,k):
        pick=self.end_state
        for i in range(k):
            new=self.generate_all_neighbor_states(pick)
            pick , cost=random.sample(new,1)[0]
            print(pick)
        return pick

    def goal_condition(self,state):
        return (state == self.end_state)

    def generate_all_neighbor_states(self, state):
        res=[]
        zero_position=state.index(0)
        for i in range(4):
            next_position=self.valid_moves[zero_position][i]
            if next_position != NO_MOVE:
                new_state=list(state)
                new_state[zero_position], new_state[next_position] = state[next_position], state[zero_position]
                # print(new_state)
                res.append([tuple(new_state), self.move_cost])
        return res

    def h_function(self,state):
        hvalue=0
        x=0
        y=0
        #Check for the each value in the state
        for value in state:
            #Comparing the state value and goal state value
            position_difference = abs(self.end_state.index(value) - state.index(value))
            #Position 0 is not considered
            if value is not 0:
                x = position_difference % 3
                y = position_difference / 3
                hvalue += x + int(y)
                if abs(self.end_state.index(value) % 3 - state.index(value) % 3) == 2 and position_difference % 3 == 1:
                    hvalue += 2
        return hvalue




# definition of the TreeNode
# defines a node of the search tree
class TreeNode:

    problem=NULL
    state=''
    parent = NULL
    f=0
    g=0
    h=0   # values of f, g and h functions related to path

    def __init__(self, problem, state, parent=0,g_value=0):
        self.problem=problem
        self.state=state
        self.parent = parent
        self.g=g_value
        self.h=problem.h_function(state)
        self.f=self.g+self.h

    # checks if the node is a goal
    def goalp(self):
        pr=self.problem
        return pr.goal_condition(self.state)

    # generates a list of new tree nodes to be added to the search fringe
    def generate_new_tree_nodes(self):
        new_neighbors = (self.problem).generate_all_neighbor_states(self.state)
        res=[]
        for new_state in new_neighbors:
            new_node=TreeNode(self.problem, new_state[0], self, self.g+new_state[1])
            res.append(new_node)
        return res

    # prints a state associated with a node
    def print_state(self):
        for j in range(0,9,3):
            print((self.state[j],self.state[j+1],self.state[j+2]))
        print(' ')

    # returns a path (an ordered list of tree nodes) from the root to this node
    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))




# definition of the hash table that can be used to store Puzzle 8 states
# use it to check for state repeats
class HashTable:
    hash={}

    def __init__(self):
        self.hash={}

    def in_hashp(self, item):
        return (item in self.hash)

    def add_hash(self, item, value=0):
        self.hash[item]=value

    def get_hash_value(self, item):
        if item in self.hash:
            return self.hash[item]
        else:
            return -1
    def delete_hash(self):
        del(self.hash)
        self.hash={}


def print_path(path):
    for node in path:
        node.print_state()



Example1=(1,2,3,4,6,0,7,5,8)
Example2=(2,3,0,1,5,6,4,7,8)
Example3=(4,1,2,7,6,3,0,5,8)
Example4=(4,1,2,7,6,3,5,8,0)
Example5=(5,3,0,4,7,6,2,1,8)
