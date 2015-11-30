#write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "* * * * * python /usr/lib/python2.7/dist-packages/metricgenerator/common/subscriber.py /tmp/config.cfg Constants" >> mycron
echo "* * * * * python /usr/lib/python2.7/dist-packages/metricgenerator/consumer.py /tmp/config.cfg Constants /tmp/metricgenerator/consumer" >> mycron
#install new cron file
crontab mycron
rm mycron
