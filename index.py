# Python 2.7.3
import re
import os
import collections
import time


class index:
    def __init__(self, path):
        self.path = path
        pass

    def buildIndex(self):

        doc_files = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]

        index = {}

        for each_file in doc_files:

            with open(self.path + "/" + each_file) as file:
                text = file.read().replace('\n',' ')

            text_array = re.sub('[^a-zA-Z \n]', '', text).lower().split()

            token_dictionary = {}

            for idx, token in enumerate(text_array):

                if token not in token_dictionary.keys():

                    token_dictionary[token] = [idx]

                else:
                    token_dictionary[token].append(idx)

            index[each_file] = token_dictionary

        inverted_index = {}

        for key, value in index.items():
            doc_id = key
            position_word_index = value

            for word, position in position_word_index.items():

                if word not in inverted_index:

                    inverted_index[word] = []

                inverted_index[word].append({doc_id: position})

        print(inverted_index)




# def and_query(self, query_terms):
# function for identifying relevant docs using the index

# def print_dict(self):
# function to print the terms and posting list in the index

# def print_doc_list(self):
# function to print the documents and their document id

a = index("C:/Users/Temp/Documents/GitHub/inverted-index/collection")
a.buildIndex()
