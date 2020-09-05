#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea=[]
        for i in range(len(heights)):
            area=height=heights[i]
            for j in range(i, len(heights)):
                width=j-i+1
                height=min(height, heights[j])
                area=max(area, width*height)
            maxarea.append(area)
        return max(maxarea or [0])

class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, heights):
        ids, area = [], 0

        #1. 增加末尾高度0，统一算法最后一步的操作
        #2. 依次取每个高度的编号和值
        for id, height in enumerate(heights + [0]):
            #如果ids堆栈未取空，且突然遇到一个变小的高度：
            while ids and height < heights[ids[-1]]:
                # 弹出距离当前高度最近的编号
                popped_id = ids.pop()
                # 计算它的“左边界“编号：
                # 如果堆栈里还有，那么就是那个下一个（距离当前编号更远的）编号
                # 否则，用-1.这样抵消掉下面的减一算法，使得数字0代表宽度1
                left_id = ids[-1] if ids else -1
                #如果列表为空，则宽度为id，否则为id-ids[-1]-1
                # 计算从弹出编号，向左能拉长到的最远（直到左边界）宽度
                width = id - left_id - 1
                area = max(area, width * heights[popped_id])
            #否则，如果是递增或等高，或者堆栈取空（比较完了），依次压入堆栈中
            ids.append(id)
        return area

class Solution:     #(Sun 30 Aug 2020 08:07:45 PM DST)
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                max_area = max(min(heights[i:j+1]) * (j-i+1), max_area)
        return max_area

    """
    ||   ✘ Time Limit Exceeded
    ||   ✘ 94/96 cases passed (N/A)
    ||   ✘ Testcase: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,27
    """

class Solution:     #(Sun 30 Aug 2020 08:09:32 PM DST)
    def largestRectangleArea(self, heights: List[int]) -> int:
        return max(min(heights[i:j+1]) * (j-i+1) for i in range(len(heights)) for j in range(i, len(heights)))
# @lc code=end
