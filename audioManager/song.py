class Song:
    #class constructor
    def __init__(self,id, title, len_sec,author):
        self.id=id
        self.title=title
        self.len_sec=len_sec
        self.author=author
    
    def __str__(self):
        #return "Im an album"
        return f"{self.id} - {self.title} -{self.len_sec}secs"