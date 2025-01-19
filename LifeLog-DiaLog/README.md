# LifeLog-Dialog
[LifeLog-Dialog](https://github.com/ntunlplab/Lifelog-DiaLog) is a lifelog dataset for life event detection from daily dialog.

Every single object in `DiaLog.json` is formatted as a line in `DiaLog.txt` by `preProcess.py`.  
e.g.   
Original data:
```json
{
    "dialog_id": 6,
    "turns": 4,
    "events": [
        {
            "S1": [],
            "S2": []
        },
        {
            "S1": [],
            "S2": [
                "Perception_experience",
                "Request"
            ]
        },
        {
            "S1": [],
            "S2": []
        },
        {
            "S1": [],
            "S2": []
        }
    ]
}
```
After processing:
```
6 4 events:{ [{ }{ }] [{ }{ Perception_experience Request }] [{ }{ }] [{ }{ }] }
```