#include<iostream>
#include<algorithm>     // for library function sort()
using namespace std;

/* Defining the structue of a node */
struct node
{
    int data;
    struct node *left, *right;
};


/* A function to create a node with the key passed to it */
struct node *newNode(int data)
{
    struct node *temp =  (struct node *)malloc(sizeof(struct node)); 
    temp->data = data; 
    temp->left = temp->right = NULL; 
    return temp; 
}

/* Prints inorder traversal*/
void printInorder(struct node *root)
{
    if(root != NULL)
    {
        printInorder(root->left);
        cout << root->data << " ";
        printInorder(root->right);
    }
}

/* Creates the inorder traversal array */
void createInorderArray(struct node *root, int inorder[], int *i)
{
    if(root != NULL)
    {
        createInorderArray(root->left, inorder, i);
        inorder[*i]=root->data;
        (*i)++;
        createInorderArray(root->right, inorder, i);
    }
}

/* Counts the number of nodes in the tree, to get the size of array
for creating it dynamically to store inorder traversal*/
int countNodes(struct node* root)
{
    if(root==NULL)
        return 0;
        // recursively returns sum of left and right sub-tree
    return countNodes(root->left)+countNodes(root->right)+1;
}

/* Change the values of the inorder traversal of tree with the given inorder traversal */
void changeNodes(struct node *root, int inorder[], int *i)
{
    if(root!=NULL)
    {
        changeNodes(root->left, inorder, i);
        root->data=inorder[*i];
        (*i)++;
        changeNodes(root->right, inorder, i);
    }
}

/* Converts binary tree to BST */
void bTree_to_BST(struct node* root)
{
    if(root==NULL)
        return;

    // creates a dynamic array to store inorder traversal of the tree
    int n=countNodes(root);
    int *in = new int[n];
    int i=0;
    createInorderArray(root, in, &i);

    // Sort the array using library function
    sort(in, in+n);

    // change each element of inorder traversal
    // of the tree with sorted inorder array
    i=0;
    changeNodes(root, in, &i);

    // delete dynamically created array.
    delete [] in;

}

int main()
{
    struct node* root=newNode(0);
    root->left=newNode(1);
    root->right=newNode(2);
    root->left->left=newNode(3);
    root->left->right=newNode(4);
    root->right->left=newNode(5);
    root->left->left->right=newNode(6);
    root->right->left->right=newNode(7);
    root->left->left->right->right=newNode(8);
    /*      The following tree is constructed
                          0
                        /  \
                       1    2
                      / \  /
                      3 4  5
                       \    \
                        6    7
                         \
                          8

    */

    cout << "Inorder traversal of the constructed binary tree:" << endl;
    printInorder(root);
    cout << endl;

    cout << "Inorder traversal of the converted binary search tree:" << endl;
    bTree_to_BST(root);
    printInorder(root);
    
    return 0;
}