#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
vanilla breadth first search
- relies on  Puzzle8.py module
"""

# //Deepika Srinivasan
# // 700693073
# //Certificate of Authenticity: “I certify that the codes/answers of this assignment are entirely my own work.”


import Puzzle8
from Puzzle8 import*

 ### ++++++++++++++++++++++++++++++++++++++++++++++++++++
 ### A_Star_Search_stats


def A_Star_Search_stats():
    print('Stats')
    print('Total Nodes expanded:' ,nodes_expanded)
    print('Total Nodes generated:' ,nodes_generated)
    print('Maximum queue length:' ,max_queue_length)
    print('Length of solution Path:' ,length_solution_path)

nodes_expanded=0;
nodes_generated=0;
max_queue_length=0;

 #### ++++++++++++++++++++++++++++++++++++++++++++++++++++
 #### A_Star_Search

def A_Star_Search(problem):

    global nodes_expanded
    global nodes_generated
    global max_queue_length

    #list to sort the queue based on ascending f value(i.e f=h+g)
    list_whole_queue=[]

    queue =deque([])
    root=TreeNode(problem,problem.initial_state)
    queue.append(root)

    while len(queue)>0:
        if max_queue_length<len(queue):
            max_queue_length=len(queue)

        next=queue.popleft()

        #nodes choosen for expansion from queue so increment the counter
        nodes_expanded+=1

        if next.goalp():
            del(queue)
            return next.path()
        else:
            new_nodes=next.generate_new_tree_nodes()
            for new_node in new_nodes:
                #new nodes generated so increment the counter
                nodes_generated+=1

                #add the node to the queue
                queue.append(new_node)

            #make a list of the queue generated so we can sort the list on f values
            list_whole_queue=list(queue)

            #sort the list based on f value
            list_whole_queue.sort(key=lambda x: x.f, reverse=False)

            #clear the queue so we dont add duplicate nodes back in queue
            queue.clear()

            #copy the sorted list back into queue
            for tree in list_whole_queue:
                queue.append(tree)

            #Check the queue on whether the tree is sorted based on f value
            #for tree in queue:
            #    tree.print_state()
            #    print("Tree f value found is",tree.f)


    print('No solution')
    return NULL

problem=Puzzle8_Problem(Example1)
output=  A_Star_Search(problem)
length_solution_path=len(output)
print('Solution Example 1:')
print_path(output)
A_Star_Search_stats()

# wait = input("PRESS ENTER TO CONTINUE.")

# problem=Puzzle8_Problem(Example2)
# output=  A_Star_Search(problem)
# length_solution_path=len(output)
# print('Solution Example 2:')
# print_path(output)
# A_Star_Search_stats()

# wait = input("PRESS ENTER TO CONTINUE.")

# problem=Puzzle8_Problem(Example3)
# output=  A_Star_Search(problem)
# length_solution_path=len(output)
# print('Solution Example 3:')
# print_path(output)
# A_Star_Search_stats()

# wait = input("PRESS ENTER TO CONTINUE.")

# problem=Puzzle8_Problem(Example4)
# output=  A_Star_Search(problem)
# length_solution_path=len(output)
# print('Solution Example 4:')
# print_path(output)
# A_Star_Search_stats()

# Solution to Example 5 may take too long to calculate using vanilla bfs
# problem=Puzzle8_Problem(Example5)
# output=  A_Star_Search(problem)
# length_solution_path=len(output)
# print('Solution Example 5:')
# print_path(output)
# A_Star_Search_stats()
