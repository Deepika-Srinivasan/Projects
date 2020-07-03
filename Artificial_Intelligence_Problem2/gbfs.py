#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:01:00 2019
vanilla breadth first search
- relies on  Puzzle8.py module

@author: Milos Hauskrecht (milos)
"""

# //Deepika Srinivasan
# // 700693073
# //Certificate of Authenticity: “I certify that the codes/answers of this assignment are entirely my own work.”


import Puzzle8
from Puzzle8 import*

 ### ++++++++++++++++++++++++++++++++++++++++++++++++++++
 ### Greedy_Best_First_Search_stats 


def Greedy_Best_First_Search_stats():
    print('Stats')
    print('Total Nodes expanded:' ,nodes_expanded)
    print('Total Nodes generated:' ,nodes_generated)
    print('Maximum queue length:' ,max_queue_length)
    print('Length of solution Path:' ,length_solution_path)
    
nodes_expanded=0;
nodes_generated=0;
max_queue_length=0;
max_queue_length_before_deletion=0;

 ### ++++++++++++++++++++++++++++++++++++++++++++++++++++
 ### Greedy_Best_First_Search 

def Greedy_Best_First_Search(problem):
    global nodes_expanded
    global nodes_generated
    global max_queue_length
    global max_queue_length_before_deletion
    
    #to find the treenode with min_h value
    min_h=100
    
    queue =deque([])
    root=TreeNode(problem,problem.initial_state)
        
    queue.append(root)   
    while len(queue)>0:
        if max_queue_length<len(queue):
            max_queue_length=len(queue)
        next=queue.popleft()
        
        #node picked for expansion so increase the counter
        nodes_expanded+=1
        
        if next.goalp():
            del(queue)
            return next.path()
        else:
            new_nodes=next.generate_new_tree_nodes()
            for new_node in new_nodes:
                #node generated so increment the counter
                nodes_generated+=1
                                
                #check the h value and find the node which is minimum
                if new_node.h<min_h:
                    candidate_for_expansion=new_node
                    min_h=new_node.h
            queue.append(candidate_for_expansion)         
    print('No solution')
    return NULL

problem=Puzzle8_Problem(Example1) 
output= Greedy_Best_First_Search(problem)
length_solution_path=len(output)
print('Solution Example 1:')
print_path(output)
Greedy_Best_First_Search_stats()

# wait = input("PRESS ENTER TO CONTINUE.")

# problem=Puzzle8_Problem(Example2) 
# output= Greedy_Best_First_Search(problem)
# length_solution_path=len(output)
# print('Solution Example 2:')
# print_path(output)
# Greedy_Best_First_Search_stats()

# wait = input("PRESS ENTER TO CONTINUE.")

# problem=Puzzle8_Problem(Example3) 
# output= Greedy_Best_First_Search(problem)
# length_solution_path=len(output)
# print('Solution Example 3:')
# print_path(output)
# Greedy_Best_First_Search_stats()

# wait = input("PRESS ENTER TO CONTINUE.")

# problem=Puzzle8_Problem(Example4) 
# output= Greedy_Best_First_Search(problem)
# length_solution_path=len(output)
# print('Solution Example 4:')
# print_path(output)
# Greedy_Best_First_Search_stats()

# wait = input("PRESS ENTER TO CONTINUE.")

# problem=Puzzle8_Problem(Example5) 
# output= Greedy_Best_First_Search(problem)
# length_solution_path=len(output)
# print('Solution Example 5:')
# print_path(output)
# Greedy_Best_First_Search_stats()