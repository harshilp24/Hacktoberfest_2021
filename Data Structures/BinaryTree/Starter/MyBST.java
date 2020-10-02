import java.util.Stack;
public class MyBST<K extends Comparable<K>, V> {
    /**
     * This class is a static nested class of the MyBST class. Objects of 
     * this class represent nodes of the tree and contain a key for sorting, 
     * a value, and pointers to the children and parent of this object.
     * 
     * @param <K>
     * @param <V>
     */
    static class MyBSTNode<K, V> {
        // This represents the key that we are using to sort our nodes.
        K key; 
        // This represents the data stored by this MyBSTNode.
        V value; 
        // his stores a reference to the parent node of this MyBSTNode.
        MyBSTNode<K, V> parent; 
        // This stores a reference to the left child of this MyBSTNode.      
        MyBSTNode<K, V> left; 
        // This stores a reference to the right child of this MyBSTNode
        MyBSTNode<K, V> right; 
        public MyBSTNode(K key, V value, MyBSTNode<K, V> parent){
            // setting this.parent to parent
            this.parent = parent;
            // setting this.ley to key
            this.key = key;
            // setting this.value to value
            this.value = value;
            // setting left and right to null
            left = null;
            right = null;
            
        }
        /**
         * Method whoch returns the key of the node
         * @return K key
         */
        public K getKey(){
            K valueReturn = this.key;
            return valueReturn;
        }
        /**
         * Method which returns the value of this node.
         * @return V value
         */
        public V getValue(){
            V valueReturn = this.value;
            return valueReturn;
        }
        /**
         *  Method which Returns the parent of this node 
         * @return myBSTNode 
         */
        public MyBSTNode<K, V> getParent(){
            return this.parent;
        }
        /**
         *  Method which Returns the left child of this node 
         * @return myBSTNode 
         */
        public MyBSTNode<K, V> getLeft(){
            return this.left;
        }
        /**
         *  Method which Returns the right child of this node 
         * @return myBSTNode 
         */
        public MyBSTNode<K, V> geRight(){
            return this.right;
        }
        /**
         * Method which Change the key of this node to be the argument key.
         * @param newKey
         */
        public void setKey(K newKey){
            // change key to newKey
            this.key = newKey;
        }
        /**
         * Method which Change the value of this node to be the argument value.
         * @param newValue
         */
        public void setValue(K newValue){
            // change key to newValue
            this.Value = newValue;
        }
        /**
         * Method which changes the parent of this node to be the arguement node
         * @param newParent
         */
        public void setParent(MyBSTNode<K, V> newParent){
            this.parent = newParent;
        }
        /**
         * Method which changes the left child of this node to be the arguement 
         * node
         * @param newLeft
         */
        public void setLeft(MyBSTNode<K, V> newLeft){
            this.left = newLeft;
        }
        /**
         * Method which changes the right child of this node to be thearguement 
         * node
         * @param newRight
         */
        public void setRight(MyBSTNode<K, V> newRight){
            this.right = newRight;
        }
        /**
         * Method which returns the node with the smallest key greater than the
         *  key of this node.
         * @return MyBSTNode 
         */
        public MyBSTNode<K, V> successor(){
            // if right node od this key is not null
            if(this.getRight()!= null){
                // creating current Node  to hold the node's right
                MyBSTNode<K, V> currNode = this.getRight();
                // looping while the left node is not null
                while(currNode.getLeft()!= null){
                    currNode = currNode.getLeft();
                }
                // If there is no larger key, return null.
                if(currNode == null){
                    return null;
                }
                return currNode;
            }
            //  if right subtree of node is null
            else{
                // go up to find a node which is the left child of it's parent
                MyBST<K, V> parentNode= this.getParent();
                // creating current Node  to hold the node's right
                MyBSTNode<K, V> currNode = this;
                while(parentNode!= null && currNode == parent.getRight()){
                    currNode = parentNode;
                    parentNode = parentNode.getParent();
                }
                // If there is no larger key, return null.
                if(parentNode == null){
                    return null;
                }
                return parentNode;
            }
        }
    }
    /**
     * This class is the public class of this file. It represents a binary
     *  search tree where sorting is done based on the keys. 
     * It is not a self-balancing tree.
     * @param <K> key
     * @param <V> Value
     */
    public class MyBST<K extends Comparable<K>, V> {
        // This is a reference to the root node of our tree.
        MyBSTNode<K, V> root; 
        // This represents the number of nodes in our tree. 
        int size;
        /**
         *  Constructor which creates an empty BST.
         */
        public MyBST(){
            // initilaizes root to null 
            root = null;
            // size to 0
            size = 0;
        }
        /**
         * Method which returns the successor
         * @param node
         * @return
         */
        protected MyBSTNode<K, V> successor(MyBSTNode<K, V> node){
            // if node is null return null
            if(node == null){
                return null;
            }
            // if right node od this key is not null
            if(node.getRight()!= null){
                // creating current Node  to hold the node's right
                MyBSTNode<K, V> currNode = node.getRight();
                // looping while the left node is not null
                while(currNode.getLeft()!= null){
                    currNode = currNode.getLeft();
                }
                // If there is no larger key, return null.
                if(currNode == null){
                    return null;
                }
                return currNode;
            }
            //  if right subtree of node is null
            else{
                // go up to find a node which is the left child of it's parent
                MyBST<K, V> parentNode= node.getParent();
                // creating current Node  to hold the node's right
                MyBSTNode<K, V> currNode = this;
                while(parentNode!= null && currNode == parent.getRight()){
                    currNode = parentNode;
                    parentNode = parentNode.getParent();
                }
                // If there is no larger key, return null.
                if(parentNode == null){
                    return null;
                }
                return parentNode;
            }
        }
        /**
         * Method which return the size
         * @return
         */
        public int size(){
            return this.size;
        }
        /**
         * Method which insert a new node containing the arguements key and v
         * value into the binary search tree
         * @param key
         * @param value
         * @return
         */
        public V insert(K key, V value){
            // if key is null throw exception
            if(key == null){
                throw new NullPointerException();
            }
            // creating valueReturn to hold value of returned key and setting 
            // it to nukk
            V valueReturn = null;
            if(root.getKey.compareTo(key)==0){
                // setting it's value to value
                root.setValue(value);
            }
            else{
                // creating variable to hold comparison's result
                int comparisonResult = key.compareTo(root.getValue());
                // creating new Node  
                MyBSTNode<K, V> newNode=  new MyBSTNode(key, value, currNode);
                // if size is 0 i.e. bst is empty
                if(size == 0){
                    root = newNode;
                }
                // creating current Node and storing root
                MyBSTNode<K, V> currNode = root;
                while(currNode!=null){
                    // if key is less than the root we traverse to the left
                    // subtree
                    if(comparisonResult < 0){
                        if(currNode.getLeft()== null){
                            // setting new node
                            currNode.setLeft(newNode);
                            return valueReturn;
                        }
                        currNode = currNode.getLeft();
                        comparisonResult = key.compareTo(currNode);
                    }
                    // if they are equal to each other
                    else if(comparisonResult == 0){
                        // setting valueReturn value
                        valueReturn = currNode.getValue();
                        // setting the value of currNode
                        currNode.setValue(value); 
                        // rreturning the replaced value
                        return valueReturn;
                    }
                    else{
                        if(currNode.getRight()== null){
                            // setting new node
                            currNode.setRight(newNode);
                            return valueReturn;
                        }
                        // traversing the right subtree otherwise
                        currNode = currNode.getRight();
                        comparisonResult = key.compareTo(currNode);
                    }
                }

            }
        }
        /**
         * Mehod which Search for a node with key equal to key and 
         * return the value associated with that node
         * @param key
         * @return value associated with that node
         */
        public V search(K key){
             // if key is null return null
             if(key == null){
                throw null;
            }
            // creating valueReturn to hold value of returned key and setting 
            // it to nukk
            V valueReturn = null;
            if(root.getKey.compareTo(key)==0){
                // returning the root's value
                return root.getValue();
            }
            else{
                // creating variable to hold comparison's result
                int comparisonResult = key.compareTo(root.getValue());
                // creating current Node and storing root
                MyBSTNode<K, V> currNode = root;
                while(currNode!=null){
                    // if key is less than the root we traverse to the left
                    // subtree
                    if(comparisonResult < 0){
                        currNode = currNode.getLeft();
                        comparisonResult = key.compareTo(currNode);
                    }
                    // if they are equal to each other
                    else if(comparisonResult == 0){
                        // setting valueReturn value
                        valueReturn = currNode.getValue();
                        return valueReturn;
                    }
                    else{
                        // traversing the right subtree otherwise
                        currNode = currNode.getRight();
                        comparisonResult = key.compareTo(currNode);
                    }
                }
                // returning default value if element was not found
                return valueReturn;

            }
        }
        /**
         * Method which Search for a node with key equal to key and return 
         * the value associated with that node
         * @param key
         * @return vale associated with that node
         */
        public V remove(K key){
            if(key == null){
                return null;
            }
            V returnedValue = serach(key);
            if(returnedValue == null){
                // element doesnt exist
                return null;
            }
            else{
                // if root is to be removed
                if(root.getKey.compareTo(key)==0){
                    root = null;
                    // decrementing size
                    size--;
                    return returnedValue;
                }
                else{
                    // creating variable to hold comparison's result
                    int comparisonResult = key.compareTo(root.getValue());
                    // creating current Node and storing root
                    MyBSTNode<K, V> currNode = root;
                    while(currNode!=null){
                        // if key is less than the root we traverse to the left
                        // subtree
                        if(comparisonResult < 0){
                            currNode = currNode.getLeft();
                            comparisonResult = key.compareTo(currNode);
                        }
                        // if they are equal to each other
                        else if(comparisonResult == 0){
                            break;
                        }
                        else{
                            // traversing the right subtree otherwise
                            currNode = currNode.getRight();
                            comparisonResult = key.compareTo(currNode);
                        }
                    }
                    MyBSTNode<K, V> leftChild = currNode.getLeft();
                    MyBSTNode<K, V> rightChild = currNode.getRight();
                    // if currNode has a single child
                    // if leftchild is null
                    if((leftChild == null && rightChild != null)){
                        // setting left of parent
                        currNode.getParent().setRight(rightChild);
                        // moving child's place up
                        currNode = rightChild;
                        // decrementing size
                        size--;
                    }
                    // if rightchild is null
                    else if( leftChild !=null && rightChild==null){
                        // setting left of parent
                        currNode.getParent().setLeft(leftChild);
                        // moving child's place up
                        currNode = leftChild;
                        // decrementing size
                        size--;
                    }// if node to be removed is a leaf
                    else if(leftchild == null & rightChild == null){
                        int comparedParent = currNode.getKey().compareTo(currNode.getParent().getKey());
                        // if courrnode's key is less than the parent's
                        if(comparedParent < 0){
                            // this means currNode is left child
                            // setting left of parent
                            currNode.getParent().setLeft(null);
                            // removing currNode
                            currNode = null;
                            // decrementing size
                            size--;
                        }else{
                            // it's the right  hild
                            // setting left of parent
                            currNode.getParent().setLeft(null);
                            // removing currNode
                            currNode = null;
                            // decrementing size
                            size--;
                        }
                    }
                    else{
                        // node has two children
                        // creating succesor node
                        MyBSTNode<K, V> succesorNode = succesor(currNode);
                        // replacing the data in currNode with it's succesor's 
                        // data
                        currNode.setValue(succesorNode.getValue());
                        // setting key
                        currNode.setKey(succesorNode.getKey());
                        // now removing succesor Node
                        remove(succesorNode);
                    }
                    
                    // returnging the returned Value
                    return returnedValue;
                }
            }
        }
    }
    /**
     * Method which does an in-order traversal of the tree, adding each node 
     * to the end of an ArrayList
     * @return arrayList
     */
    public ArrayList<MyBSTNode<K, V>> inorder(){
        ArrayList<MyBSTNode<K, V>> arrList = new ArrayList<>();
        // if tree is mepty return empty arrayList;
        if(size == 0){
            return arrList;
        }
        else{
            // creating currNode and storing root
            MyBSTNode<K,V> currNode = root;
            // creating a stack to help traverse
            Stack<MyBSTNode> stack = new Stack<>();
            //adding the current node to the stack
            stack.push(currNode);
            while( currNode != null || stack.size()!=0){
                
                while( currNode!=null){
                    //adding the current node to the stack
                    stack.push(currNode);
                    currNode = currNode.getLeft();
                }
                
                if(currNode == null && stack.size()!=0){
                    // popping the top element from stack
                    MyBSTNode<K, V> poppedElement = stack.pop();
                    arrList.add(poppedElement);
                    currNode = poppedElement.getRight();
                }
            }
            return arrList;
        }

    }
}
