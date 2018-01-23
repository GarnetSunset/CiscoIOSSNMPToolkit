from telnetlib import Telnet

class doTelnet:

	def __init__(self, host, port, user, password):
		# Initilize variables
		self.host = host
		self.port = port
		self.user = user
		self.password = password

		# TODO Add support for user control of terminal_type
		self.terminal_type = 'vty100'

		# Set login status, 0 = login failed 1 = login success
		login_status = 0

	def connect(self):
		# Connect to target
		try:
			self.telnet = Telnet(self.host, self.port)
			print('[*]\tSuccessfully opened telnet connection to {0}:{1}'.format(self.host, self.port))
		except Exception as e:
			print('[!]\tError opening telnet connection to {0}:{1}\n{2}'.format(self.host, self.port, e))	

	def login(self):
		# Configure login variables for input
		self.user = self.user.encode('ascii') + b'\n'
		self.password = self.password.encode('ascii') + b'\n'
		self.terminal_type = self.terminal_type.encode('ascii') + b'\n'

		# Do login
		# TODO Add functionality for user control of expected login prompt (some servers send 'Username: ', I'm sure theres other options)
		self.telnet.read_until(b'login: ')
		self.telnet.write(self.user)
		self.telnet.read_until(b'Password: ')
		try:
			self.telnet.write(self.password)
		except Exception as e:
			print('[!]\tError authenticating to {0}:{1}\n{2}'.format(self.host, self.port, e))
		else:
			print('[*]\tSuccessfully authenticated to {0}:{1}'.format(self.host, self.port))
			self.login_status = 1
		finally:
			pass

		# Set terminal type
		self.telnet.write(self.terminal_type)

	def cmd(self, command):
		# Configure command variable for input
		self.command = self.command.encode('ascii') + b'\n'

		# Run commands
		self.telnet.write(self.command)

		# Collect output
		# TODO Do something with this output
		self.output = self.telnet.read_all.decode('ascii')

	def getOutput(self):
		return self.output

	def getStatus(self):
		return self.login_status

	def close(self):
		# Close connection
		self.telnet.close()
