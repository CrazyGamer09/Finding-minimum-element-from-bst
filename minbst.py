#User function Template for python3

##Structure of the node
'''
class Node:
    data=0
    left=None
    right=None

'''

def minValue(root):
    ##Your code here
    if(root.data==None):
        return -1
    elif(root.left==None):
        return root.data
    else:
        return minValue(root.left)
        
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    data=0
    left=None
    right=None


def createNewNode(value):
    temp=Node()
    temp.data=value
    temp.left=None
    temp.right=None
    return temp
    

def newNode(root,data):
    if(root is None):
        root=createNewNode(data)
    elif(data<root.data):
        root.left=newNode(root.left,data);
    else:
        root.right=newNode(root.right,data)
        
    return root
    

def main():
    testcases=int(input())
    while(testcases>0):
        root=None
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        for i in arr:
            root=newNode(root,i)
        print(minValue(root))
        testcases-=1

if __name__=="__main__":
    main()
# } Driver Code Ends