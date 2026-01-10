# share_hanyudacidian

[![Create Releases](https://github.com/scillidan/share_hanyudacidian/actions/workflows/releases.yml/badge.svg)](https://github.com/scillidan/share_hanyudacidian/actions/workflows/releases.yml)

This is not a stable or officially release. Data from `汉语大词典源数据合并.txt` on [《汉语大词典》施工现场11.2](https://forum.freemdict.com/t/topic/16759). Read more on [hanyudacidian.cn](https://www.hanyudacidian.cn)，[Wikipedia](https://zh.wikipedia.org/wiki/%E6%BC%A2%E8%AA%9E%E5%A4%A7%E8%A9%9E%E5%85%B8).

## Usage

1. Download files from [Releases](https://github.com/scillidan/share_hanyudacidian/releases).
2. Use them in GoldenDict (StarDict format), sdcv.
3. See preview screenshot [here](asset/).

### GoldenDict

- GoldenDict → Edit → Dictionaries
	- Sources → Transliteration → Chinese Conversion → All (On)
	- Groups → Add group → `zh`
	- Put Dictionaries `Simplified to traditional Chinese`, `HanYuDaCiDian` into `zh`

Then you can search TC words used SC words. Here, you also can make an alt `word` table by converting `word` table. Same as doing for the TC/Original part in `meaning` content. But I don't think it's a way that can be maintained.

### sdcv

```sh
export STARDICT_DATA_DIR="<path_to_dictionaries>"
sdcv --color --use-dict HanYuDaCiDian -n <word>
```

```sh
# Search words with simplified and traditional forms both
cargo install hanconv
chmod +x ./sdcv-hanyu.sh
./sdcv-hanyu.sh <word>
```

```sh
# Install
ln -sfn $(pwd)/sdcv-hanyu.sh ~/.local/bin/hanyu
hanyu <word>
# Uninstall
rm ~/.local/bin/hanyu
```
