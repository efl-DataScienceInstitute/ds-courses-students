# Quiz – Introduction to Python
Dieses Übungsblatt beinhaltet Aufgaben zu dem efl-Kurs Introduction to Python, die euer Wissen zu den Kursinhalten basierend auf dem bereits verwendeten Gaming-Datensatz abfragen. Bitte bearbeitet diese Aufgaben eigenständig und erstellt eure Lösung in Form von dokumentiertem Code, in dem ihr eure Vorgehensweise beschreibt und auf die konkrete Frage im Quiz Bezug nehmt. Ihr könnt gerne das Code-Skeleton (8-case_study_skeleton.py) als Ausgangsbasis verwenden.

Sendet eure Lösungen bis zum 31. Dezember 2023 23:59 Uhr an dscourses@eflab.de mit dem Betreﬀ „Lösungen zum Python-Quiz“. Das Abschicken eurer Lösung ist Voraussetzung für den Erhalt eines Zertifikats für die Teilnahme am oben genannten Kurs.

Zur Bearbeitung der Fragen verwendet bitte folgende Python Bibliotheken: 
os 
pandas 
numpy 
matplotlib 
seaborn

Viel Erfolg und Spaß bei den Übungen! 

Aufgaben zur eigenständigen Bearbeitung:

Globale Umsätze
Berechne welche Plattform im Jahr 2010 den größten Umsatz (Global_Sales) ausweist? 
Wie groß ist der größte Umsatz?
Berechne welche Plattform im Jahr 2010 den geringsten Umsatz (Global_Sales) ausweist? 
Wie groß ist der geringste Umsatz? 
Tipp: https://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html  

Neue Spiele
Wie viele neue Spiele gibt es im Jahr 2013, d.h. all jene Spiele, die es in den vorherigen Jahren nicht gab? 
Tipp: Bitte verwende set für diese Aufgabe. 

Spielenamen	 
Wie heißt das Spiel mit dem längsten Namen?
Wie heißt das Spiel mit dem kürzesten Namen?
Umsatz	 
Überprüfe, ob für jedes Spiel gilt: Global_Sales = NA_Sales + EU_Sales + JP_Sales + Other_Sales. 
Tipp: Erstelle für den rechten Teil der Formel eine neue Variable calcSales. 
In wie vielen Fällen ist der in 4.1 stehende Ausdruck nicht korrekt?
Erstelle einige zusammenfassende Statistiken zu der Diﬀerenz calcSales - Global_Sales: 
Maximum 
Minimum 
Durchschnitt 
Varianz 
5% Perzentil
95% Perzentil Tipp: https://docs.scipy.org/doc/numpy/reference/generated/numpy.percentile.html 


Mario	 
Finde alle Spiele, die das Wort "Mario" beinhalten. Wie viele Spiele sind dies? 
Erstelle einen neuen Ordner "Mariogames". Speichere die in 5.1 identifizierten Spiele mit den Spalten Name, Platform und Year in eine Datei "Mariogames/Mariogames.csv". 
Erstelle ein Balkendiagramm ("bar plot"), um die Anzahl an Mariospielen pro Plattform zu zeigen.
