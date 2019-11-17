import re
import argparse


def parse_arguments():
    """
    Parse commandline arguments
    :return:
    """
    parser = argparse.ArgumentParser(description='Usage: python3 highlighter.py <syntaxfile> <themefile> <sourcefile>')

    # Set up arguments
    parser.add_argument('syntaxfile', type=str,
                        help='The file with all regex patterns')

    parser.add_argument('themefile', type=str,
                        help='Contains all the color themes')

    parser.add_argument('sourcefile', type=str,
                        help='The source file to use color theme on')

    args = parser.parse_args()
    if(args.syntaxfile.endswith(".syntax") and args.themefile.endswith(".theme")):
        return args
    else:
        print("Error: Not correct file")
        print("Run program with: python3 highlighter.py <syntax> <theme> <file>")
        exit(1)


def read_syntax_file(syntax_file):
    """
    Method for reading the theme file, and adding
    the correlation between the type and pattern to a dictionary
    :param syntax_file: Text file with regex pattern and key-description
    :return:
    """
    # Added encoding='utf8' to make it run on windows pycharm and ubuntu system as well as mac
    with open(syntax_file, encoding='utf8') as syntax:
        syntax_definition = syntax.read()

    # Use regex to divide pattern from keyword in a more strict manner
    pattern_syntax = re.compile(r'"(.+)": (.+)')
    matches_syntax = pattern_syntax.findall(syntax_definition)

    # Loop through lines in the syntax matches and create a dict with key and corresponding pattern
    syntax_dictionary = {}
    for item in matches_syntax:
        syntax_dictionary[item[1]] = item[0]
    return syntax_dictionary


def read_theme_file(theme_file):
    """
    Method for reading the theme file, and adding
    the correlation between the pattern and color to a dictionary.
    :param theme_file: Text file with color code and key-description
    :return:
    """
    # open and read the theme file
    with open(theme_file) as theme:
        theme_definition = theme.read()

    # Create a dict and separate by newlines
    theme_dictionary = dict()
    theme_definition = theme_definition.split('\n')

    # Loop through lines and create a dict containing keyword and color
    for definition in theme_definition:
        theme_pattern, theme_color = definition.split(': ')
        theme_dictionary[theme_pattern] = theme_color
    return theme_dictionary


def color_format(text, code=5):
    """
    Setting the format code for the coloring ref:
    https://misc.flogisoft.com/bash/tip_colors_and_formatting
    :param text: pattern
    :param code: color code
    :return:
    """
    start = "\033[{}m".format(code)
    end = "\033[0m"
    return start + text + end


def color_file(syntax_dictionary, theme_dictionary, source_file):

    """
    method to read from the source file and printing it out after
    coloring the text, by replacing the leftmost non-overlapping
    occurrence of syntax_pattern in color with the string returned by color_format
    :param syntax_dictionary: Dict with regex pattern and key-description
    :param theme_dictionary: Dict with color code and key-description
    :param source_file: Text file to highlight
    :return: None
    """
    # Open and read file
    with open(source_file) as file:
        text = file.read()

        # looping through the keys in the dictionary
        for key in syntax_dictionary.keys():

            # Find the matches in the text
            replacement = re.search(syntax_dictionary[key], text)

            # Color matches if there are any
            if replacement is not None:
                color = color_format(replacement.group(), theme_dictionary[key])
                text = re.sub(syntax_dictionary[key], color, text)
        # Print out the results
        print(text)


if __name__ == '__main__':
    # Parse arguments
    args = parse_arguments()

    # Process the input file
    syntax_file = read_syntax_file(args.syntaxfile)
    theme_file = read_theme_file(args.themefile)
    source_file = args.sourcefile

    # Highlight the matches
    color_file(syntax_file, theme_file, source_file)

