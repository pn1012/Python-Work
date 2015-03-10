import collections
import scipy.stats as stats
import matplotlib.pyplot as plt

data = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
c = collections.Counter(data)

print c

count_sum = sum(c.values())

for k,v in c.iteritems():
    print "The frequency of number " + str(k) + " is " + str(float(v)/count_sum)
    
plt.boxplot(data)
plt.savefig('/Users/PatrickCoryNichols/Desktop/Box_Plot.jpg')
plt.close()

plt.hist(data, histtype = 'bar')
plt.savefig('/Users/PatrickCoryNichols/Desktop/Histogram.jpg')
plt.close()

plt.figure()
graph1 = stats.probplot(data,dist="norm", plot = plt)
plt.savefig('/Users/PatrickCoryNichols/Desktop/Norm_Dist.jpg')
plt.close()