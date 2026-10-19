import json

user = {
  "name": "Anna",
  "age": 20
}

text = json.dumps(user, ensure_ascii=False, indent=2)

try:
  restored = json.loads(text)
except json.JSONDecodeError:
  print("json decode error")
