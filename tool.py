import json
import re

input_file = "vocabulary.txt"
output_file = "vocabulary.json"

data = []

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        # trường hợp có (type)
        match = re.match(r"(.+?)\((.+?)\):(.+)", line)

        if match:
            voca = match.group(1).strip()
            word_type = match.group(2).strip()
            meaning = match.group(3).strip()

        else:
            # trường hợp không có type
            parts = line.split(":", 1)
            voca = parts[0].strip()
            meaning = parts[1].strip() if len(parts) > 1 else ""
            word_type = ""

        data.append({
            "voca": voca,
            "type": word_type,
            "meaning": meaning
        })

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Convert xong!")