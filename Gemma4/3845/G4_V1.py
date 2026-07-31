class Solution(object):
    def maxXor(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def get_max_xor_subarray(arr):
            """Findet den maximalen XOR-Wert eines Subarrays innerhalb eines segments."""
            if not arr:
                return 0
            
            # Trie-basierter Ansatz für Max-XOR-Subarray
            # Wir speichern die Prefix-XORs im Trie
            max_val = 0
            prefix_xor = 0
            trie = {}
            
            def insert(val):
                node = trie
                for i in range(15, -1, -1):
                    bit = (val >> i) & 1
                    if bit not in node:
                        node[bit] = {}
                    node = node[bit]
            
            def query(val):
                node = trie
                current_xor = 0
                for i in range(15, -1, -1):
                    bit = (val >> i) & 1
                    wanted = 1 - bit
                    if wanted in node:
                        current_xor |= (1 << i)
                        node = node[wanted]
                    elif bit in node:
                        node = node[bit]
                    else:
                        return 0
                return current_xor

            insert(0)
            for x in arr:
                prefix_xor ^= x
                max_val = max(max_val, query(prefix_xor))
                insert(prefix_xor)
            
            return max_val

        unique_nums = sorted(set(nums))
        global_max_xor = 0
        
        # Wir iterieren über jeden möglichen Minimalwert v im Array.
        # Alle Elemente des Subarrays müssen im Bereich [v, v + k] liegen.
        for v in unique_nums:
            # Wir suchen nur nach Intervallen, in denen v tatsächlich das Minimum sein könnte.
            # Das bedeutet, wir betrachten alle zusammenhängenden Segmente aus Elementen in [v, v+k].
            
            segments = []
            current_segment = []
            
            for x in nums:
                if v <= x <= v + k:
                    current_segment.append(x)
                else:
                    if current_segment:
                        segments.append(current_segment)
                        current_segment = []
            if current_segment:
                segments.append(current_segment)
            
            # Für jedes valide Segment berechnen wir den Max-XOR
            for seg in segments:
                # Optimierung: Nur berechnen, wenn das Segment groß genug oder 
                # potenziell besser als das bisherige Ergebnis ist.
                global_max_xor = max(global_max_xor, get_max_xor_subarray(seg))
        
        return global_max_xor
