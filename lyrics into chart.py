## lyrics

''' Ah, ba ba ba ba Barbara Ann Ba ba ba ba Barbara Ann Oh Barbara Ann take my hand Barbara Ann
You got me rockin' and a-rollin'
Rockin' and a-reelin'
Barbara Ann ba ba
Ba Barbara Ann
 
...more lyrics...
 
Ba ba ba ba Barbara Ann
Ba ba ba ba Barbara Ann

# now in a variable format

"Ah, ba ba ba ba Barbara Ann
Ba ba ba ba Barbara Ann
 
Oh Barbara Ann take my hand
Barbara Ann
You got me rockin' and a-rollin'
Rockin' and a-reelin'
Barbara Ann ba ba
Ba Barbara Ann
 
...more lyrics...
 
Ba ba ba ba Barbara Ann
Ba ba ba ba Barbara Ann'''


# now in a variable format
                          
lyrics = "Ah, Ba Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann Oh Barbara Ann Take My Hand Barbara Ann You Got Me Rockin' And A-Rollin' Rockin' And A-Reelin' Barbara Ann Ba Ba Ba Barbara Ann ...More Lyrics... Ba Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann"


# then we split in a list of words

list_of_lyrics = lyrics.split(' ')
print (list_of_lyrics)
['Ah,', 'Ba', 'Ba', 'Ba', 'Ba', 'Barbara', 'Ann', 'Ba', 'Ba', 'Ba', 'Ba', 'Barbara', 'Ann', 'Oh', 'Barbara', 'Ann', 'Take', 'My', 'Hand', 'Barbara', 'Ann', 'You', 'Got', 'Me', "Rockin'", 'And', "A-Rollin'", "Rockin'", 'And', "A-Reelin'", 'Barbara', 'Ann', 'Ba', 'Ba', 'Ba', 'Barbara', 'Ann', '...More', 'Lyrics...', 'Ba', 'Ba', 'Ba', 'Ba', 'Barbara', 'Ann', 'Ba', 'Ba', 'Ba', 'Ba', 'Barbara', 'Ann']


print (len(list_of_lyrics))
51


# we know count consider only words, not occurence, with set()

unique_words=set(list_of_lyrics)
print (unique_words)
print (len(unique_words))
17

# now we create a dictionaries {word:occurence} using dict.fromkeys() 

word_histogram = dict.fromkeys(unique_words, 0)
print (word_histogram)
{'...More': 0, "A-Reelin'": 0, "A-Rollin'": 0, 'Ah,': 0, 'And': 0, 'Ann': 0, 'Ba': 0, 'Barbara': 0, 'Got': 0, 'Hand': 0, 'Lyrics...': 0, 'Me': 0, 'My': 0, 'Oh': 0, "Rockin'": 0, 'Take': 0, 'You': 0}


# with a loop, we polulate the dictionarie from the list

word_histogram = dict.fromkeys(unique_words, 0)
for word in list_of_lyrics:
    word_histogram[word] = word_histogram[word]+ 1 
print (word_histogram)
{'Ann': 8, 'Lyrics...': 1, 'You': 1, "Rockin'": 2, 'And': 2, 'Me': 1, 'Ba': 19, 'Barbara': 8, '...More': 1, 'Hand': 1, "A-Rollin'": 1, "A-Reelin'": 1, 'Take': 1, 'Got': 1, 'Ah,': 1, 'Oh': 1, 'My': 1}


# now we visualize the data

import plotly
from plotly.offline import iplot, init_notebook_mode
from plotly import tools
import plotly.graph_objs as go
init_notebook_mode(connected=True)
 
trace = {'type': 'bar', 'x': list(unique_words), 'y': list(word_histogram.values())}
 
plotly.offline.iplot({'data': [trace]})