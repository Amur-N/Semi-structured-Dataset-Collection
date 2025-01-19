# govtrack
[govtrack](https://www.govtrack.us/) is a website providing APIs for tracking legislation and votes in the United States Congress.

This repo only includes parts of its original files and may not be the latest data.     
`Current-US-Representatives.json` and `Current-US-Senators.json` are fetched by [senator](https://www.govtrack.us/api/v2/role?current=true&role_type=senator) and [representative](https://www.govtrack.us/api/v2/role?current=true&role_type=representative) respectively. `preProcess.py` transforms the `objects` list of JSON files into the corresponding TXT files. `US-Rep-1.txt`, `US-Rep-2.txt` and `US-Sen.txt` are excerpted versions of those TXT files.  
e.g.  
Original data:
```json
{
    "caucus": null,
    "congress_numbers": [
        116,
        117,
        118
    ],
    "current": true,
    "description": "Junior Senator for Washington",
    "district": null,
    "enddate": "2025-01-03",
    "extra": {
        "address": "511 Hart Senate Office Building Washington DC 20510",
        "contact_form": "https://www.cantwell.senate.gov/public/index.cfm/email-maria",
        "office": "511 Hart Senate Office Building",
        "rss_url": "http://www.cantwell.senate.gov/public/index.cfm/rss/feed"
    },
    "leadership_title": null,
    "party": "Democrat",
    "person": {
        "bioguideid": "C000127",
        "birthday": "1958-10-13",
        "cspanid": 26137,
        "fediverse_webfinger": null,
        "firstname": "Maria",
        "gender": "female",
        "gender_label": "Female",
        "lastname": "Cantwell",
        "link": "https://www.govtrack.us/congress/members/maria_cantwell/300018",
        "middlename": "",
        "name": "Sen. Maria Cantwell [D-WA]",
        "namemod": "",
        "nickname": "",
        "osid": "N00007836",
        "pvsid": null,
        "sortname": "Cantwell, Maria (Sen.) [D-WA]",
        "twitterid": "SenatorCantwell",
        "youtubeid": "SenatorCantwell"
    },
    "phone": "202-224-3441",
    "role_type": "senator",
    "role_type_label": "Senator",
    "senator_class": "class1",
    "senator_class_label": "Class 1",
    "senator_rank": "junior",
    "senator_rank_label": "Junior",
    "startdate": "2019-01-03",
    "state": "WA",
    "title": "Sen.",
    "title_long": "Senator",
    "website": "https://www.cantwell.senate.gov"
}
```
After processing:
```
None [ 116 117 118 ] True "Junior Senator for Washington" None 2025-01-03 {'address': '511 Hart Senate Office Building Washington DC 20510', 'contact_form': 'https://www.cantwell.senate.gov/public/index.cfm/email-maria', 'office': '511 Hart Senate Office Building', 'rss_url': 'http://www.cantwell.senate.gov/public/index.cfm/rss/feed'} "None" Democrat None 2025-01-03 [ C000127 1958-10-13 26137 None Maria female Female Cantwell https://www.govtrack.us/congress/members/maria_cantwell/300018  "Sen. Maria Cantwell [D-WA]"   N00007836 None "Cantwell, Maria (Sen.) [D-WA]" "SenatorCantwell" "SenatorCantwell" ] 202-224-3441 senator Senator class1 "Class 1" junior Junior 2019-01-03 WA Sen. Senator https://www.cantwell.senate.gov
```