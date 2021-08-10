txt_file = "TwitterData/run1/AATweets1.txt"
file = open('TwitterData/run1/AATweets1.txt', 'r')
lines = str(file.readlines())
mystr = lines.replace('\n', '. ')
new_txt_file = "TwitterData/run1/AATweets1.txt"

with open(new_txt_file, "w") as my_output_file:
    [ my_output_file.write(mystr)]
my_output_file.close()
