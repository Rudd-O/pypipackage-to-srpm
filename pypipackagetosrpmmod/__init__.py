import sys

__version__ = "0.0.20"


def mangle_name(name):
  name = name.rstrip()
  # special case dnspython.
  if name == "dnspython":
      return "python%s-dns" % (sys.version_info.major, )
  if "asn1-modules" in name:
      return "python%s-pyasn1-modules" % (sys.version_info.major, )
  if "asn1" in name:
      return "python%s-pyasn1" % (sys.version_info.major, )
  if name == "BeautifulSoup4":
      name = "beautifulsoup4"
  if name == "Jinja2":
      name = "jinja2"
  if name == "Werkzeug":
      name = "werkzeug"
  if name == "Babel":
      name = "babel"
  if name.startswith("python"):
    return name
  # Special case pytz.
  if name.startswith("pytz"):
    return "python%s-%s" % (sys.version_info.major, name)
  if name.startswith("PySocks") or name.startswith("pyaes"):
    return "python%s-%s" % (sys.version_info.major, name.lower())
  if name.startswith("py"):
    return "python%s-%s" % (sys.version_info.major, name[2:])
  return "python%s-%s" % (sys.version_info.major, name)


def gen_requires(in_reqs):
  requires = []
  for l in in_reqs:
    l = l.strip()
    l = l.replace(" ", "")
    if not l:
      continue
    if l.startswith("["):
        break
    toks = l.split(",")
    pkg = None
    for tok in toks:
        seps = [">=", "<=", ">", "<", "==", "~=", None]
        ver = None
        for sep in seps:
            if sep is None:
                pass
            elif sep in tok:
                tok, ver = tok.split(sep)
                tok, ver = tok.strip(), ver.strip()
                if sep == "~=":
                    sep = ">="
                break
        assert not (ver is None and sep is not None)
        assert not (sep is None and ver is not None)
        if tok.strip():
            pkg = tok.strip()
        if ver is None:
            dep = mangle_name(pkg)
        else:
            dep = mangle_name(pkg) + " " + sep + " " + ver
        requires.append(dep)
  return requires
