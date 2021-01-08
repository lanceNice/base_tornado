#!/bin/sh

path=$2

# 判断是否存在路径
if [ "${path}" ]; then
  logfile=${path}'log/celery.log'
  pidfile=${path}'log/celery.pid'
  echo "#### logfile path ####"
  echo "$logfile"
else
  logfile='log/celery.log'
  pidfile='log/celery.pid'
  echo "$logfile"
fi

tasks_name='tasks'
process_num=2

case $1 in
   start) celery multi start -B -A  $tasks_name worker -l info --logfile=$logfile --pidfile=$pidfile  -c $process_num -n middle_service.%h;;
   restart) celery multi restart -B -A  $tasks_name worker -l info --logfile=$logfile --pidfile=$pidfile  -c $process_num -n middle_service.%h;;
   stop) celery multi stop -B -A  $tasks_name worker --pidfile=$pidfile;;
   *) echo "require start|stop|restart" ;;
esac