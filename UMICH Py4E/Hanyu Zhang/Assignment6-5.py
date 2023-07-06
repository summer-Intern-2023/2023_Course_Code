text = "X-DSPAM-Confidence:    0.8475"

start = text.find('0')
end = text.find('5')

sub = text[start : end+1]
print(float(sub))