import json

with open('./Current-US-Senators.json', 'r', encoding='utf-8') as file:
    data_sen = json.load(file)

with open('Current-US-Senators.txt', 'w', encoding='utf-8') as file:
    for o in data_sen["objects"]:
        file.write(f'{o["caucus"]}')
        file.write(" [ ")
        for cn in o["congress_numbers"]:
            file.write(f'{cn} ')
        file.write("] ")
        file.write(f'{o["current"]} "{o["description"]}" {o["district"]} {o["enddate"]}')
        file.write(f' {o["extra"]} ')
        file.write(f'"{o["leadership_title"]}" {o["party"]} {o["district"]} {o["enddate"]}')
        file.write(f' [ {o["person"]["bioguideid"]} {o["person"]["birthday"]} {o["person"]["cspanid"]} {o["person"]["fediverse_webfinger"]} {o["person"]["firstname"]} {o["person"]["gender"]} {o["person"]["gender_label"]} {o["person"]["lastname"]} {o["person"]["link"]} {o["person"]["middlename"]} "{o["person"]["name"]}" {o["person"]["namemod"]} {o["person"]["nickname"]} {o["person"]["osid"]} {o["person"]["pvsid"]} "{o["person"]["sortname"]}" "{o["person"]["twitterid"]}" "{o["person"]["youtubeid"]}" ] ')
        file.write(f'{o["phone"]} {o["role_type"]} {o["role_type_label"]} {o["senator_class"]} "{o["senator_class_label"]}" {o["senator_rank"]} {o["senator_rank_label"]} {o["startdate"]} {o["state"]} {o["title"]} {o["title_long"]} {o["website"]}\n')

with open('./Current-US-Representatives.json', 'r', encoding='utf-8') as file:
    data_rep = json.load(file)

with open('Current-US-Representatives.txt', 'w', encoding='utf-8') as file:
    for o in data_rep["objects"]:
        file.write(f'{o["caucus"]}')
        file.write(" [ ")
        for cn in o["congress_numbers"]:
            file.write(f'{cn} ')
        file.write("] ")
        file.write(f'{o["current"]} "{o["description"]}" {o["district"]} {o["enddate"]}')
        file.write(f' {o["extra"]} ')
        file.write(f'"{o["leadership_title"]}" {o["party"]} {o["district"]} {o["enddate"]}')
        file.write(f' [ {o["person"]["bioguideid"]} {o["person"]["birthday"]} {o["person"]["cspanid"]} {o["person"]["fediverse_webfinger"]} {o["person"]["firstname"]} {o["person"]["gender"]} {o["person"]["gender_label"]} {o["person"]["lastname"]} {o["person"]["link"]} {o["person"]["middlename"]} "{o["person"]["name"]}" {o["person"]["namemod"]} {o["person"]["nickname"]} {o["person"]["osid"]} {o["person"]["pvsid"]} "{o["person"]["sortname"]}" "{o["person"]["twitterid"]}" "{o["person"]["youtubeid"]}" ] ')
        file.write(f'{o["phone"]} {o["role_type"]} {o["role_type_label"]} {o["senator_class"]} {o["senator_rank"]} {o["startdate"]} {o["state"]} {o["title"]} {o["title_long"]} {o["website"]}\n')