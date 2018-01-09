def singleline_diff(line1, line2):

#min_len = len(line1) if len(line1)< len(line2) else len(line2)
 
  if len(line1) <= len(line2):
      min_len = line1
  else:
      min_len = line2

  for i in range(len(min_len)):
      if line1[i] != line2[i]:
          return (i)

      elif len(line1) != len(line2):
          return len(min_len)
      else:
          return "IDENTICAL"
