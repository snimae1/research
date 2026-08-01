class Solution(object):

    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        # dp[i][j] speichert alle möglichen XOR-Werte, 
        # die man erreichen kann, wenn man bei (i, j) ankommt.
        # Wir nutzen eine Liste von Sets für die DP-Tabelle.
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        # Startpunkt initialisieren
        dp[0][0].add(grid[0][0])
        
        # Die erste Zeile füllen (man kann nur von links kommen)
        for j in range(1, n):
            val = grid[0][j]
            for prev_xor in dp[0][j-1]:
                dp[0][j].add(prev_xor ^ val)
                
        # Die erste Spalte füllen (man kann nur von oben kommen)
        for i in range(1, m):
            val = grid[i][0]
            for prev_xor in dp[i-1][0]:
                dp[i][0].add(prev_xor ^ val)
                
        # Den Rest der Matrix füllen
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                # Werte von oben übernehmen und XOR-en
                for prev_xor in dp[i-1][j]:
                    dp[i][j].add(prev_xor ^ val)
                # Werte von links übernehmen und XOR-en
                for prev_xor in dp[i][j-1]:
                    dp[i][j].add(prev_xor ^ val)
        
        # Das Ergebnis ist der kleinste Wert im Set des Zielfeldes (m-1, n-1)
        return min(dp[m-1][n-1])
