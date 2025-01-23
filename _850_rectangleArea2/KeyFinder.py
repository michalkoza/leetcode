from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Rectangle:
    left: int
    right: int
    top: int
    down: int

    def is_in(self, rectangle: "Rectangle"):
        return (
            self.left >= rectangle.left
            and self.right <= rectangle.right
            and self.top <= rectangle.top
            and self.down >= rectangle.down
        )

    def area(self):
        return (self.right - self.left) * (self.top - self.down)


class Solution:
    def rectangleArea(self, input: List[List[int]]):
        xs = sorted({x for x1, _, x2, _ in input for x in [x1, x2]})
        ys = sorted({y for _, y1, _, y2 in input for y in [y1, y2]})

        rectangles = [
            Rectangle(left=left, right=right, top=top, down=down)
            for left, down, right, top in input
        ]
        sub_rectangles = set()

        for x1, x2 in zip(xs, xs[1:]):
            for y1, y2 in zip(ys, ys[1:]):
                sub_rectangles.add(Rectangle(left=x1, right=x2, down=y1, top=y2))

        area = 0

        for sub_rectangle in sub_rectangles:
            if any(sub_rectangle.is_in(rectangle) for rectangle in rectangles):
                area += sub_rectangle.area()
                area %= 10**9 + 7
            else:
                print(f"not counting {sub_rectangle}")
                g = any(sub_rectangle.is_in(rectangle) for rectangle in rectangles)
                print(g)
        return area
