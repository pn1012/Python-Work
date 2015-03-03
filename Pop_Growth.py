import collections
population_dict = collections.defaultdict(int)

with open('/Users/patrickcorynichols/Projects/Thinkful/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)

    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = int(line[5])
        line[7] = int(line[7])
        if line[1] == 'Total National Population':
            population_dict[line[0]] += float(line[5])/float(line[7])

with open('/Users/patrickcorynichols/Projects/Thinkful/national_population_density.csv', 'w') as outputFile:
    outputFile.write('continent,Pop_Growth\n')
    for k, v in population_dict.iteritems():
        outputFile.write(k + ',' + str(v) + '\n')