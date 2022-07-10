
# solutuon 1

  def first_non_repeating_letter(string):
      string_lower = string.lower()
      for i, letter in enumerate(string_lower):
          if string_lower.count(letter) == 1:
              return string[i]

      return ""


  
# solutuon 2

  def first_non_repeating_letter(string):
      newstring = string[:]
      string = string.lower()
      result = ''

      for i in string:
          if (string.find(i, (string.find(i)+1))) == -1:
              result = i
              break

      if result == '':
          return result

      return result if result in newstring else result.upper()


  
# solutuon 3

  def first_non_repeating_letter(string):
      singles = [i for i in string if string.lower().count(i.lower()) == 1]
      return singles[0] if singles else ''
