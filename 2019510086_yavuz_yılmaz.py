import operator
import os


# !!!!!!!!!!!!!!!!!!!If you want to run the code please go to the bottom line first and run the main part !!!!!!!!!!!!!!!!!
def main():
    while True:
        number_of_books = int(input('How many book do you want to be listed (1 or 2): '))
        if number_of_books == 1 or number_of_books == 2:
            break
        else:
            print('Wrong input!!!!')
            print('Please enter 1 or 2.')
    while True:
        Word_Order = int(input('Please enter word order: '))

        if Word_Order > 0:
            break
        else:
            print('Please enter an integer greater than ZERO!!!')
    File_Output = str(input('Please enter the name of the output file: ')) + ".txt"
    if number_of_books == 1:
        Word_Order_Frequency_One_Book('book_1.txt', Word_Order, File_Output)
    else:
        Word_Order_Frequency_Two_Books('book_1.txt', 'Book_2.txt', Word_Order, File_Output)


def Word_Order_Frequency_One_Book(Book, Word_Order, File_Output):
    book_1 = ""
    try:
        file = open(Book, "r", encoding='utf-8')
        book_1 = file.read()
        file.close()
    except:
        print()
        print("Something went wrong when opening the First Book!!!")

    stop_word_list = ["the", "and", "of", "to", "a", "in", "that", "his", "it", "i", "he", "was", "with", "as", "for",
                      "is", "but", "you", "at", "had", "all", "not", "him", "this", "on", "be", "by", "from", "so",
                      "have", "her", "were", "one",
                      "there", "my", "or", "they", "me", "no", "able", "about", "above", "abroad", "according",
                      "accordingly", "across", "actually",
                      "adj", "after", "afterwards", "again", "against", "ago", "ahead", "aint",
                      "allow", "allows", "almost", "alone", "along", "alongside", "already", "also",
                      "although", "always", "am", "amid", "amidst", "among", "amongst", "an",
                      "another", "any", "anybody", "anyhow", "anyone", "anything", "anyway", "anyways",
                      "anywhere", "apart", "appear", "appreciate", "appropriate", "are", "arent", "around",
                      "as", "aside", "ask", "asking", "associated", "available", "away",
                      "awfully", "back", "backward", "backwards", "became", "because", "become",
                      "becomes", "becoming", "been", "before", "beforehand", "begin", "behind", "being",
                      "believe", "below", "beside", "besides", "best", "better", "between", "beyond",
                      "both", "brief", "came", "can", "cannot", "cant", "cant", "caption",
                      "cause", "causes", "certain", "certainly", "changes", "clearly", "cmon", "co",
                      "co.", "com", "come", "comes", "concerning", "consequently", "consider",
                      "considering", "contain", "containing", "contains", "corresponding", "could",
                      "couldnt", "course", "cs", "currently", "dare", "darent", "definitely",
                      "described", "despite", "did", "didnt", "different", "directly", "do", "does",
                      "doesnt", "doing", "done", "dont", "down", "downwards", "during", "each", "edu",
                      "eg", "eight", "eighty", "either", "else", "elsewhere", "end", "ending", "enough",
                      "entirely", "especially", "et", "etc", "even", "ever", "evermore", "every",
                      "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example",
                      "except", "fairly", "far", "farther", "few", "fewer", "fifth", "first", "five",
                      "followed", "following", "follows", "forever", "former", "formerly", "forth",
                      "forward", "found", "four", "further", "furthermore", "get", "gets",
                      "getting", "given", "gives", "go", "goes", "going", "gone", "got", "gotten",
                      "greetings", "had", "hadnt", "half", "happens", "hardly", "has", "hasnt",
                      "havent", "having", "hed", "hell", "hello", "help", "hence",
                      "here", "hereafter", "hereby", "herein", "heres", "hereupon", "hers", "herself",
                      "hes", "hi", "himself", "hither", "hopefully", "how", "howbeit",
                      "however", "hundred", "id", "ie", "if", "ignored", "ill", "im", "immediate",
                      "inasmuch", "inc", "inc.", "indeed", "indicate", "indicated", "indicates",
                      "inner", "inside", "insofar", "instead", "into", "inward", "isnt",
                      "itd", "itll", "its", "its", "itself", "ive", "just", "k", "keep", "keeps",
                      "kept", "know", "known", "knows", "last", "lately", "later", "latter", "latterly",
                      "least", "less", "lest", "let", "lets", "like", "liked", "likely", "likewise",
                      "little", "look", "looking", "looks", "low", "lower", "ltd", "made", "mainly",
                      "make", "makes", "many", "may", "maybe", "maynt", "mean", "meantime",
                      "meanwhile", "merely", "might", "mightnt", "mine", "minus", "miss", "more",
                      "moreover", "most", "mostly", "mr", "mrs", "much", "must", "mustnt",
                      "myself", "name", "namely", "nd", "near", "nearly", "necessary", "need", "neednt",
                      "needs", "neither", "never", "neverf", "neverless", "nevertheless", "new", "next",
                      "nine", "ninety", "nobody", "non", "none", "nonetheless", "noone", "no-one",
                      "nor", "normally", "nothing", "notwithstanding", "novel", "now", "nowhere",
                      "obviously", "off", "often", "oh", "ok", "okay", "old", "once",
                      "ones", "ones", "only", "onto", "opposite", "other", "others",
                      "otherwise", "ought", "oughtnt", "our", "ours", "ourselves", "out", "outside",
                      "over", "overall", "own", "particular", "particularly", "past", "per", "perhaps",
                      "placed", "please", "plus", "possible", "presumably", "probably", "provided",
                      "provides", "que", "quite", "qv", "rather", "rd", "re", "really", "reasonably",
                      "recent", "recently", "regarding", "regardless", "regards", "relatively",
                      "respectively", "right", "round", "said", "same", "saw", "say", "saying", "says",
                      "second", "secondly", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen",
                      "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several",
                      "shall", "shant", "she", "shed", "shell", "shes", "should", "shouldnt",
                      "since", "six", "some", "somebody", "someday", "somehow", "someone",
                      "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry",
                      "specified", "specify", "specifying", "still", "sub", "such", "sup", "sure", "take",
                      "taken", "taking", "tell", "tends", "th", "than", "thank", "thanks", "thanx",
                      "thatll", "thats", "thats", "thatve", "their", "theirs", "them",
                      "themselves", "then", "thence", "thereafter", "thereby", "thered",
                      "therefore", "therein", "therell", "therere", "theres", "theres", "thereupon",
                      "thereve", "these", "theyd", "theyll", "theyre", "theyve", "thing",
                      "things", "think", "third", "thirty", "thorough", "thoroughly", "those",
                      "though", "three", "through", "throughout", "thru", "thus", "till",
                      "together", "too", "took", "toward", "towards", "tried", "tries", "truly", "try",
                      "trying", "ts", "twice", "two", "un", "under", "underneath", "undoing",
                      "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "up", "upon",
                      "upwards", "us", "use", "used", "useful", "uses", "using", "usually", "v",
                      "value", "various", "versus", "very", "via", "viz", "vs", "want", "wants",
                      "wasnt", "way", "we", "wed", "welcome", "well", "well", "went", "were",
                      "were", "werent", "weve", "what", "whatever", "whatll", "whats", "whatve",
                      "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein",
                      "wheres", "whereupon", "wherever", "whether", "which", "whichever", "while",
                      "whilst", "whither", "who", "whod", "whoever", "whole", "wholl", "whom",
                      "whomever", "whos", "whose", "why", "will", "willing", "wish", "within",
                      "without", "wonder", "wont", "would", "wouldnt", "yes", "yet", "youd",
                      "youll", "your", "youre", "yours", "yourself", "yourselves", "youve", "zero",
                      "hows", "whens", "whys", "b", "c", "d", "e", "f", "g", "h",
                      "j", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "uucp", "w", "x",
                      "y", "z", "www", "amount", "bill", "bottom", "call", "computer", "con",
                      "couldnt", "cry", "de", "describe", "detail", "due", "eleven", "empty", "fifteen",
                      "fifty", "fill", "find", "fire", "forty", "front", "full", "give", "hasnt",
                      "herse", "himse", "interest", "itse”", "mill", "move", "myse”", "part", "put",
                      "show", "side", "sincere", "sixty", "system", "ten", "thick", "thin", "top",
                      "twelve", "twenty", "abst", "accordance", "act", "added", "adopted", "affected",
                      "affecting", "affects", "ah", "announce", "anymore", "apparently", "approximately",
                      "aren", "arent", "arise", "auth", "beginning", "beginnings", "begins", "biol",
                      "briefly", "ca", "date", "ed", "effect", "et-al", "ff", "fix", "gave", "giving",
                      "heres", "hes", "hid", "home", "id", "im", "immediately", "importance", "important",
                      "index", "information", "invention", "itd", "keys", "kg", "km", "largely", "lets",
                      "line", "ll", "means", "mg", "million", "ml", "mug", "na", "nay", "necessarily",
                      "nos", "noted", "obtain", "obtained", "omitted", "ord", "owing", "page", "pages",
                      "poorly", "possibly", "potentially", "pp", "predominantly", "present", "previously",
                      "primarily", "promptly", "proud", "quickly", "ran", "readily", "ref", "refs",
                      "related", "research", "resulted", "resulting", "results", "run", "sec", "section",
                      "shed", "shes", "showed", "shown", "showns", "shows", "significant", "significantly",
                      "similar", "similarly", "slightly", "somethan", "specifically", "state", "states",
                      "stop", "strongly", "substantially", "successfully", "sufficiently", "suggest",
                      "thered", "thereof", "there", "thereto", "theyd", "theyre", "thou", "though",
                      "thousand", "through", "til", "tip", "ts", "ups", "usefully", "usefulness", "ve",
                      "vol", "vols", "wed", "whats", "wheres", "whim", "whod", "whos", "widely",
                      "words", "world", "youd", "youre"]

    splitWords = book_1.split()
    punc = '''!()-[]{};:'"“”\,1234567890’—<>./?@#$%^&*_~'''

    for i in range(len(splitWords)):
        splitWords[i] = splitWords[i].lower()  # LowerCase part
        for ele in splitWords[i]:  # removing punctuation
            if ele in punc:
                splitWords[i] = splitWords[i].replace(ele, "")

    New_Splitted_Words = []  # I created a new list because when I do it with remove it takes up to 3-4 minutes but adding it to a new list takes a few seconds
    for word in splitWords.copy():
        if word not in stop_word_list:
            New_Splitted_Words.append(word)

    allWords = {}
    new_word = ''
    flag = False
    for i in range(
            len(New_Splitted_Words) - Word_Order):  # space checks and word counting part according to given word_order
        for j in range(Word_Order):
            if New_Splitted_Words[i + j] == ' ' or New_Splitted_Words[i + j] == '':
                flag = True
                break
            else:
                new_word += New_Splitted_Words[i + j] + ' '
        if not flag:  # If the flag is true, it means a space, so no appending is done.
            if new_word not in allWords:
                allWords[new_word] = 1
            else:
                allWords[new_word] += 1
        flag = False
        new_word = ''

    listed_words = dict(sorted(allWords.items(), key=operator.itemgetter(1), reverse=True))  # sorting dictionary

    if os.path.exists(File_Output):  # the part that checks if there is a file with that name
        os.remove(File_Output)

    open_output_file = open(File_Output, "x", encoding='utf-8')
    open_output_file.close()
    Output = open(File_Output, "a", encoding='utf-8')
    Output.write('| WORD      | WORD     | \n')
    Output.write('| ORDER     | ORDER    | \n')
    Output.write('| FREQUENCY | SEQUENCE | \n')
    Output.write('------------------------ \n')

    for key in listed_words.keys():
        line = '{:>7}     | {:>8} \n'.format(listed_words[key], key)
        Output.write(line)
    Output.close()


def Word_Order_Frequency_Two_Books(Book_1, Book_2, Word_Order, File_Output):
    book_1 = ""
    book_2 = ""
    try:
        file1 = open(Book_1, "r", encoding='utf-8')
        book_1 = file1.read()
        file1.close()
    except:
        print()
        print("Something went wrong when opening the First Book!!!")
    try:
        file2 = open(Book_2, "r", encoding='utf-8')
        book_2 = file2.read()
        file2.close()
    except:
        print()
        print("Something went wrong when opening the Second Book!!!")
    stop_word_list = ["the", "and", "of", "to", "a", "in", "that", "his", "it", "i", "he", "was", "with", "as", "for",
                      "is", "but", "you", "at", "had", "all", "not", "him", "this", "on", "be", "by", "from", "so",
                      "have", "her", "were", "one",
                      "there", "my", "or", "they", "me", "no", "able", "about", "above", "abroad", "according",
                      "accordingly", "across", "actually",
                      "adj", "after", "afterwards", "again", "against", "ago", "ahead", "aint",
                      "allow", "allows", "almost", "alone", "along", "alongside", "already", "also",
                      "although", "always", "am", "amid", "amidst", "among", "amongst", "an",
                      "another", "any", "anybody", "anyhow", "anyone", "anything", "anyway", "anyways",
                      "anywhere", "apart", "appear", "appreciate", "appropriate", "are", "arent", "around",
                      "as", "aside", "ask", "asking", "associated", "available", "away",
                      "awfully", "back", "backward", "backwards", "became", "because", "become",
                      "becomes", "becoming", "been", "before", "beforehand", "begin", "behind", "being",
                      "believe", "below", "beside", "besides", "best", "better", "between", "beyond",
                      "both", "brief", "came", "can", "cannot", "cant", "cant", "caption",
                      "cause", "causes", "certain", "certainly", "changes", "clearly", "cmon", "co",
                      "co.", "com", "come", "comes", "concerning", "consequently", "consider",
                      "considering", "contain", "containing", "contains", "corresponding", "could",
                      "couldnt", "course", "cs", "currently", "dare", "darent", "definitely",
                      "described", "despite", "did", "didnt", "different", "directly", "do", "does",
                      "doesnt", "doing", "done", "dont", "down", "downwards", "during", "each", "edu",
                      "eg", "eight", "eighty", "either", "else", "elsewhere", "end", "ending", "enough",
                      "entirely", "especially", "et", "etc", "even", "ever", "evermore", "every",
                      "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example",
                      "except", "fairly", "far", "farther", "few", "fewer", "fifth", "first", "five",
                      "followed", "following", "follows", "forever", "former", "formerly", "forth",
                      "forward", "found", "four", "further", "furthermore", "get", "gets",
                      "getting", "given", "gives", "go", "goes", "going", "gone", "got", "gotten",
                      "greetings", "had", "hadnt", "half", "happens", "hardly", "has", "hasnt",
                      "havent", "having", "hed", "hell", "hello", "help", "hence",
                      "here", "hereafter", "hereby", "herein", "heres", "hereupon", "hers", "herself",
                      "hes", "hi", "himself", "hither", "hopefully", "how", "howbeit",
                      "however", "hundred", "id", "ie", "if", "ignored", "ill", "im", "immediate",
                      "inasmuch", "inc", "inc.", "indeed", "indicate", "indicated", "indicates",
                      "inner", "inside", "insofar", "instead", "into", "inward", "isnt",
                      "itd", "itll", "its", "its", "itself", "ive", "just", "k", "keep", "keeps",
                      "kept", "know", "known", "knows", "last", "lately", "later", "latter", "latterly",
                      "least", "less", "lest", "let", "lets", "like", "liked", "likely", "likewise",
                      "little", "look", "looking", "looks", "low", "lower", "ltd", "made", "mainly",
                      "make", "makes", "many", "may", "maybe", "maynt", "mean", "meantime",
                      "meanwhile", "merely", "might", "mightnt", "mine", "minus", "miss", "more",
                      "moreover", "most", "mostly", "mr", "mrs", "much", "must", "mustnt",
                      "myself", "name", "namely", "nd", "near", "nearly", "necessary", "need", "neednt",
                      "needs", "neither", "never", "neverf", "neverless", "nevertheless", "new", "next",
                      "nine", "ninety", "nobody", "non", "none", "nonetheless", "noone", "no-one",
                      "nor", "normally", "nothing", "notwithstanding", "novel", "now", "nowhere",
                      "obviously", "off", "often", "oh", "ok", "okay", "old", "once",
                      "ones", "ones", "only", "onto", "opposite", "other", "others",
                      "otherwise", "ought", "oughtnt", "our", "ours", "ourselves", "out", "outside",
                      "over", "overall", "own", "particular", "particularly", "past", "per", "perhaps",
                      "placed", "please", "plus", "possible", "presumably", "probably", "provided",
                      "provides", "que", "quite", "qv", "rather", "rd", "re", "really", "reasonably",
                      "recent", "recently", "regarding", "regardless", "regards", "relatively",
                      "respectively", "right", "round", "said", "same", "saw", "say", "saying", "says",
                      "second", "secondly", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen",
                      "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several",
                      "shall", "shant", "she", "shed", "shell", "shes", "should", "shouldnt",
                      "since", "six", "some", "somebody", "someday", "somehow", "someone",
                      "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry",
                      "specified", "specify", "specifying", "still", "sub", "such", "sup", "sure", "take",
                      "taken", "taking", "tell", "tends", "th", "than", "thank", "thanks", "thanx",
                      "thatll", "thats", "thats", "thatve", "their", "theirs", "them",
                      "themselves", "then", "thence", "thereafter", "thereby", "thered",
                      "therefore", "therein", "therell", "therere", "theres", "theres", "thereupon",
                      "thereve", "these", "theyd", "theyll", "theyre", "theyve", "thing",
                      "things", "think", "third", "thirty", "thorough", "thoroughly", "those",
                      "though", "three", "through", "throughout", "thru", "thus", "till",
                      "together", "too", "took", "toward", "towards", "tried", "tries", "truly", "try",
                      "trying", "ts", "twice", "two", "un", "under", "underneath", "undoing",
                      "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "up", "upon",
                      "upwards", "us", "use", "used", "useful", "uses", "using", "usually", "v",
                      "value", "various", "versus", "very", "via", "viz", "vs", "want", "wants",
                      "wasnt", "way", "we", "wed", "welcome", "well", "well", "went", "were",
                      "were", "werent", "weve", "what", "whatever", "whatll", "whats", "whatve",
                      "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein",
                      "wheres", "whereupon", "wherever", "whether", "which", "whichever", "while",
                      "whilst", "whither", "who", "whod", "whoever", "whole", "wholl", "whom",
                      "whomever", "whos", "whose", "why", "will", "willing", "wish", "within",
                      "without", "wonder", "wont", "would", "wouldnt", "yes", "yet", "youd",
                      "youll", "your", "youre", "yours", "yourself", "yourselves", "youve", "zero",
                      "hows", "whens", "whys", "b", "c", "d", "e", "f", "g", "h",
                      "j", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "uucp", "w", "x",
                      "y", "z", "www", "amount", "bill", "bottom", "call", "computer", "con",
                      "couldnt", "cry", "de", "describe", "detail", "due", "eleven", "empty", "fifteen",
                      "fifty", "fill", "find", "fire", "forty", "front", "full", "give", "hasnt",
                      "herse", "himse", "interest", "itse”", "mill", "move", "myse”", "part", "put",
                      "show", "side", "sincere", "sixty", "system", "ten", "thick", "thin", "top",
                      "twelve", "twenty", "abst", "accordance", "act", "added", "adopted", "affected",
                      "affecting", "affects", "ah", "announce", "anymore", "apparently", "approximately",
                      "aren", "arent", "arise", "auth", "beginning", "beginnings", "begins", "biol",
                      "briefly", "ca", "date", "ed", "effect", "et-al", "ff", "fix", "gave", "giving",
                      "heres", "hes", "hid", "home", "id", "im", "immediately", "importance", "important",
                      "index", "information", "invention", "itd", "keys", "kg", "km", "largely", "lets",
                      "line", "ll", "means", "mg", "million", "ml", "mug", "na", "nay", "necessarily",
                      "nos", "noted", "obtain", "obtained", "omitted", "ord", "owing", "page", "pages",
                      "poorly", "possibly", "potentially", "pp", "predominantly", "present", "previously",
                      "primarily", "promptly", "proud", "quickly", "ran", "readily", "ref", "refs",
                      "related", "research", "resulted", "resulting", "results", "run", "sec", "section",
                      "shed", "shes", "showed", "shown", "showns", "shows", "significant", "significantly",
                      "similar", "similarly", "slightly", "somethan", "specifically", "state", "states",
                      "stop", "strongly", "substantially", "successfully", "sufficiently", "suggest",
                      "thered", "thereof", "there", "thereto", "theyd", "theyre", "thou", "though",
                      "thousand", "through", "til", "tip", "ts", "ups", "usefully", "usefulness", "ve",
                      "vol", "vols", "wed", "whats", "wheres", "whim", "whod", "whos", "widely",
                      "words", "world", "youd", "youre"]

    splitWords1 = book_1.split()
    splitWords2 = book_2.split()

    punc = '''!()-[]{};:'"“”\,1234567890’—<>./?@#$%^&*_~'''

    for i in range(len(splitWords1)):
        splitWords1[i] = splitWords1[i].lower()  # LowerCase part
        for ele in splitWords1[i]:  # removing punctuation
            if ele in punc:
                splitWords1[i] = splitWords1[i].replace(ele, "")

    for i in range(len(splitWords2)):
        splitWords2[i] = splitWords2[i].lower()  # LowerCase part
        for ele in splitWords2[i]:  # removing punctuation
            if ele in punc:
                splitWords2[i] = splitWords2[i].replace(ele, "")

    New_Splitted_Words1 = []  # I created a new list because when I do it with remove it takes up to 3-4 minutes but adding it to a new list takes a few seconds
    for word in splitWords1.copy():
        if word not in stop_word_list:
            New_Splitted_Words1.append(word)

    New_Splitted_Words2 = []  # I created a new list because when I do it with remove it takes up to 3-4 minutes but adding it to a new list takes a few seconds
    for word in splitWords2.copy():
        if word not in stop_word_list:
            New_Splitted_Words2.append(word)

    allWords1 = {}
    new_word = ''
    flag = False
    for i in range(
            len(New_Splitted_Words1) - Word_Order):  # space checks and word counting part according to given word_order
        for j in range(Word_Order):
            if New_Splitted_Words1[i + j] == ' ' or New_Splitted_Words1[i + j] == '':
                flag = True
                break
            else:
                new_word += New_Splitted_Words1[i + j] + ' '
        if not flag:  # If the flag is true, it means a space, so no appending is done.
            if new_word not in allWords1:
                allWords1[new_word] = 1
            else:
                allWords1[new_word] += 1
        flag = False
        new_word = ''

    allWords2 = {}
    new_word = ''
    flag = False
    for i in range(
            len(New_Splitted_Words2) - Word_Order):  # space checks and word counting part according to given word_order
        for j in range(Word_Order):
            if New_Splitted_Words2[i + j] == ' ' or New_Splitted_Words2[i + j] == '':
                flag = True
                break
            else:
                new_word += New_Splitted_Words2[i + j] + ' '
        if not flag:  # If the flag is true, it means a space, so no appending is done.
            if new_word not in allWords2:
                allWords2[new_word] = 1
            else:
                allWords2[new_word] += 1
        flag = False
        new_word = ''

    all_words_in_two_books = {}

    for word1 in allWords1:  # the part that adds the words in the two books to the new dictionary
        if word1 in allWords2:
            all_words_in_two_books[word1] = allWords1[word1] + allWords2[word1]
        else:  # the part that adds words in one book that are not in the other to the new dictionary
            all_words_in_two_books[word1] = allWords1[word1]

    for word2 in allWords2:  # the part that adds words in one book that are not in the other to the new dictionary
        if word2 not in all_words_in_two_books:
            all_words_in_two_books[word2] = allWords2[word2]

    listed_words = dict(
        sorted(all_words_in_two_books.items(), key=operator.itemgetter(1), reverse=True))  # sorting dictionary

    if os.path.exists(File_Output):  # the part that checks if there is a file with that name
        os.remove(File_Output)

    open_output_file = open(File_Output, "x", encoding='utf-8')
    open_output_file.close()
    Output = open(File_Output, "a", encoding='utf-8')

    Output.write('| TOTAL     | BOOK 1    | BOOK 2    | WORD     | \n')
    Output.write('| ORDER     | ORDER     | ORDER     | ORDER    | \n')
    Output.write('| FREQUENCY | FREQUENCY | FREQUENCY | SEQUENCE | \n')
    Output.write('------------------------------------------------ \n')
    for key in listed_words.keys():
        if key not in allWords1:  # The part where words that are in one book but not in the other are added to the other dictionary with a value of 0
            allWords1[key] = 0
        elif key not in allWords2:
            allWords2[key] = 0
        line = '{:>7}     | {:>7}   |{:>7}    |{:>8}\n'.format(listed_words[key], allWords1[key], allWords2[key], key)
        Output.write(line)
    Output.close()


#main()
