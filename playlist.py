# a Playlist class that supports len(playlist) 
class Playlist:
    def __init__(self, songs):
        self.songs = songs
    def __len__(self):
        return len(self.songs)

p1 = Playlist(["Song A", "Song B", "Song C", "Song D"])
print("Total songs:", len(p1))