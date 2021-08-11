def combineData1 (file1, file2, file3):
    filenames = [file1, file2, file3]

    with open("TwitterData/run1/OneAllTweets1.txt","w") as outfile:
        for names in filenames:
            with open(names) as infile:
                outfile.write(infile.read())
        outfile.write(". ")

def combineData2 (file1, file2, file3):
    filenames = [file1, file2, file3]

    with open("TwitterData/run2/OneAllTweets2.txt","w") as outfile:
        for names in filenames:
            with open(names) as infile:
                outfile.write(infile.read())
        outfile.write(". ")

def combineData3 (file1, file2, file3):
    filenames = [file1, file2, file3]

    with open("TwitterData/run3/OneAllTweets3.txt","w") as outfile:
        for names in filenames:
            with open(names) as infile:
                outfile.write(infile.read())
        outfile.write(". ")

combineData1("TwitterData/run1/OneAATweets1.txt", "TwitterData/run1/OneHispTweets1.txt", "TwitterData/run1/OneWhiteTweets1.txt")
combineData2("TwitterData/run2/OneAATweets2.txt", "TwitterData/run2/OneHispTweets2.txt", "TwitterData/run2/OneWhiteTweets2.txt")
combineData3("TwitterData/run3/OneAATweets3.txt", "TwitterData/run3/OneHispTweets3.txt", "TwitterData/run3/OneWhiteTweets3.txt")