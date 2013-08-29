cat "$1" |sed -e 's/\x96//g;s/\x93/"/g;s/\x94/"/g;s/\x92/\x27/g;s/\xa0//g' >"$1-fixed"
