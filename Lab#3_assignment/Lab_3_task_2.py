import csv
import numpy as np
import matplotlib.pyplot as plt
import random
#the characteristics data seperated by this following names
CustomerID = []
Genre = []
Age = []
Annual_income= []
Spending_Score = []

#get data from the customer.csv file
def take_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            #print(', '.join(row))
            CustomerID.append(int(row[0]))
            Genre.append(str(row[1]))
            Age.append(int(row[2]))
            Annual_income.append(int(row[3]))
            Spending_Score.append(int(row[4]))
    return

take_data('Customers.csv')
#plot the clsuter group in the following color formets
def plot_cluster(moon,cluster, iteration):
    color = 10 * ['r.','g.','k.','c.','b.','m.']
    print('Iteration number : ',iteration)
    for l in cluster.keys():
        for m in range(len(cluster[l])):
            plt.plot(cluster[l][m][0], cluster[l][m][1], color[l], markersize=10)
    #plt.figure() where the clsters center value are represented by the +
    plt.scatter(moon[:,0],moon[:,1],marker = '+', s = 150, linewidths = 5, zorder = 10)
    plt.show()

#initialize the clustering
def cluster_content(X, moon):
    cluster = {}
    for x in X:
        value = min([(i[0],np.linalg.norm(x - moon[i[0]]))for i in enumerate(moon)], key=lambda s:s[1])[0]
        try:
            cluster[value].append(x)
        except:
            cluster[value] = [x]
    return cluster
#applying the clustering algorithme by measuring mean of the input data
def Apply_Kmeans(X, K, N):
    temp1 = np.random.randint(N, size = K)
    oldmoon = np.array([X[i]for i in temp1])
    temp2 = np.random.randint(N, size=K)
    newmoon = np.array([X[i] for i in temp2])
    cluster = cluster_content(X, oldmoon)
    iteration = 0
    plot_cluster(oldmoon,cluster,iteration)
    while not matched(newmoon, oldmoon):
        iteration = iteration + 1
        oldmoon = newmoon
        cluster = cluster_content(X,newmoon)
        plot_cluster(newmoon, cluster,iteration)
        newmoon = new_center(newmoon, cluster)
    plot_cluster(newmoon, cluster, iteration)
    return
#after each iteration make the new center value for the each cluster
def new_center(moon, cluster):
    keys =sorted(cluster.keys())
    newmoon = np.array([(np.mean(cluster[k],axis = 0))for k in keys])
    #for k in keys:
    #    newmoon.append(np.mean(cluster[k],axis = 0))
    return newmoon

def matched(newmoon, oldmoon):
    return (set([tuple(a)for a in newmoon]) == set([tuple(a)for a in oldmoon]))

#the number of clsters will be made by Kmeans clustering
K = 5
X = np.array([[Spending_Score,Annual_income,Age,CustomerID]])
X = np.reshape(X, (len(X.T), 4))
#N=200 the number of points utilizing in the clustering
temp = Apply_Kmeans(X, K,150)