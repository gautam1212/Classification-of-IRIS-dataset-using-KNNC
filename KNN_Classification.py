import math
import random
import matplotlib.pyplot as plt

# Classes of MNIST Iris Dataset
class_list = ['Iris-setosa','Iris-versicolor','Iris-virginica']

#print class_list
class_count = len(class_list)
dataset = []
attribs = 0
k_max = 25
accuracy = [0.0]*k_max

def Find_distance(val,i):
    return math.sqrt(pow(val[0]-i[0],2) + pow(val[1]-i[1],2) + pow(val[2]-i[2],2) + pow(val[3]-i[3],2))

def KNN():
    
    # randomly shuffling dataset
    random.shuffle(dataset)
    train = dataset[:int(0.8*len(dataset))]
    test = dataset[int(0.8*len(dataset)):]

    
    positive = [0]*k_max
    # kss = [0]*k_max

    for line in test:

        distance = []
        # print line
        for i in train:
            d = Find_distance(line,i)
            distance.append([d,i[4]])

        # Sort the distances to select first K values
        distance.sort()
        
        count = [0]*class_count
        for K in range(1,k_max):
            count[ distance[K-1][1] ] += 1
            max_type = max(count)
            m=max_type
            # kss[K]=K
            for i in  range(0,class_count):
                if(count[i] == max_type):
                    #print class_list[i]
                    if(i == line[4]):
                        positive[K]+=1
                    break

    
    # kss[0]=0
    for K in range(1,k_max):
        accuracy[K] += positive[K]*100.0/len(test)


def Data_Load():
    f = open('MNIST_Iris.txt')
    data = (f.read())
    lines = data.split('\n')


    for line in lines:
        values = line.split()
        #print (val)
        attribs = len(values)-1
        for i in range(0,attribs):
            values[i] = float(values[i])

        for i in range(0,class_count):
            if(values[4] == class_list[i]):
                values[4] = i

        #print (val)
        dataset.append(values)

def main():
    Data_Load()

    runs = 10
    for i in range(0,runs):
        KNN()
    kss = [0]*k_max
    for K in range(1,k_max):
        accuracy[K] = accuracy[K]/runs
        kss[K]=K
        print "Accuracy is ", accuracy[K],"% for K-Value:",K
    
    accuracy[0]=0.0
    # Graph Plot
    # plt.plot(kss,accuracy)
    # plt.xlabel('K')
    # plt.ylabel('accuracy')
    # plt.show()

if (__name__ == "__main__"):
    main()
