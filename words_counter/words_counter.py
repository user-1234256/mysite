from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import re
from collections import Counter

# to do: add error handling

def tag_visible(element):
    if element.parent.name in [
            'style', 'script', 'head', 'title', 'meta', '[document]'
    ]:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(url):

    html = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(html, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)

    visible_text_string = " ".join(t.strip().lower() for t in visible_texts)

    pattern = r"[^\w\d\s\']+|(?<=\s)'|'(?=\s)"

    """
    Regex explanation:

    [^] matches everything but everything inside the blockquotes
    \w matches any word character (equal to [a-zA-Z0-9_])
    \d matches a digit (equal to [0-9])
    \s matches any whitespace character (equal to [\r\n\t\f\v ])
    \' matches the character ' literally (case sensitive)
    + matches between one and unlimited times, as many times as possible, giving back as needed
    | - or
    (?<=\s)' Match ' preceded by a whitespace char - to remove quotes
    '(?=\s) Match ' when followed by a whitespace char - to remove quotes
    """


    text = re.sub(pattern, '', visible_text_string)

    words_list = text.split()

    return words_list


def count_words(words_list, sort_method=None):
    counter = Counter(words_list)

    if sort_method == 'word_count':
        return counter.most_common()
    elif sort_method == 'alphabetical':
        return sorted(counter.items())
    else:
        return list(counter.items())


def main(url, sort_method=None):
    words_list = text_from_html(url)
    result = count_words(words_list, sort_method)
    return result
