# Representation for th entire Industry.
# This has a list of Movies
# Where "" is another class
class Industry:
    def __init__(self, list_of_movies):
        self.list_of_movies = list_of_movies
      
      
    def __repr__(self):  
       return 'SILC(list_of_movies=%s)' % (self.list_of_movies)
    
    def __str__(self):  
       return 'SILC(list_of_movies=%s)' % (self.list_of_movies)
   
   
    # Returns the count of songs in all the movies    
    def count_songs(self): 
        # Loop through entire movies classes list
        # find the count of songs in each movie
        total_songs = 0
        for movie in self.list_of_movies:
            total_songs = movie.songs + total_songs

        #return the total
        return total_songs
               
            
# Representation for one movie
# This has a list of movies 
class Movie_class:
    def __init__(self, list_of_movies):
        self.list_of_movies = list_of_movies
   
    def __init__(self, lyricist, musicdirector, singer, songs):
        self.lyricist =lyricist
        self.musicdirector = musicdirector
        self.singer = singer
        self.songs =songs
  
    def __repr__(self):  

       return 'Movie_class(lyricist=%s, musicdirector=%s, singer=%s, songs=%s)' % (self.lyricist, self.musicdirector, self.singer ,self.songs)
    
      
       
# Representation for a Music Director      
class Music_Director:
    def __init__(self, moviename, songs_composed):
        self.name = moviename
        self.songs_composed = songs_composed
  
    def __repr__(self):  
       return 'Music_Director(moviename=%s, , songs_composed=%s)' % (self.moviename,  self.songs_composed)
    
    def __str__(self):  
       return 'Music_Director(moviename=%s, songs_composed=%s)' % (self.moviename,  self.songs_composed)

# Representation for Lysricist 
# A Lyricist has a movie name, no of songs wrote 
  
class Lyricist:
    def __init__(self, moviename, songs_wrote):
        self.moviename = moviename
        self.songs_wrote = songs_wrote
  
    def __repr__(self):  
       return 'Student(moviename=%s, songs_wrote=%s)' % (self.moviename, self.songs_wrote)
    
    def __str__(self):   
       return 'Student(moviename=%s, songs_wrote=%s)' % (self.moviename, self.songs_wrote)
    
       
# Representation for Singer 
# A Singer has a movie name, no of songs sang 
  
class Singer:
    def __init__(self, moviename, songs_sang):
        self.moviename = moviename
        self.songs_sang = songs_sang
  
    def __repr__(self):  
       return 'Student(moviename=%s, songs_sang=%s)' % (self.moviename, self.songs_sang)
    
    def __str__(self):   
       return 'Student(moviename=%s, songs_sang=%s)' % (self.moviename, self.songs_sang)
    
    
    
#-----------------------------
# all the test data (classes and objects) are created here
#-----------------------------
       
#create an instance of singer
singer_1 = Singer("Coco",  3)


#create an instance of singer
singer_1 = Singer("Home",  3)


       
#create an instance of Lyricist
lyricist_1 = Lyricist("Coco",  5)


#create an instance of Lyricist
lyricist_2 = Lyricist("Home",  3)


#create an instance of MusicDirector
musicdirector_1 = Music_Director("LionKing",  5)


#create an instance of MusicDirector
musicdirector_2 = Music_Director("Minnions",  3)



#create an instance of movie1
Lionking = Movie_class("lyricist_1", "musicdirector_1", "singer_1" ,5)


#create an instance of Movie2
Minnions = Movie_class("lyricist_2", "musicdirector_2" ,"singer_2", 5)

#create an instance of movie3
Coco = Movie_class("lyricist_1", "musicdirector_1", "singer_1" ,2)


#create an instance of Movie4
Home = Movie_class("lyricist_2", "musicdirector_2" ,"singer_2", 4)

#Create the entire Movie Industry in 2021
# which is consisting of several movies Classes
list_of_movies  =[Lionking, Minnions, Coco,  Home]
industry_2021 = Industry(list_of_movies)
# print(industry_2021)

# Now get the total count of the students in all CS Classes at SILC

total_count_of_songs = industry_2021.count_songs()
print("Entire industry --> ", Industry)
print("Total Count of Songs in movies", total_count_of_songs)

