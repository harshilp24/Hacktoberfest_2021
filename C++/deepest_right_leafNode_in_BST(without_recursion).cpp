#include<iostream>
#include<queue>
using namespace std;

/* This class encapsulates the methods used for the BST */
template<class T>
class Tree
{
    /* Defines the structure of the node */
    struct node
    {
        T data;
        node *left, *right;
    };
    node *root;
    /* Creates new node and assign value to it */
    node* newNode(int val)
    {
        node* temp=new node;
        temp->data=val;
        temp->left=temp->right=nullptr;

        return temp;
    }
    /* Utility function to get the deepest left node in a binary tree */
    node* getDeepestNode(node* root)
    {
        if(root==nullptr)
            return nullptr;
        
        queue<node*> q;
        q.push(root);

        node* result = nullptr; 
  
        // traverse until the queue is empty 
        while (!q.empty()) 
        { 
            node* temp = q.front(); 
            q.pop(); 
    
            if (temp->left) 
            { 
                q.push(temp->left); 
                 
            } 
            // In level by level traversal, the last  
            // right leaf node will be the deepest one, 
            if (temp->right) 
            {
                temp=temp->right;
                q.push(temp); 
                // if left tree is pushed, it is checked if it is a leaf
                if (temp->left==nullptr && temp->right==nullptr) 
                    result = temp;
            }
        } 
        return result; 
    }
    public:
        void construct();
        void getDeepestNode();
};

/* function to construct the BST */
template<class T>
void Tree<T>::construct()
{
    // construct a tree 
    root = newNode(1); 
    root->left = newNode(2); 
    root->right = newNode(3); 
    root->left->left = newNode(4); 
    root->left->right = newNode(5); 
    root->right->left = newNode(6); 
    root->right->right = newNode(7); 
    root->left->left->left = newNode(8); 
    root->left->left->right = newNode(9); 
}

template<class T>
void Tree<T>::getDeepestNode()
{
    node* result=getDeepestNode(root);

    if (result) 
        cout << "Deepest right leaf node in the binary tree is " << result->data << endl; 
    else
        cout << "Right leaf not found" << endl; 
}

int main()
{
    Tree<int> tree;
    tree.construct();
    /* The following tree is constructed:
               1
             /  \ 
            2     3
           / \   / \ 
          4  5  6   7
         / \
        8   9
    */
    tree.getDeepestNode();

    return 0;
}