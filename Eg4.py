"""
4. Given dictionary representing a student name as a key and corresponding value is a grade which
he obtained in different subjects. WAP update each dict value with average score obtained by
each student respectively.
scores = {“Student1”: [65, 68, 59, 52, 69, 65, 55, 59],
“Student2”: [60, 64, 60, 60, 88, 64, 68, 75],
“Student3”: [59, 72, 64, 62, 66, 68, 72, 73],
“Student4”: [82, 62, 61, 54, 71, 89, 75, 73]
}
"""
scores = {"Student1": [65, 68, 59, 52, 69, 65, 55, 59],
"Student2": [60, 64, 60, 60, 88, 64, 68, 75],
"Student3": [59, 72, 64, 62, 66, 68, 72, 73],
"Student4": [82, 62, 61, 54, 71, 89, 75, 73]
}
for ch in scores:
    num = 0.0
    length = len(scores[ch])
    for val in scores[ch]:
        num = num + val
    Average = num/length
    scores[ch] = Average
print scores      
