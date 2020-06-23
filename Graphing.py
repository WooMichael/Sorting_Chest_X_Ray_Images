import re
import numpy as np
with open("true_results.txt", 'r') as file:
    true_results_arr = list()
    for line in file:
        new_line = line.split(" ")
        print(len(new_line))
        if len(new_line) > 1:
            for rs in new_line:
                print(rs)
                rs = rs.replace('\n','')
                true_results_arr.append(rs)
#    true_results_arr.pop(0)
    print(true_results_arr)

with open("prediction_results.txt", 'r') as file:
    prediction_results_arr = list()
    for line in file:
        new_line = line.split(" ")
        print(len(new_line))
        if len(new_line) > 1:
            for rs in new_line:
                print(rs)
                rs = rs.replace('\n','')
                prediction_results_arr.append(rs)
   # prediction_results_arr.pop(0)
    print(prediction_results_arr)
print(len(true_results_arr),len(prediction_results_arr))
total_results = [i for i,j in zip(true_results_arr,prediction_results_arr) if i == j]
print(total_results)
print(len(total_results))