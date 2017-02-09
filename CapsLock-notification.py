import sys
import os
import time
import ctypes
import signal # atexit is useless when it is terminated

# import daemon
import pynotify

libX11 = ctypes.CDLL("libX11.so")
display = libX11.XOpenDisplay(0)
		
def sig_hdr(sig_num, frame):
	global libX11, display
	libX11.XCloseDisplay(display)
	sys.exit(0)
	
def main(argv):
	global libX11, display
	state = ctypes.c_bool(False)	
	atom = libX11.XInternAtom(display, "Caps Lock", ctypes.c_bool(False))
	libX11.XkbGetNamedIndicator(display, atom, 0, ctypes.byref(state), 0, 0)
	flag = state.value
	
	signal.signal(signal.SIGINT, sig_hdr)
	signal.signal(signal.SIGTERM, sig_hdr)
	
	if not pynotify.init("caps"):
		sys.exit(1)
	
	uri_on = "file://" + '''your dir''' + "/capslock-on.png"
	uri_off = "file://" + '''your dir''' + "/capslock-off.png"
	caps_notify = pynotify.Notification("CapsLock Notification")
	
# Perhaps libX11 is not compatible with python-daemon. If you know the reason, please tell me. Thanks.
#	with daemon.DaemonContext():
	while True:
		libX11.XkbGetNamedIndicator(display, atom, 0, ctypes.byref(state), 0, 0)
		if flag != state.value:
			if flag:
				caps_notify.update("CapsLock Notification", "CapsLock OFF", uri_off)
				caps_notify.show()
			else:
				caps_notify.update("CapsLock Notification", "CapsLock ON", uri_on)
				caps_notify.show()
			flag = state.value
		time.sleep(0.5)

if __name__ == "__main__":
	main(sys.argv[1:])
