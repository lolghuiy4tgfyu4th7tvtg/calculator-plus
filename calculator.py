# Import Modules Needed
import ttkbootstrap as ttk, math, threading
from ttkbootstrap.constants import *

# Starter Variables
numeral = None
operation = None
times_divided_by_zero = 0

# Number Input
def number_insert(n):
	disp.insert(END, str(n))

# Addition, Subtraction, Multipication, Division, and Exponentiation Operation Switch
def add():
	global operation, numeral
	operation = '+'
	if disp.get() == '':
		return
	numeral = float(disp.get())
	disp.delete(0, END)

def sub():
	global operation, numeral
	operation = '-'
	if disp.get() == '':
		return
	numeral = float(disp.get())
	disp.delete(0, END)

def multi():
	global operation, numeral
	operation = '*'
	if disp.get() == '':
		return
	numeral = float(disp.get())
	disp.delete(0, END)

def divis():
	global operation, numeral
	operation = '/'
	if disp.get() == '':
		return
	numeral = float(disp.get())
	disp.delete(0, END)

def exponent():
	global operation, numeral
	operation = '^'
	if disp.get() == '':
		return
	numeral = float(disp.get())
	disp.delete(0, END)

# Constants
def mathematical_constants(option):
	if option == 'pi':
		disp.delete(0, END)
		disp.insert(END, str(math.pi))
	elif option == 'e':
		disp.delete(0, END)
		disp.insert(END, str(math.e))
	elif option == 'tau':
		disp.delete(0, END)
		disp.insert(END, str(math.tau))
	elif option == 'inf':
		disp.delete(0, END)
		disp.insert(END, str(math.inf))

# The Actual Math
def equal():
	global operation, numeral
	if operation == '+':
		if numeral == None or disp.get() == '':
			return
		another_numeral = float(disp.get())
		try:
			answer = numeral + another_numeral
		except OverflowError:
			ttk.dialogs.dialogs.Messagebox.show_error('OverflowError: Number Too Large!', title='Calculator', parent=root)
			return
		clear()

		disp.insert(END, answer)
	elif operation == '-':
		if numeral == None or disp.get() == '':
			return
		another_numeral = float(disp.get())
		answer = numeral - another_numeral
		clear()

		disp.insert(END, answer)
	elif operation == '*':
		if numeral == None or disp.get() == '':
			return
		another_numeral = float(disp.get())
		try:
			answer = numeral * another_numeral
		except OverflowError:
			ttk.dialogs.dialogs.Messagebox.show_error('OverflowError: Number Too Large!', title='Calculator', parent=root)
			return
		clear()

		disp.insert(END, answer)
	elif operation == '/':
		global times_divided_by_zero
		if numeral == None or disp.get() == '':
			return
		another_numeral = float(disp.get())
		try:
			answer = numeral / another_numeral
			clear()
		except ZeroDivisionError:
			times_divided_by_zero += 1
			if times_divided_by_zero in [5, 8, 10, 11, 12, 13]:
				ttk.dialogs.dialogs.Messagebox.show_error('STOP IT!!!!!!!!!!', title='Calculator', parent=root)
			elif times_divided_by_zero == 6:
				ttk.dialogs.dialogs.Messagebox.show_error('You\'re Frying My Circuts', title='Calculator', parent=root)
			elif times_divided_by_zero == 7:
				ttk.dialogs.dialogs.Messagebox.show_error('Repatedly trying won\'t change this!', title='Calculator', parent=root)
			elif times_divided_by_zero == 9:
				ttk.dialogs.dialogs.Messagebox.show_error('Didn\'t you hear what I said?', title='Calculator', parent=root)
			elif times_divided_by_zero == 14:
				ttk.dialogs.dialogs.Messagebox.show_error('Alright, do whatever you want.', title='Calculator', parent=root)
			
			elif times_divided_by_zero > 2 and times_divided_by_zero < 14:
				ttk.dialogs.dialogs.Messagebox.show_error('I Still Cannot Divide By Zero', title='Calculator', parent=root)
			else:
				ttk.dialogs.dialogs.Messagebox.show_error('Cannot Divide By Zero', title='Calculator', parent=root)
			return

		clear()

		disp.insert(END, answer)
	elif operation == '^':
		if numeral == None or disp.get() == '':
			return
		another_numeral = float(disp.get())
		try:
			answer = numeral ** another_numeral
		except OverflowError:
			ttk.dialogs.dialogs.Messagebox.show_error('OverflowError: Number Too Large!', title='Calculator', parent=root)
			return
		clear()

		disp.insert(END, answer)

# Clear All Operations
def clear():
	global numeral, operation
	disp.delete(0, END)
	numeral = None
	operation = None

# Advanced Operations
def square_root(*args):
	if disp.get() == '':
		return
	new_num = math.sqrt(float(disp.get()))
	disp.delete(0, END)
	disp.insert(END, str(new_num))

def ten_power(*args):
	try:
		new_num = 10 ** float(disp.get())
	except OverflowError:
		ttk.dialogs.dialogs.Messagebox.show_error('OverflowError: Number Too Large!', title='Calculator', parent=root)
		return
	disp.delete(0, END)
	disp.insert(END, str(new_num))

def euler_power(*args):
	try:
		new_num = math.exp(float(disp.get()))
	except OverflowError:
		ttk.dialogs.dialogs.Messagebox.show_error('OverflowError: Number Too Large!', title='Calculator', parent=root)
		return
	disp.delete(0, END)
	disp.insert(END, str(new_num))

def advanced_power(exponent):
		if disp.get() == '':
			return
		another_numeral = float(disp.get())
		try:
			answer = another_numeral ** exponent
		except OverflowError:
			ttk.dialogs.dialogs.Messagebox.show_error('OverflowError: Number Too Large!', title='Calculator', parent=root)
			return
		disp.delete(0, END)

		disp.insert(END, answer)

def lcm():
	go_off_of = ttk.dialogs.dialogs.Querybox.get_string(prompt='Enter your digits (separate with a comma)', title='Calculator', initialvalue=None, parent=root)
	try:
		go_off_of = [int(x) for x in go_off_of.replace(' ', '').split(',')]
		print(go_off_of)
	except ValueError:
		ttk.dialogs.dialogs.Messagebox.show_error('ValueError: GCM and LCM do not support decimal numbers!', title='Calculator', parent=root)
		return

	print(math.lcm(*go_off_of))
	disp.delete(0, END)
	disp.insert(0, math.lcm(*go_off_of))

def gcf():
	go_off_of = ttk.dialogs.dialogs.Querybox.get_string(prompt='Enter your digits (separate with a comma)', title='Calculator', initialvalue=None, parent=root)
	try:
		go_off_of = [int(x) for x in go_off_of.replace(' ', '').split(',')]
		print(go_off_of)
	except ValueError:
		ttk.dialogs.dialogs.Messagebox.show_error('ValueError: GCM and LCM do not support decimal numbers!', title='Calculator', parent=root)
		return

	print(math.gcd(*go_off_of))
	disp.delete(0, END)
	disp.insert(0, math.gcd(*go_off_of))

def logarithm(func):
	if func == 'log':
		base = ttk.dialogs.dialogs.Querybox.get_string(prompt='Enter your base (type e for euler\'s number)', title='Calculator', initialvalue=None, parent=root)
		if base == 'e':
			base = math.e
		elif base.isdigit():
			base = float(base)
		else:
			return
		new_num = math.log(float(disp.get()), base)
		disp.delete(0, END)
		disp.insert(END, str(new_num))
	elif func == '2':
		new_num = math.log2(float(disp.get()))
		disp.delete(0, END)
		disp.insert(END, str(new_num))
	elif func == '10':
		new_num = math.log10(float(disp.get()))
		disp.delete(0, END)
		disp.insert(END, str(new_num))

def triginometry(func):
	if func == 'gamma':
		new_num = math.gamma(float(disp.get()))
		disp.delete(0, END)
		disp.insert(END, str(new_num))
	elif func == 'cos':
		new_num = math.cos(float(disp.get()))
		disp.delete(0, END)
		disp.insert(END, str(new_num))
	elif func == 'acos':
		new_num = math.acos(float(disp.get()))
		disp.delete(0, END)
		disp.insert(END, str(new_num))
	elif func == 'sin':
		new_num = math.sin(float(disp.get()))
		disp.delete(0, END)
		disp.insert(END, str(new_num))
	elif func == 'asin':
		new_num = math.asin(float(disp.get()))
		disp.delete(0, END)
		disp.insert(END, str(new_num))
	elif func == 'tan':
		new_num = math.tan(float(disp.get()))
		disp.delete(0, END)
		disp.insert(END, str(new_num))
	elif func == 'atan':
		new_num = math.atan(float(disp.get()))
		disp.delete(0, END)
		disp.insert(END, str(new_num))

	elif func == 'acosh':
		new_num = math.acosh(float(disp.get()))
		disp.delete(0, END)
		disp.insert(END, str(new_num))
	elif func == 'asinh':
		new_num = math.asinh(float(disp.get()))
		disp.delete(0, END)
		disp.insert(END, str(new_num))
	elif func == 'atanh':
		new_num = math.atanh(float(disp.get()))
		disp.delete(0, END)
		disp.insert(END, str(new_num))
	elif func == 'cosh':
		new_num = math.cosh(float(disp.get()))
		disp.delete(0, END)
		disp.insert(END, str(new_num))
	elif func == 'sinh':
		new_num = math.sinh(float(disp.get()))
		disp.delete(0, END)
		disp.insert(END, str(new_num))
	elif func == 'tanh':
		new_num = math.tanh(float(disp.get()))
		disp.delete(0, END)
		disp.insert(END, str(new_num))

def key_press(evt):
    if evt.keycode == 16:
    	print('Shift!')

def theme_change():
	def settheme():
		ttk.Style().theme_use(combo.get().lower())
		t.destroy()

	t = ttk.Toplevel(root)
	t.resizable(False, False)
	t.title('Change Theme')

	ttk.Label(t, text='Change Theme').grid(row=0, column=0, columnspan=3, pady=5)

	val = ['litera', 'simplex', 'journal', 'yeti', 'superhero', 'vapor', 'cyborg', 'darkly']
	combo = ttk.Combobox(t, values=[l.title() for l in val], state='readonly')
	combo.grid(padx=5, row=1, column=0, columnspan=3, sticky='ew')

	ttk.Label(t, text=' ').grid(row=2, column=0, padx=20)
	ttk.Button(t, text='Cancel', bootstyle='danger', command=lambda:t.destroy()).grid(row=2, column=1, pady=10)
	ttk.Button(t, text='Apply', bootstyle='success', command=settheme).grid(row=2, column=2, padx=5)

	t.wait_window()

# Create Window and Resize It
root = ttk.Window(title='Calculator')
root.minsize(350, 450)
root.geometry('400x450')

# Create Display Entry
disp = ttk.Entry(root, width=30)
disp.pack(fill=X, padx=10, pady=10)

# Create Numerical Buttons and Frame
number_frame = ttk.Frame(root)
number_frame.pack(padx=5, fill='both', expand=1, pady=5)
number_buttons = [
	ttk.Button(number_frame, text='0', command=lambda:number_insert(0)),
	ttk.Button(number_frame, text='1', command=lambda:number_insert(1)),
	ttk.Button(number_frame, text='2', command=lambda:number_insert(2)),
	ttk.Button(number_frame, text='3', command=lambda:number_insert(3)),
	ttk.Button(number_frame, text='4', command=lambda:number_insert(4)),
	ttk.Button(number_frame, text='5', command=lambda:number_insert(5)),
	ttk.Button(number_frame, text='6', command=lambda:number_insert(6)),
	ttk.Button(number_frame, text='7', command=lambda:number_insert(7)),
	ttk.Button(number_frame, text='8', command=lambda:number_insert(8)),
	ttk.Button(number_frame, text='9', command=lambda:number_insert(9)),
]

# Display Numerical Buttons
row=0
column=0
for number, btn in enumerate(number_buttons):
	if number == 0:
		continue
	btn.grid(row=row, column=column, ipady=25, ipadx=25, sticky='nesw')
	column += 1
	if column == 3:
		column = 0
		row += 1

# Display Operation Buttons
ttk.Button(number_frame, text='0', command=lambda:number_insert(0)).grid(row=3, column=0, ipadx=25, ipady=25, sticky='nesw')
ttk.Button(number_frame, text='.', command=lambda:number_insert('.')).grid(row=3, column=1, ipadx=24, ipady=25, sticky='nesw')
ttk.Button(number_frame, text='C', command=clear, bootstyle='warning').grid(row=3, column=2, ipadx=24, ipady=25, sticky='nesw')
ttk.Button(number_frame, text='+', command=add, bootstyle='secondary').grid(row=0, column=3, ipadx=24, ipady=25, sticky='nesw')
ttk.Button(number_frame, text='-', command=sub, bootstyle='secondary').grid(row=1, column=3, ipadx=25, ipady=25, sticky='nesw')
ttk.Button(number_frame, text='x', command=multi, bootstyle='secondary').grid(row=2, column=3, ipadx=25, ipady=25, sticky='nesw')
ttk.Button(number_frame, text='/', command=divis, bootstyle='secondary').grid(row=3, column=3, ipadx=25, ipady=25, sticky='nesw')
ttk.Button(number_frame, text='^', command=exponent, bootstyle='secondary').grid(row=4, column=3, ipadx=25, ipady=25, sticky='nesw')
ttk.Button(number_frame, text='=', command=equal, bootstyle='success').grid(row=4, column=0, ipadx=104, ipady=25, columnspan=3, sticky='nesw')

number_frame.grid_rowconfigure(0, weight=3)
number_frame.grid_rowconfigure(1, weight=3)
number_frame.grid_rowconfigure(2, weight=3)
number_frame.grid_rowconfigure(3, weight=3)
number_frame.grid_rowconfigure(4, weight=3)
number_frame.grid_columnconfigure(0, weight=3)
number_frame.grid_columnconfigure(1, weight=3)
number_frame.grid_columnconfigure(2, weight=3)
number_frame.grid_columnconfigure(3, weight=1)

# Menu
root.menu = ttk.Menu(root)
root['menu'] = root.menu

oper = ttk.Menu(root.menu)
root.menu.add_cascade(label='Basic Operations', menu=oper)
oper.add_command(label=u'Least Common Multiple', command=lcm)
oper.add_command(label=u'Greatest Common Factor', command=gcf)
oper.add_command(label=u'Gamma', command=lambda: triginometry('gamma'), underline=1)
oper.add_separator()
oper.add_command(label=u'Square Root (\u221A)', command=square_root, underline=7)
oper.add_command(label=u'10^x ', command=ten_power, underline=3)
oper.add_command(label=u'x^2  (Square)', command=lambda: advanced_power(2), underline=2)
oper.add_command(label=u'x^3  (Cube)', command=lambda: advanced_power(3), underline=2)

adv = ttk.Menu(root.menu)
root.menu.add_cascade(label='Advanced Operations', menu=adv)

ex = ttk.Menu(adv)
adv.add_cascade(label='Lograithmic Functions ', menu=ex)
ex.add_command(label=u'e^x ', command=euler_power, underline=1)
ex.add_command(label=u'Log', command=lambda:logarithm('log'), underline=3)
ex.add_command(label=u'Log (Base 2)', command=lambda: logarithm('2'), underline=2)
ex.add_command(label=u'Log (Base 10)', command=lambda: advanced_power('10'), underline=2)

trig = ttk.Menu(adv)
adv.add_cascade(label='Triginometry ', menu=trig)
trig.add_command(label=u'Cosine (cos)', command=lambda: triginometry('cos'))
trig.add_command(label=u'Sine (sin)', command=lambda: triginometry('sin'))
trig.add_command(label=u'Tangent (tan)', command=lambda: triginometry('tan'))
trig.add_separator()
trig.add_command(label=u'Arc Cosine (acos)', command=lambda: triginometry('acos'))
trig.add_command(label=u'Arc Sine (asin)', command=lambda: triginometry('asin'))
trig.add_command(label=u'Arc Tangent (atan)', command=lambda: triginometry('atan'))
trig.add_separator()
trig.add_command(label=u'Hyperbolic Cosine (cosh)', command=lambda: triginometry('cosh'))
trig.add_command(label=u'Hyperbolic Sine (sinh)', command=lambda: triginometry('sinh'))
trig.add_command(label=u'Hyperbolic Tangent (tanh)', command=lambda: triginometry('tanh'))
trig.add_separator()
trig.add_command(label=u'Inverse Hyperbolic Cosine (acosh)', command=lambda: triginometry('acosh'))
trig.add_command(label=u'Inverse Hyperbolic Sine (asinh)', command=lambda: triginometry('asinh'))
trig.add_command(label=u'Inverse Hyperbolic Tangent (atanh)', command=lambda: triginometry('atanh'))

const = ttk.Menu(root.menu)
root.menu.add_cascade(label='Constants ', menu=const)
const.add_command(label=u'Pi (\u03C0)', command=lambda: mathematical_constants('pi'))
const.add_command(label=u'Euler\'s Number (e)', command=lambda: mathematical_constants('e'))
const.add_command(label=u'Tau (\u03C4)', command=lambda: mathematical_constants('tau'))
const.add_command(label=u'Infinity (\u221E)', command=lambda: mathematical_constants('inf'))

prefer = ttk.Menu(root.menu)
root.menu.add_cascade(label='Preferences ', menu=prefer)
prefer.add_command(label=u'Change Theme', command=theme_change)

# Event Mainloop
root.bind('<Control-Key-q>', square_root)
number_frame.bind('<Key-0>', lambda x:number_insert(0))
number_frame.bind('<Key-1>', lambda x:number_insert(1))
number_frame.bind('<Key-2>', lambda x:number_insert(2))
number_frame.bind('<Key-3>', lambda x:number_insert(3))
number_frame.bind('<Key-4>', lambda x:number_insert(4))
number_frame.bind('<Key-5>', lambda x:number_insert(5))
number_frame.bind('<Key-6>', lambda x:number_insert(6))
number_frame.bind('<Key-7>', lambda x:number_insert(7))
number_frame.bind('<Key-8>', lambda x:number_insert(8))
number_frame.bind('<Key-9>', lambda x:number_insert(9))
number_frame.bind('<Key-+>', lambda x:add())
number_frame.bind('<Key-->', lambda x:sub())
number_frame.bind('<Key-*>', lambda x:multi())
number_frame.bind('<Key-/>', lambda x:divis())
number_frame.bind('<Key-^>', lambda x:exponent())
root.bind('<Return>', lambda x:equal())
number_frame.bind('<Key>', key_press)

root.mainloop()