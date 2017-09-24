def uses_all(word, required):
  for letter in required:
    if letter not in word:
      return False
    return True

