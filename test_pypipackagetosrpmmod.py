import os
import sys
import unittest


sys.path.append(os.path.dirname(__file__))


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
            "python2-httplib2 < 1dev",
            "python2-httplib2 >= 0.9.2",
            "python2-google-auth >= 1.4.1",
            "python2-google-auth-httplib2 >= 0.0.3",
            "python2-someshit >= 0.0.4",
            "python2-six < 2dev",
            "python2-six >= 1.6.1",
            "python2-uritemplate < 4dev",
            "python2-uritemplate >= 3.0.0",
        ]
        out_ = mod.gen_requires(in_)
        self.assertEqual(exp_, out_)
