from scraper import ChromeDriver
from arabic_reshaper import reshape

SHORTS_LINK = 'https://www.youtube.com/shorts/'

num_suffixes = {'K': 1000, 'M': 1000000, 'B': 1000000000}

def to_num(str):
    try:
        return int(str)
    except ValueError:
        return int(float(str[:len(str) - 1]) * num_suffixes[str[-1]])

driver = ChromeDriver()

unique_links = []

driver.get('https://www.viewstats.com/top-list?filterBy=subs&interval=ms_weekly&madeForKids=true&movies=true&musicChannels=true&tab=channels')

driver.cooldown(3)

names = driver.finds_selector('div.vs-channel-name')
ids = driver.finds_selector('div.vs-channel-id')

names = [f'{names[n].text} ({ids[n].text})' for n in range(len(names))]

new_subs = driver.finds_selector('div.vs-item.vs-item--green > div')
new_subs = [to_num(new_sub.text.replace(',', '')) for new_sub in new_subs]

total_subs = driver.finds_selector('div > div:nth-child(4).vs-item')[1:]
total_subs = [to_num(total_sub.text.replace(',', '')) for total_sub in total_subs]

total_views = driver.finds_selector('div > div:nth-child(5).vs-item')[1:]
total_views = [to_num(total_view.text.replace(',', '')) for total_view in total_views]

channels = [
    {
        'name': reshape(names[n]),
        'new_subs': new_subs[n],
        'total_subs': total_subs[n],
        'total_views': total_views[n]
    } for n in range(len(names))
]

with open('channels.csv', 'w') as file:
    file.write('channel,new_subs,total_subs,total_views\n')

with open('channels.csv', 'a') as file:
    for channel in channels:
        print(channels.index(channel) + 1, channel["name"])
        file.write(f'{channel["name"]},{channel["new_subs"]},{channel["total_subs"]},{channel["total_views"]}\n')

driver.quit()