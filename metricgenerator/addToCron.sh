#write out current crontab
sudo crontab -l > mycron
#echo new cron into cron file
echo "* * * * * /usr/lib/python2.7/dist-packages/metricgenerator/common/subscriber.py /tmp/config.cfg Constants" >> mycron
echo "* * * * * /usr/lib/python2.7/dist-packages/metricgenerator/consumer.py /tmp/config.cfg Constants /tmp/metricgenerator/consumer" >> mycron
#install new cron file
sudo crontab mycron
sudo rm mycron
