import os
import numpy as np
import matplotlib.pyplot as plt



# get the directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# build the full path to the CSV file
filename = os.path.join(script_dir, "AG_NO3_fill_cells_remove_NAN_2.csv")

data = np.loadtxt(filename, delimiter=",", skiprows=1, usecols=1)
student_flag = np.loadtxt(filename, delimiter=",", skiprows=1, usecols=2)



def anomaly(q, W, x):
  # start with the first window
  T1 = np.percentile(x[0:W], q, method="linear") # set T1
  
  flag = list(x[0:W] >= T1) # elementwise compare all values in our first window with T1. True=anomaly, False=normal.
  
  T = [0, T1] # this is going to list the percentile for each window (init with a 0 at the beginning so indices line up)
  
  for i in range(W,x.size): # loop through all remaining unclassified elements in x
    Tval = np.percentile(x[i-W+1:i+1], q, method="linear") # set each T value
    T.append(Tval)            # append each T value
    flag.append(x[i] >= Tval) # set whether each x value is an anomaly
  
  return flag, T # return the flags and the thresholds


W = 1000 # choose window size
q = 86 # choose anomaly cutoff percentile
# W=1000 and q=86% seems to be a good tradeoff, with both our accuracies exceeding their respective thresholds by about the same amount

flag, T = anomaly(q, W, data) # find the set of anomalies


# now, we must assess the accuracy rates by calculating tp, fp, fn, tn

tp=0; fp=0; fn=0; tn=0
for a, b in zip(flag, student_flag): # loop through all flags
  if a and b==1:
    tp += 1 # true positive: anomaly detected and present
  elif a and b!=1:
    fp += 1 # false positive: anomaly detected but not present
  elif not a and b==1:
    fn += 1 # false negative: anomaly not detected but present
  else:
    tn += 1 # true negative: anomaly not detected and not present


print( "True positives: "+str(tp))
print("False positives: "+str(fp))
print("False negatives: "+str(fn))
print( "True negatives: "+str(tn)) # print the 4 amounts of each type of detection

normAccuracy = tn/(tn+fp) # true negatives divided by number of non-anomalies
anomAccuracy = tp/(tp+fn) # true positives divided by number of anomalies

print("Normal event detection accuracy: "+str(100*normAccuracy)+"%")
print("Anomaly event detection accuracy: "+str(100*anomAccuracy)+"%") # print both accuracy rates






"""# and now, for the README, we must also create a scatter plot

x = np.arange(data.size) # the x coordinates of the points

colors = [] # list of colors for our scatter plot
sizes = np.zeros(data.size) # list of thicknesses for each point in our plot

for i in range(data.size):
  a = flag[i]
  b = student_flag[i]
  if a and b==1:
    colors.append('green') # true positive: color it green
    sizes[i] = 10
  elif a and b!=1:
    colors.append('purple') # false positive: color it purple
    sizes[i] = 0.01
  elif not a and b==1:
    colors.append('red') # false negative: color it red
    sizes[i] = 10
  else:
    colors.append('blue') # true negative: color it blue
    sizes[i] = 0.01

plt.scatter(x, data, c=colors, s=sizes)

from matplotlib.lines import Line2D

# add a legend so we know what each dot does
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='TP', markerfacecolor='green', markersize=5),
    Line2D([0], [0], marker='o', color='w', label='FP', markerfacecolor='purple', markersize=3),
    Line2D([0], [0], marker='o', color='w', label='FN', markerfacecolor='red', markersize=5),
    Line2D([0], [0], marker='o', color='w', label='TN', markerfacecolor='blue', markersize=3)
]
plt.legend(handles=legend_elements)

plt.show()"""