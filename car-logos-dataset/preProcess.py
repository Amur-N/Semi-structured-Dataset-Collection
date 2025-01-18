import json

with open('./car-logos-dataset.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

with open('car-logos-dataset.txt', 'w', encoding='utf-8') as file:
    for d in data:
        file.write(f'{d["name"]} {d["slug"]} {{ {d["image"]["source"]} {d["image"]["thumb"]} {d["image"]["optimized"]} {d["image"]["original"]} {d["image"]["localThumb"]} {d["image"]["localOptimized"]} {d["image"]["localOriginal"]} }}\n')