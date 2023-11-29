#! /usr/bin/env python3
# -*- coding = utf8 -*-

gr_datafile = 'data_source.csv'

with open(gr_datafile, 'rt') as df:
    for ln in df.readlines():
        lln = ln.split(',')
        nm, lnm, addr, twn, cntr, in_d, in_t, eml_1, eml_2, cd, up_t = lln
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


