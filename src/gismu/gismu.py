#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# gismu.py
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


#########################
# CLASS GISMU           #
#########################
class Gismu:
    """
Definition of a Gismu, with rafsi, translation in english, definition, 
references to another gismu,...
    """

# CONSTRUCTOR #################################################################
    def __init__(self, name, rafsi, english, globenglish, 
                 definition, unknow, comment):
            # attributes
            self.name, self.rafsi, self.english = name, rafsi, english
            self.globenglish, self.definition = globenglish, definition
            self.unknow, self.comment = unknow, comment



# CONVERSION ##################################################################
    def __str__(self):
        return(   "GISMU      : " + self.name
              + "\nrafsi      : " + self.rafsi
              + "\nenglish    : " + self.english
              + "\nconcept    : " + self.globenglish
              + "\ndefinition : " + self.definition
              + "\nunknow     : " + self.unknow
              + "\ncomment    : " + self.comment
        )



