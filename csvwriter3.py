# this is my csv writer program, for easy input of poll sampling data

# first step is a menu request
# then a input>list system
# then a csv conversion

import csv

print "Welcome to the Poll Sampling data .csv maker"

print "This program will allow the user to directly input sampling data"
print "And export it as a csv list for further use in excel/data software."

print "Please select from the following options:"
print "Start"
print "Quit"

input = raw_input("> ")

if input == "Start":

    # headers section for capture of parties contesting
    headers = ["Polling district"]

    parties = raw_input("Please enter the political party (delimited with a\
 comma): ")

    headers += parties.split(",")

    #party_split = parties.split(",")

    #headers.append(party_split)

    print headers

    print "Please note the format of your headers when submitting votes \
 per party"
    cont = "y"

    line1 = []

    while (cont == "y"):

        line1.append(raw_input("Please enter the Polling district: "))

        votes = []

        for fiesta in parties.split(","):
            votes.append(raw_input(("Please enter votes for %s: ") % fiesta))

        line1 += votes

        print line1

        cont = raw_input("Do you wish to add another row? (y/n): ")

    table1 = []
    table1 += headers, line1

    print "Now it is time to make your inputs into a CSV file"
    print "Here is a summary of your data."
    print table1
    print "Please confirm you wish to proceed"
    proc = raw_input("> ")
    if proc == "y":
        with open('newcsv.csv', 'w') as csvfile:
            noter = csv.writer(csvfile)
            noter.writerows(table1)
            print "CSV created!"
            print "Goodbye."
else:
    quit()
