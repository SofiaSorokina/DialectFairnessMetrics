txt_file = "TwitterData/run1/AllTweets1.txt"
file = open(txt_file, 'r')
lines = file.readlines()
mystr = str(list(map(str.strip,lines)))
new_txt_file = "TwitterData/run1/AllTweets1.txt"

with open(new_txt_file, "w") as my_output_file:
    [ my_output_file.write(mystr)]
my_output_file.close()
