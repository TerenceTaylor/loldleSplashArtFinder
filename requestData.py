import requests


championList = []

r = requests.get('http://ddragon.leagueoflegends.com/cdn/12.21.1/data/en_US/champion.json')


data = r.json()['data']

for key in data:
    championList.append(key)




for champ in championList:
    for x in range(0, 50):
        image = requests.get('https://ddragon.leagueoflegends.com/cdn/img/champion/splash/' + champ + '_' + str(x) + '.jpg')
        fileName = 'splashes/' + champ + '_' + str(x) + '.png'

        if image.status_code == 200:
            with open (fileName, 'wb') as f:
                f.write(image.content)

