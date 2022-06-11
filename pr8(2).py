import re


def main(source):
    pattern = r"([0-9-]*)to([a-z_0-9']*)"
    i = {}
    spaceremove = source.replace(" ", "").replace("\n", "")
    new = re.findall(pattern, spaceremove)
    for news in new:
        i[news[1].replace("'", "")] = int(news[0])
    return i


print(main("""
|| equ #-4754 to 'anrebe' equ #-3318 to'soveis_1' equ#4681 to
'xeququ' ||
"""))
