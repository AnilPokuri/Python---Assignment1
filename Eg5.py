holy_rivers =["Ganges", "Godavari", "Brahmaputra", "Narmada", 
              "Yamuna", "Mahanadi", "Kaveri", "Tapti"]

Val = 0
for ch in holy_rivers:
    print ch
    num = 0
    for i in ch:
        print i
        num = num + ord(i)
    print num
    holy_rivers[Val] = num
    Val = Val + 1 
print holy_rivers
