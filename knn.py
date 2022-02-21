import sys

import numpy as np
import csv
import pandas as pd
import  math
def Knn(data,k):
    case_base_list=form_case_base(data)
    do_classifcation(case_base_list,data,int(k))
    for i in case_base_list:
        print(i[0]+","+str(i[1])+","+str(i[2]))

def do_classifcation(case_base,data,k):

    count=0
    for i in range(0,len(data)):
        instance = data.iloc[i].tolist()
        distances=[]
        points=[]
        if (data.iloc[i].tolist() in case_base):
            continue
        else:
            for j in range(0,len(case_base)):
                    x = np.array(case_base[j][1:])
                    dist = eculidean_distance(x, np.array([instance[1:]]))
                    distances.append(dist)
                    points.append(case_base[j])


        distan_sort,points_sort=zip(*sorted(zip(distances, points)))
        distan_sort=distan_sort[:k]
        points_sort=points_sort[:k]
        print(distan_sort)
        print(points_sort)
        break
        weight_A=0
        weight_B=0
        class_val=""
        for m in range(0,k):
            if(points_sort[m][0]=='A'):
                weight_A+=calc_weights(distan_sort[k-1],distan_sort[0],distan_sort[m])

            else:
                weight_B+=calc_weights(distan_sort[k-1],distan_sort[0],distan_sort[m])
            print(calc_weights(distan_sort[k-1],distan_sort[0],distan_sort[m]))
        if(weight_A>weight_B):
            class_val='A'
        else:
            class_val='B'
        if(class_val!=instance[0]):
            count+=1


    print(count)

def calc_weights(farthest_dist,least_dist,instance_dist):

    if farthest_dist == least_dist:
        return 1
    else:
        return (farthest_dist - instance_dist )/ (farthest_dist - least_dist)

def form_case_base(data):
    case_base = []
    case_base.append(data.iloc[0].tolist())
    # case_base.append(data.iloc[1].tolist())

    # print(case_base)
    for i in range(1, len(data)):
        instance = data.iloc[i].tolist()
        min_dist=[]
        points=[]
        class_val=""
        for j in range(0, len(case_base)):
            x = np.array(case_base[j][1:])
            dist=eculidean_distance(x, np.array([instance[1:]]))
            min_dist.append(dist)
            points.append(case_base[j])


        sorted_list1,sorted_list2=zip(*sorted(zip(min_dist, points)))
        # print(sorted_list2[0][0])
        if(sorted_list2[0][0]!=instance[0]):
            case_base.append(instance)


    return case_base



def eculidean_distance(x, y):
        dist = np.sqrt(np.sum(np.square(x-y)))
        return dist

if __name__ == "__main__":
    expected_args = ["--data","--k"]
    arg_len = len(sys.argv)
    info = []

    for i in range(len(expected_args)):
        for j in range(1, len(sys.argv)):
            if expected_args[i] == sys.argv[j] and sys.argv[j + 1]:
                info.append(sys.argv[j + 1])
    k=info[1]
    data = pd.read_csv(info[0], header=None)
    Knn(data,k)

    # python student.py --data Example-shuffled.csv  --k 4
