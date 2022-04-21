class Solution:
    def lengthLongestPath(self, input: str) -> int:
        st = []
        ans, i, n = 0, 0, len(input)
        while i < n:
            # 检测当前文件的深度
            depth = 1
            while i < n and input[i] == '\t':
                depth += 1
                i += 1

            # 统计当前文件名的长度
            length, isFile = 0, False
            while i < n and input[i] != '\n':
                if input[i] == '.':
                    isFile = True
                length += 1
                i += 1
            i += 1  # 跳过换行符

            while len(st) >= depth:
                st.pop()
            if st:
                length += st[-1] + 1
            if isFile:
                ans = max(ans, length)
            else:
                st.append(length)
        return ans