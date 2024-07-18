
def sort_anagrams(list_of_strings):
    anagrams_list = []
    seen_words = set()

    for word1 in list_of_strings:
        if word1 in seen_words:
            continue

        anagram_group = []
        sorted_word1 = ''.join(sorted(word1))

        for word2 in list_of_strings:
            sorted_word2 = ''.join(sorted(word2))
            if sorted_word1 == sorted_word2:
                anagram_group.append(word2)
                seen_words.add(word2)

        anagrams_list.append(anagram_group)

    return anagrams_list