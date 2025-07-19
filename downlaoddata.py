import requests

url="https://raw.githubusercontent.com/freeCodeCamp/boilerplate-medical-data-visualizer/main/medical_examination.csv"
response=requests.get(url)
if response.status_code == 200:
    with open("medical_examination.csv",'w',encoding='utf-8')as file:
        file.write(response.text)
        print("Data has been downloaded successfully")
else:
    print(f"Failed to download:status_code={response.status_code}")