#!/bin/sh /etc/rc.common
# Example script
# Copyright (C) 2007 OpenWrt.org

USE_PROCD=1
START=10
STOP=15

# Change the next 3 lines to suit where you install your script and what you want to call it
DIR=/opt/trafficmonphil
DAEMON=$DIR/trafficServer.py
DAEMON_NAME=trafficServerService


start_service() {
  procd_open_instance
  procd_set_param command /usr/bin/python $DAEMON

  # respawn automatically if something died, be careful if you have an alternative process supervisor
  # if process dies sooner than respawn_threshold, it is considered crashed and after 5 retries the service is stopped
  procd_set_param respawn ${respawn_threshold:-3600} ${respawn_timeout:-5} ${respawn_retry:-5}

  procd_set_param limits core="unlimited"  # If you need to set ulimit for your process
  #procd_set_param file /var/etc/your_service.conf # /etc/init.d/your_service reload will restart the daemon if these files have changed
  #procd_set_param netdev dev # likewise, except if dev's ifindex changes.
  #procd_set_param data name=value ... # likewise, except if this data changes.
  procd_set_param stdout 1 # forward stdout of the command to logd
  procd_set_param stderr 1 # same for stderr
  procd_close_instance
}
reload_service()
{
        echo "Explicitly restarting service, are you sure you need this?"
        stop
        start
}