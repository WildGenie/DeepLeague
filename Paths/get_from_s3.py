import requests


for i in range(393):
    response = requests.get(
        f'https://s3.amazonaws.com/esports-anal/6789/img_{str(i)}_champ_1.png',
        stream=True,
    ).content

    with open(f'frames/{str(i)}.jpg', 'wb') as handler:
        handler.write(response)
