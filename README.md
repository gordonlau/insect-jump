insect-jump
===========

This is a funny recursive problem mentioned by my lecturer when I was in college.  He asked the following problem,
For a road with N steps long, and with a insect that can travel at most S steps each time. How many combination are there for that insect to finish that road?

In the following diagram,the number in the parenthesus is the steps travelled by the insect.

For N = 4 , S = 2
The possible combinations are,

Start (1111) Target  
Start (2 11) Target   
Start (12 1) Target  
Start (112 ) Target  
Start (2 2 ) Target

This problem has an elegant analytic solution when S >= N, that is the insect can jump  further than the whole distance.
As every step in the road is either stepped or not stepped. The number of possible combination thus is 2^N-1.

For the other cases, I doubt that if there is any analytic solution. It seems that every S and N can be calculated with a recursive
function easily.

I wrote a python version of this recursive function. I think it is possible( but not quite easy) to translate this recursive function into a iterative one. If you have a better solution, please contribute to this repository to let
other notify the internal harmony of this problem. Thank you.

Enjoy!



