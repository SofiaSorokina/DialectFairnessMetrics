import csv

#takes existing csv and txt files and writes lines from csv into txt
def csvTotxt(csv_filename, txt_filename):
    csv_file = csv_filename
    txt_file = txt_filename
    with open(txt_file, "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
            [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
        my_output_file.close()

#takes existing txt file with lines and rewrites it so that each line is put into one list, also creates a new txt with just one line of text
def oneLine1(filename):
    txt_file = "TwitterData/run1/" + filename
    file = open(txt_file, 'r')
    lines = file.readlines()
    clean_lines = list(map(str.strip,lines))
    mystr = str(clean_lines)
    new_txt_file = "TwitterData/run1/" + filename

    with open(new_txt_file, "w") as my_output_file:
        [ my_output_file.write(mystr)]
    my_output_file.close()

    f= open("TwitterData/run1/One" + filename,"w+")
    oneLine = '. '.join([str(elem) for elem in clean_lines])
    f.write(oneLine)

def oneLine2(filename):
    txt_file = "TwitterData/run2/" + filename
    file = open(txt_file, 'r')
    lines = file.readlines()
    clean_lines = list(map(str.strip,lines))
    mystr = str(clean_lines)
    new_txt_file = "TwitterData/run2/" + filename

    with open(new_txt_file, "w") as my_output_file:
        [ my_output_file.write(mystr)]
    my_output_file.close()

    f= open("TwitterData/run2/One" + filename,"w+")
    oneLine = '. '.join([str(elem) for elem in clean_lines])
    f.write(oneLine)

def oneLine3(filename):
    txt_file = "TwitterData/run3/" + filename
    file = open(txt_file, 'r')
    lines = file.readlines()
    clean_lines = list(map(str.strip,lines))
    mystr = str(clean_lines)
    new_txt_file = "TwitterData/run3/" + filename

    with open(new_txt_file, "w") as my_output_file:
        [ my_output_file.write(mystr)]
    my_output_file.close()

    f= open("TwitterData/run3/One" + filename,"w+")
    oneLine = '. '.join([str(elem) for elem in clean_lines])
    f.write(oneLine)

csvTotxt("TwitterData/run1/AATweets1.csv", "TwitterData/run1/AATweets1.txt")
oneLine1("AATweets1.txt")
csvTotxt("TwitterData/run1/AllTweets1.csv", "TwitterData/run1/AllTweets1.txt")
oneLine1("AllTweets1.txt")
csvTotxt("TwitterData/run1/HispTweets1.csv", "TwitterData/run1/HispTweets1.txt")
oneLine1("HispTweets1.txt")
csvTotxt("TwitterData/run1/WhiteTweets1.csv", "TwitterData/run1/WhiteTweets1.txt")
oneLine1("WhiteTweets1.txt")

csvTotxt("TwitterData/run2/AATweets2.csv", "TwitterData/run2/AATweets2.txt")
oneLine2("AATweets2.txt")
csvTotxt("TwitterData/run2/AllTweets2.csv", "TwitterData/run2/AllTweets2.txt")
oneLine2("AllTweets2.txt")
csvTotxt("TwitterData/run2/HispTweets2.csv", "TwitterData/run2/HispTweets2.txt")
oneLine2("HispTweets2.txt")
csvTotxt("TwitterData/run2/WhiteTweets2.csv", "TwitterData/run2/WhiteTweets2.txt")
oneLine2("WhiteTweets2.txt")

csvTotxt("TwitterData/run3/AATweets3.csv", "TwitterData/run3/AATweets3.txt")
oneLine3("AATweets3.txt")
csvTotxt("TwitterData/run3/AllTweets3.csv", "TwitterData/run3/AllTweets3.txt")
oneLine3("AllTweets3.txt")
csvTotxt("TwitterData/run3/HispTweets3.csv", "TwitterData/run3/HispTweets3.txt")
oneLine3("HispTweets3.txt")
csvTotxt("TwitterData/run3/WhiteTweets3.csv", "TwitterData/run3/WhiteTweets3.txt")
oneLine3("WhiteTweets3.txt")