score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(s):
    if type(s) != str:
        print "Please check your input"
        return "Error"
    else:
        your_score = 0
        s2 = s.lower()
        for i in range(len(s)):
            for j in score:
                if s2[i] == j:
                    your_score += score[j]
        print your_score
        return your_score
    
scrabble_score(8)