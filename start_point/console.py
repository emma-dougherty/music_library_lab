import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist('Radiohead')
saved_artist = artist_repository.save(artist1)
artist2 = Artist('Prince')
saved_artist = artist_repository.save(artist2)

album1 = Album('In Rainbows', 'rock', artist1)
album_repository.save(album1)

album2 = Album('Purple Rain', 'rock', artist2)
album_repository.save(album2)