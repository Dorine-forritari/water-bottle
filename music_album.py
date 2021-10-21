'''
Write a class called `MusicAlbum` that has the attributes: 'band', 'title' and 'year'.
It has a constructor with 3 parameters. 
By deafult the band name should be "unknown band", title by default should be "unknown" and the year should be "unknown year" by default.

The class has only 2 methods (excluding __init__)
* __str__ : function that returns the following string "Album {name of album} by {name of band}, released in {year released}."
* set_album(band, title, year) : function that overwrites attributes in the class. If a field is not supplied in the parameter, 
the default is the same as in the constructor.

Note: It can happen that you might have to overwrite existing data with a default value, when calling set_album.
'''


class MusicAlbum:
    def __init__(self, band = 'unknown band', title = 'unknown', year = 'unknown year'):
        self.band = band
        self.title = title
        self.year = year

    def __str__(self):
        return f"Album {self.title} by {self.band}, released in {self.year}."

    def set_album(self, band = 'unknown band', title = 'unknown', year = 'unknown year'):
        self.band = band
        self.title = title
        self.year = year
        

