
import json
print("HERE")

import glob, random
filename = random.choice(glob.glob("sources/*.json")) #change dir name to whatever
print("chose filename = ", filename)
# # filename = 'sources/startup_quotes.json'
with open(filename, 'r') as f:
  data = json.load(f)

print(data)