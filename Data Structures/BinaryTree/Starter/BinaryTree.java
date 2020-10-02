/**	
 *  Title: class BinaryTree
 *  FileName: BinaryTree.java
 *  Name: Lavanya Verma	
 *  Student ID: A1587TWO569
 *  CSE1TWO Account: cse12sp2O0bcr
 *  Date: May 16 2020
 * Source: None
 *	
 * Description: BinaryTree class which extends Comparable interface. It is the 
 * implementation of a Binary Tree with different methods that add, remove, find
 * minValue, size and height of a binary tree
 * 
 */	
import java.util.List;
import java.util.LinkedList;
import java.util.Queue;
/**
 * BinaryTree class which extends Comparable interface. It is the 
 * implementation of a Binary Tree with different methods that add, remove,
 *  find minValue, size and height of a binary tree
 * @param <E>
 */
public class BinaryTree<E extends Comparable<E>> {
    // static Varialbes
    public static final int HEIGHT_CALCULATE_TWO = 2;
    // instance variable of BinaryTree
    // The root node of our binary tree
    Node root;
    // The number of nodes in our binary tree.
    int size;
    /**
     *  Node class which is an inner class of BinaryTree.
     * Used in implementation of the BinaryTree
     */
    protected class Node{
        // the left child of this node
        Node left;
        // the right child of this node
        Node right;
        // the data stored in this node
        E data;
        /**
         * Constructor that initializes data variable and other instance 
         * variables
         * @param data 
         */
        public Node(E data){
            this.data = data;
            // creating terminal node by setting left and right to null
            this.left = null;
            this.right = null;
        }
        /**
         * Method to set left instance variable to the arguement passed in 
         * @param left left node
         */
        public void setLeft(Node left){
            // seeting left variable
            this.left = left;

        }
        /**
         * Method to set left instance variable to the arguement passed in 
         * @param left
         */
        public void setRight(Node right){
            // seeting right variable
            this.right = right;

        }
        /**
         * Method to Set the data instance variable to the argument 
         * that was passed in.
         * @param data 
         */
        public void setData(E data){
            // setting data variable
            this.data = data;
            
        }
        /**
         * Method to return left child
         * @return Left child of Node
         */
        public Node getLeft(){
            //returning Left child of Node
            return this.left;
        }
        /**
         * Method to return right child
         * @return right child of node
         */
        public Node getRight(){
            // returning  right child of node
            return this.right;
        }
        /**
         * Method to return the data stored in this node
         * @return data at node
         */
        public E getData(){
            //returning data
            return this.data;
        }
    }
    /**
     * No-args constructor should create an empty binary tree
     */
    public BinaryTree(){
        //setting root to null
        this.root = null;
        // setting size to 0
        this.size = 0;
    }
    /**
     * Contructor that Initialize the instance variables so that we now
     *  have a root node containing data and a size of 1
     * @param data to be inserted in Node
     */
    public BinaryTree(E data){
        // creating root from data
        this.root = new Node(data);
        // setting size to 1
        this.size = 1;
    }
    /**
     * Constructor that adds each element in list to the binary tree
     * @param list 
     */
    public BinaryTree(List<E> list){
        // looping thriugh and adding each element
        for(int i = 0 ; i < list.size(); i++){
            this.add(list.get(i));
        }
    }
    /**
     * Method to Add a new Node containing element to the binary tree in
     *  level order and updatesize accordingly.
     * @param element element to be added
     */
    public void add(E element){
       // throw NullPointerException when element is null
       if(element == null){
        throw new NullPointerException();
        }
        else{
            // creating new Node
            Node newNode = new Node(element);
            // if size is 0
            if(size == 0){
                // adding as root
                this.root = new Node(element);
                // increasng size
                size+=1;
                // returning
                return;
            }
            else{
                // creating queue of Nodes
                Queue<Node> queue = new LinkedList<Node>();
                // adding root node to queue
                queue.add(root);
                // traversing while the queue is not empty
                while(!queue.isEmpty()){
                    // setting current node to the root node's value
                    Node currNode = queue.poll();
                    // if both the nodes are empty
                    if(currNode.getLeft()==null && currNode.getRight()==null){
                        // adding element at left node
                        currNode.setLeft(newNode);
                        // increasng size
                        size+=1;
                        return;
                    }
                    // if the rightNode is null
                    else if(currNode.getRight()==null){
                        // adding element at Right node
                        currNode.setRight(newNode);
                        // increasng size
                        size+=1;
                        return;
                    }
                    // when they are both not null
                    else{
                        // adding them both to queue
                        queue.add(currNode.getLeft());
                        queue.add(currNode.getRight());

                    }
                }
                // increasing size
                size+=1;
            }
        }
    }
    /**
     * Method to Remove the specified element in the binary tree and replace
     *  it with the node in the rightmost position in the lowest level
     * @param element to be removed
     * @return boolean whether removal was successful
     */
    public boolean remove(E element){
        // throw NullPointerException when element is null
        if(element == null){
            throw new NullPointerException();
        }
        // creating queue of Nodes for finding oyt the last node
        Queue<Node> queue = new LinkedList<Node>();
        // if binarytree is empty return false
        if(size == 0){
            return false;
        }
        // element to be removes is at root and size is 1
        if(size ==1){
            if(root.getData().compareTo(element) == 0){
                // removing root
                this.root = null;
                // setting size to 0
                this.size = 0;
                // returning true
                return true;
            } 
            else{
                // else if size is 1 and it doesn't match with element 
                // return false
                return false;
            }
        }
        // if element is present
        if(containsBFS(element)){
            // finding out the last node
            // else adding root to queue
            queue.add(root);
            // creating node to hold the last node
            Node lastNode = root;
            // while queue is not empty
            // loop to find out the lastNode
            // traversing while it is empty
            while(!queue.isEmpty()){
                // setting current node to the root node's value
                Node currNode = queue.poll();
                // if both the nodes are empty
                if(currNode.getLeft()==null && currNode.getRight()==null){
                    // breaking
                    break;
                }
                // if the rightNode is null i.e. left Node is last node
                else if(currNode.getRight()==null){
                    // updating lastNode
                    lastNode = currNode.getLeft();
                    // breaking
                    break;
                }
                // when they are both not null
                else{
                    // adding them both
                    queue.add(currNode.getLeft());
                    queue.add(currNode.getRight());
                    lastNode = currNode.getRight();
                } 
            }
            // finding out parent Node of lastNode
            // creating queue of Nodes
            Queue<Node> queueforParent = new LinkedList<Node>();
            // last node elemt's data
            E lastNodeData = lastNode.getData();
            // creating Parent Node tol hold parentt node's data
            Node parentNode = root;
            // now finding the parent node of lastNode
            queueforParent.add(root);
            // while queue is not empty
            while(!queueforParent.isEmpty()){
                // creating current Node with the top element of queue
                Node currNode = queueforParent.poll();
                // if both the child nodes are empty
                if(currNode.getLeft()==null || currNode.getRight()==null){
                    // it is a leaf so we break
                    break;
                }
                // when they are both not null
                //checking both nodes
                if(currNode.getLeft() == lastNode 
                || currNode.getRight() == lastNode ){
                    parentNode = currNode;
                    break;
                }
                // else add it to queue
                queueforParent.add(currNode.getLeft());
                queueforParent.add(currNode.getRight());
                // updating parent Node to top element
                parentNode = queueforParent.peek();

                
            }
            // now finding the node to remove
            // creating queue of Nodes
            Queue<Node> queueforRemove = new LinkedList<Node>();
            // adding root to the queue
            queueforRemove.add(root);
            while(!queueforRemove.isEmpty()){
                // creating current Node with the top element of queue
                Node currNode = queueforRemove.poll();
                // checking if currNode is the node to be removed   
                if(currNode.getData().compareTo(element) == 0){
                    // setting data to last node's data
                    currNode.setData(lastNodeData);
                    // checking which node is the last node
                    if(parentNode.getRight() == lastNode){
                        // setting it to null
                        parentNode.setRight(null);
                    }
                    else{
                        // setting it to null
                        parentNode.setLeft(null);
                    }
                    // decreasing size
                    size--;
                    // returning true
                    return true;
                }
                // else adding both the nodes to queue
                else{
                    // if left node is not nulll adding it
                    if(currNode.getLeft()!=null){
                        queueforRemove.add(currNode.getLeft());
                    }
                    // if right node is not null adding it
                    if(currNode.getRight()!=null){
                        queueforRemove.add(currNode.getRight());
                    }
                }
            }
            return false;
        }
        return false; 
    }
    /**
    * Method to Check if element is in the binary tree. Return true if 
    * element is in the binary tree and false otherwise.
    * @param element to be checked
    * @return boolean true if element is contained
    */
    public boolean containsBFS(E element){
        // throw NullPointerException when element is null
        if(element == null){
            throw new NullPointerException();
        }
        // if brinary tree empty
        if(size == 0){
            return false;
        }
        // creating queue of nodes
        Queue<Node> queue = new LinkedList<Node>();
        // adding root to queue
        queue.add(root);
        // chcecking with root element
        if((root.data).equals(element)){
            return true;
        }
        // while queue is not empty
        while(!queue.isEmpty()){
            // creating current Node with the top element of queue
            Node currNode = queue.poll();
            // if both the child nodes are empty
            if(currNode.getLeft()==null && currNode.getRight()==null){
                // returning false
                return false;
            }
            // if the rightNode is null
            else if(currNode.getRight()==null){
                // check value
                if(currNode.getLeft().getData().compareTo(element) == 0){
                    return true;
                }
            }
            // when they are both not null
            else{
                //checking left node
                if(currNode.getLeft().getData().compareTo(element) == 0){
                    return true;
                }
                // else add it to queue
                queue.add(currNode.getLeft());
                // checking right Node
                if(currNode.getRight().getData().compareTo(element) == 0){
                    return true;
                }
                // else add it to queue
                queue.add(currNode.getRight());

            }

        }
        return false;
       
    }
    /**
     * Method to Return the height of the binary tree.
     * @return heigt of the binary tree
     */
    public int getHeight(){
        // if size is 0 or 1 return 0
        if(size == 0 || size == 1){
            return 0;
        }
        else{
            return 
            (int)(Math.floor(
                Math.log(size)*(1.00)/Math.log(HEIGHT_CALCULATE_TWO)));
        }
    }
    /**
     * Methd to return the number of node in teh binary tree
     * @return int number of nodes
     */
    public int getSize(){
        //returning height
        return size;
    }
    /**
     * Method to Return the minimum value stored in the binary tree. 
     * @return E minValur in BinaryTree
     */
    public E minValue(){
        if(size == 0){
            return null;
        }
        else{
            // creating variable to hold minValue and setting to root's data
            E minValue = root.getData();
            // if size is 1 returning the root
            if(size==1){
                return minValue;
            }
            // creating queue of Nodes
            Queue<Node> queue = new LinkedList<Node>();
            // adding root node to queue
            queue.add(root);
            // while queue is not empty
            while(!queue.isEmpty()){
                // creating current Node with the top element of queue
                Node currNode = queue.poll();
                // if both the child nodes are empty
                if(currNode.getLeft()==null && currNode.getRight()==null){
                    // returning minValue
                    return minValue;
                }
                // if the rightNode is null
                else if(currNode.getRight()==null){
                    // checking left's value is lesser than min value'
                    if(currNode.getLeft().getData().compareTo(minValue) < 0 ){
                        // updating minValue and retuning it
                        minValue = currNode.getLeft().getData();
                        return minValue;
                    }
                }
                // when they are both not null
                else{
                    //checking left node
                    if(currNode.getLeft().getData().compareTo(minValue) < 0){
                        // updating MinValue
                        minValue = currNode.getLeft().getData(); 
                    }
                    // then add it to queue
                    queue.add(currNode.getLeft());
                    // checking right Node
                    if(currNode.getRight().getData().compareTo(minValue) < 0){
                        // updating minValue
                        minValue = currNode.getRight().getData(); 
                    }
                    // then add it to queue
                    queue.add(currNode.getRight());

                }

            }
            // retuning minValue
            return minValue;
        }
    }
}