/*
Given a m x n matrix grid which is sorted in non-increasing
 order both row-wise and column-wise, return the number of negative
  numbers in grid.
Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3

TimeComplexity : O(n+m)
*/

public class CountingNegativeNumber_SortedMatrix {
    public static void main(String[] args) {
        try {
        int [][]arr={
            {4,3,2,-1},
            {3,2,1,-1},
            {1,1,-1,-2},
            {-1,-1,-2,-3}
        };
        MySolution_Search_2DNegative_Arr obj =new MySolution_Search_2DNegative_Arr();
        System.out.print("Number of negative numbers : ");
        System.out.println(obj.countNegatives(arr));
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
class MySolution_Search_2DNegative_Arr{
    public int countNegatives(int[][] grid) {
        int count =0;
           int columnpoint = grid[0].length-1;
           for (int i = 0; i < grid.length; i++) {
               for (int j = columnpoint; j >= 0; j--) {
                   if(grid[i][j]<0){
                       count+=grid.length-i;
                    columnpoint--;
                   }else{
                       break;
                   }
               }
           }
       return count;      
       }
}