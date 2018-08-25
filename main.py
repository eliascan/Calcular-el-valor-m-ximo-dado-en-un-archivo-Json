import json

file = 'probability.json'

with open(file, 'r', encoding='utf-8') as proba:
    sts = json.loads(proba.read())


def maxProbability(data):
    probaMax = []
    tagName = []

    datos = data['predictions']

    for row in datos:
        probaMax.append(row['probability'])
        tagName.append(row['tagName'])

    return max(list(zip(probaMax, tagName)))


print(maxProbability(sts))
