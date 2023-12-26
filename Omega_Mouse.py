from talon import Module, Context, actions, ctrl, app
import typing

mod = Module()
mod.tag("om_on", desc="Signals Omega Mouse is toggled on")
mod.tag("omega_full", desc="Signals Full Mode is active")
mod.tag("omega_lite", desc="Signals Lite Mode is active")
mod.tag("omega_basic", desc="Signals Basic Mode is active")
mod.tag("om_tracking", desc="Signals omega mouse is tracking head movements and awaiting a second pop")

ctx = Context()
ctx_switch = Context()
ctx_switch.matches = """
tag: user.om_on
"""


# ---------- Variables ----------
om_state: bool = False
omega_mode: int = 0
om_tracking: bool = False


# ---------- Settings ----------
setting_omega_mouse_mode = mod.setting(
    "omega_mouse_mode",
    type=int,
    default=0,
    desc="Determines which mode of Omega Mouse to use. 0 = Full. 1 = Lite. 2 = Basic"
    )

setting_gaze_capture_interval = mod.setting(
    "gaze_capture_interval",
    type=str,
    default="50ms",
    desc="Sets gaze time window for cursor movement after 'popping noise'/'relo' commands"
    )

setting_head_track_lag = mod.setting(
    "head_track_lag",
    type=str,
    default="50ms",
    desc="Sets interval after gaze tracking before head tracking starts"
    )

# ========== NON-CALLABLE FUNCTIONS ==========
# Releases all modifier keys (Mac users need to replace "alt:up" with "cmd:up")
def omega_mouse_modifiers_release_function() -> None:
    actions.key("ctrl:up")
    actions.key("shift:up")
    actions.key("alt:up")
    actions.key("super:up")
    #actions.key("cmd:up")

def enable_tracking_state() -> None:
    global om_tracking
    om_tracking = True
    update_tags()

def disable_tracking_state() -> None:
    global om_tracking
    om_tracking = False
    update_tags()

def get_tracking_state() -> bool:
    global om_tracking
    return om_tracking

def update_tags() -> None:
    global om_state
    global omega_mode

    tags: list[str] = []
    if om_state:
        tags.append("user.om_on")
        match omega_mode:
            case 0:
                tags.append("user.omega_full")
            case 1:
                tags.append("user.omega_lite")
            case 2:
                tags.append("user.omega_basic")
            case _:
                pass

        if get_tracking_state():
            tags.append("user.om_tracking")

    ctx.tags = tags

# ========== CALLABLE FUNCTIONS ==========
@mod.action_class
class OmegaMouseActions:

    def omega_mouse_toggle():
        """Toggles Omega Mouse on/off. When toggling on, checks for mode value."""
        global om_state
        global omega_mode
        
        if om_state == False:
            om_state = True
            omega_mode = setting_omega_mouse_mode.get()
            if omega_mode == 0:
                actions.tracking.control_toggle(True)
                actions.tracking.control_gaze_toggle(False)
                actions.tracking.control_head_toggle(False)
                actions.tracking.control_zoom_toggle(False)
                disable_tracking_state()
                update_tags()
                print(f"Full mode. First pop = {disable_tracking_state()}. tags = {list(ctx.tags)}")
            elif omega_mode == 1:
                actions.tracking.control_toggle(True)
                actions.tracking.control_gaze_toggle(False)
                actions.tracking.control_head_toggle(False)
                actions.tracking.control_zoom_toggle(False)
                update_tags()
                print(f"Lite mode. First pop = {disable_tracking_state()}. tags = {list(ctx.tags)}")                
            elif omega_mode == 2:
                actions.tracking.control_toggle(True)
                actions.tracking.control_gaze_toggle(False)
                actions.tracking.control_head_toggle(True)
                actions.tracking.control_zoom_toggle(False)
                update_tags()
                print(f"Basic mode. First pop = {disable_tracking_state()}. tags = {list(ctx.tags)}")
        else:
            om_state = False
            actions.tracking.control_toggle(False)
            actions.tracking.control_gaze_toggle(True)
            actions.tracking.control_head_toggle(True)
            actions.tracking.control_zoom_toggle(False)
            disable_tracking_state()
            update_tags()
            print(f"Omega Mouse off. First pop = {disable_tracking_state()}. tags = {list(ctx.tags)}")
                
    def omega_mouse_restart():
        """Resets Omega Mouse to initial state. Re-checks mode value."""
        global om_state
        global omega_mode
        
        if om_state == True:
            omega_mode = setting_omega_mouse_mode.get()
            if omega_mode == 0:
                actions.tracking.control_toggle(True)
                actions.tracking.control_gaze_toggle(False)
                actions.tracking.control_head_toggle(False)
                actions.tracking.control_zoom_toggle(False)
                disable_tracking_state()
                update_tags()
                print(f"Full mode. First pop = {disable_tracking_state()}. tags = {list(ctx.tags)}")
            elif omega_mode == 1:
                actions.tracking.control_toggle(True)
                actions.tracking.control_gaze_toggle(False)
                actions.tracking.control_head_toggle(False)
                actions.tracking.control_zoom_toggle(False)
                update_tags()
                print(f"Lite mode. First pop = {disable_tracking_state()}. tags = {list(ctx.tags)}")
            elif omega_mode == 2:
                actions.tracking.control_toggle(True)
                actions.tracking.control_gaze_toggle(False)
                actions.tracking.control_head_toggle(True)
                actions.tracking.control_zoom_toggle(False)
                update_tags()
                print(f"Basic Mode. First pop = {disable_tracking_state()}. tags = {list(ctx.tags)}")
        else:
            pass
    
    def omega_mouse_left_click():
        """Normal Left Click when Omega Mouse is off"""
        actions.mouse_click(0)
    
    def omega_mouse_left_modup_click():
        """Left Click that releases modifier keys afterwards when Omega Mouse is off"""
        actions.mouse_click(0)
        omega_mouse_modifiers_release_function()
    
    def omega_mouse_double_click():
        """Normal Double Click when Omega Mouse is off"""
        actions.mouse_click(0)
        actions.mouse_click(0)
    
    def omega_mouse_relocate():
        """Does nothing when Omega Mouse is off"""
        print("Does nothing when Omega Mouse is off")
    
    def omega_mouse_wait():
        """Does nothing when Omega Mouse is off"""
        print("Does nothing when Omega Mouse is off")

    def omega_mouse_state_check():
        """Checks state of Omega Mouse"""
        gaze_window = setting_gaze_capture_interval.get()
        head_lag = setting_head_track_lag.get()
        print("Omega Mouse states listed below...")
        print("om_state =", om_state)
        print("tags =", list(ctx.tags))
        print(f"gaze window interval = {gaze_window}")
        print(f"head track lag = {head_lag}")
        print("om_tracking =", disable_tracking_state())
        print(f"Drag State = {len(ctrl.mouse_buttons_down()) != 0}")
        #print(f" - Left Drag = {0 in list(ctrl.mouse_buttons_down())}")
        #print(f" - Middle Drag = {2 in list(ctrl.mouse_buttons_down())}")
        #print(f" - Right Drag = {1 in list(ctrl.mouse_buttons_down())}")


# ========== OVERRIDDEN FUNCTIONS ==========
@ctx_switch.action_class("user")
class OmegaMouseSwitchOverrides:

    # Turns off Omega Mouse states first before setting Control Mouse to default active state.
    # Helps to insure other eye tracking modes work as intended
    # (with no active remnants from Omega Mouse).
    def control_mouse_switch():
        """Turns off Omega Mouse first before switching to Control Mouse."""
        global om_state
        om_state = False
        actions.tracking.control_toggle(True)
        actions.tracking.control_gaze_toggle(True)
        actions.tracking.control_head_toggle(True)
        actions.tracking.control_zoom_toggle(False)
        disable_tracking_state()
        ctx.tags = []
        print("""Omega Mouse switched to Control Mouse. 'om_state' is now set to False.
              Omega Mouse tags are disabled.""")
    
    # Turns off Omega Mouse and Control Mouse first before setting Zoom Mouse to
    # default active state. Helps to insure other eye tracking modes work as intended
    # (with no active remnants from Omega Mouse).
    def zoom_mouse_switch():
        """Turns off Omega Mouse first before switching to Zoom Mouse."""
        global om_state
        om_state = False
        actions.tracking.control_toggle(False)
        actions.tracking.control_gaze_toggle(True)
        actions.tracking.control_head_toggle(True)
        actions.tracking.control_zoom_toggle(True)
        disable_tracking_state()
        ctx.tags = []
        print("""Omega Mouse switched to Zoom Mouse.'om_state' is now set to False.
              Omega Mouse tags are disabled.""")

# Enable Omega Mouse on startup
def on_ready():
    actions.user.omega_mouse_toggle()

app.register("ready", on_ready)
