# Fix
exec { 'Fix phpp typo':
  command => '/bin/sed -i \'s/.phpp/.php/\' /var/www/html/wp-settings.php'
}

exec { 'restart server':
  command => '/usr/sbin/service apache2 restart'
}