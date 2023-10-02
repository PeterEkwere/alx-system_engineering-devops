#!/usr/bin/env bash

/server_name _;/a\
	error_page 404 /404.html;\
        location /404 {\
                root /etc/nginx/html;\
		internal;\
        }
