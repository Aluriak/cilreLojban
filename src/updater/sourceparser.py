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
        if line != '':

            # split, tuple and return
            return tuple(map(lambda _ : _.strip(),
                             [line[:8],
                              line[8:21],
                              line[21:42],
                              line[42:63],
                              line[63:160],
                              line[160:170],
                              line[170:]
                             ]))

        else: return None
