import patterns

def strip_honorific(s):
    for pattern in patterns.patterns:
        if pattern.match(s):
            return pattern.sub("", s)
    return s
