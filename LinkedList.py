# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:36:53 2017

@author: ma
"""
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        
    def getData(self):
        return self.data
        
    def getNext(self):
        return self.next
        
    def setData(self,data):
        self.data = data
    
    def setNext(self,newNext):
        self.next = newNext
        
class List:
    def __init__(self):
        self.head = None
         
    def isEmpty(self):
        return self.head == None
        
    def add(self,data):
        node = Node(data)
        node.setNext(self.head)
        self.head = node
    
    def size(self):
        count = 0
        node = self.head
        if None != node:
            node = self.head
            while node != None:
                count += 1
                node = node.getNext()
                
        return count
        
    def search(self,finddata):
        count = 1
        node = self.head
        found = False
        while node!=None and found == False:
            if node.getData() == finddata:
                found = True
                print("value found @ ",count) 
            
            node = node.getNext()
            count += 1
        if found==False:
            print("value found not found")
            
    def printList(self):
        node = self.head
        while node!=None:
            print(" ", node.getData())
            node = node.getNext()
            
    def remove(self,dataToRemove):
        currentNode = self.head
        preNode = self
        while currentNode != None:
            if currentNode.getData() == dataToRemove:
                preNode.setNext(currentNode.getNext())
                print("element removed", dataToRemove)
                currentNode = currentNode.getNext()
            else:
                preNode = currentNode
                currentNode = currentNode.getNext()


