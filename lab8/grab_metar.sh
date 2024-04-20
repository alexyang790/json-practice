#!bin/bash 

curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85" > aviation.json
jq '.' < aviation.json > formatted_avaiation.json

cat formatted_avaiation.json | jq -r .[].receiptTime | head -n 6
