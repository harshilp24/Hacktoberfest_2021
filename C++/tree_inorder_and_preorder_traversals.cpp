#include<iostream>
using namespace std;

/* Defines the structure of the node */
struct node
{
    int data;
    node *left, *right;
};

/* A function to create a node with the key passed to it */
struct node *newNode(int data)
{
    struct node *temp =  (struct node *)malloc(sizeof(struct node)); 
    temp->data = data; 
    temp->left = temp->right = NULL; 
    return temp; 
}

/* Prints the inorder traversal of the BST */
void printInorder(struct node *root)
{
    if(root != NULL)
    {
        printInorder(root->left);
        cout << root->data << " ";
        printInorder(root->right);
    }
}

/* Returns the index of the element of the postorder in the inorder traversal */
int getInorderIndex(int in[], int l, int h, int data)
{
    for(int j=l; j<h; j++)
        //checks until the element is found in the inorder traversal
        if(data==in[j])
            return j;
}

/* A recursive function to construct the binary tree from the inorder traversal
and preorder traversal */
struct node *construct(int in[], int pre[], int l, int h)
{
    //a static variable, so that the preIndex doesn't change throughout the 
    //program
    static int preIndex=0;

    //creates a node with elements of preorder traversal pre[]
    //and index of preorder is incremented 
    struct node *temp=newNode(pre[preIndex++]);

    //if the start and the end is equal, that means this node has no children
    if(l==h)
        return temp;

    //gets the index from the inorder traversal in[]
    int inoderIndex=getInorderIndex(in, l, h, temp->data);
    //elements to the left of the index are pushed into left sub-tree
    temp->left=construct(in, pre, l, inoderIndex-1);
    //elements to the right of the index are pushed into right sub-tree
    temp->right=construct(in, pre, inoderIndex+1, h);    

    return temp;
}


int main()
{
    int inorder[]={35,30,18,21,15,20,16,17,39,12,45};
    int preorder[]={20,21,30,35,18,15,12,17,16,39,45};
    int size=sizeof(preorder)/sizeof(preorder[0]);

    struct node *root=construct(inorder, preorder,0,size-1);

    cout << "Inorder traversal is:" << endl;
    printInorder(root);
    
    return 0;
}