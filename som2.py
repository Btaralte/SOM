#Author:Lalbiakthuama(18CE10034),Indrajeet(18CE10032),Jalaj Patidar(18CE10033) ,Civil Engineering student, IIT KGP
import numpy as np
import random
import math
def euclid_distance(arr1,arr2):
    x = list(zip(list(arr1),list(arr2)))
    d = 0
    for i in x:
        d = d+(i[0]-i[1])*(i[0]-i[1])
    return d 
def cluster(matrix,arr,s):
    temp = []
    for i in range(s):
        d = euclid_distance(matrix[i],arr)
        temp.append(d)
    x = temp.index(min(temp))
    x = x+1
    return x    

input_matrix = []
n = int(input("Enter the no of inputs:"))
print("")
length = int(input("Enter the no of attributes:"))
print("")
file1 = open(input("Enter the name of the input file:").strip(),'r')
file2 = file1.readlines()
for i in range(len(file2)):
    temp_list = file2[i].strip().split()
    temp_list = list(map(float,temp_list))
    if len(temp_list)!=0:
        input_matrix.append(temp_list)
print("")    
s = int(input("Enter the number of clusters:"))
print("")
input_matrix = np.array(input_matrix)
weight_matrix = np.zeros((s,length))
for i in range(s):
    for j in range(length):
        weight_matrix[i][j]=random.random()
print("-----------------------------------------------------------------------------------------------")
print("")
r_initial = float(input("Enter the learning rate: "))
r = r_initial
steps = 0
print("")
t = int(input("Enter the number of iterations:"))
print("")
for i in range(int(t//n)):
    for j in range(n):
        euclid = []
        for k in range(s):
            d = euclid_distance(weight_matrix[k],input_matrix[j])
            euclid.append(d)
        winning_index = euclid.index(min(euclid))
        weight_matrix[winning_index]=weight_matrix[winning_index]+r*(input_matrix[j]-weight_matrix[winning_index])
        steps = steps+1
        
        r = r_initial*(1 - steps/t)
print("-----------------------------------------------------------------------------------------------")
print("")
for i in range(1,s+1):
    print("Cluster "+str(i)+" :           ",end='')
    for j in range(n):
        x = cluster(weight_matrix,input_matrix[j],s)
        if x == i:
            print("Input "+str(j+1)+","+" "*(5-len(str(j+1))),end='')
    print("") 
    print("")       
print("-----------------------------------------------------------------------------------------------")
print("")
while True:
    x = input("Do you want to find out in which cluster an arbitrary input belongs?(Enter Yes or No):")
    print("")
    if x == "No" or x == "no" or x == "NO":
        print("Goodbye!! The program will terminate!")
        break
    else:
        arr = list(map(float,input("Enter the attributes of the arbitrary input : ").strip().split()))
        y = cluster(weight_matrix,arr,s)
        print("")
        print("")
        print("The arbitrary input belongs to Cluster "+str(y))
        print("")
        print("")