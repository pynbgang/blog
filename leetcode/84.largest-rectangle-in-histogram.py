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
# @lc code=end
