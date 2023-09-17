cipher='cvqBeqacRtqazEigwiAobxrKobxrAobxrLwgk8Lwgk8CrtuiTzahfFreqc{bnjrZwgk8Ikgd4Pj85ePgb_e_rwqr7fvbmHjklo3tews_hmkogooyf0vbnk0ii87Drfgh_n kiwutfb0ghk9ro987k5tfb_hjiouo087ptfcv}'
cipher=cipher[3:] 
flag = '' 
for x in range(0,len(cipher),1): 
    if x%5==0: 
       flag +=cipher[x]
print(flag)