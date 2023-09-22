# This script kills a process called killmenow
exec { 'pkill':
  command => '/usr/bin/pkill killmenow',
  path    => '/usr/bin',
}
