class anagram_generator:
    '''Simple Anagram Generator which uses the 'shuffle' function in the python
'random' module:

    Args:
            word    (string)    :    word to re-arrange
    '''
    def __init__(self, word_list):
        self._words = word_list
        for word in self._words:
            print self._scramble(word)

    def _scramble(self, word):
        from random import shuffle
        _as_list = list(word)
        shuffle(_as_list)
        return ''.join(_as_list)
