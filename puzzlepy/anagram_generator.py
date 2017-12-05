class anagram_generator:
    '''Simple Anagram Generator which uses the 'shuffle' function in the python
'random' module:

    Args:
            word_list    (list of strings)    :    words to re-arrange
    '''
    def __init__(self, word_list):
        self._words = word_list
        self._result = []
        for word in self._words:
            self._result.append(self._scramble(word))

    def __str__(self):
        out_str = ''
        for word in self._result:
            out_str += word
            out_str += '\n'
        return out_str

    def _scramble(self, word):
        from random import shuffle
        _as_list = list(word)
        shuffle(_as_list)
        return ''.join(_as_list)
