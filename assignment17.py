TP=1
TN=90
FP=1
FN=8
total=TP+TN+FP+FN

accuracy=(TP+TN)/total

error_rate=(FP+FN)/total

precision=TP/(TP+FP)

recall=TP/(TP+FN)

print(accuracy)
print(error_rate)
print(precision)
print(recall)
print(round(recall,2))