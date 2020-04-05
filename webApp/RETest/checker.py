import re

# pattern: a regular expression, samples: a list with string elements
# return a list that indicates match result
# e.g. [(sample1, result1), (sample2, result2), ...]
def regular_expression_checker(pattern, samples):
    
    results = []
    
    for sample in samples:
        obj = re.search(pattern, sample)
        if obj:
            results.append((sample, obj.group()))
        else:
            results.append((sample, False))
    
    return results

