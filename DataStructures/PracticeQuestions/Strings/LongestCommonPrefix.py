def longestCommonPrefix(self, strs):
        prefix = strs[0] if strs else ''
        while True:
            if all(s.startswith(prefix) for s in strs):
                return prefix
            prefix = prefix[:-1]