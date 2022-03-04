class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s_, paths_, res_):
            if not s_ and len(paths_) == 4:
                res_.append('.'.join(paths_))
                return
            if len(s_) > (4 - len(paths_)) * 3:
                return
            for i in range(1, 4):
                if i > len(s_):
                    continue
                if s_[0] == '0' and len(s_[:i]) > 1:
                    continue
                if int(s_[:i]) <= 255:
                    dfs(s_[i:], paths_ + [s_[:i]], res_)
            # pass
        paths = []
        res = []
        dfs(s, paths, res)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.restoreIpAddresses("255255255255"))
    print(solution.restoreIpAddresses("0000"))
