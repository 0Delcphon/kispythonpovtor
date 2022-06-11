import re


def main(source):
    pattern = r'\`([a-z_0-9]*)<-([0-9-]*)'
    i = {}
    spaceremover = source.replace(" ", "").replace("\n", "")
    new = re.findall(pattern, spaceremover)
    for news in new:
        i[news[0]] = int(news[1])
    return i


print(main("""
{{ {{ loc `veisat <- 6713}} {{loc `leorri_468<- 1868 }}{{ loc
`leeda_430 <- -9875}}}}
"""))