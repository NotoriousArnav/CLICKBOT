# wrap import statement in try-except block to prevent failure
try:
	import pyautogui
except ModuleNotFoundError:
	# Install module if it is not installed
	print("pyautogui module not installed.")
	print("Installing pyautogui...")
	import pip
	pip.main(['install','pyautogui'])

#Change coord here for your Use
coord = (353,550)

for i in range(100):
	pyautogui.click(x=coord[0], y=coord[1])
