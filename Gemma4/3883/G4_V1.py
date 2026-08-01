class Solution(object):
    def countArrays(self, digitSum):
        """
        :type digitSum: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        MAX_VAL = 5000
        
        # Vorbereiten der Quersummen für alle Zahlen von 0 bis 5000
        # sum_digits[i] speichert die Summe der Ziffern der Zahl i
        sum_digits = [0] * (MAX_VAL + 1)
        for i in range(MAX_VAL + 1):
            s = 0
            temp = i
            while temp > 0:
                s += temp % 10
                temp //= 10
            sum_digits[i] = s

        n = len(digitSum)
        # dp[v] ist die Anzahl der validen Arrays, die mit dem Wert v enden.
        dp = [0] * (MAX_VAL + 1)
        
        # Initialisierung für das erste Element digitSum[0]
        first_sum = digitSum[0]
        for v in range(MAX_VAL + 1):
            if sum_digits[v] == first_sum:
                dp[v] = 1
        
        # Iteration über den Rest des digitSum-Arrays
        for i in range(1, n):
            current_target_sum = digitSum[i]
            
            # Wir berechnen eine Präfixsumme der vorherigen DP-Werte.
            # prefix_sum[v] ist die Summe von dp[0] bis dp[v-1].
            prefix_sum = [0] * (MAX_VAL + 2)
            for v in range(MAX_VAL + 1):
                prefix_sum[v+1] = (prefix_sum[v] + dp[v]) % MOD
            
            new_dp = [0] * (MAX_VAL + 1)
            # Eine Zahl v ist nur gültig, wenn ihre Quersumme passt.
            # Die Anzahl der Möglichkeiten ist die Summe aller vorangegangenen validen Zahlen (prefix_sum).
            for v in range(MAX_VAL + 1):
                if sum_digits[v] == current_target_sum:
                    new_dp[v] = prefix_sum[v+1]
            
            dp = new_dp
            
        # Das Ergebnis ist die Summe aller Werte in der letzten DP-Tabelle.
        return sum(dp) % MOD
