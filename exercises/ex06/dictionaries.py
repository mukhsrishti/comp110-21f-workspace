"""Practice with dictionaries."""

__author__ = "730402368"

# Define your functions below

#invert
def invert(start: dict[str, str])->dict[str, str]:
    """Testing!"""
    end = dict()
    for key in start:
        if start[key] in end:
            raise KeyError ("a duplicate")
        end[start[key]]= key
    return end

#favorite colors
def favorite_color(data: dict[str, str]) -> str:
    color_frequency= dict()
    for key in data:
        color_frequency[data[key]] = 0
    for key in data:
        color_frequency[data[key]] += 1
    max: str = ""
    for key in color_frequency:
        if max: 
            if color_frequency[key] > color_frequency[max]:
                max= key
            else:
                max= key
    return max

#count
def count(lst: list[str])->dict[str, int]:
    count_frequency = dict()
    for i in lst:
        if i in count_frequency:
            count_frequency[i] +=1
        else:
            count_frequency[i]= 1
    return count_frequency