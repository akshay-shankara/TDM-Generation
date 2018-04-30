import os
import nltk
import textmining
from scipy import sparse
import numpy as np

default_stopwords = set(nltk.corpus.stopwords.words('english'))

file_directory = ('input_directory_path')
path_length = sum([len(files) for r, d, files in os.walk(file_directory)])
print(path_length, file_directory)

file_directory = 'input_directory_path/file'    # filenames = file01.txt, file02.txt...
intermediate_dir2 = '/Users/akshay/Desktop/Intermediate/intFreq'

i = 0
j = 0
while i < path_length:
    with open(file_directory + str(i) + ".txt", "r") as f:
        words = nltk.word_tokenize(f.read())

        # Remove single-character tokens (mostly punctuation)
        words = [word for word in words if len(word) > 1]

        # Remove numbers
        words = [word for word in words if not word.isnumeric()]

        # Lowercase all words (default_stopwords are lowercase too)
        words = [word.lower() for word in words]

        # Remove special characters
        words = [word.lower() for word in words.isalpha()]

        # Remove stopwords
        words = [word for word in words if word not in default_stopwords]

        # Calculate frequency distribution
        fdist = nltk.FreqDist(words)

        file_directory2 = ('output_directory_path/fileFreq%d.txt' % i)
        input_file = open(file_directory2, 'w')

        intermediate_dir = ('intermediate_dir/intFreq%d.txt' % i)
        intermediate_file = open(intermediate_dir, 'w')

        for word, frequency in fdist.most_common(1500):
            input_file.write(u'{}:{}\n'.format(word, frequency))
            intermediate_file.write(u'{} '.format(word))
    i += 1

tdm = textmining.TermDocumentMatrix()

i = 0

while i < path_length:
    with open(intermediate_dir2 + str(i) + ".txt", "r")as f:
        info = f.read()
        i += 1
        tdm.add_doc(info)


def compile_row_string(a_row):
    return str(a_row).strip(']').strip('[').replace(' ', '')


file_directory2 = 'output_directory/TDM.txt'
input_file = open(file_directory2, 'w')
for rows in tdm.rows(cutoff=1):
    input_file.write(compile_row_string(rows) + '\n')