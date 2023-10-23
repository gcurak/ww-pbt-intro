
def count_vowels(string: str, include_y):
  vowels = 'aeiouAEIOU'
  if include_y:
      vowels = 'aeiouAEIOUY'
  tally = []
  for c in string:
      if c in vowels:
          tally.append(1)
  return sum(tally)