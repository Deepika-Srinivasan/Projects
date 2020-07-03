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
#git test
#test branch comment
# i want to check the new chages
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
 #### check_cyclic_repeats

def check_cyclic_repeats(node):
    global parents
    return node in parents

 #### ++++++++++++++++++++++++++++++++++++++++++++++++++++
 #### breadth first search cycles


nodes_expanded=0;
nodes_generated=0;
max_queue_length=0;
parents={()}

def breadth_first_search_cycles(problem):
    global nodes_expanded
    global nodes_generated
    global max_queue_length
    global parents

    queue =deque([])
    root=TreeNode(problem,problem.initial_state)
    queue.append(root)

    while len(queue)>0:
        if max_queue_length<len(queue):
            max_queue_length=len(queue)
        next=queue.popleft()

        if next.goalp():
            del(queue)
            return next.path()

        else:
            #make sure current state is not same like its parents and not entering a cycle
            if not check_cyclic_repeats(next.state):
                #print("Node not in parents so expanding it")
                parents.add(next.state) #add this current state in Parent set
                new_nodes=next.generate_new_tree_nodes()
                nodes_expanded+=1 #increment counter as this node is selected for expansion
                for new_node in new_nodes:
                    queue.append(new_node)
                    nodes_generated+=1 #increment counter for every new node generated


    print('No solution')
    return NULL

problem=Puzzle8_Problem(Example1)
output=  breadth_first_search_cycles(problem)
print('Solution Example 1:')
print_path(output)
length_solution_path=len(output)
breadth_first_search_stats()

#wait = input("PRESS ENTER TO CONTINUE.")

# problem=Puzzle8_Problem(Example2)
# output=  breadth_first_search_cycles(problem)
# print('Solution Example 2:')
# print_path(output)
# length_solution_path=len(output)
# breadth_first_search_stats()

# wait = input("PRESS ENTER TO CONTINUE.")

# problem=Puzzle8_Problem(Example3)
# output=  breadth_first_search_cycles(problem)
# print('Solution Example 3:')
# print_path(output)
# length_solution_path=len(output)
# breadth_first_search_stats()

# wait = input("PRESS ENTER TO CONTINUE.")

# problem=Puzzle8_Problem(Example4)
# output=  breadth_first_search_cycles(problem)
# print('Solution Example 4:')
# print_path(output)
# length_solution_path=len(output)
# breadth_first_search_stats()

# Solution to Example 5 may take too long to calculate using vanilla bfs
# problem=Puzzle8_Problem(Example5)
# output=  breadth_first_search_cycles(problem)
# print('Solution Example 5:')
# print_path(output)
