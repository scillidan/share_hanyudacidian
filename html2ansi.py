# Write by GPT-4o mini🧙‍♂️, scillidan🤡
# Purpose: Convert HanYuDaCiDian Tabfile's HTML tags to ANSI escape codes. The result can continue to be converted into StarDict(.ifo) files for sdcv.
# Usage: python html2ansi.py <input_file> <output_file>

import sys

def process_text(text):
	replacements = {
		'<span style="color:red;">': "\033[31m",
		'<span style="color:yellow;">': "\033[33m",
		'<span style="color:blue;">': "\033[34m",
		"</span>": "\033[0m",
		"<u>": "\033[4m",
		"</u>": "\033[0m",
		"<br />": r"\n",
	}
	for old, new in replacements.items():
		text = text.replace(old, new)
	return text

def main():
	if len(sys.argv) != 3:
		print("Usage: python cli.py input output")
		sys.exit(1)
	input_file = sys.argv[1]
	output_file = sys.argv[2]

	with open(input_file, "r", encoding="utf-8") as f:
		content = f.read()

	processed = process_text(content)

	with open(output_file, "w", encoding="utf-8") as f:
		f.write(processed)

if __name__ == "__main__":
	main()
