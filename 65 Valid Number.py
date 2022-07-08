class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()

        parts = s.split("e")
        if len(parts) > 2:
            return False

        for i, part in enumerate(parts):
            if not part:
                return False

            if part[0] in ("-", "+"):
                part = part[1:]

            seen_dot = False
            seen_digit = False

            for val in part:
                if val == ".":
                    if seen_dot or i == 1:
                        return False
                    else:
                        seen_dot = True

                elif val.isdigit():
                    seen_digit = True

                else:
                    return False

            if not seen_digit:
                return False

        return True