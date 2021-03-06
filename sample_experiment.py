#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04),
    on Sun Dec 18 20:22:52 2016
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'sample_experiment'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1440, 900), fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
text_instruction = visual.TextStim(win=win, name='text_instruction',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "wait_scanner"
wait_scannerClock = core.Clock()
text_scanner = visual.TextStim(win=win, name='text_scanner',
    text="Waiting for scanner...\n(Press 'a')",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "task"
taskClock = core.Clock()
text_variables_task = visual.TextStim(win=win, name='text_variables_task',
    text='default text',
    font='Arial',
    pos=[0,0.5], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
text_task = visual.TextStim(win=win, name='text_task',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "stimuli_pic"
stimuli_picClock = core.Clock()
stim_image_1 = visual.ImageStim(
    win=win, name='stim_image_1',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_7 = visual.TextStim(win=win, name='text_7',
    text='*** Only the picture for 10 seconds ... ***',
    font='Arial',
    pos=[0, 0.5], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "breath_trigger"
breath_triggerClock = core.Clock()
stim_image_2 = visual.ImageStim(
    win=win, name='stim_image_2',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_breath = visual.TextStim(win=win, name='text_breath',
    text="*** Waiting for breath key input ('e', 'i')... ***",
    font='Arial',
    pos=[0, 0.5], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "trigger_odor"
trigger_odorClock = core.Clock()
import serial

# open port
# port = serial.Serial("COM4", 19200, timeout=0.5)

stim_image_3 = visual.ImageStim(
    win=win, name='stim_image_3',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_5 = visual.TextStim(win=win, name='text_5',
    text='*** Triggering odor for 5 seconds ... ***',
    font='Arial',
    pos=[0, 0.5], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "answer"
answerClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Which picture did you see?\napple (1)\nstrawberry (2)\nwood (3)\npencil (4)',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()

text_feedback_1 = visual.TextStim(win=win, name='text_feedback_1',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "rating"
ratingClock = core.Clock()
text_rating = visual.TextStim(win=win, name='text_rating',
    text='Did you like it?',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
##IMPORTED CODE

from psychopy.iohub import launchHubServer, EventConstants
io=launchHubServer()
keyboard_scale = io.devices.keyboard

##IMPORTED CODE

rating_scale = visual.RatingScale(win=win, name='rating_scale', marker=u'triangle', size=1.0, pos=[0.0, -0.4], low=0, high=1, precision=100, showValue=False, markerExpansion=0, scale=u'', markerStart=u'5')

# Initialize components for Routine "end"
endClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Closing text goes here.\n\nBye!',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction"-------
t = 0
instructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
text_instruction.setText('Placeholder welcome text.\n\nEnter here basic information about the following task.\nIncluding instructions and how to response.\n\n- Press 1, 2, 3 or 4 to continue -')
key_instruction = event.BuilderKeyResponse()
# keep track of which components have finished
instructionComponents = [text_instruction, key_instruction]
for thisComponent in instructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instruction* updates
    if t >= 0.0 and text_instruction.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instruction.tStart = t
        text_instruction.frameNStart = frameN  # exact frame index
        text_instruction.setAutoDraw(True)
    
    # *key_instruction* updates
    if t >= 0.0 and key_instruction.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_instruction.tStart = t
        key_instruction.frameNStart = frameN  # exact frame index
        key_instruction.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_instruction.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_instruction.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_instruction.keys = theseKeys[-1]  # just the last key pressed
            key_instruction.rt = key_instruction.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_instruction.keys in ['', [], None]:  # No response was made
    key_instruction.keys=None
thisExp.addData('key_instruction.keys',key_instruction.keys)
if key_instruction.keys != None:  # we had a response
    thisExp.addData('key_instruction.rt', key_instruction.rt)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "wait_scanner"-------
t = 0
wait_scannerClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_scanner = event.BuilderKeyResponse()
# keep track of which components have finished
wait_scannerComponents = [text_scanner, key_scanner]
for thisComponent in wait_scannerComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "wait_scanner"-------
while continueRoutine:
    # get current time
    t = wait_scannerClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_scanner* updates
    if t >= 0.0 and text_scanner.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_scanner.tStart = t
        text_scanner.frameNStart = frameN  # exact frame index
        text_scanner.setAutoDraw(True)
    
    # *key_scanner* updates
    if t >= 0.0 and key_scanner.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_scanner.tStart = t
        key_scanner.frameNStart = frameN  # exact frame index
        key_scanner.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_scanner.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_scanner.status == STARTED:
        theseKeys = event.getKeys(keyList=['a'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_scanner.keys = theseKeys[-1]  # just the last key pressed
            key_scanner.rt = key_scanner.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wait_scannerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wait_scanner"-------
for thisComponent in wait_scannerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_scanner.keys in ['', [], None]:  # No response was made
    key_scanner.keys=None
thisExp.addData('key_scanner.keys',key_scanner.keys)
if key_scanner.keys != None:  # we had a response
    thisExp.addData('key_scanner.rt', key_scanner.rt)
thisExp.nextEntry()
# the Routine "wait_scanner" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli_data.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "task"-------
    t = 0
    taskClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_variables_task.setText("*** Stim Nr. "+ str(stim_nr) + " of available 16 (randomly chosen) ***")
    text_task.setText('Task instruction goes here.\n In the following task you have to ...\n- Press 1, 2, 3 or 4 to continue -')
    key_task = event.BuilderKeyResponse()
    # keep track of which components have finished
    taskComponents = [text_variables_task, text_task, key_task]
    for thisComponent in taskComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "task"-------
    while continueRoutine:
        # get current time
        t = taskClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_variables_task* updates
        if t >= 0.0 and text_variables_task.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_variables_task.tStart = t
            text_variables_task.frameNStart = frameN  # exact frame index
            text_variables_task.setAutoDraw(True)
        
        # *text_task* updates
        if t >= 0.0 and text_task.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_task.tStart = t
            text_task.frameNStart = frameN  # exact frame index
            text_task.setAutoDraw(True)
        
        # *key_task* updates
        if t >= 0.0 and key_task.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_task.tStart = t
            key_task.frameNStart = frameN  # exact frame index
            key_task.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_task.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_task.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', 'left', 'right', 'space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_task.keys = theseKeys[-1]  # just the last key pressed
                key_task.rt = key_task.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "task"-------
    for thisComponent in taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_task.keys in ['', [], None]:  # No response was made
        key_task.keys=None
    trials.addData('key_task.keys',key_task.keys)
    if key_task.keys != None:  # we had a response
        trials.addData('key_task.rt', key_task.rt)
    # the Routine "task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "jitter"-------
    t = 0
    jitterClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    jitterComponents = [text]
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "jitter"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = jitterClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in jitterComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "jitter"-------
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "stimuli_pic"-------
    t = 0
    stimuli_picClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    stim_image_1.setImage(pic_file)
    # keep track of which components have finished
    stimuli_picComponents = [stim_image_1, text_7]
    for thisComponent in stimuli_picComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimuli_pic"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimuli_picClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim_image_1* updates
        if t >= 0.0 and stim_image_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim_image_1.tStart = t
            stim_image_1.frameNStart = frameN  # exact frame index
            stim_image_1.setAutoDraw(True)
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if stim_image_1.status == STARTED and t >= frameRemains:
            stim_image_1.setAutoDraw(False)
        
        # *text_7* updates
        if t >= 0.0 and text_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_7.tStart = t
            text_7.frameNStart = frameN  # exact frame index
            text_7.setAutoDraw(True)
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_7.status == STARTED and t >= frameRemains:
            text_7.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimuli_picComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimuli_pic"-------
    for thisComponent in stimuli_picComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "breath_trigger"-------
    t = 0
    breath_triggerClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_listen_to_breath = event.BuilderKeyResponse()
    stim_image_2.setImage(pic_file)
    # keep track of which components have finished
    breath_triggerComponents = [key_listen_to_breath, stim_image_2, text_breath]
    for thisComponent in breath_triggerComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "breath_trigger"-------
    while continueRoutine:
        # get current time
        t = breath_triggerClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_listen_to_breath* updates
        if t >= 0.0 and key_listen_to_breath.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_listen_to_breath.tStart = t
            key_listen_to_breath.frameNStart = frameN  # exact frame index
            key_listen_to_breath.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_listen_to_breath.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_listen_to_breath.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_listen_to_breath.keys = theseKeys[-1]  # just the last key pressed
                key_listen_to_breath.rt = key_listen_to_breath.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *stim_image_2* updates
        if t >= 0.0 and stim_image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim_image_2.tStart = t
            stim_image_2.frameNStart = frameN  # exact frame index
            stim_image_2.setAutoDraw(True)
        
        # *text_breath* updates
        if t >= 0.0 and text_breath.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_breath.tStart = t
            text_breath.frameNStart = frameN  # exact frame index
            text_breath.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in breath_triggerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "breath_trigger"-------
    for thisComponent in breath_triggerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_listen_to_breath.keys in ['', [], None]:  # No response was made
        key_listen_to_breath.keys=None
    trials.addData('key_listen_to_breath.keys',key_listen_to_breath.keys)
    if key_listen_to_breath.keys != None:  # we had a response
        trials.addData('key_listen_to_breath.rt', key_listen_to_breath.rt)
    # the Routine "breath_trigger" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trigger_odor"-------
    t = 0
    trigger_odorClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    # open odor channel
    # port.write("\nF%x\r" %odor_channel)
    stim_image_3.setImage(pic_file)
    # keep track of which components have finished
    trigger_odorComponents = [stim_image_3, text_5]
    for thisComponent in trigger_odorComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trigger_odor"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trigger_odorClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *stim_image_3* updates
        if t >= 0.0 and stim_image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim_image_3.tStart = t
            stim_image_3.frameNStart = frameN  # exact frame index
            stim_image_3.setAutoDraw(True)
        frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if stim_image_3.status == STARTED and t >= frameRemains:
            stim_image_3.setAutoDraw(False)
        
        # *text_5* updates
        if t >= 0.0 and text_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_5.tStart = t
            text_5.frameNStart = frameN  # exact frame index
            text_5.setAutoDraw(True)
        frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_5.status == STARTED and t >= frameRemains:
            text_5.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trigger_odorComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trigger_odor"-------
    for thisComponent in trigger_odorComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # close odor channe
    # port.write("\nF%x\r" %odor_channel) 
    
    
    # ------Prepare to start Routine "answer"-------
    t = 0
    answerClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_answer = event.BuilderKeyResponse()
    # keep track of which components have finished
    answerComponents = [key_answer, text_6]
    for thisComponent in answerComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "answer"-------
    while continueRoutine:
        # get current time
        t = answerClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_answer* updates
        if t >= 0.0 and key_answer.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_answer.tStart = t
            key_answer.frameNStart = frameN  # exact frame index
            key_answer.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_answer.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_answer.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_answer.keys = theseKeys[-1]  # just the last key pressed
                key_answer.rt = key_answer.clock.getTime()
                # was this 'correct'?
                if (key_answer.keys == str(corrAns_pic)) or (key_answer.keys == corrAns_pic):
                    key_answer.corr = 1
                else:
                    key_answer.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *text_6* updates
        if t >= 0.0 and text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_6.tStart = t
            text_6.frameNStart = frameN  # exact frame index
            text_6.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in answerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "answer"-------
    for thisComponent in answerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_answer.keys in ['', [], None]:  # No response was made
        key_answer.keys=None
        # was no response the correct answer?!
        if str(corrAns_pic).lower() == 'none':
           key_answer.corr = 1  # correct non-response
        else:
           key_answer.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_answer.keys',key_answer.keys)
    trials.addData('key_answer.corr', key_answer.corr)
    if key_answer.keys != None:  # we had a response
        trials.addData('key_answer.rt', key_answer.rt)
    # the Routine "answer" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    if key_answer.corr == 1:
        txt = 'Your answer was correct.'
    else:
        txt = 'Your answer was wrong.'
    text_feedback_1.setText(str(txt))
    # keep track of which components have finished
    feedbackComponents = [text_feedback_1]
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_feedback_1* updates
        if t >= 0.0 and text_feedback_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_feedback_1.tStart = t
            text_feedback_1.frameNStart = frameN  # exact frame index
            text_feedback_1.setAutoDraw(True)
        frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_feedback_1.status == STARTED and t >= frameRemains:
            text_feedback_1.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ------Prepare to start Routine "rating"-------
    t = 0
    ratingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    
    increment = 0
    
    
    
    rating_scale.reset()
    # keep track of which components have finished
    ratingComponents = [text_rating, rating_scale]
    for thisComponent in ratingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "rating"-------
    while continueRoutine:
        # get current time
        t = ratingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_rating* updates
        if t >= 0.0 and text_rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_rating.tStart = t
            text_rating.frameNStart = frameN  # exact frame index
            text_rating.setAutoDraw(True)
        for event in keyboard_scale.getEvents():
            if event.type == EventConstants.KEYBOARD_PRESS:
                if event.key == u'right':
                    increment = 0.01 # move one step to the right
                elif event.key == u'left':
                    increment = -0.01 # move one step to the left
            if event.type == EventConstants.KEYBOARD_RELEASE:
                increment = 0 # stop changing position
        
        if 0 < rating_scale.markerPlacedAt < 1:
            rating_scale.markerPlacedAt += increment
        # *rating_scale* updates
        if t >= 0.0 and rating_scale.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_scale.tStart = t
            rating_scale.frameNStart = frameN  # exact frame index
            rating_scale.setAutoDraw(True)
        continueRoutine &= rating_scale.noResponse  # a response ends the trial
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ratingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rating"-------
    for thisComponent in ratingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # store data for trials (TrialHandler)
    trials.addData('rating_scale.response', rating_scale.getRating())
    trials.addData('rating_scale.rt', rating_scale.getRT())
    # the Routine "rating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text_4]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_4.status == STARTED and t >= frameRemains:
        text_4.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)



# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
