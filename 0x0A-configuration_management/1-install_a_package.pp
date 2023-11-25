# Install Flask version 2.1.0
package { 'Werkzeug':
  ensure   => '2.0.0',
  provider => 'pip3',
}

# Install Werkzeug version 2.0.0
package { 'werkzeug':
  ensure   => '2.0.0',
  provider => 'pip3',
}
