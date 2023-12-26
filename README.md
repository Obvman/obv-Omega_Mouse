# Omega Mouse (for Talon Voice)

### Shout Outs:
Shout out to Aegis, chaossparrot, Andreas Arvidsson, TimoTimo, Tommy Pensyl, Ziemowit Musiatowicz, and everyone at the Talon Slack channel who asnwered my rookie questions for being so patient. I learned a lot! Talon Slack channel can be found here: https://talonvoice.com/chat

## What is Omega Mouse:
Omega Mouse is an alternative way to interact with Control Mouse in Talon Voice. It’s basically just turning Gaze and Head tracking on and off at different times to change the user experience working with a hands-free mouse. It’s a simple user set that’s not very complex or robust.

There are three "modes" or behaviors that act a little differently, but generally they follow the same idea: the cursor only moves to your gaze when you *pop*, and then uses head tracking to fine tune your movement. This prevents unintended inputs from blinking or eye movements influencing the cursor. The original intention of this project is realized in "Full mode", which is basically a blend between Control Mouse and Zoom Mouse.

## YouTube Videos:
As I update Omega Mouse, these videos will inevitably become slightly out-of-date. So the current state of the project may look a little different from the videos. You can look at the video descriptions on YouTube to see what has changed since the video was uploaded (which I will do my best to update). Discrepancies will mainly include new features, but they might also displace code from the line numbers I specify in the videos. Hopefully discrepencies won't be too drastic and easy to figure out.
Omega Mouse - Entire Overview (37:19) | Omega Mouse - Setup (5:52)
:-: | :-:
[![Omega Mouse for Talon Voice - Entire Overview](https://img.youtube.com/vi/lqqNrb_iNwE/hqdefault.jpg)](https://www.youtube.com/watch?v=lqqNrb_iNwE&list=PLYFXZrgB8gIeVM7SnZI4NRcg5NEDfN9xi&index=5) | [![Omega Mouse for Talon Voice - Setup](https://img.youtube.com/vi/RveUpCPRUHs/hqdefault.jpg)](https://www.youtube.com/watch?v=RveUpCPRUHs&list=PLYFXZrgB8gIeVM7SnZI4NRcg5NEDfN9xi&index=2)

Omega Mouse - Talon File Explained (7:40) | Omega Mouse - Talon File Update - Cursor Interval Settings (8:45) | Omega Mouse - Update - 3 Commands + Overrides (3:45)
:-: | :-: | :-:
[![Omega Mouse for Talon Voice - Talon File Explained](https://img.youtube.com/vi/nyFWQ-anQSY/hqdefault.jpg)](https://www.youtube.com/watch?v=nyFWQ-anQSY&list=PLYFXZrgB8gIeVM7SnZI4NRcg5NEDfN9xi&index=3) | [![Omega Mouse for Talon Voice - Talon File Update - Cursor Interval Settings](https://img.youtube.com/vi/ediu4mcnQpM/hqdefault.jpg)](https://www.youtube.com/watch?v=ediu4mcnQpM&list=PLYFXZrgB8gIeVM7SnZI4NRcg5NEDfN9xi&index=4) | [![Omega Mouse for Talon Voice - Update - 3 Commands + Overrides](https://img.youtube.com/vi/_HO55Qlxaws/hqdefault.jpg)](https://www.youtube.com/watch?v=_HO55Qlxaws&list=PLYFXZrgB8gIeVM7SnZI4NRcg5NEDfN9xi&index=8)

Omega Mouse - Full Mode Spotlight (12:15) | Omega Mouse - Lite Mode Spotlight (5:44) | Omega Mouse - Basic Mode Spotlight (7:41)
:-: | :-: | :-:
[![Omega Mouse for Talon Voice - Full Mode Spotlight](https://img.youtube.com/vi/9pEe0V3MEUE/hqdefault.jpg)](https://www.youtube.com/watch?v=9pEe0V3MEUE&list=PLYFXZrgB8gIeVM7SnZI4NRcg5NEDfN9xi&index=4) | [![Omega Mouse for Talon Voice - Lite Mode Spotlight](https://img.youtube.com/vi/Jt_ecTYd_BI/hqdefault.jpg)](https://www.youtube.com/watch?v=Jt_ecTYd_BI&list=PLYFXZrgB8gIeVM7SnZI4NRcg5NEDfN9xi&index=5) | [![Omega Mouse for Talon Voice - Basic Mode Spotlight](https://img.youtube.com/vi/ntZiJ_JWY-k/hqdefault.jpg)](https://www.youtube.com/watch?v=ntZiJ_JWY-k&list=PLYFXZrgB8gIeVM7SnZI4NRcg5NEDfN9xi&index=6)

## Design Purpose:
The purpose was to get away from Control Mouse having the Gaze Tracking on all the time, as a few factors made this feature uncomfortable for me. First, I found the cursor constantly following my Gaze to be difficult on my eyes. Second, I have keratoconus in one eye, meaning I have to use single-eye tracking, which introduces more jitter to the cursor. And third, I found blinking to heavily displace the cursor by shooting it to the bottom of the screen. This later issue did not seem to be prevented by Control Mouse’s internal Gaze-pausing function consistently enough, which led to unsustainable eye strain. These issues could very well be personal biological issues I have with my eyes, or my setup at home. And though something like toggling the eye tracking with a shortcut could help with my first issue, I found these discomforts problematic enough to try and code my own preferred method of solving these obstacles.

This was designed with basic computer navigation in mind. It's probably too clunky for gaming purposes, like real-time RTS games. But I think it works well enough for turn-based games that primarily rely on a cursor.

## Control Mouse vs Omega Mouse Disclaimer:
**I am not a coder**, so I’m sure the code is not very advanced. In general, I do recommend you use the default Control Mouse in Talon Voice if possible. It will give you the most efficient and fluid experience of working hands-free. Omega Mouse is clunky, and was made for the niche audience of myself (and others in a similar situation). If I could use Control Mouse effectively, I would. But my personal preferences and situation made Control Mouse uncomfortable to use. So, if you cannot use Control Mouse for whatever reason, like me, you can give Omega Mouse a try.

There is also a “hidden” eye tracking mode in Talon Voice since the 0.4 release you can try first. Set Control Mouse on, Gaze Tracking off, Head Tracking on. When you look away from your cursor and move your head, the cursor will warp to your gaze. So even if the default Control mouse functionality doesn’t work for you, this might. However, I have found that 95% of the time it doesn’t really work with single eye tracking (like I have to use). Once in a while it picks up your eye gaze and shoots the cursor there, even if that was not your intention. But with 2 eye tracking, it’s fairly consistent. There is no way to disable this feature at the moment. This means it may interfere with your use of Omega Mouse. If you want to use Omega Mouse the way it was intended, I recommend you use single Eye tracking to minimize this cursor warping.

## Who is Omega Mouse For:
If you are a Talon Voice user, Omega Mouse may be for you if:
- You have to use one eye tracking instead of both eye tracking (this results in a jittery mouse)
- Your blinking normally throws your cursor off to an unsatisfactory degree
- You don’t want the cursor constantly following your Gaze.
- You like Zoom Mouse but wish it had head tracking functionality.

## Requirements:
- Talon Voice 0.4 public release (I’m subscribed to the beta, but the 0.4 release should include the required functionality.)
- Talon Community Repo Installed: https://github.com/talonhub/community
- Tobii Eye Tracker 5
- A Microphone.
	- Recommended mics for Talon Voice here: https://talon.wiki/hardware/
	- I’m using a cheap usb Koss CS-100. It works okay, but is prone to misidentifying commands.

## Set-Up:
To use Omega Mouse without unintended cursor warping, use single eye tracking. A "hidden" eye-tracking feature (mentioned in [Control Mouse vs Omega Mouse Disclaimer](#control-mouse-vs-omega-mouse-disclaimer) above) cannot be disabled at the moment. But usually doesn’t work with single eye tracking, making it the most reliable way to “disable” it so Omega Mouse can work as intended.

In order for Omega Mouse to maintain its proper functionality as error free as possible, mouse.talon must be edited in the community repo. The functions in [Eye_Tracking_Switches.py](Eye_Tracking_Switches.py) (***control_mouse_switch( )*** & ***zoom_mouse_switch( )***) must be placed into mouse.talon for the rules Control Mouse and Zoom Mouse respectively. If you want to keep the original commands intact to revert to them easily later (in case you ever remove Omega Mouse), add a "#" before the commands that are there by default to deactivate them. It should look like this in mouse.py:
```
control mouse:
	# tracking.control_toggle()
	user.control_mouse_switch()
zoom mouse:
	# tracking.control_zoom_toggle()
	user.zoom_mouse_switch()
```
*Note: Updating the community repo in the future will require you to either re-edit the mouse.py file, or resolve these merge conflicts if using Git. These edits allow Omega Mouse to turn off it’s behavior when switching to default Control Mouse or Zoom Mouse. Without these edits, if you were to switch to one of these modes from Omega Mouse, remnant behavior may continue and interfere with them.*

*Also Note: Omega Mouse must be switched to-and-from **VERBALLY**. Using the Talon menu with your mouse will bypass the switches in the code, leading to unintended behavior.*

### For Mac Users:
I don't have a Mac, so I have not tested this code on a Mac. But I assume it will work all the same. However, you will at least need to replace the "alt" key with "cmd" key in the function "omega_mouse_modifiers_release_function" found in the [Omega_Mouse.py](Omega_Mouse.py) file at line 50.

So, change this:
```
def omega_mouse_modifiers_release_function():
    actions.key("ctrl:up")
    actions.key("shift:up")
    actions.key("alt:up")
    actions.key("super:up")
    #actions.key("cmd:up")
```
To this:
```
def omega_mouse_modifiers_release_function():
    actions.key("ctrl:up")
    actions.key("shift:up")
    #actions.key("alt:up")
    actions.key("super:up")
    actions.key("cmd:up")
```

## 3 Mode Summary:
There are three “modes” in Omega Mouse (3 different contexts) that behave slightly differently: Full, Lite, and Basic. But they all follow the same idea: The cursor does not follow your eye gaze, but will warp to your eye gaze when popping, with fine-tuned movement reserved for Head tracking. FULL mode uses popping to both move the cursor and left click in a 2-phase process (like zoom mouse). LITE uses popping to warp the cursor to your gaze, but requires a separate command to click. BASIC is the same as LITE, except instead of Head tracking turning off to keep the cursor still when not in use, Head tracking remains on all the time. I found these three modes can each serve a purpose, but one may be good enough for you.

FULL MODE
-	Convenient use of popping for move-and-click
-	Clunkier to maneuver due to start-stop dynamic

LITE MODE
-	Maneuverable due to popping solely used for cursor movement.
-	Less convenient due to two commands for move-and-click

BASIC MODE
-	Most maneuverable due to popping solely used for cursor movement, and Head tracking always being on for small adjustments.
-	Less convenient due to two commands for move-and-click

The decision to make popping the primary cursor movement command across all three modes (instead of the primary clicking command typical in Talon Voice) came from noticing that moving the mouse needs to be an immediate response to feel satisfying. Clicking is easier to have patience for, since you’re hovering over your target already while you wait for Talon to parse your voice command.

### 3 Modes Explained:
**FULL MODE:** Moving the cursor and left clicking are done in a 2-phase process (like Zoom Mouse) with a popping sound. The first pop moves the cursor to your gaze (and enables Head tracking). The second pop left clicks (and disables Head tracking). If a mouse drag is occuring, the second pop will instead end the drag (including releasing any modifier keys). Actions like clicking or starting a drag will stop the cursor from moving.

It is possible that while you are in the second phase of the 2-phase process (i.e. when head tracking is active) you may want to exit the process, or stop the cusor from moving. This can be done with the voice command "wait", which will turn off tracking and reset the 2-phase process. This can be usefull if you don't want to commit to an actual click, such as changing your mind, or wanting to hover over a button to read a pop-up.

It is also possible that while you are in the second phase of the 2-phase process, you may need to move the cursor somewhere else prior to clicking. This can be done with the voice command "relo", which will relocate the cursor to your gaze by redoing the Phase-1 pop behavior. This helps make the 2-Phase process a bit less rigid, and can be useful in a few scenarios. For example:
- If the cursor did not move close enough to your desired location initially and head tracking isn't enough to compensate.
- If you change your mind about where you want the cursor to be
- If you are in the middle of a drag-and-drop process and want to move back to the start location without commiting the move.

*Note: The voice command "relo" will take longer for Talon Voice to parse than the pop sound. So expect some lag between saying "relo" and the cursor moving to your gaze.*

**LITE MODE:** Moving the cursor and left click are separated into two separate commands. Moving the cursor is done by a pop. Left click is done by saying “yum” or “gum”. Actions like mouse clicking or starting a drag will stop the cursor from moving.

The decision to settle on yum/gum came from observing the position of the tongue pre and post popping sound. The combination of popping and saying “yum” created a natural loop of commands that I found comfortable to run back-to-back. In order to pop, the back of the tongue has to block the passage of the throat to create a “cave” or “vacuum” for the pop sound to produce. After making a popping sound, the mouth remains open, but the tongue is still at the back of the throat. Having a sound that starts from the back of the throat is the most natural next sound to make (which I find “yum” to satisfy), and which most likely will need to be a left click. Likewise, to start another pop sound, the lips need to start together, which the M ending in “yum” provides.

**BASIC MODE:** The same as Lite Mode except actions like mouse clicking or starting a drag will not stop the cursor from moving, but instead will keep Head Tracking on. Essentially Control Mouse without eye gaze on all the time.

## Omega_Mouse.talon file syntax Explained
With all of the #'s in this file, it can maybe look a bit confusing, but it is important that these #'s stay where they are. This allows every voice command Omega Mouse uses to be listed in this one file.
- Lines 1, 3, 11, 25, 27, 33 are simply headers to help organize the file visually
- Lines 5-8 provide a description and options for the setting on line 9
- Lines 12-13, 15-16, 20-21 provide descriptions for the settings on lines 17 and 21

The #'s mixed in with the voice commands can look a bit messy (in lines 28-31 & 34-43)
- Voice commands without a '#' are commands actually defined in the file
- Voice commands with a '#' are commands not defined in this file, but in another talon file somewhere, like the community repo. Omega_Mouse will override the community repo behavior when these voice commands are spoken inside it's python code.

### Changing modes:
To choose which mode to use: Open the [Omega_Mouse.talon](Omega_Mouse.talon) file -> change the **user.omega_mouse_mode** setting number to 0 (Full mode), 1 (Lite mode), or 2 (basic mode) -> save the file -> If Omega Mouse was active when you made these changes, you must restart Omega Mouse to pick up the change.
```
# ----- Omega Mouse Mode Selection -----
settings():
	# Set which Omega Mouse mode to use. Omega Mouse restart required with change.
	# 0 = Full
	# 1 = Lite
	# 2 = Basic
	user.omega_mouse_mode = 0
```

### Cursor Time Intervals Explained:
The settings in the "Omega Mouse Cursor Time Intervals" block for *Gaze Capture Interval* and *Head Tracking Delay* allow you to tweak the response of Omega Mouse when moving the cursor. This can be helpful if you find the default capture or response times too fast or slow for you. We're dealing with milliseconds here, so these are not very impactful settings. (But this will hopefully make Omega Mouse more inclusive to individuals who may blink frequently due to some conditions or dry eyes.)
```
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
```

*Gaze Capture Interval:*
- This will let you set the window of time Gaze tracking is active to capture your gaze point before turning off.
- The default value is "50ms"
- A higher value will introduce more cursor movement before settling.
- A lower value may introduce failures to capture your gaze point.
- Actual setting **user.gaze_capture_interval** on line 17

*Head Tracking Delay:*
- This will let you set the amount of time between Gaze tracking turning off and Head tracking turning on.
- The default value is "50ms"
- A higher value will introduce more "dead" time before Head tracking starts.
- A lower value is not very noticeable.
- Actual setting **user.head_track_lag** on line 21

### Changing Cursor Time Intervals:
To change these values: Open the [Omega_Mouse.talon](Omega_Mouse.talon) file -> change the “user.gaze_capture_interval” setting and/or "the user.head_track_lag" setting to the desired values -> save the file.
- Values must include the quotes.
- Values will work across all Omega Mouse modes.
- Values should not exceed a combined value of 1800ms.
	- This is because Talon Voice uses a 2 sec watchdog, and these two setting values are in code that run back-to-back. This is effectively a total time where Talon Voice is non-responsive.
	- Even values close to 2000ms will set off Talon Voice's warning. 1800ms is therefore a good buffer.
	- Honestly, I don't expect anyone to need to use a combined value of 1800ms, so this is more informational.

*Remember, Talon Voice will be non-responsive for the duration of these setting values.*

### Dictation_Overrides_OM.talon Explained:
The talon file [Dictation_Overrides_OM.talon](Dictation_Overrides_OM.talon) defines the Omega Mouse voice commands so they are useable while in Dictation Mode. They are all sandwiched between a carrot sign (^) and a dollar sign ($). This means talon will only interpret these phrases as commands (and not words to spell out) if they are the only words spoken in the phrase. So ou can't string them together, but ensures they are not accidentally activated while dictating sentences. This is probably not necessary if you are using Talon Voice's Mixed Mode.

## Omega Mouse Commands:
There are 16 commands associated with Omega Mouse, whose behavior changes based on the mode they are in. Images of command logic flow charts are provided at the bottom for a (messy) visual reference.

*Note: By default, Omega Mouse requires you to use “yum” or “gum” for left click (lite/basic modes) and "twill" for double click (all modes). Omega Mouse overrides some community repo functions to work with the community voice commands you might be familiar with. But the community voice commands for left click and double click do not use functions easily overridden. To minimize editing mouse.py in the community repo on the user end, new functions had to be created to maintain Omega Mouse behavior, hence “yum/gum” and “twill”. If you have custom voice commands, they will need to be reconciled with the Omega Mouse functions. The community repo voice commands "Touch" (left click) and "Duke" or "Dub Click" (double click) will not trigger appropriate Omega Mouse behavior; you need to use "yum/gum" and "twill", or you need to edit in a way for those default voice commands to work.*

*Also Note: If you map mouse dragging to a physical switch, the code will recognize the drag state, but the 2-phase process will not restart like it would with a verbal command. See the "noise_trigger_pop()" function in [Omega_Mouse_Full.py](Omega_Mouse_Full.py) to see the code behavior.*

### Voice Commands List:
- **Omega Mouse:** Toggles Omega Mouse on/off. Captures mode value when turning on.
- **Omega Restart:** Sets Omega Mouse to initial states. Re-captures mode value.
- **Control Mouse:** Turns Omega Mouse off and switches to default Control Mouse
  - See [Set-Up](#set-up) section to make sure mouse.py edits are done correctly
  - Remember, switching out of Omega Mouse must be done *verbally* to turn it off correctly
- **Zoom Mouse:** Turns Omega Mouse off and switches to default Zoom Mouse
  - See [Set-Up](#set-up) section to make sure mouse.py edits are done correctly
  - Remember, switching out of Omega Mouse must be done *verbally* to turn it off correctly

- ***Popping sound*:**
  - Full Mode:
    - Phase 1: Moves cursor.
    - Phase 2: Left Click. (Freezes cursor.)
    - While dragging: Phase 2 releases all mouse buttons + Modifier keys. (Freezes cursor)
  - Lite Mode:
    - Moves cursor. (Freezes cursor)
  - Basic Mode:
    - Moves cursor
  - Omega Mouse Off:
    - Community default left click
- **Yum / Gum:**
  - Full Mode:
    - Left click. (Freezes cursor)
    - While dragging: Releases Mouse buttons + Modifier Keys. (Freezes cursor)
    - (Not really meant for Full Mode, but useful if cursor already over desired target)
  - Lite Mode:
    - Left click. (Freezes cursor)
    - While dragging: Releases Mouse buttons + Modifier Keys. (Freezes cursor)
  - Basic Mode:
    - Left click.
    - While dragging: Releases Mouse buttons + Modifier Keys.
  - Omega Mouse Off:
    - Left Click.
- **Yummer / Gummer:**
  - Full Mode:
    - Left click + release modifier keys (Freezes Cursor)
    - (Not really meant for Full mode, but useful if cursor already over desired target)
  - Lite Mode:
    - Left click + release modifier keys (Freezes Cursor)
  - Basic Mode:
    - Left click + release modifier keys
  - Omega Mouse Off:
    - Left click + release modifier keys
- **Twill:**
  - Full Mode:
    - Double click (Freezes cursor)
  - Lite Mode:
    - Double click (Freezes cursor)
  - Basic Mode:
    - Double click
  - Omega Mouse Off:
    - Double click
- **Trio:**
  - Full Mode:
    - Triple click (Freeze cursor)
  - Lite Mode:
    - Triple click (Freeze cursor)
  - Basic Mode:
    - Triple click
  - Omega Mouse Off:
    - Triple click
- **Con:**
  - Full Mode:
    - Control click (Freeze cursor)
  - Lite Mode:
    - Control click (Freeze cursor)
  - Basic Mode:
    - Control click
  - Omega Mouse Off:
    - Control click
- **Shill:**
  - Full Mode:
    - Shift click (Freeze cursor)
  - Lite Mode:
    - Shift click (Freeze cursor)
  - Basic Mode:
    - Shift click
  - Omega Mouse Off:
    - Shift click
- **Relo:**
  - Full Mode:
    - Relocates cursor to gaze during Phase 2 (redoes Phase 1)
  - Lite Mode:
    - Does nothing
  - Basic Mode:
    - Does nothing
  - Omega Mouse Off:
    - Does nothing
- **Wait:**
  - Full Mode:
    - Freezes cursor. (Does not release drag or modifier keys)
  - Lite Mode:
    - Freezes cursor. (Does not release drag or modifier keys)
  - Basic Mode:
    - Freezes cursor. (Does not release drag or modifier keys)
  - Omega Mouse Off:
    - Does nothing
- **Drag:**
  - Full Mode:
    - Starts a left mouse button hold. (Freezes cursor) (Alters 2-phase popping behavior)
  - Lite Mode:
    - Starts a left mouse button hold. (Freezes cursor)
  - Basic Mode:
    - Starts a left mouse button hold.
  - Omega Mouse Off:
    - Community default drag
- **Drop / Drag End / End Drag:**
  - Full Mode:
    - Releases all mouse buttons + Modifier keys. (Freezes cursor)
  - Lite Mode:
    - Releases all mouse buttons + Modifier keys. (Freezes cursor)
  - Basic Mode:
    - Releases all mouse buttons + Modifier keys.
  - Omega Mouse Off:
    - Community default drag end
- **Omega Check State:**
  - Full Mode:
    - Prints state of variables and tags in Talon log viewer (for troubleshooting)
  - Lite Mode:
    - Prints state of variables and tags in Talon log viewer (for troubleshooting)
  - Basic Mode:
    - Prints state of variables and tags in Talon log viewer (for troubleshooting)
  - Omega Mouse Off:
    - Prints state of variables and tags in Talon log viewer (for troubleshooting)

## Omega Mouse Logic Flow Chart for visual reference
![OmegaMouse_Default_logic_chart](https://github.com/MichaelOmegatron/Omega_Mouse/assets/71417272/4ba132b2-0aa0-46c2-b993-23d44b2c334f)

![OmegaMouse_Full_logic_chart_p1](https://github.com/MichaelOmegatron/Omega_Mouse/assets/71417272/30b2db13-f153-4745-9949-2be4f9f2e59a)

![OmegaMouse_Full_logic_chart_p2](https://github.com/MichaelOmegatron/Omega_Mouse/assets/71417272/af8c679a-45f4-4aaf-8a82-194bcee64987)

![OmegaMouse_Lite_logic_chart](https://github.com/MichaelOmegatron/Omega_Mouse/assets/71417272/7b0919e6-544b-4c38-bca5-3b13bf2b391a)

![OmegaMouse_Basic_logic_chart](https://github.com/MichaelOmegatron/Omega_Mouse/assets/71417272/63f88309-35b3-4749-9ded-ba3b8daed32d)
