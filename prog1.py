"""This is the final program for coursera python data representation"""
IDENTICAL = -1


def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """

    if len(line1) <= len(line2):
        min_len = len(line1)
    else:
        min_len = len(line2)

    for i in range(min_len):
        if line1[i] != line2[i]:
            return i
    if len(line1) != len(line2):
        return min_len
    return IDENTICAL

def get_file_lines(filename):
    """Returns a list of lines from the file named filename."""

    fileopen = open(filename, "rt")
    read_text = fileopen.readlines()
    for line in read_text:
        print(line)
    fileopen.close()
    return read_text

