import re


def abbreviate(words):
    words = re.findall(r"[\w']+", words)
    result_word = ''
    for word in words:
        result_word += word.replace('_', '')[0]
    return result_word.upper()

