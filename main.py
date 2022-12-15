import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--path")
parser.add_argument("--mode")
parser.add_argument("--country", required=False)
parser.add_argument("--year")
parser.add_argument("--output", required=False)
args = parser.parse_args()
path = args.path
mode = args.mode
country = args.country
year = args.year
pathOutput = args.output

def countMedals(medals):
    gold = 0
    bronze = 0
    silver = 0
    countAthletes = 0
    for line in lines:
        if int(year) not in yearsOlymp:
            print('No olymp this year')
            nextLine = file.readline()
            quit()
        splitLine = line.split('\t')
        medalLine = splitLine[-1][:-1]
        nameAthlete = splitLine[1]
        countryAthlete = splitLine[-9]
        sportAthlete = splitLine[-3]
        if country in countryAthlete or country in splitLine:
            if year in splitLine:
                while countAthletes < 10:
                    if nameAthlete not in names and medalLine != 'NA':
                        if (pathOutput != None):
                                fileOutput.write(f'{nameAthlete} - {sportAthlete} - {medalLine} \n')
                        print(nameAthlete,"-",sportAthlete,"-",medalLine)
                        countAthletes += 1
                        names.append(nameAthlete)
                    else:
                        break

                medals.append(medalLine)


    if len(names) == 0:
        if (pathOutput != None):
                fileOutput.write('invalid country')
        print('invalid country')
        quit()
    if len(medals) < 10:
        if (pathOutput != None):
                fileOutput.write(f'that year {country} had less than 10 medals \n')
        print('that year',country,'had less than 10 medals')


    # for medal in medals:
    #     if medal == 'Gold':
    #         gold += 1
    #     elif medal == 'Silver':
    #         silver += 1
    #     elif medal == 'Bronze':
    #         bronze += 1
    #
    # return gold+silver+bronze

def total_medals(year):
    dict = {}
    with open(path, 'r') as file:
        headline = file.readline()
        line = file.readline()
        line = line.split("\t")
        if year == line[9]:
            if line[-1] != "NA\n":
                if line[1] not in dict:
                    dict[line[1]] = [line[-1]]
                else:
                    dict[line[1]].append(line[-1])
        print(dict)
        for people in dict:
            print(people, ' : ', dict[people])



names = []
medals = []
yearsOlymp = []

for i in range(1896,2016,4):
    yearsOlymp.append(i)

if (pathOutput != None):
    fileOutput = open(pathOutput,"w")

with open(path, 'r') as file:
    lines = file.readlines()
lines = lines[1:]

if mode == 'total':
    total_medals(year)
else:
    countMedals(medals)




if (pathOutput != None):
        fileOutput.write(f'Summary medals : {countMedals(medals)} \n')
if (pathOutput != None):
    fileOutput.close()


