from json import loads
import pandas as pd
from matplotlib import pyplot
from sys import argv

if len(argv) < 3:
    print(f"Usage: python {argv[0]} <min population in millions> <min vaccination percent>")
    exit()

worldmeter = loads(open("worldmeter.json").read())
worldmeter_lastweek = loads(open("worldmeter_lastweek.json").read())

indexes = [1, 10, 11, 13, 14]
data = {}
countries = set()

for i in range(len(worldmeter)):
    worldmeter[i] = [worldmeter[i][j].replace(',', '').lower() for j in indexes]
    data[worldmeter[i][0]] = {
        "worldmeter": worldmeter[i],
        "worldmeter_lastweek": None,
        "vaccinations": None,
    }
    countries.add(worldmeter[i][0])

indexes = [1, 9]
common = 0
for i in range(len(worldmeter_lastweek)):
    worldmeter_lastweek[i] = [worldmeter_lastweek[i][j].replace(',', '').lower() for j in indexes]
    if worldmeter_lastweek[i][0] in countries:
        common += 1
    if worldmeter_lastweek[i][0] in data:
        data[worldmeter_lastweek[i][0]]["worldmeter_lastweek"] = worldmeter_lastweek[i]

#print(common)

def fmt(v):
    if '\n' in v:
        v = v.split('\n')[1]
    return v.replace(',', '').replace('%', '')


vaccinations = loads(open("google_vaccinations.json").read())
indexes = [0, 3]
common2 = 0
for i in range(len(vaccinations)):
    vaccinations[i] = [fmt(vaccinations[i][j]).lower() for j in indexes]
    if vaccinations[i][0] in data:
        data[vaccinations[i][0]]["vaccinations"] = vaccinations[i]
    if vaccinations[i][0] in countries:
        common2 += 1

#print(common2)

to_del = []
for k in data.keys():
    if data[k]["vaccinations"] is None or \
        data[k]["worldmeter_lastweek"] is None or \
            '' == data[k]["worldmeter"][2] or \
            '' == data[k]['vaccinations'][1] or \
            int(data[k]["worldmeter"][-1]) < 1e6 * int(argv[1]) or \
            '' == data[k]['worldmeter_lastweek'][1] or \
            float(data[k]["vaccinations"][1].replace('>', '')) <= int(argv[2]) or \
            float(data[k]["vaccinations"][1].replace('>', '')) > 100:

        #if data[k]["vaccinations"] is None or data[k]["worldmeter_lastweek"] is None:
        #    print(k, "missing data")
        to_del.append(k)
for k in to_del:
    del data[k]

d = {"country": [], "deaths": [], "vaccines": [], "deaths_lastweek": []}


def permil_to_percent(v):
    return float(v) / 1e6 * 100


for k in data:
    d["country"].append(k)
    d["deaths"].append(permil_to_percent(data[k]["worldmeter"][2]))
    d["deaths_lastweek"].append(float(data[k]["worldmeter_lastweek"][1]))
    d["vaccines"].append(float(data[k]["vaccinations"][1].replace('>', '')))

df = pd.DataFrame(d)
pd.set_option("display.max_rows", 10, "display.max_columns", None)
print(f"Countries in the dataset: {len(df)}")
print("Correlations:")
print(df.corr())

#pyplot.hist(df['vaccines'], bins=20)
#pyplot.show()

#pyplot.scatter(df["vaccines"], df["deaths"])
#pyplot.scatter(df["vaccines"], df["deaths_lastweek"])
#pyplot.show()