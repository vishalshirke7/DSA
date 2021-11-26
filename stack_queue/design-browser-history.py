"""
https://leetcode.com/problems/design-browser-history/
"""

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = 0
        self.top = 0
        self.stack = [homepage]

    def visit(self, url: str) -> None:
        self.cur += 1
        if self.cur == len(self.stack):
            self.stack.append(url)
        else:
            self.stack[self.cur] = url
        self.top = self.cur

    def back(self, steps: int) -> str:
        self.cur = max(self.cur - steps, 0)
        return self.stack[self.cur]        

    def forward(self, steps: int) -> str:
        self.cur = min(self.cur + steps, self.top)
        return self.stack[self.cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)