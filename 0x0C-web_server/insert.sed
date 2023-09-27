#!/usr/bin/env bash


/server_name _;/a\
        location /redirect_me {\
                return 301 http://youtube.com/;\
        }
