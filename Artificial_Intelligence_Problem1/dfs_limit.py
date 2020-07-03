#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:01:00 2019
vanilla breadth first search
- relies on  Puzzle8.py module

@author: Milos Hauskrecht (milos)

//Deepika Srinivasan 
//700693073 
//Certificate of Authenticity: “I certify that the codes/answers of this assignment are entirely my own work.” 
"""

import Puzzle8
from Puzzle8 import*

 #### ++++++++++++++++++++++++++++++++++++++++++++++++++++
 #### breadth_first_search_stats 

def breadth_first_search_stats():
    #print('Stats')
    print('Total Nodes expanded:' ,nodes_expanded)
    print('Total Nodes generated:' ,nodes_generated)
    print('Maximum queue length:' ,max_queue_length)
    print('Length of solution Path:' ,length_solution_path)

    
 #### ++++++++++++++++++++++++++++++++++++++++++++++++++++
 #### breadth first search cycles         
        

nodes_expanded=0;
nodes_generated=0;
max_queue_length=0;
max_queue_length_before_deletion=0;

def depth_first_search_limit(problem,limit):
    global nodes_expanded
    global nodes_generated
    global max_queue_length
    global max_queue_length_before_deletion
    my_hash=HashTable()
    
    queue =deque([])
    root=TreeNode(problem,problem.initial_state)
    queue.append(root)
    
    #Add root into hashtable
    my_hash.add_hash(root.state)
     
    while len(queue)>0:
        if max_queue_length<len(queue):
            max_queue_length=len(queue)
        
        next=queue.popleft()
                
        if next.goalp():
            if max_queue_length_before_deletion<len(queue):
                max_queue_length_before_deletion=len(queue)
            del(queue)
            my_hash.delete_hash()
            return next.path()
        else:
            #Check whether current node is within limit
            if next.g<limit:
                new_nodes=next.generate_new_tree_nodes()
                nodes_expanded+=1 #increment counter as this node is expanded
                for new_node in new_nodes:
                    nodes_generated+=1 #increment counter for every new node generated
                    
                    #Only if my new node is not already in myhash,add it in queue and the hashtable as well
                    if not my_hash.in_hashp(new_node.state):
                        queue.appendleft(new_node)
                        my_hash.add_hash(new_node.state,my_hash.get_hash_value(next.state)+1)
                                            
    print('No solution')
    return NULL
  
problem=Puzzle8_Problem(Example1) 
output=  depth_first_search_limit(problem,10)
print('Solution Example 1:')
print_path(output)
length_solution_path=len(output)
breadth_first_search_stats()

# wait = input("PRESS ENTER TO CONTINUE.")

# problem=Puzzle8_Problem(Example2) 
# output=  depth_first_search_limit(problem,10)
# print('Solution Example 2:')
# print_path(output)
# length_solution_path=len(output)
# breadth_first_search_stats()

# wait = input("PRESS ENTER TO CONTINUE.")

# problem=Puzzle8_Problem(Example3) 
# output=  depth_first_search_limit(problem,10)
# print('Solution Example 3:')
# print_path(output)
# length_solution_path=len(output)
# breadth_first_search_stats()

# wait = input("PRESS ENTER TO CONTINUE.")

# problem=Puzzle8_Problem(Example4) 
# output=  depth_first_search_limit(problem,10)
# print('Solution Example 4:')
# print_path(output)
# length_solution_path=len(output)
# breadth_first_search_stats()

# Solution to Example 5 may take too long to calculate using vanilla bfs
# problem=Puzzle8_Problem(Example5) 
# output=  depth_first_search_limit(problem,10)
# print('Solution Example 5:')
# print_path(output)
