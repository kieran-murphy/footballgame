import random
import time
import json
from pprint import pprint as pp

with open('teams.txt') as f:
    data = json.load(f)

for i in data:
    data[i]['score'] = 0

with open('teams.txt', 'w') as json_file:
        json.dump(data, json_file)