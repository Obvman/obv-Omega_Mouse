# ===== SETTINGS =====

# ----- Omega Mouse Mode Selection -----
settings():
	# Set which Omega Mouse mode to use. Omega Mouse restart required with change.
	# 0 = Full
	# 1 = Lite
	# 2 = Basic
	user.omega_mouse_mode = 0
	
# ----- Omega Mouse Cursor Time Intervals -----
# Applies to all modes. No restart required with change, only save.
# Total between both settings should be under 1800ms. Must use quotes in value.
settings():
	# GAZE CAPTURE INTERVAL: Sets amount of time gaze is captured for cursor movement.
	# Default = "50ms"
	user.gaze_capture_interval = "50ms"
	
	# HEAD TRACKING DELAY: Sets interval after gaze tracking before head tracking starts.
	# Default = "50ms"
	user.head_track_lag = "50ms"



# ===== VOICE COMMANDS =====

# ----- Omega Mouse Toggle Switching -----
omega mouse: user.omega_mouse_toggle()
omega restart: user.omega_mouse_restart()
#control mouse: {uses Omega Mouse function placed into mouse.talon. See "Set-Up" in readme.}
#zoom mouse: {uses Omega Mouse function placed into mouse.talon. See "Set-Up" in readme.}
omega check state: user.omega_mouse_state_check()



# ----- Omega Mouse Features -----
#*Popping Noise*: {overrides default pop click for Omega Mouse functionality}
