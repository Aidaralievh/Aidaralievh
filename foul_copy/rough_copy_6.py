'name_link': i.find('div', class_='shortstroyHead').find('a').get('href'),
'ani_img': i.find('div', class_='shortstoryContent').find('img').get('src'),
"short_story": i.find("div", id_="shortstoryContent").get_text(strip=True),