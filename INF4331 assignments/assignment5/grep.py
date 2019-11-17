import re
import argparse


def parse_arguments():
    """
    Parses commandline arguments
    :return: Arguments
    """
    parser = argparse.ArgumentParser(
        description='Usage: python3 highlighter.py <textfile> <words_to_search> --highlight(optional)')

    # Set up arguments
    parser.add_argument('textfile', type=str,
                        help='The text file to search through')

    parser.add_argument('words_to_search', type=str,
                        help='Contains what words to search for')

    parser.add_argument('--highlight',
                        help='Highlight the matches if True',
                        default=False, action='store_true')

    args = parser.parse_args()
    return args


def create_pattern_dictionary(patterns):
    """
    Creates a dictionary with the patterns and a corresponding
    color for that pattern.
    Will recycle colors if the list of colors reach the end.
    :param patterns: String containing the word patterns to search for
    :return: pattern_dict
    """

    # Create a list of 23 different colors
    # list of colors
    color_list = [31, 32, 33, 34, 35, 36, 90, 91, 92, 93, 94, 95, 96]

    # Create dict from pattern and colors
    pattern_dict = {}
    i = 0  # color counter
    for pattern in patterns:
        if i == len(color_list):  # Recycles colors if reached end of list
            i = 0
        pattern_dict[pattern] = color_list[i]
        i += 1
    return pattern_dict


def grep_file(text_file, word_file, highlight=False):
    """
    Method for searching through the files and
    finding which words are in the text file.
    The coloring it if flag is sent, if not just printing
    the lines with the words in it
    :param text_file: The text file to search through
    :param word_file: The file containing the patterns to look for
    :param highlight: Boolean to highlight the words if it is set to True
    :return: Lines with matches
    """

    lines = ''  # Will contain the lines that have matches

    # Separate textfile and wordfile by newline
    text_file = text_file.split("\n")
    word_file = word_file.split("\n")

    # Create a regex that search for all the patterns
    # Also create a dict that assigns a color to the word in the word file so that it is not random anymore
    search_pattern = ''
    patterns = create_pattern_dictionary(word_file)
    for word in word_file:
        search_pattern += '({})|'.format(word)
    search_pattern = search_pattern[:-1]

    # Loop through the textfile, line by line
    for text_line in text_file:
        # Check if there are any matches
        if re.search(search_pattern, text_line):
            # Check if highlight flag is set
            if highlight is True:

                # Loop through the word patterns
                for pattern in patterns:
                    # Add color encoding to the word
                    color = color_format(patterns[pattern], pattern)

                    # Replace the match with the color encoded word in that line.
                    text_line = re.sub(pattern, color, text_line)

            # Add the line if there was any matches
            lines += f'{text_line}\n'
    return lines


def color_format(color, word):
    """
    Takes in the color and pattern and returns the pattern with
    color encoding
    :param color: The color code
    :param word: The word pattern to match
    :return: Color encoded pattern
    """
    
    # Encode the word with the color
    start = "\033[{}m".format(color)
    end = "\033[0m"
    return start + word + end


if __name__ == '__main__':

    # Parse command line arguments
    args = parse_arguments()

    # Open and read files
    with open(args.textfile) as txt_file, open(args.words_to_search) as word_file:
        text = txt_file.read()
        words = word_file.read()

        # Grep the file using the patterns from the word_file
        grep = grep_file(text, words, args.highlight)

    # Print results from grep
    if grep is not '':
        print(grep)
    else:
        print("There was no matches")

