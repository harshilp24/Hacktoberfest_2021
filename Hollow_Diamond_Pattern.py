"""
Print hollow diamond pattern using '*'. See examples for more details.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each line contains a single odd integer N - the size of the diamond.

Constraints

1 <= T <= 100
3 <= N <= 201

Output Format

For each test case, print the test case number as shown, followed by the diamond pattern, separated by newline.

Sample Input 0

4
3
7
5
15
Sample Output 0

Case #1:
 *
* *
 *
Case #2:
   *
  * *
 *   *
*     *
 *   *
  * *
   *
Case #3:
  *
 * *
*   *
 * *
  *
Case #4:
       *
      * *
     *   *
    *     *
   *       *
  *         *
 *           *
*             *
 *           *
  *         *
   *       *
    *     *
     *   *
      * *
       *

"""

test_cases = int(input())

def place_stars(pattern, positions):
    for i in positions:
        pattern[i] = '*'
    return ''.join(pattern)

def star_positions(lines):
    stars = [[lines]]
    return stars + [[lines-i, lines+i] for i in range(1, lines+1)]

def make_pattern(size):
    pattern = [' ' * (2*(size+1)-1) for i in range(size+1)]
    stars = star_positions(size)
    line = 0

    for star in stars:
        pattern[line] = place_stars(list(pattern[line]), star)
        print(pattern[line])
        line += 1

    for i in pattern[:-1][::-1]:
        print(i)

for i in range(test_cases):
    n = int(input())

    print('Case #' + str(i + 1) + ':')
    make_pattern( n // 2)



