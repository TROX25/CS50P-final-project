# TEXT ANALYZER
     Video Demo:  https://www.youtube.com/watch?v=-Rhe7z-8ib0
     Description:

    - Text Analyzer takes a .txt file (text.txt by default) from user input via terminal using ArgParse.

    - After that, program loads that file and starts working on it.

    - Based on users input, selected file is being thoroughly analyzed by txt_analyze function. If word exists in dictionary, id adds +1 to an amount. If it doesnt exist yet, it creates an instance with amount equal to 1. It also strips words from any unwanted punctuation and capitalizes every words

    - Then function txt_popstop removes user selected stop words (default is set to: a, an, the) from the list and returns a list without these words

    - At the end, text_sorted(loaded with a return from previous step which is a List_Without_Stop_Words) does the following:
        - prompts user to sort list either alphabetically or by amount
        - prints selected outcome in order to ease potential testing
        - uses nested txt_write function and saves final result to a new file.


    FUNCTIONS:
    1. txt_load -> Loads lines from .txt file and divides it into words.

    2. txt_analyze -> Analyzes amount of words in text.

    3. txt_popstop -> Takes list of dict of used words and subtracts words such as: a, an, the, etc...

    4. txt_sorted -> Takes a list of dicts with words and sorts it either by amount ar alphabetically.

    5. txt_write -> Writes list of words with an amount to a .txt file + info on sort type.

