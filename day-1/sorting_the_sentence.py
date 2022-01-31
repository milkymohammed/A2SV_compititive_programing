class Solution:
    def sortSentence(self, s: str) -> str:
        sentence = ""
        wordSet = {}
        for c in s:
            if(c.isdigit()):
                sentence +=c
                wordSet[sentence[-1]] = sentence[:-1]
                sentence = ""
            elif(c == ' '):
                continue;
            else:
                sentence += c
        sentence = ""
        for i  in sorted(wordSet):
            sentence += wordSet[i]
            sentence += " "
        return sentence[:-1]
