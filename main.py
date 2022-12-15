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


#python main.py --path data.tsv --mode medals --country USA --year 1972
#python main.py --path data.tsv --mode total --year 1972

medals = []

if (pathOutput != None):
    fileOutput = open(pathOutput, "w")


def countMedals(medals):
    gold = 0
    bronze = 0
    silver = 0
    countAthletes = 0
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
            countryAthlete = splitLine[-9]
            sportAthlete = splitLine[-3]
            if country in countryAthlete or country in splitLine:
                if year in splitLine:
                    while countAthletes < 10:
                        if nameAthlete not in names and medalLine != 'NA':
                            if (pathOutput != None):
                                fileOutput.write(f'{nameAthlete} - {sportAthlete} - {medalLine} \n')
                            print(nameAthlete, "-", sportAthlete, "-", medalLine)
                            countAthletes += 1
                            names.append(nameAthlete)
                        else:
                            break

                    medals.append(medalLine)

            nextLine = file.readline()

    for medal in medals:
        if medal == 'Gold':
            gold += 1
        elif medal == 'Silver':
            silver += 1
        elif medal == 'Bronze':
            bronze += 1

    if len(names) == 0:
        if (pathOutput != None):
            fileOutput.write('invalid country')
        print('invalid country')
        quit()

    if len(medals) < 10:
        if (pathOutput != None):
            fileOutput.write(f'that year {country} had less than 10 medals \n')
        print('that year', country, 'had less than 10 medals')

    return print(
        f'{gold} gold medals, {silver} silver medals, {bronze} bronze medals, total : {gold + bronze + silver}')


def total_medals(year):
    if int(year) not in yearsOlymp:
        print('No olymp this year')
        quit()
    dict = {

    }
    with open(path, 'r') as file:
        file.readline()
        line = file.readline()
        while line:
            splitLine = line.split('\t')
            if year == splitLine[9]:
                if splitLine[-1][:-1] != "NA":
                    key = splitLine[-9]
                    dict.setdefault(key, [])
                    if len(dict[key]) == 0:
                        dict[key].append(0)
                        dict[key].append(0)
                        dict[key].append(0)
                    medal = splitLine[-1][:-1].lower()
                    if medal == "gold":
                        dict[key][0] += 1
                    elif medal == "silver":
                        dict[key][1] += 1
                    elif medal == "bronze":
                        dict[key][2] += 1

            line = file.readline()


        for key in dict:
            print(key, " - ", dict[key][0], " - ", dict[key][1], " - ", dict[key][2])

    return dict


names = []
countAthletes = 0
yearsOlymp = []

for i in range(1896, 2016, 4):
    yearsOlymp.append(i)


if mode == 'total':
    total_medals(year)
else:
    countMedals(medals)

if (pathOutput != None):
    fileOutput.write(f'Summary medals : {countMedals(medals)} \n')
if (pathOutput != None):
    fileOutput.close()
