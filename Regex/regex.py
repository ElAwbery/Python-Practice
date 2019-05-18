"""
Created on Thu May 16 13:19:12 2019

@author: ElAwbery
"""
'''
All of the exercises in this file are taken from https://www.pirogram.com
The pirogram site has explanations, a walk-through and interactive tests.
'''
# SEction 1, Regex introduction
import re

regex_pattern = r"Sq" # r marks the string as 'raw string mode' 

a=re.search(regex_pattern, "Squirtle"),
b=re.search(regex_pattern, "Squiffy"),
c=re.search(regex_pattern, "pppoo/&sssSquirtle...mrp"),
d=re.search(regex_pattern, ""),
e=re.search(regex_pattern, "quirtle"),
f=re.search(regex_pattern, "0192746"),
g=re.search(regex_pattern, "packsquit"),
h=re.search(regex_pattern, "'Squirtle'")
i=re.search(regex_pattern, "Sooquirtlfare"),
j=re.search(regex_pattern, "ArthurqS"),
k=re.search(regex_pattern, "))"),
l=re.search(regex_pattern, "__"),
m=re.search(regex_pattern, "SquirtleSquirtleSquirtle")

pattern_list=[a, b, c, d, e, f, g, h, i, j, k, l, m]

# when the pattern is found, re.search returns the pattern object
# when the pattern is not found, re.search returns None
for pattern in pattern_list:
   print(pattern)

#Section 2, matching characters
# if you want to avoid matches to strings in quotes, use special characters
   
def has_dot(movie_name):
   if re.search("\.", movie_name)==None:
        return False
   else:
        return True

assert has_dot('Mr. Pip') == True
assert has_dot('The D.I.') == True
assert has_dot('Stardust') == False
assert has_dot('Superman') == False

'''
Write a function match_movie_name that takes a movie name as input. 
If the movie name has at least one 4 letter word in the middle of movie name, 
it returns True. Otherwise, it returns False.
'''
REGEX = r" [A-Z|a-z][A-Z|a-z][A-Z|a-z][A-Z|a-z] "

def match_movie_name(movie_name):
    if re.search(REGEX, movie_name)==None:
        return False
    else:
        return True

assert match_movie_name('Gone With The Wind') == True
assert match_movie_name('Star Wars: The Last Jedi') == True
assert match_movie_name('2010: the year we make contact') == True
assert match_movie_name('Superman') == False

'''
Write a function match_movie_name that takes a movie name as input. 
If the movie name has a number within a single word, return True. 
Otherwise, return False.
'''
REGEX = r"[A-Z|a-z][0-9][A-Z|a-z]"

def match_movie_name(movie_name):
    if re.search(REGEX, movie_name)==None:
        return False
    else:
        return True    

assert match_movie_name('Se7en') == True
assert match_movie_name('Thr3e') == True
assert match_movie_name('E=mc2') == False
assert match_movie_name('2001: A Space Odyssey') == False
assert match_movie_name('Superman') == False 

'''
Write a function bat_cat_rat which takes a movie name as input. 
If the movie name has any of the bat, cat or rat words, return True. 
Otherwise, return False.
'''    
REGEX = r"[b|c|r|B|C|R]at"

def bat_cat_rat(movie_name):
    if re.search(REGEX, movie_name)==None:
        return False
    else:
        return True        
    
assert bat_cat_rat('Bat Whispers') == True
assert bat_cat_rat('Cat and Dog') == True
assert bat_cat_rat('King Rat') == True
assert bat_cat_rat('The Ghosts') == False    
    
'''
Write a function match_movie_name that takes a movie name as input. 
It returns True if the movie has at least 8 characters in the name. 
Otherwise, it returns False.
'''    
REGEX = r"........"

def match_movie_name(movie_name):    
    if re.search(REGEX, movie_name)==None:
        return False
    else:
        return True  
    
assert match_movie_name('Se7en') == False
assert match_movie_name('Thr3e') == False
assert match_movie_name('E=mc2') == False
assert match_movie_name('2001: A Space Odyssey') == True
assert match_movie_name('Superman') == True
    
'''
Write a function match_movie_name that takes a movie name as input. 
It returns True if the movie has a word which is at least 4 letter long 
followed by another word which is at least 3 letter long. 
Otherwise, it returns False.
'''    
REGEX = r"\w\w\w\w\s\w\w\w"

def match_movie_name(movie_name):
    if re.search(REGEX, movie_name)==None:
        return False
    else:
        return True

assert match_movie_name('Bat Whispers') == False
assert match_movie_name('Cat and Dog') == False
assert match_movie_name('King Rat') == True
assert match_movie_name('The Ghosts') == False
    
'''
Write a function match_movie_name that takes a movie name as input. 
It returns True if the movie has a word which is at least 4 letter long 
followed by another word which is at least 3 letter long or vice versa 
(i.e. a 3 letter long word is followed by a 4 letter long word). 
Otherwise, it returns False.
'''    
    
REGEX=r"\w\w\w\s\w\w\w\w|\w\w\w\w\s\w\w\w"  
 
def match_movie_name(movie_name):
    if re.search(REGEX, movie_name)==None:
        return False
    else:
        return True

assert match_movie_name('Bat Whispers') == True
assert match_movie_name('Cat and Dog') == False
assert match_movie_name('King Rat') == True
assert match_movie_name('The Ghosts') == True    
    
'''
Write a function match_movie_name that takes a movie name as input. 
It returns True if the movie has a number surrounded by one letter on each side. 
Otherwise, it returns False.
'''      
REGEX=r"\D\d\D"  
  
def match_movie_name(movie_name):
    if re.search(REGEX, movie_name)==None:
        return False
    else:
        return True    

assert match_movie_name('Se7en') == True
assert match_movie_name('Thr3e') == True
assert match_movie_name('E=mc2') == False
assert match_movie_name('2001: A Space Odyssey') == False
assert match_movie_name('Superman') == False

'''
Write a function match_movie_name that takes a movie name as input. 
It returns True if the movie has two consecutive non-word letters (Hint: use \W). 
Otherwise, it returns False.
'''
REGEX=r"\W\W"   
 
def match_movie_name(movie_name):
    if re.search(REGEX, movie_name)==None:
        return False
    else:
        return True 

assert match_movie_name('Star Wars: Return of the Jedi') == True
assert match_movie_name('Star Trek: Voyager') == True
assert match_movie_name('Erkan & Stefan 2') == True
assert match_movie_name('Cat And Dog') == False
assert match_movie_name('Alice in Wonderland') == False

# Section 3, matching repetitions
# syntax to say precisely how many times a match should occur

REGEX=r"[\w|\s]{12}"

def match_movie_name(movie_name):
    if re.search(REGEX, movie_name)==None:
        return False
    else:
        return True 
    
assert match_movie_name('Se7en') == False
assert match_movie_name('Superman') == False
assert match_movie_name('Spiderman Returns') == True
assert match_movie_name('2001: A Space Odyssey') == True
assert match_movie_name('Star Wars: Return of the Jedi') == True

REGEX=r"-\d{1,3}|\d{1,3}"

def match_number(s):
    if re.search(REGEX, s)==None:
        return False
    else:
        return True
    
assert match_number('-733') == True
assert match_number('4') == True
assert match_number('3') == True
assert match_number('AB') == False
assert match_number('DEF') == False

'''
Write a function match_number that takes a string as input. 
It returns True if the string matches numbers -999 to 999. 
The positive numbers could be prefixed with + (e.g. 97 and +97 are valid). 
Otherwise, it returns False. So, it should match -999, -998, …, 998, 999. 
Use the {m,n} convention to specify occurrences. Hint: in this case, [+-] 
have 0 to 1 occurrence and \d has 1 to 3
'''
REGEX=r"[+-]{0,1}\d{1,3}"

def match_number(s):
    if re.search(REGEX, s)==None:
        return False
    else:
        return True
assert match_number('-733') == True
assert match_number('4') == True
assert match_number('3') == True
assert match_number('+42') == True
assert match_number('AB') == False
assert match_number('DEF') == False

'''
Write a function match_movie_name that takes a movie name as input. 
It returns True if the movie has a word which is at least 4 letter long 
followed by another word which is at least 3 letter long. 
Otherwise, it returns False.
'''
REGEX=r"\w{4}\s\w{3}"

def match_movie_name(movie_name):
    if re.search(REGEX, movie_name)==None:
        return False
    else:
        return True 

assert match_movie_name('Bat Whispers') == False
assert match_movie_name('Cat and Dog') == False
assert match_movie_name('King Rat') == True
assert match_movie_name('The Ghosts') == False

'''
Write a function match_movie_name that takes a movie name as input. 
It returns True if the movie has a word which is at least 4 letter long 
followed by another word which is at least 3 letter long or vice versa 
(i.e. a 3 letter long word is followed by a 4 letter long word). 
Otherwise, it returns False.
'''
REGEX=r"\w{3}\s\w{4}|\w{4}\s\w{3}"

def match_movie_name(movie_name):
    if re.search(REGEX, movie_name)==None:
        return False
    else:
        return True

assert match_movie_name('Bat Whispers') == True
assert match_movie_name('Cat and Dog') == False
assert match_movie_name('King Rat') == True
assert match_movie_name('The Ghosts') == True

'''
Write a function match_number that takes a string as input. 
It returns True if the string matches numbers -999 to 999. 
The positive numbers could be prefixed with + (e.g. 97 and +97 are valid). 
Otherwise, it returns False.
So, it should match -999, -998, …, 998, 999. Use ? in the regex.
'''
REGEX=r"[-+]?\d"

def match_number(s):
    if re.search(REGEX, s)==None:
        return False
    else:
        return True

'''
Write a function match_url that takes a url as input. 
It returns True if the url is of type http (http://) or https (https://). 
Otherwise, it returns False.
'''
REGEX=r"http[:|s]?:?//"

def match_url(url):
    if re.search(REGEX, url)==None:
        return False
    else:
        return True
    
assert match_url('https://www.google.com') == True
assert match_url('http://www.google.com') == True
assert match_url('https://www.yahoo.com') == True
assert match_url('http://www.yahoo.com') == True
assert match_url('ftp://www.google.com') == False
assert match_url('scp://www.yahoo.com') == False
assert match_url('http-proto') == False
assert match_url('https is a protocol') == False

'''
Write a function match_url that takes a url as input. 
It returns True if the url is of type http (http://) or https (https://) 
AND the url domain is .com or .org. Otherwise, it returns False.
'''
REGEX=r"http[:|s]?:?//.*com|.*org"

def match_url(url):
    if re.search(REGEX, url)==None:
        return False
    else:
        return True

assert match_url('https://www.google.com') == True
assert match_url('http://yahoo.org') == True
assert match_url('http://www.facebook.com/profile') == True
assert match_url('http://www.wattpad.com/tags/fiction') == True
assert match_url('ftp://www.google.com') == False
assert match_url('http://www.yahoo.net') == False
assert match_url('https://www.facebook.com') == True
assert match_url('https://www.photo.net') == False

'''
Write a function match_sentence that takes a string as input. 
It returns True if the string has word cat followed by dog. 
Otherwise, it returns False. Hint: use repetition of . to match word & space 
characters.
'''
REGEX=r"cat.*dog"

def match_sentence(string):
    if re.search(REGEX, string)==None:
        return False
    else:
        return True

assert match_sentence('The cat chased the dog.') == True
assert match_sentence('The cat ran away from the dog.') == True
assert match_sentence('The dog looked at the cat with confusion.') == False
assert match_sentence('The dog was friendly to the cat.') == False
assert match_sentence('The cat drank milk.') == False

'''
Write a function match_sentence that takes a string as input. 
It returns True if the string has word cat followed by dog or vice versa 
(i.e. dog followed by cat). Otherwise, it returns False.
'''
REGEX=r"cat.*dog|dog.*cat"

def match_sentence(string):
    if re.search(REGEX, string)==None:
        return False
    else:
        return True

assert match_sentence('The cat chased the dog.') == True
assert match_sentence('The cat ran away from the dog.') == True
assert match_sentence('The dog looked at the cat with confusion.') == True
assert match_sentence('The dog was friendly to the cat.') == True
assert match_sentence('The cat drank milk.') == False

'''
Write a function match_movie_name that takes a movie name as input. 
It returns True if the movie has at least three words. 
Otherwise, it returns False.
'''
REGEX=r"\w+\s+\w+\s+\w+"

def match_movie_name(movie_name):
    if re.search(REGEX, movie_name)==None:
        return False
    else:
        return True
    
assert match_movie_name('Gone With The Wind') == True
assert match_movie_name('Superman') == False
assert match_movie_name('La La Land') == True
assert match_movie_name('The Sixth Sense') == True
assert match_movie_name('Braveheart') == False

'''
Write a function match_movie_name that takes a movie name as input. 
It returns True if the movie has at least three words. 
Otherwise, it returns False.
Note: you have to match : as part of characters between words. 
Hint: you can use [] or | for matching characters between words.
'''
REGEX=r".+\s+.+\s+.+"

def match_movie_name(movie_name):
    if re.search(REGEX, movie_name)==None:
        return False
    else:
        return True

assert match_movie_name('Gone With The Wind') == True
assert match_movie_name('Superman') == False
assert match_movie_name('Star Wars: The Last Jedi') == True
assert match_movie_name('2010: the year we make contact') == True
assert match_movie_name('Braveheart') == False

'''
Write a function match_sentence that takes a string as input. 
It returns True if the string has two years. Otherwise, it returns False.
'''
REGEX=r"\d{4}.+\d{4}"

def match_sentence(string):
    if re.search(REGEX, string)==None:
        return False
    else:
        return True

assert match_sentence('1984 comes before 1999.') == True
assert match_sentence('In 2015, I bought 2 cars.') == False
assert match_sentence('2004 comes after 2001.') == True
assert match_sentence('There was a flood in 1999.') == False
assert match_sentence('12345678 is a long number.') == False

# Section 4, matching boundaries

'''
Write a function mentions_dog that takes a string as input. 
It returns True if the string mentions animal dog. 
Otherwise, it returns False.
'''
REGEX=r"\bdog\b"

def mentions_dog(string):
    if re.search(REGEX, string)==None:
        return False
    else:
        return True
    
assert mentions_dog('a dog was barking.') == True
assert mentions_dog('dog is a loyal animal.') == True
assert mentions_dog('this is my dog.') == True
assert mentions_dog('is it a dogfish?') == False
assert mentions_dog('dogfood is about using your own software.') == False

'''
Write a function match_sentence that takes a string as input. 
It returns True if there is at least one word with exactly 5 letters. 
Otherwise, it returns False.
'''   
REGEX=r"\b\w{5}\b"

def match_sentence(string):
    if re.search(REGEX, string)==None:
        return False
    else:
        return True

assert match_sentence('I am a super human.') == True
assert match_sentence('Spice route is not spicy.') == True
assert match_sentence('Cat cannot climb.') == True
assert match_sentence('Spiderman returns is not interesting.') == False
assert match_sentence('Cat can jump.') == False

'''
Write a function match_sentence that takes a string as input. 
It returns True if there is a year in 4 digit format. 
Otherwise, it returns False.
'''
REGEX=r"\b\d{4}\b"

def match_sentence(string):
    if re.search(REGEX, string)==None:
        return False
    else:
        return True

assert match_sentence('In year 2000, there was an earthquake.') == True
assert match_sentence('1984.') == True
assert match_sentence("In 2020, I'll be 20 years old") == True
assert match_sentence('I am 20 years old now.') == False
assert match_sentence('123456789 is a really long number.') == False

'''
Write a function match_movie_name that takes a movie name as input. 
It returns True if the movie name has only one word. 
Otherwise, it returns False.
'''
REGEX=r"^\w+$"

def match_movie_name(movie_name):
    if re.search(REGEX, movie_name)==None:
        return False
    else:
        return True

assert match_movie_name('Superman') == True
assert match_movie_name('1984') == True
assert match_movie_name('Spiderman Returns') == False
assert match_movie_name('2001: A Space Odyssey') == False
assert match_movie_name('AM1200') == True
assert match_movie_name('I.Q.') == False

'''
Write a function match_movie_name that takes a movie name as input. 
It returns True if the movie name does not have any whitespace character (hint: \S). 
Otherwise, it returns False.
'''
REGEX = r"^\S+$"

def match_movie_name(movie_name):
    if re.search(REGEX, movie_name):
        return True
    else:
        return False

assert match_movie_name('Superman') == True
assert match_movie_name('1984') == True
assert match_movie_name('Spiderman Returns') == False
assert match_movie_name('2001: A Space Odyssey') == False
assert match_movie_name('AM1200') == True
assert match_movie_name('I.Q.') == True

'''
Write a function valid_url that takes a string as input. 
It returns True if the string is a valid url. Otherwise, it returns False.
'''
REGEX=r"^http[:|s]?:?//\S.+com|\S.+org$"

def valid_url(url):
    if re.search(REGEX, url)==None:
        return False
    else:
        return True

assert valid_url('http://www.google.com') == True
assert valid_url('http://www.yahoo.com') == True
assert valid_url('http://www.wattpad.com') == True
assert valid_url('http:// google.com') == False
assert valid_url('A url looks like http://www.google.com') == False

REGEX=r"^http[:|s]?:?//\S.+com|\S.+org/?|html$"

def valid_url(url):
    if re.search(REGEX, url)==None:
        return False
    else:
        return True
    
assert valid_url('http://www.google.com') == True
assert valid_url('https://www.yahoo.com') == True
assert valid_url('https://www.wattpad.com') == True
assert valid_url('https://en.wikipedia.org/') == True
assert valid_url('http:// google.com') == False
assert valid_url('A url looks like http://www.google.com') == False
assert valid_url('https://www.yahoo.com') == True
assert valid_url('https://www.wattpad.com/tags/children') == True
assert valid_url('http://localhost:8000/test-page.html') == True

# Section 5, regex beyond match

'''
Write a function first_five_letter_word that takes a string as input. 
If the string starts with a five letter word, the function returns that word. 
Otherwise, it returns None.
'''
REGEX=r"^\w{5}\b"

def first_five_letter_word(s):
    match = re.search(REGEX, s)
    if match:
        return match.group()
       
assert first_five_letter_word('Sense and Sensibility') == 'Sense'
assert first_five_letter_word('Gumby: The Movie') == 'Gumby'
assert first_five_letter_word("Jason's Lyric") == 'Jason'
assert first_five_letter_word('Superman') == None
assert first_five_letter_word('2009: Lost Memories') == None
assert first_five_letter_word('Sensibility and Sense') == None

'''
Write a function extract_adverb that takes a string as input. 
If the string has an adverb (strictly, deadly, objectively etc) , 
the function returns that adverb. Otherwise, it returns None.
'''
REGEX=r"\b\w+ly\b"

def extract_adverb(s):
    match = re.search(REGEX, s)
    if match:
        return match.group()  
    
assert extract_adverb('Strictly Ballroom') == 'Strictly'
assert extract_adverb('Tough and Deadly') == 'Deadly'
assert extract_adverb('Heavenly Creatures') == 'Heavenly'
assert extract_adverb('Superman') == None

'''
Write a function extract_email that takes a string as input. 
If the string has an email address, the function returns that. 
Otherwise, it returns None.
'''
REGEX=r"\w+@\w+\b.\w+\b"

def extract_email(s):
    match = re.search(REGEX, s)
    if match:
        return match.group()

assert extract_email('smith@yahoo.com - Steve Smith') == 'smith@yahoo.com'
assert extract_email('hi@turtleprogrammer.com - Turtle') == 'hi@turtleprogrammer.com'
assert extract_email('rama@gmail.com') == 'rama@gmail.com'
assert extract_email('Superman') == None
assert extract_email('rama @gmail.com') == None

'''
Write a function extract_site_name that takes a string as input. 
If the string is a valid url (i.e. http://www.<site>.com), it returns the <site>. 
Otherwise, it returns None.
'''
REGEX=r"(^http[:|s]?:?//www.)(.*)(\.com|\.net|\.org)"

def extract_site_name(s):
    match = re.search(REGEX, s)
    if match:
        return match.group(2)

assert extract_site_name('http://www.google.com') == 'google'
assert extract_site_name('http://www.yahoo.com') == 'yahoo'
assert extract_site_name('http://www.facebook.com') == 'facebook'
assert extract_site_name('www.facebook.com') == None
assert extract_site_name('facebook.com') == None

'''
Write a function extract_host_site_name that takes a string as input. 
If the string is a valid url (i.e. http://<host>.<site>.com), 
it returns a tuple of the form (<host>,<site>). Otherwise, it returns None.
'''
REGEX=r"(^http[:|s]?:?//)(\w+).(.*)(\.com|\.net|\.org)"

def extract_host_site_name(s):
    match = re.search(REGEX, s)
    if match:
        return (match.group(2), match.group(3))

assert extract_host_site_name('http://mail.google.com') == ('mail', 'google')
assert extract_host_site_name('http://en.wikipedia.org') == ('en', 'wikipedia')
assert extract_host_site_name('http://www.facebook.com') == ('www', 'facebook')
assert extract_host_site_name('www.facebook.com') == None
assert extract_host_site_name('facebook.com') == None   

'''
Your task is to write a function extract_item_quantity that takes a string as 
input. The string is of the format <item>: <quantity>. The function returns a 
tuple of the format (<item>, <quantity>) if it finds the input string in 
correct format. Otherwise, it returns None.
Note: the <quantity> should be returned as integer.
'''
REGEX=r"^(\w+)\s*:\s*(\d*)"

def extract_item_quantity(s):
    match = re.search(REGEX, s)
    if match: 
        item = match.group(1)
        quantity = match.group(2)
        try: 
            quantity = int(quantity)
        except:
            return None
        else:
            return (item, quantity)

assert extract_item_quantity('spoons: 4') == ('spoons', 4)
assert extract_item_quantity('bowls :6') == ('bowls', 6)
assert extract_item_quantity('cups   :   8') == ('cups', 8)
assert extract_item_quantity('pans: ') == None
assert extract_item_quantity(': 4') == None

'''
Write a function extract_middle_name that takes a name as input. 
It returns the middle name of the person by using named groups in regex.
'''
# ?P declares that we will give a name to the group
REGEX_PATTERN = r"^\w+\s(?P<middle_name>\b\w+\b)\s\w+"

def extract_middle_name(name):
    match = re.search(REGEX_PATTERN, name)
    if not match:
        return None
    else:
        return match.group('middle_name')

assert extract_middle_name('George Bernard Shaw') == 'Bernard'
assert extract_middle_name('Ram Prakash Kripal') == 'Prakash'

'''
Given a url of the form http://www.<site>.com, we want to extract the <site>. 
Define the variable REGEX_PATTERN using named groups such that:
if the url is not in the given format, the regex will not match.
if the url is in the given format, the named group site will have the site name.
'''
REGEX_PATTERN = r"(^http[:|s]?:?//www.)(?P<site>.*)(\.com|\.net|\.org)"

match = re.search(REGEX_PATTERN, 'http://www.google.com')
assert match != None
assert match.group('site') == 'google'
match = re.search(REGEX_PATTERN, 'blah blah blah')
assert match == None

'''
Given a url of the form http://<host>.wikipedia.org, we want to extract the <host>. 
Define the variable REGEX_PATTERN using named groups such that:
if the url is not in the given format, the regex will not match.
if the url is in the given format, the named group host will have the host name.
'''
REGEX_PATTERN = r"(^http[:|s]?:?//)(?P<host>\b\w+\b)"

match = re.search(REGEX_PATTERN, 'http://en.wikipedia.org')
assert match != None
assert match.group('host') == 'en'
match = re.search(REGEX_PATTERN, 'blah blah blah')
assert match == None

'''
Write REGEX_PATTERN such that we can split data in item and quantity.
'''
REGEX_PATTERN=r"\W+"

assert re.split(REGEX_PATTERN, 'Onion  :    2') == ['Onion', '2']
assert re.split(REGEX_PATTERN, 'Onion:2') == ['Onion', '2']

# Example usimg findall
text = "The growth was more in 2001 compred to 2002."
years = re.findall(r"\d+", text)
print(years)
  
