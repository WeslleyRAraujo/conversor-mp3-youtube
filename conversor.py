import youtube_dl
import sys
import os.path
from random import randint

def run():

    if len(sys.argv) > 1 and os.path.isfile('list.txt') and sys.argv[1] == '-file':
        # Open the list with the links
        file_list_txt = open('list.txt', 'r')
        file_list = file_list_txt.read()
        if(len(file_list) > 0):
            links = file_list.split("\n")
            file_list_txt.close()
            
            # Convert all links
            for link in links:
                color = randint(30, 70)
                print("\033[1;" + str(color) + "m" + "Link: " + link + "\033[0;0m")
                convert_mp3(link)
            # Delete the content of list.txt
            file_list_txt = open('list.txt', 'w')
            file_list_txt.seek(0)
            file_list_txt.close()
        else:
            print("Empty File!")
    else:
        video_url = input("please enter youtube video url:")
        convert_mp3(video_url)

def convert_mp3(video_link):
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_link,
        download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }],
        'outtmpl':'download/' + filename,
        'quiet': False
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))

if __name__=='__main__':
    run()
