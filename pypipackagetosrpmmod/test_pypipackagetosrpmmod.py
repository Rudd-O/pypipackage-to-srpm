import os
import sys
import unittest


sys.path.append(os.path.dirname(__file__))
pv = sys.version_info.major

import pypipackagetosrpmmod as mod


class TestRequires(unittest.TestCase):

    def test_weird_requires(self):
        in_ = """httplib2<1dev,>=0.9.2
google-auth>=1.4.1
google-auth-httplib2>=0.0.3
someshit~=0.0.4
six<2dev,>=1.6.1
uritemplate<4dev,>=3.0.0""".splitlines()
        exp_ = [
            "python%s-httplib2 < 1dev" % pv,
            "python%s-httplib2 >= 0.9.2" % pv,
            "python%s-google-auth >= 1.4.1" % pv,
            "python%s-google-auth-httplib2 >= 0.0.3" % pv,
            "python%s-someshit >= 0.0.4" % pv,
            "python%s-six < 2dev" % pv,
            "python%s-six >= 1.6.1" % pv,
            "python%s-uritemplate < 4dev" % pv,
            "python%s-uritemplate >= 3.0.0" % pv,
        ]
        out_ = mod.gen_requires(in_)
        self.assertEqual(exp_, out_)

    def test_mangle_name_enter(self):
        assert mod.mangle_name("Babel\n") == "python%s-babel" % pv
