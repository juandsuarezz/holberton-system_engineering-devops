#Executes a kill command to a process called killmenow
exec { 'pkill':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}