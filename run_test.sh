CWD="$(cd -P -- "$(dirname -- "$0")" && pwd -P)"
export PYTHONPATH="$CWD"

 cd test
 rm *.pyc
 python -m unittest discover -s .
