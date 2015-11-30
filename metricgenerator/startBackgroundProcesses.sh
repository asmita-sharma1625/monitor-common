export PYTHONPATH=$PYTHONPATH:monitor-common/metricgenerator/:monitor-common/metricgenerator/common/:monitor-common:
python metricgenerator/common/create_config.py /tmp/config.cfg Constants --service nova-api --logdir /tmp/metricgenerator/logs --filename metric.log --socket tcp://127.0.0.1:5581
python metricgenerator/common/subscriber.py /tmp/config.cfg Constants &
python metricgenerator/consumer.py /tmp/config.cfg Constants /tmp/metricgenerator/consumer &
