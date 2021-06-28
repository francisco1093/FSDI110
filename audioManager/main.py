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
import pickle
#Globals
catalog=[]

#Functions

def serialize_data():
    try:
        writter=open("songManager.data","wb") #write binary
        pickle.dump(catalog,writter)
        writter.close()
        print("**Data saved!")
    except:
        print()

def deserialize_data():
    try:
        reader:open("songManager.data","rb")#read binary
        temp_list=pickle.load(reader)
        reader.close()
        for item in temp_list:
            catalog.append(item)
        print(f"Loaded {len(catalog)}")
    except:
        print("**Error: No datas was loaded!")




def register_song():
    print_catalog(False)
    
    id=int(input("Please select an Id: "))
    print_header("Register a song")
    found = False
    for album in catalog:
        if(album.id ==id):
            found=True
            print_header("register a song to "+album.title)
            title = input("Provide the Title: ")
            lenSec = input("Provide the Length: ")
            author = input("Provide the author: ")

            id=1
            if(len(album.song)>0):
                id=album.song[-1].id+1

            song = Song(id,title,lenSec,author)
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

def print_catalog(show_songs):
    print_header("Your current catalog")
    for album in catalog:
        print(album)

    if(show_songs):
        print("-"*30)
        id = input("Select an Album to see its songs, or [x] to close")
        if(id =="x"):return

        try:
            the_id = int(id)
            found = False
            for album in catalog:
                if(album.id ==the_id):
                    found=True
                    print_header("Songs of the Album: "+ album.title)
                    for song in album.song:
                        print(song)
                    return album
            
            if(not found):
                print("**Error: Invalid Id, try again!")

        except:
            print("Error")
        






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


def delete_song():
    album =print_catalog(True)
    print("-"*30)
    id = input("Select the Id of the song to delete: ")

    found = False
    for song in album:
      if(song.id == id):
            found=True
            album.song.remove(song)
            print(" Song Removed!")
           
def delete_album():
    print_catalog(False)
    print("-"*30)
    id = input("Select the Id of the Album to delete: ")
    the_id = int(id)
    found = False
    for album in catalog:
        if(album.id ==the_id):
            found=True
            if(len(album.song)<1):
                catalog.remove(album)
                print("Album removed")
            else:
                print("Error album not empty")


def most_expensive():
    max_price=0
    maxTitle=""
    for album in catalog:
        if(album.price >max_price):
            max_price=album.price
            maxTitle=album.title
    print("Most expensive album "+maxTitle)

def get_categories():
    categories=[]
    for album in catalog:
        categories.append(album.genre)

    categories=list(dict.fromkeys(categories))
    print_header("Genres:")
    print(*categories, sep = "\n")




deserialize_data()
option=""
while(option!="q"):
    clear()
    print_menu()
    option=input("Please select an option: ")

    if(option=="q"):
        break
    if(option=="1"):
        register_album()
        serialize_data()

    if(option=="2"):
        register_song()
        serialize_data()

    if(option=="3"):
        print_catalog(True)

    if(option=="4"):
        count_all_songs()
    
    if(option=="5"):
        total_price()
    
    if(option=="7"):
        delete_song()
        serialize_data()

    if(option=="6"):
        delete_album()
        serialize_data()
    
    
    if(option=="8"):
        most_expensive()
    
    
    if(option=="9"):
        get_categories()

    input("Press Enter to continue...")
