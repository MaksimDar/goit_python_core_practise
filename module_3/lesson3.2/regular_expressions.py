import re

string = 'Novak Djokovic[a] (born 22 May 1987) is a Serbian professional tennis ' \
'player. Djokovic has been ranked as the world No. 1 in men singles"\  ' \
'by the Association of Tennis Professionals (ATP) for a record 428 weeks,' \
' finished as the year-end No. 1 a record eight times, and has been ranked No. 1 at least once in a year for a record 13 different years. He has won 101 ATP' \
' Tour–level singles titles, including a record 24 majors (among which a record ten Australian Open titles), a record 40 Masters, a record seven year-end championships, and an Olympic gold medal. Djokovic is the only man in tennis ' \
'history to be the reigning champion of all four majors at once across three different surfaces. In singles, he is the only man to achieve a triple Career Grand Slam, and the only player to complete a Career Golden Masters, a feat he' \
' has accomplished twice. Djokovic is the only player in singles to have won all of the Big Titles over the course of his career.'

pattern = r'[0-9]+'
result = re.search(pattern, string)
print(result)

# print(result.span())

# first,last = result.span()
# print(string[first:last])
######## ============ alternative
print(result.group())

result = re.findall(pattern, string)

print(result)

result = re.findall('\s+', string)

print(result)

pattern = r'\d+'
result = re.findall(pattern, string)

print(result)

pattern = r'[0-9]{3}'
result = re.findall(pattern, string)

print(result)
