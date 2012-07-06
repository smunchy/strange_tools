__author__ = 'sean'

# sax is built in to python.
import xml.sax

# xml.sax.ContentHandler is built into Python.
#
class MovieHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.CurrentData = " "
        self.type = " "
        self.format = " "
        self.year = " "
        self.rating = " "
        self.stars = " "
        self.description = " "

    # call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        # movie must be in quotes " " because it is the name of the main tag in the xml.
        if tag == "movie":
            print " ****MOVIE**** "
            title = attributes["title"]
            print "Title:", title


    # Call when an elements ends
    # tag must be in endElement() as a parameter.
    # Otherwise it will state that it's been given two arguments when only one parameter is there.
    def endElement(self, tag):
        if self.CurrentData == "type":
            print "Type:", self.type

        elif self.CurrentData == "format":
            print "Format:", self.format

        elif self.CurrentData == "year":
            print "Year:", self.year

        elif self.CurrentData == "rating":
            print "Rating:", self.rating

        elif self.CurrentData == "stars":
            print "Stars:", self.stars

        elif self.CurrentData == "description":
            print "Description:", self.description

        self.CurrentData = ""

    # Call when a character is ready
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content

        elif self.CurrentData == "format":
            self.format = content

        elif self.CurrentData == "year":
            self.year = content

        elif self.CurrentData == "rating":
            self.rating = content

        elif self.CurrentData == "stars":
            self.stars = content

        elif self.CurrentData == "description":
            self.description = content

# if __name__ == "__main__" means that this entire module can be a stand a lone program or reusable, when in Python.
if __name__ == "__main__":

    # create a xml reader
    # This is made into an attribute later on, down the lines.
    parser = xml.sax.make_parser()

    # turn off names spaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    # This is calling the whole class of MovieHandler.
    # It's then being passed into the parsing parse.
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse("movies.xml")