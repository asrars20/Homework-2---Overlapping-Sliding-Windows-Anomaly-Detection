# Homework-2---Overlapping-Sliding-Windows-Anomaly-Detection
In this assignment you will detect anomalies in a Nitrate time series using a threshold-based method with fixed-size, overlapping sliding windows (step size = 1). You will compute a q-percentile threshold within each window and classify the newly added data point as normal or anomaly. Ground truth indicates there are 77 anomaly events in total.

#Figure highlighting detected anomalies (e.g., scatter/line plot with anomalies marked)
![Anomalies](Figure_1.png)

#Chosen W and q with rationale (brief)
W=1000, q= 86%
q is the around the value needed in order to have an above 80% accuracy for the normal and above 75% accuracy for the anamolies. CHoosing q to be 85% would've also given us these values, so it's not down to the 1%, it's just 86% was roughly what was needed so that the inaccuracy is balanced between those two. 
Our chosen w value was mostly personal choice, it's the geometric mean between 500 and 2000 which is our lowest and highest values. Having a high w does make a differenece in terms of accuracy for w, but when q ia about 85-86%, then the w value barely causes a difference. A q value of about 1000 is about what was needed to have the best accuracy for both values, but it doesn't make the most of a difference

#Normal accuracy and Anomaly accuracy (with TP, FP, FN, TN counts)
True Positive: 109, False Positive: 5346, False negative: 32, True negative: 25303
Normal event detection accuracy:82.55734281705766%
Anomaly event detection accuracy:77.30496453900709%

#Any design choices (one-sided vs two-sided threshold, handling of NaNs, etc.)
One sided was chosen because it works in real time and has a lower delay time, overall it's more convinient,quciker and consistent for results.



