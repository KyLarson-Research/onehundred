#File Name: onehundreddaysofcode.py
#Author: Kyle Carlton Larson
#Purpose to create an auto schedule generator for GC to structure work
#Format =
#-------BOF.ics
#BEGIN:VEVENT
#DTSTART:20160206T160000Z
#DTEND:20160206T170000Z
#DTSTAMP:20201124T175045Z
#UID:69hjioj2cgpjgbb274s36b9k6ko6cbb2chj3ab9i65ij8c9lc5h3cdj36c@google.com
#CREATED:20160201T184852Z
#DESCRIPTION:
#LAST-MODIFIED:20160201T184852Z
#LOCATION:Cimarron Center\, W Clearview Blvd\, Surprise\, AZ 85387\, United 
# States
#SEQUENCE:0
#STATUS:CONFIRMED
#SUMMARY:Blood donation Agua Fria room
#TRANSP:OPAQUE
#END:VEVENT
#-------EOF.ics
#notes
# 20160206T160000Z
# yyyyMMdd'T'HHmmss
#
import datetime as dt

def mkCalendarStr(org_str):
	cal_str =''
	full =''
	cal_str += 'BEGIN:VCALENDAR'+'\n'
	cal_str += 'PRODID:-//Google Inc//Google Calendar 70.9054//EN'+'\n'
	cal_str += 'VERSION:2.0'+'\n'
	cal_str += 'CALSCALE:GREGORIAN'+'\n'
	cal_str += 'METHOD:PUBLISH'+'\n'
	cal_str += 'X-WR-CALNAME:kyle10204@gmail.com'+'\n'
	cal_str += 'X-WR-TIMEZONE:America/Phoenix'+'\n'
#	cal_str += 'BEGIN:VTIMEZONE'+'\n'
#	#cal_str += 'TZID:America/Denver'+'\n'
#	#cal_str += 'X-LIC-LOCATION:America/Denver'+'\n'
#	#cal_str += 'BEGIN:DAYLIGHT'+'\n'
#	#cal_str += 'TZOFFSETFROM:-0700'+'\n'
#	#cal_str += 'TZOFFSETTO:-0600'+'\n'
#	#cal_str += 'TZNAME:MDT'+'\n'
#	cal_str += 'DTSTART:19700308T020000'+'\n'
#	cal_str += 'RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU'+'\n'
#	cal_str += 'END:DAYLIGHT'+'\n'
#	cal_str += 'BEGIN:STANDARD'+'\n'
#	cal_str += 'TZOFFSETFROM:-0600'+'\n'
#	cal_str += 'TZOFFSETTO:-0700'+'\n'
#	cal_str += 'TZNAME:MST'+'\n'
#	cal_str += 'DTSTART:19701101T020000'+'\n'
#	cal_str += 'RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU'+'\n'
#	cal_str += 'END:STANDARD'+'\n'
#	cal_str += 'END:VTIMEZONE'+'\n'
	cal_str += 'BEGIN:VTIMEZONE'+'\n'
	cal_str += 'TZID:America/Phoenix'+'\n'
	cal_str += 'X-LIC-LOCATION:America/Phoenix'+'\n'
	cal_str += 'BEGIN:STANDARD'+'\n'
	cal_str += 'TZOFFSETFROM:-0700'+'\n'
	cal_str += 'TZOFFSETTO:-0700'+'\n'
	cal_str += 'TZNAME:MST'+'\n'
	cal_str += 'DTSTART:19700101T000000'+'\n'
	cal_str += 'END:STANDARD'+'\n'
	cal_str += 'END:VTIMEZONE'+'\n'
	full = cal_str + org_str + 'END:VCALENDAR'
	return full
	
def addEventStr(event_name, summary, location, date):
	event_str = ''
	event_str += 'BEGIN:VEVENT' + '\n'
	event_str += 'DTSTART:'+date+ 'T80000Z' + '\n'
	event_str += 'DTEND:'+date+'T110000Z'+ '\n'
	#event_str += 'DTSTAMP:20201124T175045Z'
	event_str += 'UID:69hjioj2cgpjgbb274s36b9k6ko6cbb2chj3ab9i65ij8c9lc5h3cdj36c@google.com' + '\n'#user id
	event_str += 'CREATED:20160201T184852Z' + '\n'
	event_str += 'DESCRIPTION:'+ event_name + '\n'
	event_str += 'LAST-MODIFIED:20160201T184852Z' + '\n'
	event_str += 'LOCATION:'+ location +'\n'
	event_str += 'SEQUENCE:0' + '\n'
	event_str += 'STATUS:CONFIRMED' + '\n'
	event_str += 'SUMMARY:' + summary + '\n'
	event_str += 'TRANSP:OPAQUE' + '\n'
	event_str += 'END:VEVENT' + '\n'
		#event_str += str(dt.datetime.today())
	#event_str += '\n'
	#event_str += event_name
	return event_str
	
	
date_obj = dt.datetime.today()

eventDate = date_obj+ dt.timedelta(days=1)
eventDate = eventDate.strftime("%Y%m%d")
work = 'dev' + str(eventDate)
eventName = work + 'name'
eventSummary = work + 'summary'
eventLocation = 'home'

fname = work+'v8'
f = open(fname+".ics", "a")#open and append

def daysOfCode(days):
	work = 'dev' 
	eventName = work + 'name'
	eventSummary = work + 'summary'
	eventLocation = 'home'	
	repeatEventStr =''
	for days in range(1,days):
		work ='dev'+str(days+1)
		eventName = work + ' day ' +str((days+1)%4)
		eventSummary = work 
		eventLocation = 'home'
		eventDate = date_obj+ dt.timedelta(days=days)
		eventDate = eventDate.strftime("%Y%m%d")
		repeatEventStr += addEventStr(eventName, eventSummary, eventLocation, eventDate)
	return repeatEventStr
		
f.write( mkCalendarStr( daysOfCode(100) ) )
f.close()

f = open(fname + ".ics", "r")
print(f.read())