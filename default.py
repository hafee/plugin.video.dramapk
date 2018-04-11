# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Pakistani Dramas from Youtube channels
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.dramapk'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID1 = "HUMTVOST"
YOUTUBE_CHANNEL_ID2 = "UC4JCksJF76g_MdzPVBJoC3Q"
YOUTUBE_CHANNEL_ID3 = "UCdmkPG3FG48A27-PrD-lC8A"
YOUTUBE_CHANNEL_ID4 = "UCe9JSDmyqNgA_l2BzGHq1Ug"
YOUTUBE_CHANNEL_ID5 = "UCatkw-24OJitQmOVKPhQk1g"
YOUTUBE_CHANNEL_ID6 = "UCecuhrESo2Pit4YDg8CQiGg"
YOUTUBE_CHANNEL_ID7 = "UCvZZ2w4QeQ5peDwOIPzlsjg"
YOUTUBE_CHANNEL_ID8 = "UC2m98kh188cg_9x248IZM9A"
YOUTUBE_CHANNEL_ID9 = "UCU1r97baEf3JJI5fY6NtMpA"
YOUTUBE_CHANNEL_ID10 = "UCQ5a6t32eTalvd-n2jQN1QQ"
YOUTUBE_CHANNEL_ID11 = "Urdu1TV"
YOUTUBE_CHANNEL_ID12 = "UC8JcgtFZBIIEr5h5JbfeHzA"
YOUTUBE_CHANNEL_ID13 = "UC5s8STnSC2SMsg09uFSfq7g"
YOUTUBE_CHANNEL_ID14 = "MashaBearEN"

# Entry point
def run():
    plugintools.log("dramapk.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("dramapk.main_list "+repr(params))
        
    plugintools.add_item( 
        #action="", 
        title="HUM TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID1+"/",
        thumbnail=icon,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="ARY Digital",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID2+"/",
        thumbnail=icon,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="A Plus Entertainment",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID3+"/",
        thumbnail=icon,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="HAR PAL GEO",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID4+"/",
        thumbnail=icon,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="TV One",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID5+"/",
        thumbnail=icon,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="ATV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID6+"/",
        thumbnail=icon,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="PTV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID7+"/",
        thumbnail=icon,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Aaj Entertainment",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID8+"/",
        thumbnail=icon,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Express Entertainment",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID9+"/",
        thumbnail=icon,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Pakistan popular dramas",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID10+"/",
        thumbnail=icon,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Urdu One",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID11+"/",
        thumbnail=icon,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Kids Islamic Stories",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID12+"/",
        thumbnail=icon,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Kids Quaid Say Baatein",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID13+"/",
        thumbnail=icon,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Kids Masha and The Bear",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID14+"/",
        thumbnail=icon,
        folder=True )

	
run()
