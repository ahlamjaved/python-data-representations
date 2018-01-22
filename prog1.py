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

    for index in range(min_len):
        if line1[index] != line2[index]:
            return index
    if len(line1) != len(line2):
        return min_len
    return IDENTICAL

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx - index of first difference between the lines
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.
      If either input line contains a newline or carriage return,
      then returns an empty string.
      If idx is not a valid index, then returns an empty string.
    """
    if line1.find("\n") >= 0 or line2.find("\n") >= 0 or line2.find("\r") >= 0 \
        or line1.find("\r") >= 0:
        return ""
    if len(line1) <= len(line2):
        min_len = len(line1)
    else:
        min_len = len(line2)
    if idx < 0 or idx > min_len:
        return ""

    output = line1 + "\n" + formatted_diff(idx) + "\n" + line2 + "\n"

    return output

def formatted_diff(idx):
    """
    creates the second line of the function singleline_diff_format that places = for every
    index up until the first change, then adds a ^.
    """
    output = ""
    for _ in range(idx):
        output = output + "="
    return output + "^"

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if len(lines1) <= len(lines2):
        min_len = len(lines1)
    else:
        min_len = len(lines2)
    for index in range(min_len):
        line1 = lines1[index]
        line2 = lines2[index]
        diff = singleline_diff(line1, line2)
        if diff >= 0:
            return (index, diff)
    if len(lines1) != len(lines2):
        return (min_len, 0)
    return (IDENTICAL, IDENTICAL)

def get_file_lines(filename):
    """Returns a list of lines from the file named filename."""

    fileopen = open(filename, "rt")
    read_text = fileopen.readlines()
    content = []
    for line in read_text:
        clean_txt = line.rstrip()
        content.append(clean_txt)
    fileopen.close()
    return content

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """

    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    diff = multiline_diff(lines1, lines2)

    if diff[0] != -1 and diff[1] != -1:
        return "Line " + str(diff[0]) + ":\n" + \
        singleline_diff_format(lines1[diff[0]], lines2[diff[0]], diff[1])
    return "No differences\n"

