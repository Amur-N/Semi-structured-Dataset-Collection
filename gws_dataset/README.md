# gws_dataset
[gws_dataset](https://github.com/invictus-ir/gws_dataset) are Google Workspace Audit logs containing several attacks.

All TXT files are processed from corresponding JSON files by `preProcess.py`. To be specific, each object in the list `activities` of the JSON file is formatted as a multiline record.
e.g.   
Original data:
```json
{"kind": "admin#reports#activity", "id": {"time": "2022-08-15T16:24:44.109Z", "uniqueQualifier": "5523217719890872442", "applicationName": "admin", "customerId": "C00mpaiwz"}, "etag": "\"_ZVRqe-BUDYcYeOIPo-gm6Eh1QaGne4ACjHHI6qsr6A/EYtS4krKgXYuDxHeQI0XKvr-hBw\"", "actor": {"callerType": "USER", "email": "admin@cloud-response.com", "profileId": "111440584475724055600"}, "ipAddress": "209.94.244.98", "events": [{"type": "SECURITY_INVESTIGATION", "name": "SECURITY_INVESTIGATION_QUERY", "parameters": [{"name": "INVESTIGATION_DATA_SOURCE", "value": "ADMIN LOG EVENTS"}, {"name": "INVESTIGATION_QUERY", "value": "(empty)"}]}]}
```
After processing:
```
{
admin#reports#activity { 2022-08-15T16:24:44.109Z 5523217719890872442 admin C00mpaiwz } "_ZVRqe-BUDYcYeOIPo-gm6Eh1QaGne4ACjHHI6qsr6A/EYtS4krKgXYuDxHeQI0XKvr-hBw" { USER admin@cloud-response.com 111440584475724055600 } 209.94.244.98
	{
	SECURITY_INVESTIGATION SECURITY_INVESTIGATION_QUERY
		{ INVESTIGATION_DATA_SOURCE ADMIN LOG EVENTS }
		{ INVESTIGATION_QUERY (empty) }
	}
}
```