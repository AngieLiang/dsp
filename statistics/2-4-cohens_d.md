[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)
```python
import nsfg
import numpy as np

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

def CohenEffectSize(group1, group2):
    """Computes Cohen's effect size for two groups.
    
    group1: Series or DataFrame
    group2: Series or DataFrame
    
    returns: float if the arguments are Series;
             Series if the arguments are DataFrames
    """
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d
    
CohenEffectSize(firsts.prglngth, others.prglngth)
0.028879044654449883

CohenEffectSize(firsts.totalwgt_lb,others.totalwgt_lb)
-0.088672927072602006

#difference
-0.088672927072602006/0.028879044654449883
-3.0704937830739034
```
The Cohen's Effect Size for the difference in pregnancy length for first babies and others is 3 times smaller than the Cohen's effect Size for the difference in weight for first and other babies.
    
