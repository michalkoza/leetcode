from typing import List


class Solution:
    def rectangleArea(self, input: List[List[int]]):

        def is_in(rect1, rect2):
            return (
                rect1[0] >= rect2[0]
                and rect1[2] <= rect2[2]
                and rect1[1] >= rect2[1]
                and rect1[3] <= rect2[3]
            )

        xs = sorted({x for x1, _, x2, _ in input for x in [x1, x2]})
        ys = sorted({y for _, y1, _, y2 in input for y in [y1, y2]})

        area = 0

        for x1, x2 in zip(xs, xs[1:]):
            for y1, y2 in zip(ys, ys[1:]):
                sub_rectangle = (x1, y1, x2, y2)
                if any(is_in(sub_rectangle, rectangle) for rectangle in input):
                    new_area = (sub_rectangle[2] - sub_rectangle[0]) * (
                        sub_rectangle[3] - sub_rectangle[1]
                    )
                    area = (area + new_area) % (10**9 + 7)
        return area
