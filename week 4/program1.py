"""This is the final program for coursera python data representation"""
IDENTICAL = -1


def multiline_diff(lines1, lines2):
    """Returns a three line formatted string showing the location
      of the first difference between line1 and line2."""
    line1 = lines1
    line2 = lines2

    if singleline_diff(line1, line2) >= 0:
        if len(lines1) != len(lines2):
            ln_num = singleline_diff(line1, line2)

            line1 = lines1[singleline_diff(line1, line2)]
            line2 = lines2[singleline_diff(line1, line2)]
            idx_num = singleline_diff(line1, line2)
            return (ln_num, idx_num)


    elif len(lines1) == len(lines2):
        ln_num = singleline_diff(line1, line2)

        line1 = lines1[singleline_diff(line1, line2)]

        line2 = lines2[ln_num]

        idx_num = singleline_diff(line1, line2)
        return (ln_num, idx_num)

    return (IDENTICAL, IDENTICAL)


def file_diff_format(filename1, filename2):
    """Returns a four line string showing the location of the first
      difference between the two files named by the inputs."""

    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)

    differ = (multiline_diff(lines1, lines2))

    if differ != (-1, -1):
        return '\n' + lines1[differ[0]] + '\n' + '='* (differ[1]) + '^' + '\n' \
    + lines2[differ[0]] + '\n'

    else:

        return "No differences!"

    return []

return ("Line "+ str(line_number)+":\n" + singleline_diff_format(datafile1[line_number], datafile2[line_number], idx_difference))
