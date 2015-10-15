CWD="$(cd -P -- "$(dirname -- "$0")" && pwd -P)"
export PYTHONPATH="$CWD"
echo $PYTHONPATH
 cd test
 rm *.pyc
 python -m unittest discover -s .

#cd $CWD
#cd logger
#python rotator.py /home/asmi/compute
