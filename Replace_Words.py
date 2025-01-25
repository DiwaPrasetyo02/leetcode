from typing import List
class Solution:
    def findRoot(self, word, dictSet):
        for head in range(1, len(word)):
            if word[:head] in dictSet:
                return word[:head]
        return word

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        setDict = set(dictionary)
        sentenceInList = sentence.split(" ")

        returnList = [self.findRoot(w, setDict) for w in sentenceInList]

        return " ".join(returnList)