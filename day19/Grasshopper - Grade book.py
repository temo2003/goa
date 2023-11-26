# Grade book
# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'




def get_grade(s1, s2, s3):
    if (s1 + s2 + s3)/3 >= 90 :
        return ("A")
    elif (s1 + s2 + s3)/3 >= 80 < 90 :
        return ("B")
    elif (s1 + s2 + s3)/3 >= 70 < 80 :
        return ("C")
    elif (s1 + s2 + s3)/3 >= 60 < 70 :
        return ("D")
    elif (s1 + s2 + s3)/3 >= 0 < 60 :
        return ("F")