#include<limits.h>
#include<stdio.h>
#include<stdlib.h>
#include <stdbool.h>

struct BST
{
  long long int key;
  int height;
  long long int max, high;
  struct BST *left, *right;
};


struct BST *
newNode (long long int l, long long int r)
{
  struct BST *temp = (struct BST *) malloc (sizeof (struct BST));
  temp->key = l;
  temp->max = temp->high = r;
  temp->left = temp->right = NULL;
  temp->height = 0;
  return temp;
}


int
Max (int x, int y)
{
  if (x < y)
    return y;
  else
    return x;
}

int
Min (int x, int y)
{
  if (x < y)
    return x;
  else
    return y;
}

int
Height (struct BST *node)
{
  if (node)
    {
      if (node->left && node->right)
	return 1 + Max (node->left->height, node->right->height);

      else if (node->left)
	return 1 + node->left->height;
      else if (node->right)
	return 1 + node->right->height;
      else
	return 0;

    }

  else
    return -1;
}

void
Updatemax (struct BST *node)
{
  if (node)
    {
      node->max = node->high;
      if (node->left && node->left->max > node->high)
	node->max = node->left->max;
      if (node->right && node->right->max > node->max)
	node->max = node->right->max;
    }
}


bool
AVL (struct BST *node)
{
  if (abs (Height (node->left) - Height (node->right)) < 2)
    return true;
  else
    return false;
}

void
Inorder (struct BST *node)
{
  if (node)
    {
      Inorder (node->left);
      printf ("%lld: %lld %lld   ", node->key, node->high, node->max);
      Inorder (node->right);
    }
}

struct BST *
Search (struct BST *node, long long int X)
{

  while (node)
    {
      if (X == node->key)
	return node;
      else if (X < node->key)
	node = node->left;
      else
	node = node->right;
    }
  return NULL;
}


struct BST *
Overlap (struct BST *node, long long int l, long long int r)
{

  while (node)
    {
      if (l <= node->high && node->key <= r)
	return node;
      if (node->left && node->left->max >= l)
	node = node->left;
      else
	node = node->right;
    }
  return NULL;
}

struct BST *
Rotate (struct BST *Z)
{
  struct BST *X, *Y, *T1, *T2, *T3, *T4;
  int c = 0;
  if (Height (Z->left) + 1 == Z->height)
    Y = Z->left;
  else
    {
      Y = Z->right;
      c++;
    }
  c = c * 2;
  if (Height (Y->left) + 1 == Y->height)
    X = Y->left;
  else
    {
      X = Y->right;
      c++;
    }

  if (c == 0)
    {
      T3 = Y->right;
      Y->right = Z;
      Z->left = T3;
      Z->height = Height (Z);
      X->height = Height (X);
      Y->height = Height (Y);
      Updatemax (Z);
      Updatemax (X);
      Updatemax (Y);
      return Y;

    }
  else if (c == 3)
    {

      T2 = Y->left;
      Y->left = Z;
      Z->right = T2;

      Z->height = Height (Z);
      X->height = Height (X);
      Y->height = Height (Y);
      Updatemax (Z);
      Updatemax (X);
      Updatemax (Y);
      return Y;
    }
  else if (c == 1)
    {

      T2 = X->left;
      T3 = X->right;
      Y->right = T2;
      Z->left = T3;
      X->left = Y;
      X->right = Z;

      Z->height = Height (Z);
      Y->height = Height (Y);
      X->height = Height (X);
      Updatemax (Z);
      Updatemax (Y);
      Updatemax (X);
      return X;

    }
  else
    {
      T2 = X->left;
      T3 = X->right;
      Y->left = T3;
      Z->right = T2;
      X->left = Z;
      X->right = Y;

      Z->height = Height (Z);
      Y->height = Height (Y);
      X->height = Height (X);
      Updatemax (Z);
      Updatemax (Y);
      Updatemax (X);
      return X;
    }


}

struct BST *
Insert (struct BST *node, long long int key, long long int r)
{
  // If the BST is empty, create a  new BST
  if (!node)
    return newNode (key, r);
  if (key < node->key)
    node->left = Insert (node->left, key, r);
  else if (key > node->key)
    node->right = Insert (node->right, key, r);
  node->height = Height (node);
  Updatemax (node);
  if (!AVL (node))
    {
      node = Rotate (node);
    }
  return node;
}


struct BST *
Delete (struct BST *node, long long int X)
{
  if (!node)
    return node;

  if (node->key > X)
    {
      node->left = Delete (node->left, X);
      node->height = Height (node);
      Updatemax (node);
      if (!AVL (node))
	node = Rotate (node);

      return node;
    }
  else if (node->key < X)
    {
      node->right = Delete (node->right, X);
      node->height = Height (node);
      Updatemax (node);
      if (!AVL (node))
	node = Rotate (node);
      return node;
    }


  if (node->left && node->right)
    {
      struct BST *temp = node->left;
      while (temp->right)
	temp = temp->right;
      node->key = temp->key;
      node->high = temp->high;
      node->left = Delete (node->left, temp->key);
      Updatemax (node);
    }
  else
    {
      struct BST *child;
      if (node->left)

	child = node->left;
      else
	child = node->right;
      free (node);
      return child;
    }


}


void
main ()
{
  long long int i, n = 50000, A[2][50000], l, r, c;
  struct BST *root = NULL;
  struct List *list;
  A[0][0] = 8;
  for (i = 1; i < n; ++i)
    {
      A[0][i] = rand () % 10 + 1 + A[0][i - 1];
      A[1][i] = rand () % 10 + 1 + A[0][i];
      root = Insert (root, A[0][i], A[1][i]);
    }
  root = Insert (root, 4, 6);
  root = Insert (root, 7, 8);
  for (i = 8; i < n; i++)
    root = Delete (root, A[0][i]);
  if (Overlap (root, 10, 15))
    printf ("%lld\n ", Overlap (root, 10, 15)->key);
  Inorder (root);

}
