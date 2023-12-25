import json
import requests

from collections import defaultdict

if __name__ == "__main__":
    resp = requests.get(
        "https://raw.githubusercontent.com/benjamincrom/scrabble/master/scrabble/dictionary.json"
    )

    full_list = resp.json()
    dictionary_by_len = defaultdict(list)

    # Seperate all words by lengths
    for word in full_list:
        dictionary_by_len[len(word)].append(word)

    # Create indices based on first two letters
    for length in dictionary_by_len:
        word_list = list(dictionary_by_len[length])
        indexed_dictionary = defaultdict(list)

        for word in word_list:
            indexed_dictionary[word[:2]].append(word)

        dictionary_by_len[length] = indexed_dictionary

    with open("utils/constants/dictionary.py", "w+") as f:
        json.dump(dictionary_by_len, f, ensure_ascii=False, indent=2)
