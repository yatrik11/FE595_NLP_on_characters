#!/usr/bin/env python
# coding: utf-8

# In[9]:


import collections
from textblob import TextBlob

# Opening text files to save 10 most common male and female descriptors
most_common_male = open("C:/Users/Yatri Kalathia/FE-595/most_common_male.txt", "w+")
most_common_female = open("C:/Users/Yatri Kalathia/FE-595/most_common_female.txt", "w+")

#creating function to find top descriptors
def top_descriptors():
    with open('C:/Users/Yatri Kalathia/FE-595/male.txt', "r") as file:
        file_text = file.read()
        file_text = file_text.replace("fe's", "es")
        blob = TextBlob(file_text)
        descriptors = blob.noun_phrases
        counter = collections.Counter(descriptors)
        file.close()
        
        common_desc_male = str("Most common male descriptor is '{}' and ".format(counter.most_common(10)[0][0]) +
                               "it appears {} times.".format(counter.most_common(10)[0][1]) + '\n' +
                               "Second most common male descriptor is '{}' and ".format(counter.most_common(10)[1][0]) +
                               "it appears {} times.".format(counter.most_common(10)[1][1]) + '\n' +
                               "Third most common male descriptor is '{}' and ".format(counter.most_common(10)[2][0]) +
                               "it appears {} times.".format(counter.most_common(10)[2][1]) + '\n' +
                               "Fourth most common male descriptor is '{}' and ".format(counter.most_common(10)[3][0]) +
                               "it appears {} times.".format(counter.most_common(10)[3][1]) + '\n' +
                               "Fifth most common male descriptor is '{}' and ".format(counter.most_common(10)[4][0]) +
                               "it appears {} times.".format(counter.most_common(10)[4][1]) + '\n' +
                               "Sixth most common male descriptor is '{}' and ".format(counter.most_common(10)[5][0]) +
                               "it appears {} times.".format(counter.most_common(10)[5][1]) + '\n' +
                               "Seventh most common male descriptor is '{}' and ".format(counter.most_common(10)[6][0]) +
                               "it appears {} times.".format(counter.most_common(10)[6][1]) + '\n' +
                               "Eighth most common male descriptor is '{}' and ".format(counter.most_common(10)[7][0]) +
                               "it appears {} times.".format(counter.most_common(10)[7][1]) + '\n' +
                               "Ninth most common male descriptor is '{}' and ".format(counter.most_common(10)[8][0]) +
                               "it appears {} times.".format(counter.most_common(10)[8][1]) + '\n' +
                               "Tenth most common male descriptor is '{}' and ".format(counter.most_common(10)[9][0]) +
                               "it appears {} times.".format(counter.most_common(10)[9][1]))
        
        most_common_male.write(common_desc_male)

    with open('C:/Users/Yatri Kalathia/FE-595/female.txt', "r") as file:
        file_text = file.read()
        file_text = file_text.replace("y's", "ies")
        blob = TextBlob(file_text)
        descriptors = blob.noun_phrases
        counter = collections.Counter(descriptors)
        file.close()

        common_desc_female = str("Most common female descriptor is '{}' and ".format(counter.most_common(10)[0][0]) +
                                 "it appears {} times.".format(counter.most_common(10)[0][1]) + '\n' +
                                 "Second most common female descriptor is '{}' and ".format(counter.most_common(10)[1][0])
                                 + "it appears {} times.".format(counter.most_common(10)[1][1]) + '\n' +
                                 "Third most common female descriptor is '{}' and ".format(counter.most_common(10)[2][0]) +
                                 "it appears {} times.".format(counter.most_common(10)[2][1]) + '\n' +
                                 "Fourth most common female descriptor is '{}' and ".format(counter.most_common(10)[3][0])
                                 + "it appears {} times.".format(counter.most_common(10)[3][1]) + '\n' +
                                 "Fifth most common female descriptor is '{}' and ".format(counter.most_common(10)[4][0]) +
                                 "it appears {} times.".format(counter.most_common(10)[4][1]) + '\n' +
                                 "Sixth most common female descriptor is '{}' and ".format(counter.most_common(10)[5][0]) +
                                 "it appears {} times.".format(counter.most_common(10)[5][1]) + '\n' +
                                 "Seventh most common female descriptor is '{}' and ".format(counter.most_common(10)[6][0])
                                 + "it appears {} times.".format(counter.most_common(10)[6][1]) + '\n' +
                                 "Eighth most common female descriptor is '{}' and ".format(counter.most_common(10)[7][0])
                                 + "it appears {} times.".format(counter.most_common(10)[7][1]) + '\n' +
                                 "Ninth most common female descriptor is '{}' and ".format(counter.most_common(10)[8][0]) +
                                 "it appears {} times.".format(counter.most_common(10)[8][1]) + '\n' +
                                 "Tenth most common female descriptor is '{}' and ".format(counter.most_common(10)[9][0]) +
                                 "it appears {} times.".format(counter.most_common(10)[9][1]))
        
        most_common_female.write(common_desc_female)

top_descriptors()
most_common_male.close()
most_common_female.close()

