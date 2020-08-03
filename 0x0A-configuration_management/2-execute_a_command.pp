# Executes a kill command to a process called killmenow
exec { 'pkill killmenow':
     command  => 'pkill -f killmenow',
     provider => 'shell',
}