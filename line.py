#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright 2018(c). All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
# Author: Ing. Oraldo Jacinto Simon


class CountLine(object):
    '''Count the LOCs of a python module

    '''

    def is_import_line(self, line):
        '''Returns True if the line enters the import classification.

        '''
        if line.startswith("from") or line.startswith("import"):
            return True

    def is_comment_line(self, line):
        '''Returns True if the line enters the following classifications:
        comment, docstring or line break else False'

        '''

        if line.startswith("#") or line.startswith("'") or line == '' or line.endswith("'"):
            return True

    def is_definition_class(self, line):
        '''Returns True if the line is the definition of a class.

        '''
        if line.startswith("class"):
            return True

    def is_function(self, line):
        '''Returns True if the line is the definition of a function

        '''
        if line.startswith("def "):
            return True

    def extract_name_class(self, line):
        '''Returns the name of the class taken from the definition line.

        '''
        chain = line.split()
        name = chain[1].partition("(")
        return name[0]

    def count_line(self, lines):
        '''Return a dict() with the LOC of the list lines.

        '''
        result = {}
        exclude_line = 0
        line_class = 0
        function_line = 0
        valid_line = 0
        name_class = ''
        for line in lines:
            text = line.lstrip()
            if self.is_comment_line(text) or self.is_import_line(text):
                exclude_line += 1
            elif self.is_definition_class(text):
                name_class = self.extract_name_class(text)
                line_class += 1
            elif self.is_function(text):
                function_line += 1
            else:
                valid_line += 1
        total_lines = line_class + function_line + valid_line
        result['total'] = total_lines
        result['values'] = [name_class, function_line, total_lines, '']
        return result
