#!/usr/bin/env python
import time


class FunnyMath(object):
    """
    The purpose of this class is to show how important it is to think about
    the efficiency of you algorithms. Based on my blog post about the same
    topic at http://audunnes.blogspot.dk/2016/06/the-art-of-creating-efficient-algorithms.html  # noqa E501
    """

    def __init__(self, num=0):
        """
        Initialize the object with a numeric value of numbers to sum up.
        """
        assert type(num) is int, "num was not an integer {}".format(num)
        self.num = num

    def slowest(self):
        """
        Very inefficient summary function. because it constantly updates
        the class variable during the loop.
        Reference: https://wiki.python.org/moin/PythonSpeed/PerformanceTips#Local_Variables  # noqa E501
        """
        for i in range(1, self.num):
            self.num += i
        return int(self.num)

    def faster(self):
        """
        Slightly faster summary function, because it only updates
        a local variable during the loop.
        """
        local_num = self.num
        for i in range(1, local_num):
            local_num += i
        return int(local_num)

    def fastest(self):
        """
        Efficient summary algorithm discovered by German mathematician
        Carl Friedrich Gauss.
        """
        return int(self.num**2/2.0 + self.num/2.0)

    @staticmethod
    def report(end, start, num, label):
        print('{0} approach took {1} seconds to get the result: {2}'.format(
            label, round((end-start), 2), num))


def main():
    fm = FunnyMath(num=100000000)
    start = time.time()
    num = fm.slowest()
    end = time.time()
    fm.report(end, start, num, 'Slowest')

    fm.num = 100000000
    start = time.time()
    num = fm.faster()
    end = time.time()
    fm.report(end, start, num, 'Faster')

    fm.num = 100000000
    start = time.time()
    num = fm.fastest()
    end = time.time()
    fm.report(end, start, num, 'Fastest')


if __name__ == "__main__":
    main()
