# Report functions


def get_most_played(file_name):
    sell = []
    with open(file_name, 'rt') as file:
        for line in file.readlines():
            line= line.split("\t")
            sell.append(line[1])
            sell = [float(i) for i in sell]
            max_value = max(sell)
            if max_value in sell:
                return line[0]


def sum_sold(file_name):
    sell = []
    with open(file_name, 'rt') as file:
        for line in file.readlines():
            line= line.split("\t")
            sell.append(line[1])
            sell = [float(i) for i in sell]
        return sum(map(float,sell))
                

def get_selling_avg(file_name):
    sell = []
    z = 0
    with open(file_name, 'rt') as file:
        for line in file.readlines():
            line= line.split("\t")
            sell.append(line[1])
            sell = [float(i) for i in sell]
        for i in range(0, len(sell)):
            z += sell[i]
            result = z / len(sell)
        return result


def count_longest_title(file_name):
    titles = []
    with open(file_name, 'rt') as file:
        for line in file.readlines():
            line= line.split("\t")
            titles.append(line[0])
        return max(titles, key=len)



def get_date_avg(file_name):
    years = []
    z = 0
    with open(file_name, 'rt') as file:
        for line in file.readlines():
            line= line.split("\t")
            years.append(line[2])
            years = [int(i) for i in years]
        for i in range(0, len(years)):
            z += years[i]
            result = z / len(years)
        return round(result)



def get_game(file_name, title):
    titles = []
    with open(file_name, 'rt') as file:
        for line in file.readline():
            line= line.split("\n")
            titles.append(line[0])
        file.seek(0)
        for line in file.readlines():
            line = line.split("\t")
            if line[0] == title:
                return line
            


def count_grouped_by_genre(file_name):
    resultDict = {}
    with open(file_name, 'rt') as file:
        for line in file.readlines():
            line= line.split("\t")
            key = line[3]
            resultDict[key] = resultDict.get(key, 0) + 1
        return resultDict


def bubble_sort(array):
    array2 = array[:] # Save a copy, so that original is not mutated
    last_index = len(array) - 1 # Iterate up to this position
    while last_index > 0:
        for i in range(last_index):
            a, b = array2[i], array2[i + 1] # Consecutive numbers in array
            if a > b:
                array2[i], array2[i + 1] = b, a # Swap positions
        last_index -= 1 # A new number has bubbled up, no need to inspect it again
    return array2


def get_date_ordered(file_name):
    data = []
    titles = []
    with open(file_name, 'rt') as file:
        for line in file.readlines():
            line= line.split("\t")
            data.append(line[2])
            titles.append(line[0])
            data = [int(i) for i in data] 
            i = iter(data)
            j = iter(titles)
            z = list(zip(j, i))
            z = sorted(z, key=lambda x: x[1], reverse=True)
        return list(zip(*z))
                