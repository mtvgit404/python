text = 'Мама мыла раму!'
print({key1.lower(): text.lower().count(key1)
      for key1 in sorted([ch for ch in text.lower() if ch.isalpha()])})
