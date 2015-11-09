CWD="$(cd -P -- "$(dirname -- "$0")" && pwd -P)"
export PYTHONPATH="$CWD"
echo $PYTHONPATH
find |grep "pyc$"|xargs rm -f
 cd test
 rm -rf consumer
 rm -rf logs
 rm *.pyc -f
 rm *.cfg -f
 python -m unittest discover -s .
 cd integration
 python -m unittest discover -s .
#cd $CWD
#cd logger
#python rotator.py /home/asmi/compute
