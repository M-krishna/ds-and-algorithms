Postorder traversal
-------------------
Given a tree like:

       1
      / \
     2   3
    / \ / \
   4  5 6  7

We need to print: 4 5 2 6 7 3 1

It's easy to implement the recursive version of this. Cause I've implemented it.

I find it tricky to implement the iterative version of it. So I asked AI to teach me. It proposed two solutions.

* Using two stacks
* Using one stack and a lastVisitedNode variable

1. Using two stacks
-------------------
* Initialize two empty stacks, stack1 and stack2
* Push the root node onto stack1
* Now we iterate stack1 until stack1 is empty
    * pop the element from stack1
    * Add the popped element to stack2
    * If the popped element has left node, add it to stack1
    * If the popped element has right node, add it to stack1
* Finally, we pop elements from stack2 and print it.


2. Using one stack and a lastVisitedNode variable
-------------------------------------------------
* Initialize an empty stack stack
* Push all the left nodes into stack
* Pop the element from stack
    * Process the element if,
        * the element doesn't have a right child or
        * the right child has been visited