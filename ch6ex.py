str = 'X-DSPAM-Confidence:0.8475'
pos = str.find('0')
fval = float(str[pos:])
print(fval)
