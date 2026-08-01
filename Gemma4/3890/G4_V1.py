class Solution(object):

    def findGoodIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Dictionary, um zu zählen, wie oft eine Summe von zwei Kubikzahlen vorkommt
        counts = {}
        
        # Wir iterieren durch alle möglichen Werte von a und b.
        # Da a <= b gilt und n maximal 10^9 ist, geht a und b maximal bis 1000.
        # Die Obergrenze für a liegt bei der Kubikwurzel von (n / 2).
        limit = int(n**(1/3)) + 2  # +2 als Sicherheitspuffer für Rundungsfehler
        
        for a in range(1, limit):
            a3 = a**3
            if a3 >= n: 
                break
            
            for b in range(a, limit):
                val = a3 + b**3
                
                # Wenn die Summe das Limit überschreitet, können wir für dieses 'a' 
                # aufhören, weitere 'b' zu testen, da b nur noch größer wird.
                if val > n:
                    break
                
                # Zähle die Vorkommen der Summe x = a^3 + b^3
                counts[val] = counts.get(val, 0) + 1
        
        # Wir filtern alle Zahlen heraus, die mindestens zweimal vorkamen (mindestens zwei Paare).
        good_integers = [x for x, count in counts.items() if count >= 2]
        
        # Das Ergebnis muss aufsteigend sortiert sein.
        good_integers.sort()
        
        return good_integers
