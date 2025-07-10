# share_sdcv

## Usage

For GoldenDict:

1. Download `<dict>.zip` or `<dict>.tar.gz` from [Releases](https://github.com/scillidan/share_sdcv/releases).
2. Decompress it into `<dict>/`.
3. Add `<dict>/` into GoldenDict.

For `sdcv`:

```sh
cat <dict>/<dict>.ifo
# Get bookname
export STARDICT_DATA_DIR="<path_to>/share_sdcv"
sdcv --color --use-dict=<bookname> <word>
````

## How to make `chibigenc-sc`

### Download StarDict dictionary

1. Get `stardict-chibigenc-2.4.2.tar.bz2`(汉语大词典 离线版) from [kdr2.com](https://kdr2.com/resource/stardict.html).
2. Decompress to `stardict-chibigenc-2.4.2/`.
3. Create folder `stardict-chibigenc-2.4.2-sc/`.

```sh
pip install pyglossary
pyglossary
```

1. In pyglossary:
	```
	Input File: <path_to>/stardict-chibigenc-2.4.2/chibigenc.ifo
	Input Format: StarDict (.ifo)
	Output Format: <path_to>/stardict-chibigenc-2.4.2-sc/temp/chibigenc
	Output File: Tabfile (.txt, .dic)
	```
2. Read Options → xsl → Value → True.
3. Convert.
4. Here is temporary file `chibigenc`.

### Convert TC to SC

If you used [Sublime Text](https://www.sublimetext.com/):

1. Install [ChineseOpenConvert](https://github.com/rexdf/SublimeChineseConvert) plugin with [Package Control](http://wbond.net/sublime_packages/package_control).
2. Drag `chibigenc` into Sublime Text to open.
3. `Ctrl+a` to select all → `Right_Click` → 繁简体转换 → 繁体到简体 → Do nothing until it to be completed → Save.

Or you can do `繁体到简体` with [Open Chinese Convert](https://github.com/BYVoid/OpenCC)'s CLI:

```sh
pip install opencc
C:\Users\<User>\Scoop\persist\python310\Lib\site-packages\opencc\clib\bin\opencc.exe --path C:\Users\<User>\Scoop\persist\python310\Lib\site-packages\opencc\clib\share\opencc -c t2s.json -i <path_to>/stardict-chibigenc-2.4.2-sc/temp/chibigenc -o <path_to>/stardict-chibigenc-2.4.2-sc/temp/chibigenc-sc
```

### Finally

1. In pyglossary:
	```
	Input File: <path_to>/stardict-chibigenc-2.4.2-sc/temp/chibigenc
	Input Format: Tabfile (.txt, .dic)
	Output Format: <path_to>/stardict-chibigenc-2.4.2-sc/chibigenc
	Output File: StarDict (.ifo)
	```
2. Write Options → sametypesequence → Value → x.
3. Convert.
