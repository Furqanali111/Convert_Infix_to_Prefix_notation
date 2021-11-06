#!/usr/bin/env python
# coding: utf-8

# In[1]:


# furqan ali
# 200901073
# BS-CS-01-B

from collections import deque


# creatting a class
class Stack:
    # Setting precedence of operators
    op_pre = {'^': 5, '*': 4, '/': 4, '+': 3, '-': 3, '(': 2, ')': 1}

    # creating constructor
    def __init__(self):
        self.equ = deque()

    # creating push function
    def push(self, val):
        self.equ.append(val)

    # creating pop funtion
    def pop(self):
        if self.isempty():
            return 0
        else:
            return self.equ.pop()

    # creating a function to find if the stack is empty or not
    def isempty(self):
        return len(self.equ) == 0

    # creating top function
    def top(self):
        if self.isempty():
            return False
        else:
            return self.equ[-1]

    # creating a function to find the size of stack
    def size(self):
        return len(self.equ)

    # creating the function to check if the expression one varible is an operator or not
    def OPER(self, expression):
        if expression in "abcdefghijklmnopqurstvwxyz" or expression in "ABCDEFGHIJKLMNOPQURSTVWXYZ" or expression in '1234567890':
            return True
        else:
            return False

    # creating the reverse function so we can interchange location of variables
    def reverse(self, expr):
        rev = ""
        for i in expr:
            # we are changing opening with closing bracket because we are reversing the expresion
            if i == '(':
                i = ')'
            elif i == ')':
                i = '('
            rev = i + rev
        return rev

    # changing infix to prefix
    def Prefix(self, exp):
        pre = []
        for i in exp:
            if (self.OPER(i)):
                pre += i
            elif (i in '+-*/^'):
                # checking for the precedence of the operators
                while (len(self.equ) and self.op_pre[i] < self.op_pre[self.top()]):
                    pre += self.pop()
                self.push(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                val = self.pop()
                while val != '(':
                    pre += val
                    val = self.pop()
            # end of for
        while len(self.equ):
            if (self.top() == '('):
                self.pop()
            else:
                pre += self.pop()
        return pre


# main function starts here
stack = Stack()
expression = input('Enter Expression: ')
rev = []
rev = stack.reverse(expression)
result = stack.Prefix(rev)
prefix = stack.reverse(result)
print("Prefix= ", prefix)

# In[ ]:
