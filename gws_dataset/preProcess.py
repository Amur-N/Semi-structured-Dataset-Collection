import json

with open('./input.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

with open('output.txt', 'w', encoding='utf-8') as file:
    for d in data["activities"]:
        file.write('{\n')
        file.write(f'{d["kind"]} ')
        file.write(f'{{ {d["id"]["time"]} {d["id"]["uniqueQualifier"]} {d["id"]["applicationName"]} {d["id"]["customerId"]} }} ')
        file.write(f'{d["etag"]} ')
        file.write('{ ')
        if "callerType" in d["actor"]:
            file.write(f'{d["actor"]["callerType"]} ')
        if "email" in d["actor"]:
            file.write(f'{d["actor"]["email"]} ')
        if "profileId" in d["actor"]:
            file.write(f'{d["actor"]["profileId"]} ')
        file.write('}')
        if "ipAddress" in d:
            file.write(f' {d["ipAddress"]}')
        for e in d["events"]:
            file.write("\n\t{\n\t")
            if "type" in e:
                file.write(f'{e["type"]} ')
            if "name" in e:
                file.write(f'{e["name"]}\n')
            if "parameters" in e:
                for p in e["parameters"]:
                    file.write("\t\t{ ")
                    file.write(f'{p["name"]} ')
                    if "value" in p:
                        file.write(f'{p["value"]} ')
                    if "intValue" in p:
                        file.write(f'{p["intValue"]} ')
                    if "boolValue" in p:
                        file.write(f'{p["boolValue"]} ')
                    if "multiValue" in p:
                        file.write("{ ")
                        for m in p["multiValue"]:
                            file.write(f'{m} ')
                        file.write("} ")
                    file.write("}\n")
            file.write("\t}\n")
        file.write("}\n")