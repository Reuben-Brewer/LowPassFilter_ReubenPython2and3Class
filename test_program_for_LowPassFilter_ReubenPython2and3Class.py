# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision J, 11/10/2024

Verified working on: Python 2.7, 3.8 for Windows 8.1, 10 64-bit, Ubuntu 20.04, and Raspberry Pi Buster (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

###########################################################
from LowPassFilter_ReubenPython2and3Class import *
from MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class import *
###########################################################

###########################################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
import math, numpy
import traceback
import re
import random
from random import randint
import keyboard
###########################################################

###########################################################
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
###########################################################

###########################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
###########################################################

#######################################################################################################################
#######################################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def UpdateFrequencyCalculation():
    global CurrentTime_MainLoopThread
    global LastTime_MainLoopThread
    global DataStreamingFrequency_MainLoopThread
    global DataStreamingDeltaT_MainLoopThread
    global Counter_MainLoopThread

    try:
        DataStreamingDeltaT_MainLoopThread = CurrentTime_MainLoopThread - LastTime_MainLoopThread

        if DataStreamingDeltaT_MainLoopThread != 0.0:
            DataStreamingFrequency_MainLoopThread = 1.0 / DataStreamingDeltaT_MainLoopThread

        LastTime_MainLoopThread = CurrentTime_MainLoopThread
        Counter_MainLoopThread = Counter_MainLoopThread + 1

    except:
        exceptions = sys.exc_info()[0]
        print("UpdateFrequencyCalculation ERROR, Exceptions: %s" % exceptions)
        traceback.print_exc()
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def ExitProgram_Callback(OptionalArugment = 0):
    global EXIT_PROGRAM_FLAG

    print("ExitProgram_Callback event fired!")

    EXIT_PROGRAM_FLAG = 1
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
if __name__ == '__main__':

    ####################################################
    ####################################################
    global my_platform

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname():  # os.uname() doesn't work in windows
            my_platform = "pi"
        else:
            my_platform = "linux"

    elif platform.system() == "Windows":
        my_platform = "windows"

    elif platform.system() == "Darwin":
        my_platform = "mac"

    else:
        my_platform = "other"

    print("The OS platform is: " + my_platform)
    ####################################################
    ####################################################

    ####################################################
    ####################################################
    global USE_LOWPASSFILTER_FLAG
    USE_LOWPASSFILTER_FLAG = 1

    global USE_KEYBOARD_FLAG
    USE_KEYBOARD_FLAG = 1

    global USE_PLOTTER_FLAG_Raw
    USE_PLOTTER_FLAG_Raw = 1
    
    global USE_PLOTTER_FLAG_Filtered
    USE_PLOTTER_FLAG_Filtered = 1

    global USE_SINUSOIDAL_INPUT_FLAG
    USE_SINUSOIDAL_INPUT_FLAG = 0

    global USE_SPECKLE_NOISE_FLAG
    USE_SPECKLE_NOISE_FLAG = 1
    ####################################################
    ####################################################
    
    ####################################################
    ####################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global LastTime_MainLoopThread
    LastTime_MainLoopThread = -11111.0

    global DataStreamingFrequency_MainLoopThread
    DataStreamingFrequency_MainLoopThread = -11111.0

    global DataStreamingDeltaT_MainLoopThread
    DataStreamingDeltaT_MainLoopThread = -11111.0

    global StartingTime_MainLoopThread
    StartingTime_MainLoopThread = -1

    global Counter_MainLoopThread
    Counter_MainLoopThread = 0

    global desired_angle_deg_1
    desired_angle_deg_1 = 0.0

    global SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle
    SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle = 1.0

    global SINUSOIDAL_MOTION_INPUT_MinValue
    SINUSOIDAL_MOTION_INPUT_MinValue = -90.0

    global SINUSOIDAL_MOTION_INPUT_MaxValue
    SINUSOIDAL_MOTION_INPUT_MaxValue = 90.0

    global NoiseCounter
    NoiseCounter = 0

    global NoiseCounter_FireEveryNth
    NoiseCounter_FireEveryNth = 20

    global NoiseAmplitude_Percent0to1OfSinuisoidalInputAmplitude
    NoiseAmplitude_Percent0to1OfSinuisoidalInputAmplitude = 1.0
    ####################################################
    ####################################################

    ####################################################
    ####################################################
    global LowPassFilter_ReubenPython2and3ClassObject

    global LOWPASSFILTER_OPEN_FLAG
    LOWPASSFILTER_OPEN_FLAG = -1

    global LowPassFilter_ReubenPython2and3ClassObject_MostRecentDict
    LowPassFilter_ReubenPython2and3ClassObject_MostRecentDict = dict()

    global LowPassFilter_ReubenPython2and3ClassObject_MostRecentDict_SignalInRaw
    LowPassFilter_ReubenPython2and3ClassObject_MostRecentDict_SignalInRaw = -11111.0

    global LowPassFilter_ReubenPython2and3ClassObject_MostRecentDict_SignalOutSmoothed
    LowPassFilter_ReubenPython2and3ClassObject_MostRecentDict_SignalOutSmoothed = -11111.0

    global LowPassFilter_ReubenPython2and3ClassObject_MostRecentDict_DataStreamingFrequency
    LowPassFilter_ReubenPython2and3ClassObject_MostRecentDict_DataStreamingFrequency = -11111.0
    ####################################################
    ####################################################

    ####################################################
    ####################################################
    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_Raw

    global PLOTTER_OPEN_FLAG_Raw
    PLOTTER_OPEN_FLAG_Raw = -1
    ####################################################
    ####################################################

    ####################################################
    ####################################################
    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_Filtered

    global PLOTTER_OPEN_FLAG_Filtered
    PLOTTER_OPEN_FLAG_Filtered = -1
    ####################################################
    ####################################################

    ####################################################
    ####################################################
    if USE_LOWPASSFILTER_FLAG == 1:
        try:
            LowPassFilter_ReubenPython2and3ClassObject_setup_dict = dict([("UseMedianFilterFlag", 1),
                                                                        ("UseExponentialSmoothingFilterFlag", 0),
                                                                        ("ExponentialSmoothingFilterLambda", 0.2)]) #new_filtered_value = k * raw_sensor_value + (1 - k) * old_filtered_value

            LowPassFilter_ReubenPython2and3ClassObject = LowPassFilter_ReubenPython2and3Class(LowPassFilter_ReubenPython2and3ClassObject_setup_dict)
            LOWPASSFILTER_OPEN_FLAG = LowPassFilter_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("LowPassFilter_ReubenPython2and3Class __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    ####################################################
    ####################################################

    #################################################
    #################################################
    global MyPlotterPureTkinter_MostRecentDict_Raw
    MyPlotterPureTkinter_MostRecentDict_Raw = dict()

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag_Raw
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag_Raw = -1



    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict_Raw = dict([("EnableInternal_MyPrint_Flag", 1),
                                                                                                ("NumberOfPrintLines", 10),
                                                                                                ("GraphCanvasWidth", 900),
                                                                                                ("GraphCanvasHeight", 500),
                                                                                                ("GraphCanvasWindowStartingX", 0),
                                                                                                ("GraphCanvasWindowStartingY", 0),
                                                                                                ("GUI_RootAfterCallbackInterval_Milliseconds_IndependentOfParentRootGUIloopEvents", 20)])

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict_Raw
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict_Raw = dict([("GUIparametersDict", MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict_Raw),
                                                                                        ("ParentPID", os.getpid()),
                                                                                        ("WatchdogTimerExpirationDurationSeconds_StandAlonePlottingProcess", 5.0),
                                                                                        ("MarkerSize", 3),
                                                                                        ("CurvesToPlotNamesAndColorsDictOfLists", dict([("NameList", ["Raw", "Filtered"]),("ColorList", ["Red", "Green"])])),
                                                                                        ("NumberOfDataPointToPlot", 50),
                                                                                        ("XaxisNumberOfTickMarks", 10),
                                                                                        ("YaxisNumberOfTickMarks", 10),
                                                                                        ("XaxisNumberOfDecimalPlacesForLabels", 3),
                                                                                        ("YaxisNumberOfDecimalPlacesForLabels", 3),
                                                                                        ("XaxisAutoscaleFlag", 1),
                                                                                        ("YaxisAutoscaleFlag", 0),
                                                                                        ("X_min", 0.0),
                                                                                        ("X_max", 20.0),
                                                                                        ("Y_min", 1.1*SINUSOIDAL_MOTION_INPUT_MinValue),
                                                                                        ("Y_max", 1.1*SINUSOIDAL_MOTION_INPUT_MaxValue),
                                                                                        ("XaxisDrawnAtBottomOfGraph", 0),
                                                                                        ("XaxisLabelString", "Time (sec)"),
                                                                                        ("YaxisLabelString", "Y-units (units)"),
                                                                                        ("ShowLegendFlag", 1)])

    if USE_PLOTTER_FLAG_Raw == 1:
        try:
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_Raw = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class(MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict_Raw)
            time.sleep(0.25)
            PLOTTER_OPEN_FLAG_Raw = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_Raw.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_Raw, exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPlotterPureTkinter_MostRecentDict_Filtered
    MyPlotterPureTkinter_MostRecentDict_Filtered = dict()

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag_Filtered
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag_Filtered = -1



    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict_Filtered = dict([("EnableInternal_MyPrint_Flag", 1),
                                                                                                ("NumberOfPrintLines", 10),
                                                                                                ("GraphCanvasWidth", 900),
                                                                                                ("GraphCanvasHeight", 500),
                                                                                                ("GraphCanvasWindowStartingX", 0),
                                                                                                ("GraphCanvasWindowStartingY", 510),
                                                                                                ("GUI_RootAfterCallbackInterval_Milliseconds_IndependentOfParentRootGUIloopEvents", 20)])

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict_Filtered
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict_Filtered = dict([("GUIparametersDict", MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict_Filtered),
                                                                                        ("ParentPID", os.getpid()),
                                                                                        ("WatchdogTimerExpirationDurationSeconds_StandAlonePlottingProcess", 5.0),
                                                                                        ("MarkerSize", 3),
                                                                                        ("CurvesToPlotNamesAndColorsDictOfLists", dict([("NameList", ["Raw", "Filtered"]),("ColorList", ["Red", "Green"])])),
                                                                                        ("NumberOfDataPointToPlot", 50),
                                                                                        ("XaxisNumberOfTickMarks", 10),
                                                                                        ("YaxisNumberOfTickMarks", 10),
                                                                                        ("XaxisNumberOfDecimalPlacesForLabels", 3),
                                                                                        ("YaxisNumberOfDecimalPlacesForLabels", 3),
                                                                                        ("XaxisAutoscaleFlag", 1),
                                                                                        ("YaxisAutoscaleFlag", 0),
                                                                                        ("X_min", 0.0),
                                                                                        ("X_max", 20.0),
                                                                                        ("Y_min", 1.1*SINUSOIDAL_MOTION_INPUT_MinValue),
                                                                                        ("Y_max", 1.1*SINUSOIDAL_MOTION_INPUT_MaxValue),
                                                                                        ("XaxisDFilterednAtBottomOfGraph", 0),
                                                                                        ("XaxisLabelString", "Time (sec)"),
                                                                                        ("YaxisLabelString", "Y-units (units)"),
                                                                                        ("ShowLegendFlag", 1)])

    if USE_PLOTTER_FLAG_Filtered == 1:
        try:
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_Filtered = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class(MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict_Filtered)
            time.sleep(0.25)
            PLOTTER_OPEN_FLAG_Filtered = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_Filtered.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_Filtered, exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_KEYBOARD_FLAG == 1:
        keyboard.on_press_key("esc", ExitProgram_Callback)
    #################################################
    #################################################

    #################################################
    #################################################
    if LOWPASSFILTER_OPEN_FLAG != 1:
        print("Failed to open LowPassFilter_ReubenPython2and3ClassObject.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_PLOTTER_FLAG_Raw == 1 and PLOTTER_OPEN_FLAG_Raw != 1:
        print("Failed to open MyPlotterPureTkinterClass_Object_Raw.")
        #ExitProgram_Callback()
    #################################################
    #################################################

    ####################################################
    ####################################################
    random.seed()
    ####################################################
    ####################################################

    ####################################################
    ####################################################
    ####################################################

    StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()
    while(EXIT_PROGRAM_FLAG == 0):
        ####################################################
        ####################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
        ####################################################
        ####################################################

        #################################################### GET's
        ####################################################
        if LOWPASSFILTER_OPEN_FLAG == 1:

            LowPassFilter_ReubenPython2and3ClassObject_MostRecentDict = LowPassFilter_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "DataStreamingFrequency" in LowPassFilter_ReubenPython2and3ClassObject_MostRecentDict:
                LowPassFilter_ReubenPython2and3ClassObject_MostRecentDict_SignalInRaw = LowPassFilter_ReubenPython2and3ClassObject_MostRecentDict["SignalInRaw"]
                LowPassFilter_ReubenPython2and3ClassObject_MostRecentDict_SignalOutSmoothed = LowPassFilter_ReubenPython2and3ClassObject_MostRecentDict["SignalOutSmoothed"]
                LowPassFilter_ReubenPython2and3ClassObject_MostRecentDict_DataStreamingFrequency = LowPassFilter_ReubenPython2and3ClassObject_MostRecentDict["DataStreamingFrequency"]

                #print("LowPassFilter_ReubenPython2and3ClassObject_MostRecentDict_DataStreamingFrequency: " + str(LowPassFilter_ReubenPython2and3ClassObject_MostRecentDict_DataStreamingFrequency))
        ####################################################
        ####################################################

        #################################################### SET's
        ####################################################
        ####################################################
        if LOWPASSFILTER_OPEN_FLAG == 1:

            ####################################################
            ####################################################
            if USE_SINUSOIDAL_INPUT_FLAG == 1:

                ####################################################
                time_gain = math.pi / (2.0 * SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle)
                desired_angle_deg_1 = 0.5*(SINUSOIDAL_MOTION_INPUT_MaxValue + SINUSOIDAL_MOTION_INPUT_MinValue) + math.exp(0.1*CurrentTime_MainLoopThread)*0.5 * abs(SINUSOIDAL_MOTION_INPUT_MaxValue - SINUSOIDAL_MOTION_INPUT_MinValue) * math.sin(time_gain * CurrentTime_MainLoopThread)  # AUTOMATIC SINUSOIDAL MOVEMENT
                ####################################################

            else:
                desired_angle_deg_1 = 0.0
            ####################################################
            ####################################################

            ####################################################
            ####################################################
            if USE_SPECKLE_NOISE_FLAG == 1:

                ####################################################
                NoiseCounter = NoiseCounter + 1
                if NoiseCounter == NoiseCounter_FireEveryNth:
                    NoiseAmplitude = NoiseAmplitude_Percent0to1OfSinuisoidalInputAmplitude*abs(SINUSOIDAL_MOTION_INPUT_MaxValue - SINUSOIDAL_MOTION_INPUT_MinValue)
                    NoiseValue = random.uniform(-1.0*NoiseAmplitude, NoiseAmplitude)
                    desired_angle_deg_1 = desired_angle_deg_1 + NoiseValue
                    NoiseCounter = 0
                ####################################################

            ####################################################
            ####################################################

            LowPassFilter_ReubenPython2and3ClassObject.AddDataPointFromExternalProgram(desired_angle_deg_1)
        ####################################################
        ####################################################
        ####################################################

        ####################################################
        ####################################################
        if PLOTTER_OPEN_FLAG_Raw == 1:

            ####################################################
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_Raw = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_Raw.GetMostRecentDataDict()
            #print(str(MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_Raw))

            if "StandAlonePlottingProcess_ReadyForWritingFlag" in MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_Raw:
                MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag_Raw = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_Raw["StandAlonePlottingProcess_ReadyForWritingFlag"]
            else:
                pass
            ####################################################

            ####################################################
            if MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag_Raw == 1:
                MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_Raw.ExternalAddPointOrListOfPointsToPlot("Raw",
                                                                                                                            CurrentTime_MainLoopThread,
                                                                                                                            LowPassFilter_ReubenPython2and3ClassObject_MostRecentDict_SignalInRaw)
            ####################################################

        ####################################################
        ####################################################

        ####################################################
        ####################################################
        if PLOTTER_OPEN_FLAG_Filtered == 1:

            ####################################################
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_Filtered = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_Filtered.GetMostRecentDataDict()
            #print(str(MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_Filtered))

            if "StandAlonePlottingProcess_ReadyForWritingFlag" in MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_Filtered:
                MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag_Filtered = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_Filtered["StandAlonePlottingProcess_ReadyForWritingFlag"]
            else:
                pass
            ####################################################

            ####################################################
            if MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag_Filtered == 1:
                MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_Filtered.ExternalAddPointOrListOfPointsToPlot("Filtered",
                                                                                                                                 CurrentTime_MainLoopThread,
                                                                                                                                 LowPassFilter_ReubenPython2and3ClassObject_MostRecentDict_SignalOutSmoothed)
            ####################################################

        ####################################################
        ####################################################

        ####################################################
        ####################################################
        UpdateFrequencyCalculation()
        time.sleep(0.040)
        ####################################################
        ####################################################

    ####################################################
    ####################################################
    ####################################################

    ################################################# THIS IS THE EXIT ROUTINE!
    #################################################
    print("Exiting main program 'test_program_for_LowPassFilter_ReubenPython2and3Class.")

    #################################################
    if PLOTTER_OPEN_FLAG_Raw == 1:
        MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_Raw.ExitProgram_Callback()
    #################################################
    
    #################################################
    if PLOTTER_OPEN_FLAG_Filtered == 1:
        MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_Filtered.ExitProgram_Callback()
    #################################################

    #################################################
    #################################################

#######################################################################################################################
#######################################################################################################################