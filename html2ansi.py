# Usage: python file.py <input_file> <output_file>

import sys

convert = {
    "<br />": r"\n",
    '<font style="color:red;">': "\033[31m",
    '<font style="color:blue;">': "\033[34m",
    '<font style="color:green;">': "\033[32m",
    "</font>": "\033[0m",
    "<small>": "\033[2m",
    "</small>": "\033[0m",
    "<u>": "\033[4m",
    "</u>": "\033[0m",
}

def convert_convert(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()
            for html_tag, ansi_code in convert.items():
                content = content.replace(html_tag, ansi_code)

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(content)

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python html2ansi.py input_file output_file")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convert_convert(input_file, output_file)