import re


def main(source):
    pattern = r'\((["a-z_0-9.@]*)\)->@\'([a-z_0-9]*)\''
    i = {}
    spaceremove = source.replace(" ", "").replace("\n", "")
    new = re.findall(pattern, spaceremove)
    for news in new:
        i[news[1]] = news[0].replace("@", "").replace('"', "").replace(".", ",").split(",")
    return i


print(main("""
{ <: opt array( @"qulein" . @"ororge_119" )-> @'soesbi_408'; :><: opt
array( @"qusoan_852" . @"entiat_742" . @"onzaon" ) -> @'ismati';:>
<:opt array(@"diis" . @"ririti" . @"ceanri_97" . @"raleer_51"
)->@'riage_591'; :> <:opt array( @"quxe_187".
@"reedle_690")->@'tiordi'; :>}
"""))