#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
class Tree():
    def __init__(self,maxx,time,succ=None,pred=None,level=1,val=1,weight=None,leaf=False,total_levels=3,k=1,total_nodes=1):
        self.succ=succ
        self.pred=pred
        self.level=level
        self.val=val
        self.weight=weight
        self.leaf=leaf
        self.k=k
        self.total_nodes=total_nodes
        self.time=int(np.random.randint(1) *maxx + 1)
        self.total_levels=total_levels     

     
      
 
    def generate(self,root, nb_pred_max, nb_lev, max_time, index):  
        print("val of the root is   "+str(self.k))                 
        print("adress of the root is   "+str(root))
        root.total_levels=nb_lev
        n=0
        if root.level<nb_lev:  
            if root.level==1:
                n=int (np.random.randint(1)  * nb_pred_max + 1)
                n=3
            else:
                n=int(np.random.randint(1) * nb_pred_max + 1) 
                if n==0:
                    root.leaf=True
              
         
        
            self.total_nodes=self.total_nodes+n#;//the number of nodes in the tree
            
            root.pred=[Tree(0,0) for x in range(n)]
     
            for i in range (len(root.pred)):#(int i=0;i<;i++)
                print("The number of nodes is now "+str(self.total_nodes))
                self.k+=1 
                root.pred[i]=Tree(max_time,i)
                root.pred[i].level=root.level+1
                root.pred[i].succ=root
                root.pred[i].val=self.k
                print("The node number   "+str(i)+"  at level   "+str(root.pred[i].level)+"  its value=    "+str(root.pred[i].val)+"  its successor adress is   "+str(root.pred[i].succ))
                print("*********************************************")
                self.generate(root.pred[i],nb_pred_max,nb_lev,max_time,i)
      
        
        else:
            root.leaf=True
            print("The attribute of root leaf is "+str(root.leaf))
            print(root)
     
 
    def gettotal_nodes(self):
              return self.total_nodes
    
    def settotal_nodes( a):
              self.total_nodes = a
    
 
 


# In[2]:


def main():
    N=Tree(5,0);
    N.generate(N,4,5,10,0)#;//nom racine**nb_predecesseurs max ** nb_niveau**temps de duree d'execution maximale
        
    print("++++++++++++++++++")
    print("the total number of nodes in the tree is "+str(N.gettotal_nodes()))
        
    


# In[3]:


main()


# In[ ]:





# In[ ]:




