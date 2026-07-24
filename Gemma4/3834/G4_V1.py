class Solution(object):
    def mergeAdjacent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Wir verwenden einen Stack, um die Elemente zu speichern.
        # Der Stack erlaubt es uns, sofort auf das letzte Element zuzugreifen 
        # und zu prüfen, ob ein Merge möglich ist.
        stack = []
        
        for num in nums:
            current_val = num
            
            # Während der Stack nicht leer ist und das aktuelle Element 
            # dem obersten Element des Stacks entspricht:
            while stack and stack[-1] == current_val:
                # Wir nehmen das Element vom Stack weg und addieren es zum aktuellen Wert.
                # Das Ergebnis wird dann erneut gegen den neuen Stack-Top geprüft.
                current_val += stack.pop()
            
            # Wenn kein Merge mehr möglich ist, legen wir den (eventuell modifizierten) 
            # Wert auf den Stack.
            stack.append(current_val)
            
        return stack
