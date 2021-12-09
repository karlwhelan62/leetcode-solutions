class Solution:

    def isValid(self, s: str) -> bool:

        char_dict = { "(": ")",
                      "[": "]",
                      "{": "}"}

        # replace all instances of open and close chars next to each other
        # Saves on time and memory adding, removing them from the stack
        s = s.replace("()", ""). replace("[]", "").replace("{}", "")

        # stack for holding opened chars
        char_stack = []
        for c in s:
            if c in char_dict:
                char_stack.append(c)
            # if close char, check if matches last open char or if no open char   
            elif not char_stack or char_dict[char_stack.pop()] != c:
                return False

        # if stack is empty all chars have been closed
        return not char_stack
