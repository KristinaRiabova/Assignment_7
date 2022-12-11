import argparse

parser = argparse.ArgumentParser(description="Hello")
parser.add_argument("path", type=str)
parser.add_argument("medals",type=str, default="-medals")
parser.add_argument("country", type=str)
parser.add_argument("year", type=str)
parser.add_argument("-output", type=str)
args = parser.parse_args()
path = args.path
country = args.country
year = args.year
pathOutput = args.output

def countMedals(medalsList):
    gold = 0
    bronze = 0
    silver = 0
    for medal in medalsList:
        if medal == 'Gold':
            gold += 1
        elif medal == 'Silver':
            silver += 1
        elif medal == 'Bronze':
            bronze += 1

    return gold+silver+bronze


names = []
countAthletes = 0
medals = []
yearsOlymp = []

for i in range(1896,2016,4):
    yearsOlymp.append(i)

if (pathOutput != None):
    fileOutput = open(pathOutput,"w")

with open(path, 'r') as file:
    file.readline()
    nextLine = file.readline()
    while nextLine:
        if int(year) not in yearsOlymp:
            print('No olymp this year')
            nextLine = file.readline()
            quit()
        splitLine = nextLine.split('\t')
        medalLine = splitLine[-1][:-1]
        nameAthlete = splitLine[1]
        countryAthlete = splitLine[-9].split('/')
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

        nextLine = file.readline()

    if len(names) == 0:
        if (pathOutput != None):
                fileOutput.write('invalid country')
        print('invalid country')
        quit()
    if len(medals) < 10:
        if (pathOutput != None):
                fileOutput.write(f'that year {country} had less than 10 medals \n')
        print('that year',country,'had less than 10 medals')

if (pathOutput != None):
        fileOutput.write(f'Summary medals : {countMedals(medals)} \n')
if (pathOutput != None):
    fileOutput.close()

print('Summary medals : ',countMedals(medals))
