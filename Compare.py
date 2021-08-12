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
            if x==y:
                #print ("'" + x + "' is from AATweets")
                countAA +=1

    for x in sum_list:
        for y in hisp_list:
            if x==y:
                #print ("'" + x + "' is from HispTweets")
                countH +=1

    for x in sum_list:
        for y in white_list:
            if x==y:
                #print ("'" + x + "' is from WhiteTweets")
                countWH +=1

    sumCount = countAA + countH + countWH

    print("from AA: " + str(countAA) + " or " + str(round(countAA/aa_length*100, 3)) + "% --> takes up " + str(round(countAA/sumCount*100, 3)) + "% in the summary")
    print("from Hisp: " + str(countH) + " or " + str(round(countH/hisp_length*100, 3)) + "% --> takes up " + str(round(countH/sumCount*100, 3)) + "% in the summary")
    print("from White: " + str(countWH) + " or " + str(round(countWH/white_length*100, 3)) + "% --> takes up " + str(round(countWH/sumCount*100, 3)) + "% in the summary")


print("\nSummary 1")
compare("LSA-summary/OrderSummary1.txt", "run1/AATweets1.txt", "run1/HispTweets1.txt", "run1/WhiteTweets1.txt")
print("\nSummary 2")
compare("LSA-summary/OrderSummary2.txt", "run2/AATweets2.txt", "run2/HispTweets2.txt", "run2/WhiteTweets2.txt")
print("\nSummary 3")
compare("LSA-summary/OrderSummary3.txt", "run3/AATweets3.txt", "run3/HispTweets3.txt", "run3/WhiteTweets3.txt")

