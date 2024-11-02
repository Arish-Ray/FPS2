with open ("Codingal.txt") as file:
  data = file.readlines()
  print("Words in the file are...")
  for line in data:
    word = line.split()
    print(word)
file.close()