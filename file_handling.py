feedback=input("Enter the feedback: ")

with open("feedback_log.txt","a")as log:
    log.write(feedback+"\n")

print("Thanks for you feedback is saved...! ")