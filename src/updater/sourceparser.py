#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# sourceparser.py
#
# Copyright © 2014 Mathieu Gaborit (matael) <mathieu@matael.org>
#
#
# Distributed under WTFPL terms
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.
#

class Parser:

    def __init__(self, fh):

        self.fh = fh
        fh.seek(0)
        self.fh.readline() # first line is useless

    def __iter__(self):

        line = self.fh.readline()
        while line:

            # split, tuple and return
            yield tuple(map(lambda _ : _.strip(),
                             [line[:7],
                              line[7:20],
                              line[20:41],
                              line[41:62],
                              line[62:159],
                              line[159:169],
                              line[169:]
                             ]))
            line = self.fh.readline()

