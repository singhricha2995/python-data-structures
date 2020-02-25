text = "X-DSPAM-Confidence:    0.8475";
xval= text.find('0')
fval = text[xval:]
fl=float(fval)
print(fl)
