class Song:
	def __init__(self,title ,artist_name,duration=0):
		self.title=title
		self.artist_name=artist_name
		self.duration=duration
class Album:
	def __init__(self,album_name,year,artist_name=None):
		self.album_name=album_name
		self.year=year
		if artist_name is None:
			artist_name=Artist('Varisous Artists')
		else:
			self.artist_name=artist_name
		self.track_list=[]
	def add_song(self,song,position=None):
		self.song=song
		if position is None:
			self.track_list.append(song)
		else:
			self.track_list.insert(position,song)

class Artist:
	def __init__(self,artist_name):
		self.artist_name=artist_name
		self.album_list=[]

	def add_album(self,album):
		self.album_list.append(album)

def fn_load_data():
	new_artist=None
	new_album=None
	artist_list=[]	
	with open('albums.txt','r') as all_data:
		for i in all_data:
			artist_data,album_data,year_data,song_data=tuple(i.strip('\n').split('\t'))
			#year_data=int(year_data)
			if new_artist is None:
				new_artist=Artist(artist_data)
			elif new_artist.artist_name!=artist_data:
				new_artist.add_album(album_data)
				#artist_list.append(new_artist.artist_name)
				new_artist=Artist(artist_data)
				new_album=None
			if new_album is None:
				new_album=Album(album_data,year_data,new_artist)
			elif new_album.album_name!=album_data:
				new_album.add_song(new_album)
				new_album=Album(album_data,year_data,new_artist)
			new_song=Song(song_data,new_artist)
			new_album.add_song(new_song)
			if new_artist:
				if new_album:
					new_artist.add_album(new_album)
				artist_list.append((new_artist.artist_name,new_album.album_name,year_data,new_song.title))
					#artist_list.append(new_artist)
		return artist_list
def fn_write_data(v_list):
	with open('checkfile.txt','w') as write_data:
		for k in v_list:
			write_data.write(f'{k[0]}\t{k[1]}\t{k[2]}\t{k[3]}\t \n')
			#print(k)
			


v_list=fn_load_data()
#print(v_list)
fn_write_data(v_list)