insect-jump
===========

This is a funny recursive problem mentioned by my lecturer when I was in college.  He asked the following problem,
For a road with N steps long, and with a insect that can travel at most S steps each time. How many combination are there
for that insect to finish that road?
In the following diagram, x is represented as the insect.
The number below the line is that steps travelled by the insect.

Start x_________________________________________________ Target
                          N steps
Start _x________________________________________________ Target
      1
Start __x_______________________________________________ Target
      11
For N = 4 , S = 2
The possible combinations are,

Start ____ Target  Start ____ Target   Start ____ Target  Start ____ Target  Start ____ Target
      1111               2 11                12 1               112                2 2

This problem has an elegant analytic solution when S >= N, that is the insect can jump  further than the whole distance.
As every step in the road is either stepped or not stepped. The number of possible combination thus is 2^N-1.

For the other cases, I doubt that if there is any analytic solution. It seems that every S and N can be calculated with a recursive
function easily.

I wrote a python version of this recursive function. I think it is possible( but not quite easy) to translate this recursive 
function into a iterative one.

Enjoy!



