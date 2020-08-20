# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 19:21:35 2020

@author: acer
"""
import os
import pyttsx3
decision = False

pyttsx3.speak("Hello there! welcome")
#these have correctors which can be spelling,typing or pronounciation related
start=["start","open","launch","run","execute","play",
       "rnu","rin","eun","ran","sthart","stert","strt",
       "stort","strat","atart","stret","dtart","syart",
       "strit","opan","opne","opwn","oprn","opem","opam",
       "poen","opeb","opn","opm","lonch","leunch","loench",
       "laanch","lanch","lauch","lunch","loch","leanch",
       "lsunch","excute","ezecute","egzecute","ezxecute",
       "execuet","esecute","exevute","ececute","evevute",
       "ezeuet","exacute","excute","xecute","eggsecute",
       "exceute","exacuet","wexecute","wexute","plae",
       "ple","polay","pla","paly","payl","ply"]
length1=len(start)
notepad=["notepad","text","text editor","writer","write",
         "netopad","noetpad","notpad",'neotpad','notepaid',"knotpad",
         "knoetpad","notped","notepaed",'naughtpad',"noughtpad",
         "noghtpad","nitepad","noterpad","notepda","notedap","notepa",
         "noetpaid","wrtitar","wrtier",'wryter',"ryter",'raiter','righter',
         'riter','raitar','weriter','wariter','typer','texter','taxt',
         'taext','toaxt','tekst','tikst','taext','tskst','editar','editer',
         'aditer','aediter','edotir','edotar','edutar','eduter','editoor',
         'edditor','editar','edigtar']
length2=len(notepad)
chrome=['chrome','browser','web','internet','surf','online','google','corme','chorme',
        'krome','khrome','chrom','vhrome','xrome','chirme','chrime','chrone',
        'chorne','cjorme','cjrome','chroem','crome','chrpme','wbe','weeb','qeb',
        'brawser','vrowser','nroweser','browres','brwoerser','broweser','browersr',
        'bewser','serf','sarf','sorf','srf','instarnat','intarnat','internat','intrenet',
        'intaranat','inetrenet','intaernet','onternet','pnternet','unternet','internte',
        'intranet','ineternet']
length3=len(chrome)
paint=['paint','mspaint','draw','color','art','paoint','paitn','pant','pent','panet',
       'psint','oaint','pnt','poaint','piant','paunt','patin','[aint','mspanet',
       'microsoft paint','drew','dra','drawn','sraw','drsw','colour','kolar','kolor',
       'colar','coler','coolor','cloro','coloro','colro','colouro','cholor','cholors',
       'colors','colours','colra','aart','artist','arter','ort','arth']
length4=len(paint)
end = ['end','quit','stop','exit','shut']#these do not have correctors because exiting the program may be undesirable unless specifically specified
length5=len(end)
    
while True:
	
    print("what could i do for you: ")
    query=input()
    query.lower()
    done = False
    i=0
    j=0
    k=0
    l=0
    m=0
    while i<length1 and done == False:
        if(start[i] in query):
           decision = True
        else:
           i+=1
        if decision == True:
            while j<length2 and done == False:
                if(notepad[j] in query):
                    os.system("notepad")
                    done=True
                    break
                else:
                    j+=1
            while k<length3 and done == False:
                if(chrome[k] in query):
                    os.system("chrome")
                    done=True
                    break
                else:
                   k+=1
            while l<length4 and done == False:
                if(paint[l] in query):
                    os.system("mspaint")
                    done =True
                    break
                else:
                    l+=1
    while m<length5:
        if(end[m] in query):
            exit()
        else :
            m+=1
    if(done==False):
        print("sorry i could not understand you")
        
        
                
        









