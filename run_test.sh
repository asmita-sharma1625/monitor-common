CWD="$(cd -P -- "$(dirname -- "$0")" && pwd -P)"
export PYTHONPATH="$CWD"
echo $PYTHONPATH
find |grep "pyc$"|xargs rm -f
 cd test
 rm *.pyc -f
 rm *.cfg -f
 python -m unittest discover -s .
 echo config.cfg
 cat config.cfg
 echo Config.cfg
 cat Config.cfg
 echo pconfig.cfg
 cat pconfig.cfg  
#cd $CWD
#cd logger
#python rotator.py /home/asmi/compute
