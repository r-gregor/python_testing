#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# for now a single string ... otherways for each line containing a start --> end times ...
S = "00:05:58,572 --> 00:06:13,103"

# optional (just for test)
print("Original time string: \n{}\n".format(S))

# time to +,- correct in seconds ... in real optained from user input ...
Tcorr = 5
print("Time difference: {} sec = {} ms".format(Tcorr, Tcorr*1000))

arr = '-->'

# create a LIST of elements: ['00:42:23,572', '-->', '00:42:33,103']
L1 = S.split()

# assign list elements to variables for further proccessing
T1 = L1[0].split(':')      # ['00', '42', '23,572']
T2 = L1[2].split(':')      # ['00', '42', '33,103']

# asign each list element to a variable
H1 = T1[0]
M1 = T1[1]
S1 = T1[2].split(',')[0]
mS1 = T1[2].split(',')[1]

H2 = T2[0]
M2 = T2[1]
S2 = T2[2].split(',')[0]
mS2 = T2[2].split(',')[1]

def T_to_ms(h, m ,s, ms):
    '''
    function that returns the single digit of time in ms from a list of h, m, s, ms:
    '''
    hms = int(h)*60*60*1000
    mms = int(m)*60*1000
    sms = int(s)*1000
    ms = int(ms)
    # test
    # print(hms, mms, sms, ms)

    return hms + mms + sms + ms

T1ms = T_to_ms(H1, M1, S1, mS1)
T2ms = T_to_ms(H2, M2, S2, mS2)

# Add (or substract if [-]) time difference in ms to original time in ms:
Tadd = int(Tcorr)*1000
T1ms_new = T1ms + Tadd
T2ms_new = T2ms + Tadd

    # test
    # print("T1ms = {} ms".format(T1ms))
    # print("T2ms = {} ms".format(T2ms))
    # print("Time difference = {} ms".format(Tadd))
    # print("New T1ms = {} ms".format(T1ms_new))
    # print("New T2ms = {} ms".format(T2ms_new))


def ms_to_T(Tnew):
    '''
    function that returns a list of corrected h, m. s, ms
    '''
    T_ms = Tnew//1000
    Tms = Tnew%1000

    T_s = T_ms//60
    Ts = T_ms%60

    T_m = T_s//60
    Tm = T_s%60

    T_h = T_m//60
    Th = T_m%60

    # str().zfill(2) leading zero fill single num string to two char string
    # s,ms string:
    T_s_ms = str(Ts).zfill(2) + ',' + str(Tms)

    # list of time elements:
    TL = [str(Th).zfill(2), str(Tm).zfill(2), T_s_ms]
    return TL

# run previous functions to get lists of corrected times for start and end:
T1_new = ms_to_T(T1ms_new)
T2_new = ms_to_T(T2ms_new)

# test
print("New start time:", T1_new)
print("New end time:", T2_new)

# construct a final string to output into a file
S2 = ':'.join(T1_new) + ' ' + arr + ' ' + ':'.join(T2_new)

# final corrected time string:
print("\n" + "New corrected time string: \n{}".format(S2))
