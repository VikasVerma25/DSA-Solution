# You're given three inputs, all of which are instances of an OrgChart class that 
# have a directReports property pointing to their direct reports. The first input is 
# the top manager in an organizational chart (i.e., the only instance that isn't 
# anybody else's direct report), and the other two inputs are reports in the 
# organizational chart. The two reports are guaranteed to be distinct. -
# Write a function that returns the lowest common manager to the two reports.
'''
                   A
                 /   \
               B       C
            /    \   /   \
           D      E F     G
         /  \
       H      I     
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

A = Node("A")
B = Node("B")
A.left = B
C = Node("C")
A.right = C
D = Node("D")
B.left =  D
E = Node("E")
B.right =  E
F = Node("F")
C.left = F
G = Node("G")
C.right = G
H = Node("H")
D.left = H
I = Node("I")
D.right = I

def lcm(root, n1, n2):
    if not root:
        return False
    # if found data return current node data
    elif root.data in [n1.data, n2.data]:
        return root.data
    l1 = lcm(root.left, n1, n2)
    l2 = lcm(root.right, n1, n2)
    # both left and right side return data, current node is lcm, return it
    if l1 and l2:
        return root.data
    # or return one which is not false, else return false (when both l1 and l2 are false)
    else:
        if l1: return l1
        else: return l2

print(lcm(A, E, I))

