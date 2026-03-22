import json

def convert_to_json(input_file, output_file):
    result = []

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue

        try:
            key, words_str = line.split(":")
            words = [w.strip() for w in words_str.split(",") if w.strip()]

            item = {
                "key": key.strip(),
                "words": words
            }

            result.append(item)

        except ValueError:
            print(f"Bỏ qua dòng lỗi: {line}")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("✅ Đã chuyển đổi xong!")

# ---- RUN ----
input_file = "sameword.txt"
output_file = "vocabulary_same.json"

convert_to_json(input_file, output_file)