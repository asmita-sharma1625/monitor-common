python test/create_config.py /tmp/config.cfg Constants --service nova-api --logdir /tmp/metricgenerator/logs --filename metric --socket tcp://127.0.0.1:5581
python metricgenerator/common/subscriber.py /tmp/config.cfg Constants
python metricgenerator/consumer.py /tmp/config.cfg Constants /tmp/metricgenerator/consumer
