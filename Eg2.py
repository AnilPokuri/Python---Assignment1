qualities = ["Passion", "Yearning", "Transparency", "Humble", "open-minded",  "Noble"]
output = [ ] 
for i in qualities:
    print i
    for j in i:
        if i[0] == j:
            print j
            output.append(j)
print " final output: ", output
