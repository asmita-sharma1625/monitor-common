CWD="$(cd -P -- "$(dirname -- "$0")" && pwd -P)"
export PYTHONPATH="$CWD"
echo $PYTHONPATH
find |grep "pyc$"|xargs rm -f
 cd test
 rm -rf consumer
 rm -rf logs
 #rm *.cfg -f
 
 python create_config.py config.cfg Constants --service nova --logdir ./logs --filename metric.log --socket tcp://127.0.0.1:5581
 #python ../metricgenerator/common/subscriber.py config.cfg Constants

 python -m unittest discover -s .
 cd integration
 python -m unittest discover -s .
  
 #pkill -9 -f ../../metricgenerator/common/subscriber.py
  
#cd $CWD
#cd logger
#python rotator.py /home/asmi/compute
