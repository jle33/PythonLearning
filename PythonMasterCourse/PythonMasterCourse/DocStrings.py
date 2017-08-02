class Song: #docstrings - should be """ some string """ to keep it consistent with everyone's docStrings
    """Class to represent song
    Attributes:
        title(str): Title of song
        artist(Artist): An artist object representing the songs creator.
        duration(int): The duration of the song in seconds. Can be zero.
    """
    def __init__(self, title, artists, duration=0):
        """Song method
        Args:
            title (str): Initializes the 'title' attribute
            artists (Artist): A Artist object representing the song's creator.
            duration (Operational[int]): Initial value for the 'duration' attribute.
                Will default to zero if not specified.
        """
        self.title = title
        self.artists = artists
        self.duration = duration


if __name__ == '__main__':
    aString = "Hello\n New\t\t World" #Not everything is a string such as \n \t
    print(aString)
    rawString = r"Hello\n New\t\t World" #Putting a r before the "" will make everything a string including \n \t
    print(rawString)
    backSlash = "Hello \few World" #putting a backslash '\' before some letter will attempt to decode a unicode for a specific characater from ASCII
    print(backSlash)
    backSlash = "Hello \\few World" #Putting a backslash '\' before '\'  will allow a '\' to be shown 
    print(backSlash)