# Using Puppet, install flask from pip3.
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

notify { 'Flask version':
  message => 'Python 3.8.10
Flask 2.1.0
Werkzeug 2.1.1',
}
