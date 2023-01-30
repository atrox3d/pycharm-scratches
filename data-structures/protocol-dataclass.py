from dataclasses import dataclass


@dataclass
class Protocols:
    arp = "arp"
    bootp = "bootp"
    icmp = "icmp"
    all = "all"


p = Protocols()
print(p.arp)
print("arp" in p)
print(p["arp"])

exit()

protocols = dict(arp="arp", bootp="bootp", icmp="icmp", all="all")
protocols["0"] = "all"
p = lambda: None
p.__dict__.update(protocols)
print(p.arp)
# print(p["0"])
