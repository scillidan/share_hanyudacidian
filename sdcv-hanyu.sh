#!/bin/bash

if [ -z "$1" ]; then
	echo "Usage: $0 <Chinese_word>"
	exit 1
fi

word="$1"

sc_word=$(hanconv t2s "$word")
sdcv --color --use-dict HanYuDaCiDian -n "$sc_word"

tc_word=$(hanconv s2t "$word")
sdcv --color --use-dict HanYuDaCiDian -n "$tc_word"
