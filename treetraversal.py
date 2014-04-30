from BinaryTree import  *

####main###
r = Node(10)
r1=Node(10)
binary_insert(r, Node(17))
binary_insert(r, Node(6))
binary_insert(r, Node(14))
binary_insert(r, Node(12))
binary_insert(r, Node(13))
binary_insert(r, Node(28))
binary_insert(r, Node(22))
binary_insert(r, Node(43))
binary_insert(r, Node(39))
binary_insert(r, Node(7))
binary_insert(r, Node(9))
binary_insert(r, Node(8))
binary_insert(r, Node(4))
binary_insert(r, Node(5))
binary_insert(r, Node(3))
binary_insert(r, Node(2))
binary_insert(r, Node(1))



binary_insert(r1, Node(7))
binary_insert(r1, Node(9))
binary_insert(r1, Node(15))
binary_insert(r1, Node(11))
#binary_insert(r1, Node(16))
#binary_insert(r1, Node(25))


#####tree height#####
def height(root):
   if not root:
      return 0
   else:
      return (1+max(height(root.l_child),height(root.r_child)))
##pre order###

def preOrder(root):
   if not root:
	return
   print root.data
   preOrder(root.l_child)
   preOrder(root.r_child)
print "PREORDER"
preOrder(r)

###post order###


def postOrder(root):
   if not root:
      return
   postOrder(root.l_child)
   postOrder(root.r_child)
   print root.data
print "POSTORDER"
postOrder(r)


#######in order#######
def inOrder(root):
   if not root:
      return
   inOrder(root.l_child)
   print root.data
   inOrder(root.r_child)
print "INORDER"
inOrder(r)


####SIZE of TREE#######
def treeSize(root):
   if not root:
      return 0
   else:
      return (treeSize(root.l_child)+1+treeSize(root.r_child))


print "Tree Size is "+ str(treeSize(r))



###check for identical trees###
def checkIdentical(b1,b2):
   if b1 is None and b2 is None:
      return 0
   elif b1 is not None  and b2 is not None:
      return (b1.data==b2.data and checkIdentical(b1.l_child,b2.l_child) and checkIdentical(b1.r_child ,b2.r_child))


print checkIdentical(r,r1)



##Find depth#####

def findDepth(root):
   if not root:
	return 0
   else:
	ldep=findDepth(root.l_child)
	rdep=findDepth(root.r_child)  
        if ldep>rdep:
           return ldep+1
        else:
           return rdep+1


print "Depth of tree "+str(findDepth(r1))


#### Create Identical tree###

def mirrorTree(root):
   if not root:
      return 
   else:
      mirrorTree(root.l_child)
      mirrorTree(root.r_child)
      #temp=Node(root)
      temp=root.l_child
      root.l_child=root.r_child
      root.r_child=temp	
      
	
mirrorTree(r)
print "MirrorTree"
inOrder(r)


###print all paths in  the tree ########


def printPaths(root):
   paths=[]
   getAllpaths(root,paths,0)


def getAllpaths(root,paths,pathlen):
   if not root:
      return
   #print paths,pathlen,root.data	
   paths.append(root.data)
   pathlen+=1
	
   if (root.l_child is None and root.r_child is None):
      pathprinter(paths,pathlen)
      paths=[] 	
   else:
      #print "pathlen"
      getAllpaths(root.l_child,paths,pathlen)
      getAllpaths(root.r_child,paths,pathlen)


def pathprinter(pathy,len):
   print "All paths"
   for i in range(0,len):
      print pathy[i]
   print '\n'


printPaths(r)   


##########Level Order Traversal############


def levelOrder(root):
   h=height(root)
   print "Level order"
   spiral=False
   for i in range(0,h):
      printLevelOrder(root,i)
   print "Level Order Spiral"
   for j in range(0,h):
      printLevelOrder(root,j,spiral)
      spiral=not spiral
def printLevelOrder(root,level,*spiral):
   if spiral:
	set=True
   else:
	set=False
   if not root:
      return 
   if level==1:
      print root.data
   else:
      if set:
	      printLevelOrder(root.l_child,level-1)
              printLevelOrder(root.r_child,level-1)
      else:
         if spiral:
	      printLevelOrder(root.l_child,level-1,spiral)
              printLevelOrder(root.r_child,level-1,spiral)
	 else:
	      printLevelOrder(root.r_child,level-1,spiral)
              printLevelOrder(root.l_child,level-1,spiral)

	
		
levelOrder(r)

####get All leaves#######

def getLeavesCount(root):
   if not root:
      return 0
   if root.l_child is None and root.r_child is None:
      return 1
   else:
      return(getLeavesCount(root.l_child)+getLeavesCount(root.r_child))


print "Leaves count "+str(getLeavesCount(r))


#####check for children sum property#####

def isChildSum(root):
   ldata=0
   rdata=0
   if (not root or (root.l_child is None and root.r_child is None)):
      return 1
   else:
      if root.l_child is not None:
         isChildSum(root.l_child)
      else:
         ldata=root.data
      if root.r_child is not None:
 	        isChildSum(root.r_child)
      else:
	         rdata=root.data	
      if(root.data==(rdata+ldata) and isChildSum(root.l_child) and isChildSum(root.r_child)):
         return 1
      else:
         return 0

if(isChildSum(r)):
   print "Satisfies child not property"
else:
   print "Does not satisfies child sum property" 		   	



#####Diameter of a tree#######

def treeDiameter(root):
   if not root:
      return 0
   lheight=height(root.l_child)
   rheight=height(root.r_child)
   ldiam=treeDiameter(root.l_child)
   rdiam=treeDiameter(root.r_child)
   return max(lheight+rheight+1,max(ldiam,rdiam))

diam=treeDiameter(r1)
print "Diameter of the tree is-"+str(diam)

#####height balance check####
def heightBalance(root):
   if not root:
      return 0
   else:
      lheight=height(root.l_child)
      rheight=height(root.r_child)
   if (abs(lheight-rheight)<=1 and  heightBalance(root.l_child) and heightBalance(root.r_child)):
	return 1
   else:
        return 0

#print height(r1)
if(heightBalance(r1)):
   print "The tree is balanced"
else:
   print "The tree is not balanced"


####in order using stack and loop ######


def loop_inOrder(root):
   print "InOrder with stack n loop"
   stack=[]
   done=0
   check=0	
   current=root
   while not done:
      if current is not None:
         stack.append(current)
         current=current.l_child
      else:
         if  stack:
            current=stack.pop()
            print current.data
            current=current.r_child
         else: 
            done=1
    
loop_inOrder(r1)

############Find if leaf path equal to sum#######

def hasPathsum(root,sum):
   if not root:
      return 0 
   else:
      is_der=0
      subSum=0
      subSum=sum-root.data
      if subSum==0 and root.l_child is None and root.r_child is None:
         return 1
      if root.l_child:
         is_der=is_der or hasPathsum(root.l_child,subSum)
      if root.r_child:
         is_der=is_der or hasPathsum(root.r_child,subSum)
      return is_der
         
if hasPathsum(r,26):
   print "Sum exists in path"
else:
   print "Sum not exists in path"


####build tree with given in order and pre order traversal####

###In a Preorder sequence, leftmost element is the root of the tree. So we know is root for given sequences. By searching  in Inorder sequence, we can find out all elements on left side of are in left subtree and elements on right are in right subtree. So we know below structure now####

""""
def buildTree(inorder,preorder,first_index,last_index):
    preIndex=0
    if first_index>last_index:
        return
    element=Node(preorder[preIndex])
    preIndex+=1
    if first_index==last_index:
        return element
    inIndex=inorder.index(element.data)
    root.l_child=buildTree(inorder,preorder,first_index,inIndex-1)
    root.r_child=buildTree(inorder,preorder,inIndex+1,last_index)
    return root  """


inorder=[7,10,9,12,13,14]
preorder=[12,10,7,9,14,13]
#tree_built=buildTree(inorder,preorder,0,len(preorder)-1)
#inOrder(tree_built)   
     
##########Double tree#########

def doubleTree(root):
   oldLeft=Node(root)
   if not root:
	return 
   doubleTree(root.l_child)
   doubleTree(root.r_child)
   oldLeft=root.l_child
   root.l_child=binary_insert(oldLeft.data,root.data)
   root.l_child=oldLeft


#doubleTree(r1)
#inOrder(r1)


####get max width of the tree####
def getMaxwidth(root):

   maxwidth=0
   h=height(root)
   for i in range(0,h):
      width=getWidth(root,i)
      if width>maxwidth:
         maxwidth=width
   return maxwidth

def getWidth(root,level):
   if not root:
      return 0
   if level ==1:
      return 1
   elif level>1:
      return getWidth(root.l_child,level-1)+getWidth(root.r_child,level-1)
print "The max width is - "+str(getMaxwidth(r))

###Check for foldable tree#######
def chekFoldable(root):
   res=0
   if not root:
      return 1
   mirrorTree(root.l_child)
   res=getStructTree(root.l_child,root.r_child)
   mirrorTree(root.l_child)
   return res

def getStructTree(a,b):
   if not a and not b:
      return 1
   elif (a is not None and  b is not None and getStructTree(a.l_child,b.l_child) and getStructTree(a.r_child,b.r_child)):
      return 1
   else:
      return 0


if chekFoldable(r1):
   print "Yes foldable"
else:
   print "Not foldable"


###########find nodes at K distance###################

def findKDistantnodes(root,n):
   
   if not root:
       return 
   if n==0:
       print root.data
       return
   else:
       findKDistantnodes(root.l_child,n-1)
       findKDistantnodes(root.r_child,n-1)
       
print "K distant nodes are"   
findKDistantnodes(r,2)   

####find level of the node##############

def findLevel(root,key,level):
    if not root:
        return
    if root.data==key:
        return level
    downlevel=findLevel(root.l_child,key,level+1)
    if downlevel !=0:
       return downlevel
    downlevel=findLevel(root.r_child,key,level+1)
    return downlevel    
def getLevel(root,dat):
    return findLevel(root,dat,1)
print getLevel(r,22)
