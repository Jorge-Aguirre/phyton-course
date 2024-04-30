def make_album(artist, title):
    album = {'artist': artist.title(), 'title': title.title()}
    return album

while True:
    print("\nPlease enter album's information:")
    print("(enter 'q' at any time to quit)")

    f_artist = input("Artist's Name: ")
    if f_artist == 'q':
        break

    f_title = input("Album's Title: ")
    if f_title == 'q':
        break

    album = make_album(f_artist, f_title)
    print(f"Album's information: {album}")