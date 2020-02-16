#
# @lc app=leetcode id=271 lang=python3
#
# [271] Encode and Decode Strings
#

# @lc code=start
if 0:
    class Codec:
        def encode(self, strs: [str]) -> str:
            """Encodes a list of strings to a single string.
            """

        def decode(self, s: str) -> [str]:
            """Decodes a single string to a list of strings.
        """

if 0:  #wangmazi

    class Codec:
        def encode(self, strs):
            # write your code here
            encoded = []
            for string in strs:
                for char in string:
                    if char == ":":
                        encoded.append("::")
                    else:
                        encoded.append(char)
                encoded.append(": ")
            # the res will always be ended with ": "
            # such as "lint: code: love: you: "
            return "".join(encoded)

        """
        @param: str: A string
        @return: dcodes a single string to a list of strings
        """
        def decode(self, str):
            # write your code here
            res = []
            idx = 0
            length = len(str)
            tmp_str = []
            # length - 1 because it always ends with ": "
            while idx < length - 1:
                if str[idx] == ":":
                    if str[idx + 1] == ":":
                        tmp_str.append(":")
                        idx += 2
                    elif str[idx + 1] == " ":
                        res.append("".join(tmp_str))
                        tmp_str = []
                        idx += 2
                else:
                    tmp_str.append(str[idx])
                    idx += 1
            return res
if 1:  # lmv
    class Codec:
        def encode(self, strs):
            return ''.join('%d:' % len(s) + s for s in strs)

        def decode(self, s):
            strs = []
            i = 0
            while i < len(s):
                j = s.find(':', i)
                i = j + 1 + int(s[i:j])
                strs.append(s[j+1:i])
            return strs

if 0:  # leetcode solution1

    class Codec:
        def encode(self, strs):
            """Encodes a list of strings to a single string.
            :type strs: List[str]
            :rtype: str
            """
            if len(strs) == 0:
                return chr(258)
            # encode here is a workaround to fix BE CodecDriver error
            return chr(258).join(x for x in strs)

        def decode(self, s):
            """Decodes a single string to a list of strings.
            :type s: str
            :rtype: List[str]
            """
            if s == chr(258):
                return []
            return s.split(chr(258))

if 0:  #leetcode solution2
    class Codec:
        def len_to_str(self, x):
            """
            Encodes length of string to bytes string
            """
            x = len(x)
            bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
            bytes.reverse()
            bytes_str = ''.join(bytes)
            return bytes_str

        def encode(self, strs):
            """Encodes a list of strings to a single string.
            :type strs: List[str]
            :rtype: str
            """
            # encode here is a workaround to fix BE CodecDriver error
            return ''.join(self.len_to_str(x) + x for x in strs)

        def str_to_int(self, bytes_str):
            """
            Decodes bytes string to integer.
            """
            result = 0
            for ch in bytes_str:
                result = result * 256 + ord(ch)
            return result

        def decode(self, s):
            """Decodes a single string to a list of strings.
            :type s: str
            :rtype: List[str]
            """
            i, n = 0, len(s)
            output = []
            while i < n:
                length = self.str_to_int(s[i: i + 4])
                i += 4
                output.append(s[i: i + length])
                i += length
            return output

S=Codec()
strs=["I", "don't", "care"]
S.encode(strs)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
# @lc code=end
