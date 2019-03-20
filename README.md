## Twitter data collector

Toolset for collecting tweets using Twitter streaming API and managing the files. These tools were primarily created for [Project HYTE](http://webfocus.aka.fi/ibi_apps/WFServlet?IBIF_ex=x_HakKuvaus&CLICKED_ON=&HAKNRO1=308850&UILANG=en&IBIAPP_app=aka_ext&TULOSTE=HTML). HYTE stands for *Hybrid Terrorizing. Developing a New Model for the Study of Global Media Events of Terrorist Violence*.

Before we start, we want to emphasize that the presented environement is by no means fully reliable or production-ready. There must exist more polished tools for the task. At the same time, we have been succesfull in collecting sets of tweets that enable the investigations of various hybrid media events.

First, you need a reliable server environment. We use the CSC cPouta infrastructure to run the collector. We give instructions on how to set up an environment elsewhere.

...

Start a screen 

	screen -S run.collector 


Detach a screen: ctrl+a, ctrl+d

Return to a screen 

	screen -r run.collector


You may end up collecting a volumnious stream of tweets



Folder size in descending order

    du -sh * | sort -rh

Keep watching disk usage on the server (update every 60 seconds)

    watch -n 60 df -h
