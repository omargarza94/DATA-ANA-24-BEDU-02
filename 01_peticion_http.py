import requests

BASE_URL = "https://s3.us-west-1.amazonaws.com/galileoguzman.com/data/Ejemplo_01_Laptops_Dataset.csv"

def downloader_data():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print('The server has responded XD')
        response_content = response.content
        filename = 'tmp/Ejemplo_01_Laptops_Dataset.csv'
        print(filename)
        with open(filename, 'wb') as file:
            file.write(response_content)
            print('File saved with success')
    else:
        print('Server unreachable :(')


downloader_data()