class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # Kadane for k == 0
        if k == 0:
            max_ending = max_so_far = nums[0]
            for x in nums[1:]:
                max_ending = max(x, max_ending + x)
                max_so_far = max(max_so_far, max_ending)
            return max_so_far
        
        # If we can rearrange almost everything, take all positives
        if k >= n:
            pos_sum = sum(x for x in nums if x > 0)
            if pos_sum > 0:
                return pos_sum
            return max(nums)
        
        # Coordinate compression
        uniq = sorted(set(nums))
        M = len(uniq)
        val_to_rank = {v: i+1 for i, v in enumerate(uniq)}
        val_by_rank = [0] + uniq  # 1-indexed
        
        # Fenwick tree helpers (operate on external arrays)
        def fw_add(tree_count, tree_sum, idx, d_cnt, d_sum):
            while idx <= M:
                tree_count[idx] += d_cnt
                tree_sum[idx] += d_sum
                idx += idx & -idx
                
        def fw_pref_count(tree_count, idx):
            s = 0
            while idx > 0:
                s += tree_count[idx]
                idx -= idx & -idx
            return s
        
        def fw_pref_sum(tree_sum, idx):
            s = 0
            while idx > 0:
                s += tree_sum[idx]
                idx -= idx & -idx
            return s
        
        # Find k-th smallest element in a Fenwick tree
        # Precompute highest power of two for binary lifting
        highest_bit = 1 << (M.bit_length() - 1)
        def fw_kth(tree_count, k_val):
            idx = 0
            bit = highest_bit
            while bit:
                nxt = idx + bit
                if nxt <= M and tree_count[nxt] < k_val:
                    k_val -= tree_count[nxt]
                    idx = nxt
                bit >>= 1
            return idx + 1
        
        # Sum of the smallest x elements
        def sum_smallest(tree_count, tree_sum, total_cnt, x):
            if x <= 0:
                return 0
            rank = fw_kth(tree_count, x)
            cnt_before = fw_pref_count(tree_count, rank - 1)
            sum_before = fw_pref_sum(tree_sum, rank - 1)
            v = val_by_rank[rank]
            return sum_before + (x - cnt_before) * v
        
        max_ans = -10**18
        
        # Pre-fill total sum of all elements (constant)
        total_all_sum = sum(nums)
        
        for i in range(n):
            # inside arrays (initially empty)
            in_cnt = [0] * (M + 1)
            in_sum = [0] * (M + 1)
            total_in_cnt = 0
            total_in_s = 0
            
            # outside arrays (initially all elements)
            out_cnt = [0] * (M + 1)
            out_sum = [0] * (M + 1)
            total_out_cnt = n
            total_out_s = total_all_sum
            # build outside tree
            for val in nums:
                fw_add(out_cnt, out_sum, val_to_rank[val], 1, val)
                
            for j in range(i, n):
                val = nums[j]
                r = val_to_rank[val]
                # move val from outside to inside
                fw_add(in_cnt, in_sum, r, 1, val)
                total_in_cnt += 1
                total_in_s += val
                fw_add(out_cnt, out_sum, r, -1, -val)
                total_out_cnt -= 1
                total_out_s -= val
                
                max_x = min(k, total_in_cnt, total_out_cnt)
                if max_x == 0:
                    if total_in_s > max_ans:
                        max_ans = total_in_s
                    continue
                
                # Binary search for optimal number of beneficial swaps x
                # Find largest rank r such that out_ge(r) >= in_le(r)
                lo, hi = 1, M
                best_r = -1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    in_le = fw_pref_count(in_cnt, mid)
                    out_ge = total_out_cnt - fw_pref_count(out_cnt, mid - 1)
                    if out_ge >= in_le:
                        best_r = mid
                        lo = mid + 1
                    else:
                        hi = mid - 1
                
                if best_r == -1:
                    # out_ge < in_le everywhere -> max at r=1
                    out_ge1 = total_out_cnt  # fw_pref_count(out_cnt,0)=0
                    in_le1 = fw_pref_count(in_cnt, 1)
                    ans_x = min(out_ge1, in_le1)
                else:
                    out_ge_r = total_out_cnt - fw_pref_count(out_cnt, best_r - 1)
                    in_le_r = fw_pref_count(in_cnt, best_r)
                    cand1 = min(out_ge_r, in_le_r)
                    if best_r < M:
                        out_ge_r1 = total_out_cnt - fw_pref_count(out_cnt, best_r)
                        in_le_r1 = fw_pref_count(in_cnt, best_r + 1)
                        cand2 = min(out_ge_r1, in_le_r1)
                        ans_x = max(cand1, cand2)
                    else:
                        ans_x = cand1
                
                opt_x = min(ans_x, max_x)
                
                boost = 0
                if opt_x > 0:
                    sum_in_small = sum_smallest(in_cnt, in_sum, total_in_cnt, opt_x)
                    sum_out_large = total_out_s - sum_smallest(out_cnt, out_sum, total_out_cnt, total_out_cnt - opt_x)
                    boost = sum_out_large - sum_in_small
                
                cur = total_in_s + boost
                if cur > max_ans:
                    max_ans = cur
                    
        return max_ans
