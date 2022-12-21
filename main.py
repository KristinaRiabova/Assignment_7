import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--path")
parser.add_argument("--mode", required=False)
parser.add_argument("--country", required=False)
parser.add_argument("--year", required=False)
parser.add_argument("--output", required=False)
parser.add_argument("-overall", type=str, required=False, nargs='*')
args = parser.parse_args()
path = args.path
mode = args.mode
country = args.country
year = args.year
pathOutput = args.output
countries = args.overall

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

    return print(f'{gold} gold medals, {silver} silver medals, {bronze} bronze medals, total : {gold + bronze + silver}')


def total_medals(year):
    if int(year) not in yearsOlymp:
        print('No olymp this year')
        quit()
    dict = {}
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


def overallFunc(countries):
    dict = {}

    for countryOverall in countries:
        key = countryOverall
        dict.setdefault(key, [])
        dict[key].append([])
        dict[key].append([])

    def findIndex(dictionary, needYear, key):
        for countr in dictionary:
            i = 0
            if (countr == key):
                for year in dictionary[countr][0]:
                    if needYear == year:
                        return i
                    i += 1

    with open(path, 'r') as file:
        file.readline()
        line = file.readline()
        while line:
            splitLine = line.split('\t')
            yearOverall = splitLine[9]
            if splitLine[-1][:-1] != "NA":
                if splitLine[-9] in countries:
                    key = splitLine[-9]
                    if yearOverall not in dict[key][0]:
                        dict[key][0].append(yearOverall)
                        dict[key][1].append(0)
                        dict[key][1][findIndex(dict,yearOverall,key)] += 1
                    elif yearOverall in dict[key][0]:
                        dict[key][1][findIndex(dict,yearOverall,key)] += 1

            line = file.readline()

    def maxMedals(dictionary):
        for countr in dictionary:
            i = 0
            j = 0
            maxMedal = dictionary[countr][1][0]
            for medal in dictionary[countr][1]:
                if (maxMedal <= medal):
                    maxMedal = medal
                    j = i
                i+=1
            print(countr," max medals in ",dictionary[countr][0][j]," : ",maxMedal)

    return print(maxMedals(dict))

def interactiveFunc():
    while True:
        dict = {}
        dictCountries = {}
        dictMedals = {}

        country = input("Input country")
        with open(path, 'r') as file: # открываем файл на чтение
            file.readline() # читаем заголовочную строку
            line = file.readline() # читаем первую строку с данными
            while line: # пока есть строки в файле
                splitLine = line.split('\t') # сплит по табу
                if country in splitLine[-9] or country in splitLine[-8]:
                    if splitLine[-1][:-1] != "NA":
                        key = splitLine[9]
                        dict.setdefault(key)
                        dictCountries.setdefault(key)
                        if (dict[key] == None):
                            dict[key] = 1
                            dictCountries[key] = splitLine[-4]
                        else:
                            dict[key] += 1
                            dictCountries[key] = splitLine[-4]

                        dictMedals.setdefault(key, [])

                        if (dictMedals[key] == []):
                            dictMedals[key].append(0)
                            dictMedals[key].append(0)
                            dictMedals[key].append(0)

                        if splitLine[-1][:-1] == "Gold":
                            dictMedals[key][0] += 1
                        elif splitLine[-1][:-1] == "Silver":
                            dictMedals[key][1] += 1
                        elif splitLine[-1][:-1] == "Bronze":
                            dictMedals[key][2] += 1


                line = file.readline()

            firstYear = int(key)
            maxYear = key
            countMaxYear = dict[key]
            minYear = key
            countMinYear = dict[key]
            placeOfOlymp = dictCountries[key]

            for key in dict:
                if firstYear >= int(key):
                    firstYear = int(key)
                    placeOfOlymp = dictCountries[key]
                if (dict[key] >= countMaxYear):
                    maxYear = key
                    countMaxYear = dict[key]
                if (dict[key] <= countMinYear):
                    minYear = key
                    countMinYear = dict[key]

        print("First Olymp : ", firstYear, ". Place : ", placeOfOlymp)
        print("Max medals Olymp : ", maxYear, ". Count medals : ", countMaxYear)
        print("Min medals Olymp : ", minYear, ". Count medals : ", countMinYear)

        for key in dictMedals:
            print(key," year : ", dictMedals[key][0], " gold medals, ", dictMedals[key][1], " silver medals, ",
                  dictMedals[key][2], " bronze medals")

        retry = input("Again ? y/n")
        retry = retry.lower()
        if retry == "y":
            continue
        elif retry == "n":
            quit()
        else:
            print("error")

if mode == 'total':
    total_medals(year)
elif mode == "medals":
    countMedals(medals)
elif countries != None:
    overallFunc(countries)
elif mode == 'interactive':
    interactiveFunc()

if (pathOutput != None):
    fileOutput.write(f'Summary medals : {countMedals(medals)} \n')
if (pathOutput != None):
    fileOutput.close()
