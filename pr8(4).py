import re


def main(source):
    pattern = r'\{([a-z,_0-9]*)\}\|>"([a-z_0-9]*)\"'
    i = {}
    spaceremover = source.replace(" ", "").replace("\n", "")
    new = re.findall(pattern, spaceremover)
    for news in new:
        i[news[1]] = news[0].replace(",", ",").split(",")
    return i


print(main("""
<block><section>option { eratier , ence_189 }|> "leor_709";
</section>, <section>option { diar , cees} |> "rige_343"; </section>,
<section> option { lele_858 , rati_14, biiste } |> "veraen";
</section>, </block>
"""))