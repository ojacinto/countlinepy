#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright 2018(c). All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
# Author: Ing. Oraldo Jacinto Simon


import os
import re
from line import CountLine
from texttable import Texttable, get_color_string as color, bcolors

class main(object):
    '''Calculate the number of coding lines per class and the number of functions.

    '''

    def __init__(self):
        # Going through the python directory of the program code 1.
        #rootDir = '../../Programa1/Code'
        rootDir = '.'
        res = []
        line = CountLine()
        for dirName, subdirList, fileList in os.walk(rootDir):
            for fname in fileList:
                # Processing name's file
                mo = re.search(".py$", fname)
                if mo:
                    path = './{fichero}'
                    # path = '../../Programa1/Code/{fichero}'
                    path_fname = path.format(fichero=fname)
                    try:
                        fichero = open(path_fname, "r")
                        result = fichero.read()
                        lines = result.split('\n')
                        res.append(line.count_line(lines))
                        fichero.close()
                    except:
                        print('No existe el fichero %s' % fname)
        table = Texttable()
        table.set_cols_align(["c", "c", "c", "c"])
        table.set_cols_valign(["t", "m", "b", "m"])
        head = [
        color(bcolors.GREEN,"Part Name"),
        color(bcolors.GREEN,"Number of item"),
        color(bcolors.GREEN,"Part size"),
        color(bcolors.GREEN,"Total size")]
        rows = []
        rows.append(head)
        total = 0
        for element in res:
            total += element['total']
            rows.append(element['values'])
        total = ['','', '',color(bcolors.RED,"%d" % total)]
        rows.append(total)
        table.add_rows(rows)
        print(table.draw() + "\n")
