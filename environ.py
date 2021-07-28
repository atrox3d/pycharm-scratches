import os, os.path
from string import Template

# t = Template("export GH_PUBLIC_REPOS=users/${GH_USER}/repos")
# name = "GH_USER"
# value = "atrox3d"
# d = {name:value}
# print(t.substitute(d))

os.environ["GH_USER"] = "atrox3d"
print(os.environ["GH_USER"])
print(os.path.expandvars("users/${GH_USER}/repos"))

os.environ["GH_PUBLIC_REPOS"] = "users/${GH_USER}/repos"
print(os.environ["GH_PUBLIC_REPOS"])

os.environ["GH_PUBLIC_REPOS"] = os.path.expandvars("users/${GH_USERa}/repos")
print(os.environ["GH_PUBLIC_REPOS"])
