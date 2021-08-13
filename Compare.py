def compare(sumFile, aaFile, hispFile, whFile):
    summary = open(sumFile, 'r')
    sum_contents = summary.read()
    sum_list = sum_contents.split('. ')


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
            if x in y:
                #print ("'" + x + "' is from AATweets")
                countAA +=1

    for x in sum_list:
        for y in hisp_list:
            if x in y:
                #print ("'" + x + "' is from HispTweets")
                countH +=1

    for x in sum_list:
        for y in white_list:
            if x in y:
                #print ("'" + x + "' is from WhiteTweets")
                countWH +=1

    print (sum_list)
    mystr = "this is a sentence."
    print (mystr[:-1])

    print("from AA: " + str(countAA) + " or " + str(round(countAA/aa_length*100, 3)) + "% --> takes up " + str(round(countAA/len(sum_list)*100, 3)) + "% in the summary")
    print("from Hisp: " + str(countH) + " or " + str(round(countH/hisp_length*100, 3)) + "% --> takes up " + str(round(countH/len(sum_list)*100, 3)) + "% in the summary")
    print("from White: " + str(countWH) + " or " + str(round(countWH/white_length*100, 3)) + "% --> takes up " + str(round(countWH/len(sum_list)*100, 3)) + "% in the summary")


print("\nSummary Organized 1")
compare("SUMY-summaries/OrderSummary1.txt", "run1/AATweets1.txt", "run1/HispTweets1.txt", "run1/WhiteTweets1.txt")
print("\nSummary Organized 2")
compare("SUMY-summaries/OrderSummary2.txt", "run2/AATweets2.txt", "run2/HispTweets2.txt", "run2/WhiteTweets2.txt")
"""print("\nSummary Organized 3")
compare("SUMY-summaries/OrderSummary3.txt", "run3/AATweets3.txt", "run3/HispTweets3.txt", "run3/WhiteTweets3.txt")
print("\nSummary Randomised 1")
compare("SUMY-summaries/RandomSummary1.txt", "run1/AATweets1.txt", "run1/HispTweets1.txt", "run1/WhiteTweets1.txt")
print("\nSummary Randomised 2")
compare("SUMY-summaries/RandomSummary2.txt", "run2/AATweets2.txt", "run2/HispTweets2.txt", "run2/WhiteTweets2.txt")
print("\nSummary Randomised 3")
compare("SUMY-summaries/RandomSummary3.txt", "run3/AATweets3.txt", "run3/HispTweets3.txt", "run3/WhiteTweets3.txt")"""

