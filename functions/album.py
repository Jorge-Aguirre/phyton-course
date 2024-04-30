def make_album(artist, title, number_of_songs=None):
    album = {'artist': artist.title(), 'title': title.title()}
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album

print(make_album('nirvana', 'nevermind'))
print(make_album('shakira', 'sale el sol', 13))
print(make_album('tiesto', 'drive'))