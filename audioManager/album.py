class Album:
    #class constructor
    def __init__(self,id,title,genre,artist,price,year):
        self.id=id
        self.title=title
        self.genre=genre
        self.artist=artist
        self.price=price
        self.release_year=year
        self.song = []
    
    def __str__(self):
        #return "Im an album"
        return f"{self.id} - {self.title}"