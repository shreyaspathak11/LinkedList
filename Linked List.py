# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 21:52:45 2021

@author: shrey
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
    
    def printLinkedList(self):
        temp=self.head
        if temp==None:
            print("No Linked list Present!")
        else:    
            while temp!=None:
                print (temp.data)
                temp=temp.next
        
    
    def insertAtStart(self,value):
        if self.head==None:
            p=Node(value)
            p.next=self.head
            self.head=p
        else:
            p=Node(value)
            p.next=self.head
            self.head=p
            
    def insertAtEnd(self,value):
        if self.head==None:
            p=Node(value)
            p.next=None
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            if temp.next==None:
                p=Node(value)
                temp.next=p
                p.next=None
     
    def insertByIndex(self,index,value):
        i=0
        if index==0:
            p=Node(value)
            p.next=self.head
            self.head=p
                                                    
        else:
            temp=self.head
            while i!=(index-1) :
                temp=temp.next
                i=i+1
            if i==index-1:
                p=Node(value)
                p.next=temp.next
                temp.next=p
                
            else:    
                print('Invalid Index')
    
    def insertAfterValue(self,target,value):
        temp=self.head
        while temp.data!=target:
            temp=temp.next
        if temp.data!=target:
            print('Wrong Target')
        else:
            p=Node(value)
            p.next=temp.next
            temp.next=p
            
    def insertBeforeValue(self,value,target):
        temp=self.head
        if temp.data==target:
            p=Node(value)
            p.next=temp
            self.head=p
        else:    
            while temp.next.data!=target:
                temp=temp.next
            if temp.next.data!=target:
                print('Invalid target')
            else:
                p=Node(value)
                p.next=temp.next
                temp.next=p
                
    def deleteFromStart(self):
        if self.head==None:
            print("Nothing To Delete Here")
        else: 
            self.head=self.head.next
            
    def deleteFromEnd(self):
        temp=self.head
        if self.head==None:
            print("Nothing to DElete Here")
        elif self.head.next==None:
            self.head=None
        else:     
            temp=self.head
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None    
            
    def deleteByIndex(self,index):
        i=0
        temp=self.head
        if index==0:
            self.head=self.head.next
        else:
               
            while temp.next!=None and i!=index-1:
                temp=temp.next
                i=i+1
            if i==index-1 and temp.next!=None:
                temp.next=temp.next.next  
            else:
               print('Index Invalid') 
               
             
    def deleteAValue(self,value):
         temp=self.head
         if value==self.head.data:
             self.head=self.head.next
         else:    
             while temp.next!=None and temp.next.data!=value:
                 temp=temp.next
             if temp.next==None or temp.next.data!=value:
                 print("Invalid Input")
             else:
                 temp.next=temp.next.next    
                 
    def printInReverse(self,curNode):
        #BC
        if curNode.next==None:
            return
        #IS
        nextNode=curNode.next
        self.printInReverse(nextNode)
        print(nextNode.data)
        #FS
        return
    
    def reverseLinkedList(self,curNode):
        #BC
        if curNode==None:
            return None
        if curNode.next==None:
            return curNode
        #IS
        newhead=self.reverseLinkedList(curNode.next)
        last=curNode.next
        last.next=curNode
        curNode.next=None
        #FS
        return newhead
                     
                 
#-------------------------------------------------------------------------------------------------#
ll=LinkedList()
ll.insertAtStart(30)
ll.insertAtStart(20)
ll.insertAtStart(10)
ll.insertAtEnd(40)
ll.insertAtEnd(50)
ll.head=ll.reverseLinkedList(ll.head)
ll.printLinkedList()


    