import collections

pop_dict = collections.defaultdict(int)
land_dict = collections.defaultdict(int)
density_dict = collections.defaultdict(int)

with open('/Users/patrickcorynichols/Projects/Thinkful/Lesson1_Ex6/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputfile:
    header = next(inputfile)    
    for line in inputfile:
        line = line.rstrip().split(',')
        line[5] = float(line[5])
        line[7] = float(line[7])
        if line[1] == 'Total National Population': 
            pop_dict[line[0]] += line[5]
            land_dict[line[0]] += line[7]
            
for j in range(len(pop_dict)):
     density_dict.update({pop_dict.keys()[j]:float(pop_dict.values()[j]/land_dict.values()[j])})
print density_dict