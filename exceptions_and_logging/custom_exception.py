class MinorAgedNotAllowedException(Exception):
    def __init__(self, msg):
        self.msg = msg


def can_we_allow(age):
    if age >= 18:
        print("We can allow")
    else:
        raise MinorAgedNotAllowedException(
            f"Only Adults and above aged persons are allowed, grow up first and wait for {18 - age} years :(")


can_we_allow(23)
can_we_allow(9)
