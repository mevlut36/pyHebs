class textColor:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def rgbText(r, g, b, txt):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, txt)

