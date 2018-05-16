import os.path
import json

def showResults(completeSurvey):
   print "\n"
   print completeSurvey["question"]
   print completeSurvey["Date"]

   total = completeSurvey["total"]
   print "Total answers: " + str(total)

   print "Answers: "
   for key in completeSurvey["survey"]:
      count = completeSurvey["survey"][key]
      print "   " + key + " : " + str(count) + " ( " + str("%.1f" % ((count * 1.0 / total) * 100)) +"% )"


def newSurvey():
   print "\n"
   question = raw_input("Please enter question for your survey: ")
   Date= raw_input( "Please enter the current date (mm/dd/yyyy): ")
   total = 0
   survey = {}

   while True:
      answer = raw_input("Answer: ")
      if answer in survey:
         survey[answer] = survey[answer] + 1
      else:
         survey[answer] = 1
      total = total + 1

      print "1. Record new answer"
      print "2. Show results"

      while True:
         choice = input("Youre choice: ")
         if choice == 1 or choice == 2:
            break
         print "Wrong input!"

      if choice == 2:
         break

   completeSurvey = {"question": question,"Date" :Date,"survey": survey, "total": total}
   if os.path.isfile("survey.json"):
      f = open("survey.json","r")
      history = json.load(f)
      f.close()
      history[len(history) + 1] = completeSurvey
      f = open("survey.json","w")
      json.dump(history, f)
      f.close()
   else:
      history = {"1": completeSurvey}
      f = open("survey.json","w")
      json.dump(history, f)
      f.close()
   showResults(completeSurvey)

   mainMenu()


def openHistory():
   print "\n"
   if os.path.isfile("survey.json"):
      f = open("survey.json","r")
      history = json.load(f)
      f.close()
      print "History:"
      print "<- 0. Back to Main Menu"
      for key in sorted(history):
         print "   " + key + ". " + history[key]["question"]

      while True:
         choice = str(input("Youre choice: "))
         if choice == "0":
            mainMenu()
            break
         if choice in history:
            showResults(history[choice])
            mainMenu()
            break
         print "Wrong input!"

   else:
      print "No history"
      mainMenu()


def mainMenu():
   print "\n"
   print "Welcome to Main Menu!!!"
   print "1. New Survey"
   print "2. Open History"
   print "3. Exit"

   while True:
      choice = input("Youre choice: ")
      if choice == 1:
         newSurvey()
         break
      elif choice == 2:
         openHistory()
         break
      elif choice == 3:
         break
      print "Wrong input!"


mainMenu()
