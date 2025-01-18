import json

with open('./DiaLog.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

with open('DiaLog.txt', 'w', encoding='utf-8') as file:
    for d in data:
        file.write(f'{d["dialog_id"]} {d["turns"]}')
        file.write(" events:{ ")
        for e in d["events"]:
            file.write("[{ ")
            for s in e["S1"]:
                file.write(f'{s} ')
            file.write("}{ ")
            for s in e["S2"]:
                file.write(f'{s} ')
            file.write("}] ")
        file.write("}\n")