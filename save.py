import itertools

#add classes (prob schedule 8)

with open("classes.txt", "r") as file:
  first = file.readlines()  # life / finlit = 2367


def test(lst):  #if schedule works, return the schedule, else, return None
  tell = 0
  for i in range(len(lst)):
    if str(i + 1) not in lst[i]:
      tell = 1
      break
  if tell == 0:
    return list(lst)


def findClasses(
  classes
):  #input a list of classes, returns list of lists of working schedules
  permutations = list(itertools.permutations(classes, len(classes)))
  end = []
  for i in permutations:
    end.append(test(i))
  end = [item for item in end if item is not None]
  return end


def display(lst):  #takes list of classes and displays them better
  for t in range(len(lst)):
    print(str(t + 1) + ": " + str(lst[t]) + "")


def displayListception(lstception):
  print("\nFound " + str(len(lstception)) +
        " options\n")  #display for lists in lists
  for q in range(len(lstception)):
    print("____________\n")
    print(str(q + 1) + ":\n\n")
    display(lstception[q])
  print("____________\n\n")


def full(chosen, per):
  newChosen = chosen
  swap = newChosen[per].replace(str(per + 1), "")
  newChosen[per] = swap
  newSchedules = findClasses(newChosen)
  if len(newSchedules) == 0:
    possible = False
    return
  displayListception(newSchedules)
  return (newSchedules[int(
    input("\nChoose your schedule (1 - " + str(len(newSchedules)) + "):\n\n"))
                       - 1])


final = findClasses(first)
displayListception(final)

if input("Are you ready to register (or practice)?\n\n").lower()[0] == "y":
  choice = final[
    int(input("\nChoose your schedule (1 - " + str(len(final)) + "):\n\n")) -
    1]
  possible = True
  dynamicClass = choice
  while possible:
    print("\n" * 10)
    print(display(dynamicClass))
    dynamicClass = full(
      dynamicClass,
      int(input("\nIf a class fills up, press the number of the class \n\n")) -
      1)
    print("\n" * 10 + "No schedules found with those classes\n\n\n")

else:
  print("Aight cool")

  # make going from list of classes - final one function
