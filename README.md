# The art of creating efficient algorithms

How often do we think outside the box to create a creative and efficient algorithm when we develop software?
I bet answer is "probably not often enough".

I use Python for Test Driven Development of Ansible roles, but I don't get to code as much Python as I would like.
It's one of many tools I use, but not my daily driver. Hence this example is not about how to create good algorithms in general,
but rather a reflections on how algorithms affects code performance. So please forgive me for any false assumptions and poor code quality.

While reading a book on Python 3 a few years ago, I came across an interesting anecdote about the German mathematician Carl Friedrich Gauss, who at the age of 8 was given a homework assignment to sum up all the numbers between 1 and 100. To his teacher’s astonishment Carl Friedrich answered 5050 a few seconds later, and it was the teacher had to go home and check if the answer was correct.

Instead of adding every number between 1 and 100, the young Carl Friedrich quickly realized that there were 50 pairs of unequal numbers that would sum up to 100:

```math
99 + 1
98 + 2
And so on, all the way down to 51 + 49
```

And since he had not included the number 50 yet, the answer was:

```math
(50 pairs * 100) + 50 = 5050
```

So the youngster had by himself discovered a pretty efficient algorithm for summing up integers. Not bad for an 8 year old!
According to Wikipedia this story is contested, but nevertheless it is a very good example of a creative solution for optimizing an algorithm.

## Source

My original article can be found at <http://audunnes.blogspot.dk/2016/06/the-art-of-creating-efficient-algorithms.html>
