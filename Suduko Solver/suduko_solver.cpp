#include <bits/stdc++.h>
using namespace std;

//Checking is current digit is valid or not
bool isvalid(char n,vector<vector<char>> maze,int x,int y);

//Helper Functions for isvalid function
bool isempty(vector<vector<char>> maze,int &i,int &j);  //Checks is any box is empty
bool checkbox(char n,vector<vector<char>> maze, int i,int j); //Checks if there is any repetetion in a 3*3 box

//Function to fill Sudoku

bool suduko(vector<vector<char>> &maze)
{   int i,j;
    bool t = isempty(maze,i,j);
    if(!t)
    {
        return true;
    }
    //ALGORITHM
    /* LOOPS OVER 1 - 9 AND CHECKS FOR EVERY
        DIGIT AND BACKTRACKS IF IT CREATES COLLISION */

    for(char n='1';n <= '9';n++)
     if(isvalid(n,maze,i,j))
        { maze[i][j]=n;
          if(suduko(maze))
            return true;
          else
            maze[i][j]='.';
        }
    return false;
}

int main() {
	
    //Sudoku Board
	vector<vector<char> > maze = {{'5','3','.','.','7','.','.','.','.'},
	                              {'6','.','.','1','9','5','.','.','.'},
	                              {'.','9','8','.','.','.','.','6','.'},
	                              {'8','.','.','.','6','.','.','.','3'},
	                              {'4','.','.','8','.','3','.','.','1'},
	                              {'7','.','.','.','2','.','.','.','6'},
	                              {'.','6','.','.','.','.','2','8','.'},
	                              {'.','.','.','4','1','9','.','.','5'},
	                              {'.','.','.','.','8','.','.','7','9'}};

	suduko(maze);

    //Displaying Filled Board
	for(int i = 0; i < 9;i++){
	    for(int j = 0; j< 9; j++){
	        cout<<maze[i][j]<<" ";
	    }
	    cout<<endl;
	}
	return 0;
}

 //Checks is any box is empty
bool isempty(vector<vector<char>> maze,int &i,int &j)
{
    for(int x=0;x<9;x++)
      for(int y=0;y<9;y++)
        {
            if(maze[x][y] == '.')
               {
                   i=x;
                   j=y;
                   return true;
               }
        }
    return false;
}


//Checks if there is any repetetion in a 3*3 box

bool checkbox(char n,vector<vector<char>> maze, int i,int j)
{
    for(int x=0;x<3;x++)
      for(int y=0;y<3;y++)
      {
          if(maze[i+x][j+y] == n)
            return false;
      }
    return true;
}

//Checking is current digit is valid or not
bool isvalid(char n,vector<vector<char>> maze,int x,int y)
{
    for(int i =0;i<9;i++)
    {
        if(maze[i][y]==n || maze[x][i] == n)
            return false;
    }

    if(x<3)
    {
       if(y<3)
       {
           if(!checkbox(n,maze,0,0))
              return false;
       }
       else if(y<6)
       {
              if(!checkbox(n,maze,0,3))
              return false;
        }
       else
       {
           if(!checkbox(n,maze,0,6))
              return false;
       }
    }

    else if(x<6)
    {
       if(y<3)
       {
           if(!checkbox(n,maze,3,0))
              return false;
       }
       else if(y<6)
       {
              if(!checkbox(n,maze,3,3))
              return false;
        }
       else
       {
           if(!checkbox(n,maze,3,6))
              return false;
       }
    }

    else
    {
       if(y<3)
       {
           if(!checkbox(n,maze,6,0))
              return false;
       }
       else if(y<6)
       {
              if(!checkbox(n,maze,6,3))
              return false;
        }
       else
       {
           if(!checkbox(n,maze,6,6))
              return false;
       }
    }

    return true;
}
