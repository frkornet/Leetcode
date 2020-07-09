class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p_idx, p_lookahead, p_len = 0, '', len(p)
        s_idx, s_len = 0, len(s)

        def next_char(s, s_idx, s_len):
            if s_idx>=0 and s_idx <= s_len - 1:
               return s[s_idx], s_idx + 1 
            else: 
                return '', -1

        def string_end(s_idx, s_len):
            return s_idx > s_len - 1

        def process_repetition():
            rep_char = p[p_idx]
            s_lookahead = s_idx
            while ( 
                not string_end(s_lookahead, s_len) and
                (s[s_lookahead] == rep_char or rep_char == '.')
            ):
                s_lookahead += 1
            
            while s_lookahead >= s_idx:
                s_arg = '' if string_end(s_lookahead, s_len) else s[s_lookahead:]
                p_arg = '' if string_end(p_idx + 2, p_len) else p[p_idx + 2:]
                if self.isMatch(s_arg, p_arg):
                    return True
                s_lookahead -= 1

            return False

        while not string_end(p_idx, p_len) or string_end(s_idx,s_len):
            if string_end(s_idx, s_len) and string_end(p_idx, p_len):
                return True
            
            p_lookahead = '' if string_end(p_idx + 1, p_len) else p[p_idx + 1]
            if p_lookahead == "*":
                return process_repetition()

            s_char, s_idx = next_char(s, s_idx, s_len)
            p_char, p_idx = next_char(p, p_idx, p_len)

            if ( s_char == '' or 
                 (p_char != '.' and s_char != p_char)
            ):
                return False
            
        return False

test_cases= [ ("aa", "a", False), 
              ("aa", "a*", True),
              ("ab", "a*", False), 
              ("ab", ".*", True), 
              ("aab", "c*a*b", True),
              ("aab", "c*a*b*", True),
              ("mississippi", "mis*is*p*", False),
              ("missississippi", "mis*is*p*", False),
              ("a", "ab*", True),
              ("a", "ab", False),
              ("a", "a*b", False),
              ("a", ".*..a*", False),
            ]

if __name__ == "__main__":
    soln = Solution()
    for s, p , result in test_cases:
        output = soln.isMatch(s,p)
        warning = '' if output == result else "ERROR!"
        print(f"s={s} p={p} output={output} {warning}")

    print("Done")