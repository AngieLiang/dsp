[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)
```python
from __future__ import print_function, division

%matplotlib inline

import numpy as np

import thinkstats2
import thinkplot

#PMF
rand = np.random.random(1000)
pmf = thinkstats2.Pmf(rand)
thinkplot.Pmf(pmf, linewidth = 0.1)
#Pmf of 1000 random numbers is meaningless since every value in the range have the same probability.

#CDF
cdf = thinkstats2.Cdf(rand)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel = 'random number', ylabel = 'Cdf')
#The distribution is uniform by cdf plot.
