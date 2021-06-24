"""
App: Audio Manager
Author: Francisco Cardenas
Functionality:
    -Register Albums
    -Register Songd
    -Display Catalog
"""
#imports
from display import print_menu, clear, print_header
from album import Album
from song import Song
#Globals
catalog=[]

#Functions



def register_song():
    print_catalog()
    
    id=int(input("Please select an Id: "))
    print_header("Register a song")
    found = False
    for album in catalog:
        if(album.id ==id):
            found=True
            print_header("register a song to "+album.title)
            title = input("Provide the Title: ")
            len = input("Provide the Length: ")
            author = input("Provide the author: ")
            song = Song(1,title,len,author)
            album.song.append(song)


    if(not found):
        print("**Error: Invalid Id, try again!")
    





def register_album():
    print_header("Register_album")

    title = input("Provide the Title: ")
    genre = input("Provide the Genre: ")
    artist = input("Provide the Artist Name: ")
    price = float(input("Provide the Price: "))
    release_year = int(input("Provide the Release Year: "))

    id=1
    if(len(catalog)>0):
        last = catalog[-1]
        id=last.id+1

    album = Album(id,title,genre,artist,price,release_year)
    print(album)

    catalog.append(album)
    print("Album Saved!")

def print_catalog():
    print_header("Your current catalog")
    for album in catalog:
        print(album)


def count_all_songs():
    count=0
    for album in catalog:
        count=count+len(album.song)
    print(f"Total Songs in the system {count}")

def total_price():
    total_price=0
    for album in catalog:
            total_price=total_price+album.price
    print(f"Total $ in the catalog {total_price}")



option=""
while(option!="q"):
    clear()
    print_menu()
    option=input("Please select an option: ")

    if(option=="q"):
        break
    if(option=="1"):
        register_album()

    if(option=="2"):
        register_song()

    if(option=="3"):
        print_catalog()

    if(option=="4"):
        count_all_songs()
    
    if(option=="5"):
        total_price()

    input("Press Enter to continue...")
