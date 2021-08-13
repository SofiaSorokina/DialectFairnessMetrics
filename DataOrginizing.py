import csv
import random

#takes existing csv and txt files and writes lines from csv into txt
def csvTotxt(csv_filename):
    csv_file = csv_filename
    txt_file = csv_file.replace(".csv", ".txt")
    open(txt_file,"w")
    with open(txt_file, "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
            [ my_output_file.write(''.join(row)+'\n') for row in csv.reader(my_input_file)]
        my_output_file.close()

#takes existing txt file with lines and rewrites it so that each line is put into one line
def oneLine(filename):
    txt_file = filename
    file = open(filename, 'r')
    lines = file.readlines()
    clean_lines = list(map(str.strip,lines))
    f= open(filename,"w+")
    line = '. '.join([str(elem) for elem in clean_lines])
    f.write(line)

#combines content of the files randomly and puts it unto an existing file
def randomize(file1, file2, file3, randomFile):
    aaTweets = open(file1, 'r')
    aa_contents = aaTweets.readlines()
    aa_list = list(map(str.strip,aa_contents))
    aa_length = len(aa_list)

    hispTweets = open(file2, 'r')
    hisp_contents = hispTweets.readlines()
    hisp_list = list(map(str.strip,hisp_contents))
    hisp_length = len(hisp_list)

    whiteTweets = open(file3, 'r')
    white_contents = whiteTweets.readlines()
    white_list = list(map(str.strip,white_contents))
    white_length = len(white_list)

    id = [1,2,3]
    aaID = list(range(aa_length))
    hID = list(range(hisp_length))
    whID = list(range(white_length))

    for i in aaID+hID+whID:
        ranID = random.choice(id)
        if ranID == 1:
            if aaID:
                num = random.choice(aaID)
                #print(str(num)+" "+aa_list[num])
                f = open(randomFile, "a")
                line = aa_list[num] + ". "
                f.write(line)
                aaID.remove(num)
        elif ranID == 2: 
            if hID:
                num = random.choice(hID)
                #print(str(num)+" "+hisp_list[num])
                f = open(randomFile, "a")
                line = hisp_list[num] + ". "
                f.write(line)
                hID.remove(num)
        elif ranID == 3:
            if whID:
                num = random.choice(whID)
                #print(str(num)+" "+white_list[num])
                f = open(randomFile, "a")
                line = white_list[num] + ". "
                f.write(line)
                whID.remove(num)

#combine all oneLine .txt dialects into one AllTweets file
def combineData (file1, file2, file3):
    filenames = [file1, file2, file3]
    
    if file1 == "TwitterData/run1/AATweets1.txt":
        #write run1 data in order
        fileO = open("TwitterData/run1/OrderAllTweets1.txt","w")
        for names in filenames:
            with open(names) as infile:
                fileO.write(infile.read()) #combine lines
        #make it into one line
        oneLine("TwitterData/run1/OrderAllTweets1.txt")
        #orginizing randomly
        open("TwitterData/run1/RandomAllTweets1.txt","w")
        randomize(file1, file2, file3, "TwitterData/run1/RandomAllTweets1.txt")

    elif file1 == "TwitterData/run2/AATweets2.txt":
        #write run2 data in order
        with open("TwitterData/run2/OrderAllTweets2.txt","w") as outfile:
            for names in filenames:
                with open(names) as infile:
                    outfile.write(infile.read())
        #make it into one line
        oneLine("TwitterData/run2/OrderAllTweets2.txt")
        #orginizing randomly
        open("TwitterData/run2/RandomAllTweets2.txt","w")
        randomize(file1, file2, file3, "TwitterData/run2/RandomAllTweets2.txt")

    elif file1 == "TwitterData/run3/AATweets3.txt":
        #write run3 data in order
        with open("TwitterData/run3/OrderAllTweets3.txt","w") as outfile:
            for names in filenames:
                with open(names) as infile:
                    outfile.write(infile.read())
        #make it into one line
        oneLine("TwitterData/run3/OrderAllTweets3.txt")
        #orginizing randomly
        open("TwitterData/run3/RandomAllTweets3.txt","w")
        randomize(file1, file2, file3, "TwitterData/run3/RandomAllTweets3.txt")



#converting run1 from csv to txt
csvTotxt("TwitterData/run1/AATweets1.csv")
csvTotxt("TwitterData/run1/HispTweets1.csv")
csvTotxt("TwitterData/run1/WhiteTweets1.csv")

#converting run2 from csv to txt
csvTotxt("TwitterData/run2/AATweets2.csv")
csvTotxt("TwitterData/run2/HispTweets2.csv")
csvTotxt("TwitterData/run2/WhiteTweets2.csv")

#converting run3 from csv to txt
csvTotxt("TwitterData/run3/AATweets3.csv")
csvTotxt("TwitterData/run3/HispTweets3.csv")
csvTotxt("TwitterData/run3/WhiteTweets3.csv")

#combine corresponding files together
combineData("TwitterData/run1/AATweets1.txt", "TwitterData/run1/HispTweets1.txt", "TwitterData/run1/WhiteTweets1.txt")
combineData("TwitterData/run2/AATweets2.txt", "TwitterData/run2/HispTweets2.txt", "TwitterData/run2/WhiteTweets2.txt")
combineData("TwitterData/run3/AATweets3.txt", "TwitterData/run3/HispTweets3.txt", "TwitterData/run3/WhiteTweets3.txt")