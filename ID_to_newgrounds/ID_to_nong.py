import os
import bs4
import requests
import lxml
import re
import eyed3

try:
    input_path = input("Enter the location of songs file: ")
    path = os.chdir(input_path)
except:
    print("Error, invalid directory.\nSetting default to current working directory...\n---------\n\n")
path = os.getcwd()
files = os.listdir(path)

def filter(yn=0):
    songs = []
    for file in files:
        if '.mp3' not in file:
            continue
        else:
            songs.append(file)
    if yn == 1:
        print(f"SONGS ARE: {songs}")
    return(songs)

def extract_tags(soup):
    tags_element = soup.find('dd', class_='tags')
    
    if tags_element:
        tags = [a.text for a in tags_element.find_all('a')]
        return f"Tags: {', '.join(tags)}"
    else:
        return "No tags found"

def modify_comments(audiofile, new_comments):
    # Remove existing comments
    if audiofile.tag.frame_set.get("COMM"):
        del audiofile.tag.frame_set["COMM"]

    # Add new comment
    audiofile.tag.comments.set(text=new_comments)

def get_year(text_content):
    release_year_pattern = r'(\b\d{4}\b)'
    matches = re.findall(release_year_pattern, text_content)
    return (matches[0])

def main():
    X = 0
    once = 1
    songs = filter()
    for song in songs:
        X = X+1
        if Input == '1' and once == 1:
            print("\n\n---------\n\n")
            once += 1
        print(f"OPERATION {X} OUT OF {len(songs)}")
        num = song.replace('.mp3','')
        num = re.sub(r'\D', '', num)
        url = requests.get(f'https://www.newgrounds.com/audio/listen/{num}')
        soupurl = bs4.BeautifulSoup(url.text,'lxml')
        Oops = soupurl.select_one('.pod-head h2.error')
        if Oops:
            print('not found on newgrounds')
            cursong = eyed3.load(path+f'\\{song}')
            cursong.initTag()
            cursong.tag.title = f"not found (ID:{num})"
            cursong.tag.save()
            print(f"Error ID: {num}\n\n---------\n\n")
            continue
        try:
            title = soupurl.select('h2')[0].text
            Author = soupurl.select('h4')[0].text
            Genre = soupurl.select('dd')[7].text
            Date = soupurl.find('dt', text='Uploaded').find_next('dd').text
            year = get_year(Date)
            Tags = extract_tags(soupurl)
            cursong = eyed3.load(path+f'\\{song}')
            cursong.initTag()
            cursong.tag.title = f'{title} (ID:{num})'
            cursong.tag.artist = Author
            cursong.tag.genre = Genre
            cursong.tag.release_date = year
            modify_comments(cursong, Tags)
            cursong.tag.save()
            clean_title = title.replace('\n', '').strip()
            clean_num = num.replace('\n', '').strip()
            clean_Author = Author.replace('\n', '').strip()
            clean_Genre = Genre.replace('\n', '').strip()
            clean_year = year.replace('\n', '').strip()
            clean_Tags = Tags.replace('\n', '').strip()
            print(f"Title is: {clean_title}")
            print(f"ID is: {clean_num}")
            print(f"Author is: {clean_Author}")
            print(f"Genre is: {clean_Genre}")
            print(f"Release Year: {clean_year}")
            print(f"Tags are: {clean_Tags}")
            print("\n\n---------\n\n")
        except Exception as e:
            print("ERROR MODIFYING FILE\n")
            print(e)
            print("\n---------\n")
            continue

Input = input("Enter 1 if you want to know the files to be printed to be displayed first, ignore for otherwise: ")
try:
    songs = filter(int(Input))
except ValueError:
    pass
if Input == '1':
    confirm = input("Continue? (y/n): ")
    if confirm == 'y':
        main()
    else:
        pass
else:
    main()