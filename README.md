# Script to solve NPRSundayPuzzle Name Square

![alt text][logo]

[logo]: http://media.npr.org/assets/img/2016/12/30/sundaypuzzle-widecrop-4707696fb94c18e9b9d8928c5b3bb4e53d316229-s1600-c85.jpg "The awesome Sunday Puzzle From NPR"

# The Puzzle this Solves:
[FROM SUNDAY PUZZLE ON 2017-01-01:](http://www.npr.org/2017/01/01/507567187/for-this-puzzling-retrospective-on-2016-youll-need-a-set-of-speakers)Take the four-letter men's names TODD, OMAR, DAVE and DREW. If you write them one under the other, they'll form a word square, spelling TODD, OMAR, DAVE and DREW reading down as well:

| T  | O | D | D |
| ------------- | ------------- |------------- | ------------- |
| O  | M  | A  | R |
| D  | A  | V  | E  |
| D  | R  | E  | W  |

Can you construct a word square consisting of five five-letter men's names? Any such square using relatively familiar men's names will count. I have an answer using four relatively common names and one less familiar one.

# My Approach:
For every 5 by 5 block you must have symmetry across the diagonal of the grid.  This script uses a 'brute force' method where I use a list of names to generate all permutations of 5 different names, and then check each permutation for symmetry.  I'm sure this can be optimized, and I would appreciate the feedback my email is (jxr984 at psu dot edu)

To solve this problem I needed a list of names that would be common to someone who listens to NPR.  On Kaggle.com there was a [great set of data](https://www.kaggle.com/kaggle/us-baby-names) from the US Social Security Card applications from 1880-2010.  I chose this data over census bureau data because I got easier access to historical data, and I could find a CSV file.

# Conclusion/Interesting things I learned
It was hard quantifying what a "relatively familiar" men's name is.  For instance no significant amount of children were named Adolf after WW2 but it definitely is a "relatively familiar" name.  This is a rare example of a name being killed off by an individual, but a lot of strange edge cases affect the data and make "relatively familiar" hard to quantify. I eventually filtered out any name that didn't have more than 50 names given in a particular year, and to account for the larger population growth I only used the first 700 names.  This brought the number of 5 by 5 name blocks down from over 3000 to 23.  I then discussed if each of those 23 blocks contained "relatively familiar" names with my family.

My favorite name blocks so far:
SCOTT
CORRY
ORVAL
TRACE
TYLER

I have included a text file with 3000 5 letter male name blocks I found.  

# Libraries needed:
python 2, 
pandas
