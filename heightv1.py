#!/usr/local/bin/python3

from cgitb import enable
enable()

from cgi import FieldStorage

print('Content-Type: text/html')
print()

def check_for_int(text, min, max):
	if text.strip() == '':
		return 'Required'
	try:
		num = int(text)
		if num < min:
			return 'Must be no less than ' + str(min)
		if num > max:
			return 'Must be no greater than ' +str(max)
		return ''
	except ValueError:
		return 'Must be a whole number'

form_data = FieldStorage()
feet_input = '0'
feet_int = 0
feet_msg = ''

inches_input = '0'
inches_int = 0
inches_msg = ''
cm_int = 0

if len(form_data) != 0:
	feet_input = form_data.getfirst('feet_input','')
	inches_input = form_data.getfirst('inches_input', '')
	feet_msg = check_for_int(feet_input, 0, 8)
	inches_msg = check_for_int(inches_input, 0, 11)
	if not feet_msg and not inches_msg:
		feet_int = int(feet_input)
		inches_int = int(inches_input)
		cm_int = (12 * feet_int + inches_int) * 2.5
print("""
	<!DOCTYPE html>
	<html lan="en">
		<head>
			<meta charset="utf-8" />
			<title>Getting high</title>
			<script src="heightv2.js" type="module"></script>
		</head>
		<body>
			<p>
				How tall are you?
			</p>
			<form action="heightv1.py" method="get">
				<label for="feet_input">Feet: </label>
				<input type="text" name="feet_input" id="feet_input" value="%s" />
				<span id="feet_msg">%s</span>

				<label for="inches_input">Inches: </label>
				<input type="text" name="inches_input" id="inches_input" value="%s" />
				<span id="inches_msg">%s</span>

				<label for="cm_input">Centimetres: </label>
				<input type="text" name="cm_input" id="cm_input" value="%i" disabled/>
				<input type="submit" />
			</form>
		</body>
	</html>""" % (feet_input, feet_msg, inches_input, inches_msg, cm_int))
