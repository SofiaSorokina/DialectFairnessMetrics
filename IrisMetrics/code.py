# Iris Chang
# 8/20/21

from lexrank import LexRank
import csv

dataset = []
csvfileArray = [[],[]]

print ("---------------------------------------------------------------------------------------------------------------")
option = True
while option:
    dialect = str(input('dialect: '))
    if dialect == '':
        option = False
    else:
        fileName = dialect + '.csv'
        csvfileArray[0].append(fileName)
        csvfileArray[1].append(0)
size = int(input('sample size: '))
print ("---------------------------------------------------------------------------------------------------------------")

def datasetMethod():

    for fileName in csvfileArray[0]:
        with open(fileName) as csvfile:
            for csvline in csvfile:
                dataset.append(csvline.replace('\n',''))
    with open('DATASET.csv','w') as csvfile:
        csvfile.write('\n'.join(dataset))
    return dataset

def score(dataset):

    lxr = LexRank(dataset)
    summary = '\n'.join(lxr.get_summary(dataset, size))
    with open('SUMMARY.txt','w') as txtfile:
        txtfile.write(summary)
    txtfile.close()
    scoreRank = lxr.rank_sentences(dataset, fast_power_method=False)
    scoreArray = []
    for score in scoreRank:
        scoreArray.append(score)
    scoreArray.sort(key=float, reverse=True)
    count = 0
    for score in scoreArray:
        if (count < size):
            count += 1
            print ('sample ' + str(count) + ': ' + str(score))
    print ("---------------------------------------------------------------------------------------------------------------")

def percent():

    with open('SUMMARY.txt','r') as txtfile:
        for txtline in txtfile:
            txtline = txtline.replace('\n','')
            for fileName in csvfileArray[0]:
                with open (fileName,'r') as csvfile:
                    for csvline in csvfile:
                        csvline = csvline.replace('\n','')   
                        if csvline == txtline:
                            for index in range(len(csvfileArray[0])):
                                if csvfileArray[0][index] == fileName:
                                    csvfileArray[1][index] += 1
    for index in range(len(csvfileArray[0])):
        print(csvfileArray[0][index] + ': ' + str((float(csvfileArray[1][index])/size)*100) + ' %')
    print ('---------------------------------------------------------------------------------------------------------------')

score (datasetMethod())
percent()
