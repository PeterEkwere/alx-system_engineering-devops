# This script uses pip to install flask
exec { 'flask':
  command => '/usr/bin/pip install flask==2.1.0',
  path    => ['/usr/bin'],
  unless  => '/usr/bin/pip show flask',
}
