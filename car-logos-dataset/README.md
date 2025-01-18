# car-logos-dataset
[car-logos-dataset](https://github.com/filippofilip95/car-logos-dataset) is a collection of 383 car logos images with few variations of sizes and JSON file for better usability.

Only the JSON file are processed by `preProcess.py` in this repo in order to construct TXT files. To be specific, each JSON object is formatted as a single-line record in TXT files. `car-logos-dataset.txt` is the excerpted version of `car-logos-dataset.full.txt`.
e.g.   
Original data:
```json
{
    "name": "ABT",
    "slug": "abt",
    "image": {
      "source": "https://www.carlogos.org/logo/ABT-Sportsline-logo-silver-640x250.jpg",
      "thumb": "https://raw.githubusercontent.com/filippofilip95/car-logos-dataset/master/logos/thumb/abt.png",
      "optimized": "https://raw.githubusercontent.com/filippofilip95/car-logos-dataset/master/logos/optimized/abt.png",
      "original": "https://raw.githubusercontent.com/filippofilip95/car-logos-dataset/master/logos/original/abt.jpg",
      "localThumb": "./thumb/abt.png",
      "localOptimized": "./optimized/abt.png",
      "localOriginal": "./original/abt.jpg"
    }
}
```
After processing:
```
ABT abt { https://www.carlogos.org/logo/ABT-Sportsline-logo-silver-640x250.jpg https://raw.githubusercontent.com/filippofilip95/car-logos-dataset/master/logos/thumb/abt.png https://raw.githubusercontent.com/filippofilip95/car-logos-dataset/master/logos/optimized/abt.png https://raw.githubusercontent.com/filippofilip95/car-logos-dataset/master/logos/original/abt.jpg ./thumb/abt.png ./optimized/abt.png ./original/abt.jpg }
```