# 6.00.1x Problem Set 7.
# RSS Feed Filter.
#
# Student: Javier Herrero Arnanz.

import feedparser
import string
import time
from project_util import translate_html
from Tkinter import *


#-----------------------------------------------------------------------
#
# Problem Set 7

#======================
# Code for retrieving and parsing RSS feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

#======================
# Part 1
# Data structure design
#======================

# Problem 1
class NewsStory(object):
    """
    Represents a concrete news through its guid, title, 
    subject, summary and link.
    
    GUID - a string that serves as a unique name for this news.

    Title - news title.

    Subject - news subject.

    Summary - news summary.

    Link - link to more content.
    """
    
    def __init__(self,guid, title, subject, summary, link):
        """
        Initialize the news content.
        """
        self.guid = guid 
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link
    
    def getGuid(self):
        """
        Gets news GUID.
        """
        return self.guid
        
    def getTitle(self):
        """
        Gets news title.
        """
        return self.title
        
    def getSubject(self):
        """
        Gets news subject.
        """
        return self.subject
        
    def getSummary(self):
        """
        Gets news summary.
        """
        return self.summary
                
    def getLink(self):
        """
        Gets news link.
        """
        return self.link
        

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    """
    A trigger is a rule that is evaluated over a single news story 
    and may fire to generate an alert.
    """
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers.
# Problems 2-5.
class WordTrigger(Trigger):
    """
    Word trigger abstract class.
    """
    
    def __init__(self,word):
        """
        Class's constructor.
        """
        self.word = word
    
    def isWordIn(self,text):
        """
        It returns True if the whole word 'word' is present 
        in 'text', False otherwise. 
        """
        # Replaces every punctuation mark in text with a space.
        text = text.lower()
        for char in string.punctuation:
            text = text.replace(char,' ')
        # Break up the text into a list of distinct words.
        wordsL = text.split(' ')
        # Search word into words list.
        if self.word.lower() in wordsL:
            return True
        else:
            return False
        
class TitleTrigger(WordTrigger):
    """
    This trigger fires when a news item's title contains a given word. 
    """
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return WordTrigger.isWordIn(self,story.getTitle())

class SubjectTrigger(WordTrigger):
    """
    This trigger fires when a news item's subject contains a given word. 
    """
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return WordTrigger.isWordIn(self,story.getSubject())

class SummaryTrigger(WordTrigger):
    """
    This trigger fires when a news item's summary contains a given word. 
    """
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return WordTrigger.isWordIn(self,story.getSummary())

# Composite Triggers
# Problems 6-8
class NotTrigger(Trigger):
    """
    This trigger should produce its output by inverting 
    the output of another trigger.
    """
    
    def __init__(self,trigger):
        """
        Class's constructor.
        """
        self.trig = trigger
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return (not self.trig.evaluate(story))
    

class AndTrigger(Trigger):
    """
    This trigger should take two triggers as arguments 
    to its constructor, and should fire on a news story 
    only if both of the inputted triggers would fire on that item.
    """
    
    def __init__(self,trigger1,trigger2):
        """
        Class's constructor.
        """
        self.trig1 = trigger1
        self.trig2 = trigger2

    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return (self.trig1.evaluate(story) and self.trig2.evaluate(story))
        
class OrTrigger(Trigger):
    """
    This trigger should take two triggers as arguments 
    to its constructor, and should fire if either one 
    (or both) of its inputted triggers would fire on that item.
    """

    def __init__(self,trigger1,trigger2):
        """
        Class's constructor.
        """
        self.trig1 = trigger1
        self.trig2 = trigger2

    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return (self.trig1.evaluate(story) or self.trig2.evaluate(story))
        
# Phrase Trigger
# Question 9
class PhraseTrigger(Trigger):
    """
    This fires when a given phrase is in any of the 
    story's subject, title, or summary. 
    """
    
    def __init__(self,phrase):
        """
        Class's constructor.
        """
        self.phrase = phrase
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return ((self.phrase in story.getSubject()) or (self.phrase in story.getTitle()) 
        or (self.phrase in story.getSummary()))


#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    validStories = []
    for story in stories:
        for trigger in triggerlist:
            if (trigger.evaluate(story)):
                validStories.append(story)
                break
 
    return validStories


#======================
# Part 4
# User-Specified Triggers
#======================

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1").

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    # Instantiate the trigger.
    if (triggerType == 'TITLE'):
        trigger = TitleTrigger(params[0])
    elif (triggerType == 'SUBJECT'):
        trigger = SubjectTrigger(params[0])
    elif (triggerType == 'SUMMARY'):
        trigger = SummaryTrigger(params[0])
    elif (triggerType == 'NOT'):
        trigger = NotTrigger(triggerMap[params[0]])
    elif (triggerType == 'AND'):
        trigger = AndTrigger(triggerMap[params[0]],triggerMap[params[1]])
    elif (triggerType == 'OR'):
        trigger = OrTrigger(triggerMap[params[0]],triggerMap[params[1]])
    elif (triggerType == 'PHRASE'):         
        trigger = PhraseTrigger(' '.join(params))
        
    # Adds the new trigger to the trigger map dictionary.
    triggerMap[name] = trigger
    
    return trigger

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename.
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments.
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself.
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger.
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list.
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers
    
import thread

SLEEPTIME = 60 #seconds -- how often we poll.


def main_thread(master):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    try:
        # These will probably generate a few hits...
        t1 = TitleTrigger("Obama")
        t2 = SubjectTrigger("Romney")
        t3 = PhraseTrigger("Election")
        t4 = OrTrigger(t2, t3)
        triggerlist = [t1, t4]
        
        triggerlist = readTriggerConfig("/home/ibarra/Canopy-Workspace/Codigo-6.00.1x/Problem_Set_7/triggers.txt")

        # **** from here down is about drawing ****
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)
        
        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)

        # Gather stories
        guidShown = []
        def get_cont(newstory):
            if newstory.getGuid() not in guidShown:
                cont.insert(END, newstory.getTitle()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.getSummary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.getGuid())

        while True:

            print "Polling . . .",
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

            # Process the stories
            stories = filterStories(stories, triggerlist)

            map(get_cont, stories)
            scrollbar.config(command=cont.yview)


            print "Sleeping..."
            time.sleep(SLEEPTIME)

    except Exception as e:
        print e


if __name__ == '__main__':

    root = Tk()
    root.title("Some RSS parser")
    thread.start_new_thread(main_thread, (root,))
    root.mainloop()

