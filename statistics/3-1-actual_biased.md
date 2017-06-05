[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```python
from __future__ import print_function, division

%matplotlib inline

import numpy as np

import nsfg
import first
import thinkstats2
import thinkplot

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf
    
resp = nsfg.ReadFemResp()
pmf_num = thinkstats2.Pmf(resp.numkdhh, label = 'numkdhh')
biased = BiasPmf(pmf_num, 'biased')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf_num, biased])
thinkplot.Config(xlabel='Number of children', ylabel='PMF')

pmf_num.Mean(), biased.Mean()
(1.0242051550438309, 2.4036791006642821)
