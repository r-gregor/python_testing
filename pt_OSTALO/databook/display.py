#! /usr/bin/env python3
# -*- coding = utf8 -*-

gr_datafile = 'data_source.csv'

with open(gr_datafile, 'rt') as df:
    for ln in df.readlines():
        lln = ln.split(',')
        nm, lnm, addr, twn, cntr, in_d, in_t, eml_1, eml_2, cd, up_t = lln[0], lln[1], lln[2], lln[3], lln[4], lln[5], lln[6], lln[7], lln[8], lln[9], lln[10]
        print(' name:', nm , '\n',
                'last name:', lnm, '\n',
                'address:', addr, '\n',
                'town:', twn, '\n',
                'country:', cntr, '\n',
                'date/insert:', in_d, '\n',
                'time/insert:', in_t, '\n',
                'e-mail-01:', eml_1, '\n',
                'e-mail-02:', eml_2, '\n',
                'card:', cd, '\n',
                'date/update:', up_t,)
