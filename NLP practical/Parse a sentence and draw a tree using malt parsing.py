import os
from nltk.parse import malt

# Set the MALT_PARSER environment variable
malt_parser_dir = r'C:\Users\prath\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\parse\maltparser-1.7.2'
os.environ['MALT_PARSER'] = malt_parser_dir

# Initialize MaltParser
mp = malt.MaltParser()


# Parse a sentence and get the tree
sentence = 'I saw a bird from my window.'
parsed_tree = mp.parse_one(sentence.split()).tree()

# Print the parsed tree
print(parsed_tree)

# Draw the parsed tree (requires a GUI environment)
parsed_tree.draw()
