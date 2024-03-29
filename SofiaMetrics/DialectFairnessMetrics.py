#
# By Sofia Sorokina, August 2021
#
# Input the files you want to compare in the correct order: 
# 'sumFile' for summary, 'aaFile' for African-American, 'hispFile' for Hispanic, and 'whFile' for White. 
# It will return how many tweets in the summary came from which dialect 
#
import random

def compare(sumFile, aaFile, hispFile, whFile):
    summary = open(sumFile, 'r') 
    sum_contents = summary.read()
    sum_list = sum_contents.split('. ')
    sum_list[len(sum_list)-1] = sum_list[len(sum_list)-1][:-1]

    aaTweets = open("TwitterData/" + aaFile, 'r')
    aa_contents = aaTweets.readlines()
    aa_list = list(map(str.strip,aa_contents))
    aa_length = len(aa_list)

    hispTweets = open("TwitterData/" + hispFile, 'r')
    hisp_contents = hispTweets.readlines()
    hisp_list = list(map(str.strip,hisp_contents))
    hisp_length = len(hisp_list)

    whiteTweets = open("TwitterData/" + whFile, 'r')
    white_contents = whiteTweets.readlines()
    white_list = list(map(str.strip,white_contents))
    white_length = len(white_list)

    countAA = 0
    countH = 0
    countWH = 0

    for x in sum_list:
        for y in aa_list:
            count = 0
            if x[:-1] in y:
                if count == 0:
                    #print ("'"+x+"'") #uncomment to see the which summary tweets have found comparrisons
                    #print ("'"+y+"'" + " from AA") #uncomment to see from which dialect is the compared tweet
                    countAA +=1
                    count += 1
                    break

        for y in hisp_list:
            count = 0
            if x[:-1] in y:
                if count == 0:
                    #print ("'"+x+"'") #uncomment to see which tweet is repeating
                    #print ("'"+y+"'" + " from Hisp") #uncomment to see from which dialect is the compared tweet
                    countH +=1
                    count += 1
                    break

        for y in white_list:
            count = 0
            if x[:-1] in y:
                if count == 0:
                    #print ("'"+x+"'") #uncomment to see which tweet is repeating
                    #print ("'"+y+"'" + " from White") #uncomment to see from which dialect is the compared tweet
                    countWH +=1
                    count += 1
                    break

    print("summary: "+str(len(sum_list))) #the amount of tweets in the summary
    print("count: "+str(countAA+countH+countWH)) #the amount of smilarities between the tweets in the summary and the dataset 

    print("from AA: " + str(countAA) + " or " + str(round(countAA/aa_length*100, 3)) + "% --> takes up " + str(round(countAA/len(sum_list)*100, 3)) + "% in the summary")
    print("from Hisp: " + str(countH) + " or " + str(round(countH/hisp_length*100, 3)) + "% --> takes up " + str(round(countH/len(sum_list)*100, 3)) + "% in the summary")
    print("from White: " + str(countWH) + " or " + str(round(countWH/white_length*100, 3)) + "% --> takes up " + str(round(countWH/len(sum_list)*100, 3)) + "% in the summary")


#Here you can choose which files to compare and organise them in a whay that you like.
print("\nLSA Summary Organized 1")
compare("LSA-summaries/OrderSummary1.txt", "run1/AATweets1.txt", "run1/HispTweets1.txt", "run1/WhiteTweets1.txt")
print("\nLSA Summary Randomized 1")
compare("LSA-summaries/RandomSummary1.txt", "run1/AATweets1.txt", "run1/HispTweets1.txt", "run1/WhiteTweets1.txt")
print("\nLSA Summary Organized 2")
compare("LSA-summaries/OrderSummary2.txt", "run2/AATweets2.txt", "run2/HispTweets2.txt", "run2/WhiteTweets2.txt")
print("\nLSA Summary Randomized 2")
compare("LSA-summaries/RandomSummary2.txt", "run2/AATweets2.txt", "run2/HispTweets2.txt", "run2/WhiteTweets2.txt")
print("\nLSA Summary Organized 3")
compare("LSA-summaries/OrderSummary3.txt", "run3/AATweets3.txt", "run3/HispTweets3.txt", "run3/WhiteTweets3.txt")
print("\nLSA Summary Randomized 3")
compare("LSA-summaries/RandomSummary3.txt", "run3/AATweets3.txt", "run3/HispTweets3.txt", "run3/WhiteTweets3.txt")


print("\n-----------------------------------------------------------")

print("\nSUMY Summary Organized 1")
compare("SUMY-summaries/OrderSummary1.txt", "run1/AATweets1.txt", "run1/HispTweets1.txt", "run1/WhiteTweets1.txt")
print("\nSUMY Summary Randomized 1")
compare("SUMY-summaries/RandomSummary1.txt", "run1/AATweets1.txt", "run1/HispTweets1.txt", "run1/WhiteTweets1.txt")
print("\nSUMY Summary Organized 2")
compare("SUMY-summaries/OrderSummary2.txt", "run2/AATweets2.txt", "run2/HispTweets2.txt", "run2/WhiteTweets2.txt")
print("\nSUMY Summary Randomized 2")
compare("SUMY-summaries/RandomSummary2.txt", "run2/AATweets2.txt", "run2/HispTweets2.txt", "run2/WhiteTweets2.txt")
print("\nSUMY Summary Organized 3")
compare("SUMY-summaries/OrderSummary3.txt", "run3/AATweets3.txt", "run3/HispTweets3.txt", "run3/WhiteTweets3.txt")
print("\nSUMY Summary Randomized 3")
compare("SUMY-summaries/RandomSummary3.txt", "run3/AATweets3.txt", "run3/HispTweets3.txt", "run3/WhiteTweets3.txt")

print("\n-----------------------------------------------------------")

print("\nSMMRY Summary Organized 1")
compare("SMMRY-summaries/OrderSummary1.txt", "run1/AATweets1.txt", "run1/HispTweets1.txt", "run1/WhiteTweets1.txt")
print("\nSMMRY Summary Randomized 1")
compare("SMMRY-summaries/RandomSummary1.txt", "run1/AATweets1.txt", "run1/HispTweets1.txt", "run1/WhiteTweets1.txt")
print("\nSMMRY Summary Organized 2")
compare("SMMRY-summaries/OrderSummary2.txt", "run2/AATweets2.txt", "run2/HispTweets2.txt", "run2/WhiteTweets2.txt")
print("\nSMMRY Summary Randomized 2")
compare("SMMRY-summaries/RandomSummary2.txt", "run2/AATweets2.txt", "run2/HispTweets2.txt", "run2/WhiteTweets2.txt")
print("\nSMMRY Summary Organized 3")
compare("SMMRY-summaries/OrderSummary3.txt", "run3/AATweets3.txt", "run3/HispTweets3.txt", "run3/WhiteTweets3.txt")
print("\nSMMRY Summary Randomized 3")
compare("SMMRY-summaries/RandomSummary3.txt", "run3/AATweets3.txt", "run3/HispTweets3.txt", "run3/WhiteTweets3.txt")
