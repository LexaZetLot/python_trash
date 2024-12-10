import re
match = re.match('Hello[\t]*(.*)world', 'Hello    Python world')
print(match.group(1))

match1 = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
match1.group()
print(match1.group())
print(re.split('[/:]', '/usr/home/lumberjack'))