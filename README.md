# share_sdcv

## Usage

For GoldenDict:

1. Download `<dict>.zip` or `<dict>.tar.gz` from [Releases](https://github.com/scillidan/share_sdcv/releases).
2. Decompress it into `<dict>/`.
3. Add `<dict>/` into GoldenDict.

For `sdcv`:

```sh
export STARDICT_DATA_DIR="<path_to>/share_sdcv"
# Get bookname from <dict>.ifo
sdcv --color --use-dict=<bookname> <word>
````

## How to make `chibigenc-sc`

### Download StarDict dictionary

1. Get `stardict-chibigenc-2.4.2.tar.bz2`(汉语大词典 离线版) from [kdr2.com](https://kdr2.com/resource/stardict.html).
2. Decompress to `stardict-chibigenc-2.4.2/`.
3. Create folder `stardict-chibigenc-2.4.2-sc/`.

```sh
# Windows 10
uv venv .pyglossary
.pyglossary\Scripts\activate.bat
uv pip install pyglossary lxml beautifulsoup4
mklink %USERPROFILE%\.local\bin\pyglossary.exe %CD%\.pyglossary\Scripts\pyglossary.exe
deactivate.bat
pyglossary
```

1. In pyglossary:
	```
	Input File: <path_to>/stardict-chibigenc-2.4.2/chibigenc.ifo
	Input Format: StarDict (.ifo)
	Output Format: <path_to>/stardict-chibigenc-2.4.2-sc/temp/chibigenc.txt
	Output File: Tabfile (.txt, .dic)
	```
2. Read Options → xsl → Value → True.
3. Convert.
4. Here is temporary file `chibigenc`.

### Convert TC to SC

If you used [Sublime Text](https://www.sublimetext.com/):

1. Install [ChineseOpenConvert](https://github.com/rexdf/SublimeChineseConvert) plugin with [Package Control](http://wbond.net/sublime_packages/package_control).
2. Open `chibigenc.txt` in Sublime Text.
3. `Ctrl+a` to select all → `MBtn_Right` → 繁简体转换 → 繁体到简体 → Do nothing until it to be completed → Save.
4. Rename `chibigenc.txt` to `chibigenc-sc.txt`

Or you can do `繁体到简体` with [Open Chinese Convert](https://github.com/BYVoid/OpenCC)'s CLI:

```sh
# Windows 10
uv venv .opencc --python 3.10
.opencc\Scripts\activate.bat
mklink %USERPROFILE%\.local\bin\opencc.exe %CD%\.opencc\Lib\site-packages\opencc\clib\bin\opencc.exe
deactivate.bat
opencc -c <path>/.opencc/Lib/site-packages/opencc/clib/share/opencc/t2s.json -i <path_to>/stardict-chibigenc-2.4.2-sc/temp/chibigenc.txt -o <path_to>/stardict-chibigenc-2.4.2-sc/temp/chibigenc-sc.txt
```

### Finally

1. In pyglossary:
	```
	Input File: <path_to>/stardict-chibigenc-2.4.2-sc/temp/chibigenc-sc
	Input Format: Tabfile (.txt, .dic)
	Output Format: <path_to>/stardict-chibigenc-2.4.2-sc/chibigenc
	Output File: StarDict (Merge Syns)
	```
2. Write Options → sametypesequence → Value → `x`.
3. Convert.
