#!/usr/bin/env bash

/errorfile 504 \/etc\/haproxy\/errors\/504.http/a\
\
\
\
\
frontend frontend_server\
    bind *:80\
    default_backend backend_server\
\
backend backend_server\
    balance roundrobin\
    server 352697-web-01 35.175.130.11:80 check\
    server 352697-web-02 54.165.242.35:80 check
