# Workflow Refactoring

Business process optimization has become a strategic aspect of companies' management due to the potential of cost reduction and throughput improvement.
There are several ways to achieve process optimization, depending on the level of expressiveness of the processes at hand. 
This is an anonymous repository specifically created to companion a research paper submitted to ICSOC 2022.
In such a paper, we focus on processes described using BPMN, but also including an explicit description of execution time and resources associated with tasks. 
In it, we propose a refactoring procedure whose final goal is to reduce the total execution time of the process given as input. 
Such a procedure relies on refactoring operations that reorganize the tasks in the process by taking into account the resources used by those tasks. 

This repository contains the tool implementing the process refactoring technique.
The tools has been implemented in Python.
Several examples are also provided in this repo.

Repo's contains and structure:
- the code folder contains the Python code with the implementation of the tool
- the examples folder contains several invocations of the tool in a Python script with different BPMN processes codified using our  representation.