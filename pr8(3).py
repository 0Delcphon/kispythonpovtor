import re


def main(source):
    pattern = r'\`([a-z_0-9]*)->@\'([a-z_0-9]*)\''
    i = {}
    spaceromvers = source.replace(" ", "").replace("\n", "")
    new = re.findall(pattern, spaceromvers)
    for news in new:
        i[news[1]] = news[0]
    return i


print(main("""
{<% `edre_257 ->@'xebi_602'; %>. <% `inat_612 ->@'enerat'; %>. <%
`dila_874 -> @'eddied'; %>. <% `xevete_494 ->@'aon'; %>. }
"""))
