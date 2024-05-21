story = "onkar has completed his Diploma Degree in Information Technology,By miracle and his constant Hard work" \
        " he ranked 1st in the third year with the aggregate of 94%"
print(story)

print("The length of the is :", len(story))
print("Does story ends with % ? :", story.endswith("%"))
print("There are ", story.count(" "), "whitespaces in the String")
print(story.capitalize())  # Capitalize the first letter of the string
# returns the index of the first occurrence of the specified word
print("Index of first occurred 'Technology' :", story.find("Technology"))
print(story.replace("94", "94.56"))