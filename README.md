

## Convert all apk file into zip file in the folder

```bash
Get-ChildItem -Filter "*.apk" -File | ForEach-Object { Compress-Archive -Path $.FullName -DestinationPath "$($.BaseName).zip" 
```

## Convert all zip file into text file in the folder

```bash 
Get-ChildItem -Filter "*.zip" -File | ForEach-Object { python encode.py $_.Name -o "$($_.BaseName).txt" 
```

## Convert all txt file into zip file in the folder

```bash 
Get-ChildItem -Filter "*.txt" -File | ForEach-Object { python decode.py $_.Name -o "$($_.BaseName).zip" 
```
