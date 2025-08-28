# share_hanyudacidian

[![Create Releases](https://github.com/scillidan/share_hanyudacidian/actions/workflows/releases.yml/badge.svg)](https://github.com/scillidan/share_hanyudacidian/actions/workflows/releases.yml)

## Usage

Download `.zip` from [Releases](https://github.com/scillidan/share_hanyudacidian/releases):
- For GoldenDict, use `*-stardict-html.zip`.
- For sdcv, use `*-stardict-html2ansi.zip`.
- For SilverDict, use `*-stardict-plaintext.zip`.
- For Yomitan, use `*-yomitan.zip`.

See preview screenshot [here](asset/).

### GoldenDict

- GoldenDict → Edit → Dictionaries
	- Sources → Transliteration → Chinese Conversion → All (On)
	- Groups → Add group → `zh`
	- Put Dictionaries `Simplified to traditional Chinese`, `HanYuDaCiDian` into `zh`

Then you can search TC words used SC words. Here, you also can make an alt `word` table by converting `word' table. Same as doing for the not-as-received part in `meeting' table. But I don't it's good way.

### sdcv

```sh
export STARDICT_DATA_DIR="<path_to_dictionaries>"
sdcv --color --use-dict=HanYuDaCiDian <word>
````

## How to make

1. Download `汉语大词典源数据合并.txt` from [《汉语大词典》施工现场11.2](https://forum.freemdict.com/t/topic/16759). So this is not a stable or officially version.
2. The origin layout and style from First Edition is better enough. See [HanYuDaCiDian_Vol01.jpg](HanYuDaCiDian_Vol01.jpg). Then format it by yourself. For me, I edit in Sublime Text. Used regex find, multi-cursor edit, replace all etc..
3. Use `pyglossary` to convert `done.txt` to multiple dictionary formats. I mainly use StarDict and Yomitan format.
4. You can see [releases.yml] to get some useful information about commands.
