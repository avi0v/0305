from scipy import stats
a=stats.norm.cdf(20.07,loc=20.05,scale=0.02)-stats.norm.cdf(20.06,loc=20.05,scale=0.02)
print(a)
