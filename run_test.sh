CWD="$(cd -P -- "$(dirname -- "$0")" && pwd -P)"
export PYTHONPATH="$CWD"
echo $PYTHONPATH
find |grep "pyc$"|xargs rm -f
 cd test
 rm -rf consumer
 rm -rf logs
 rm config.cfg -f
 
 python ../metricgenerator/common/create_config.py config.cfg Constants --service Test --logdir ./logs --filename metric.log --socket tcp://127.0.0.1:5588
 python ../metricgenerator/common/subscriber.py config.cfg Constants &
 #python metricgenerator/consumer.py config.cfg Constants
 python -m unittest discover -s .
 cd integration
 python -m unittest discover -s .
 ps -ef | grep subscriber | grep -v grep | awk '{print $2}' | xargs kill
  
#cd $CWD
#cd logger
#python rotator.py /home/asmi/compute
