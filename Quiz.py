# Importing the necessary module(s)
import time

# A well-maintained Quiz built to unlock the power of your mind. This, being a class, acts as a blueprint for its objects(instances).
class Quiz:
    levels = {}
    def __init__(self):
        self.username = " "
        self.gameplay_num = 1
        self.level_num = 0
        self.net_levels = 0
        self.level_name = " "
        self.question_set = []
        self.quest_num = 0
        self.net_questions = 0
        self.question = " "
        self.options = []
        self.correct_ans = ' '
        self.earning = self.penalty = self.score = 0
        self.right_attempts, self.wrong_attempts, self.skips = 0, 0, 0
    def setup(self):
        """Sets up all the requirements to start the Game!"""
        print "\n\t[Starts at : ", time.asctime(),"]\n\n"
        time.clock()
        print "Welcome to the World of Mind-Boggling and Brainstorming! You've now entered into the Quiz..\n"
        time.sleep(.75)
        name = raw_input(' Hey Human, I\'m the QuizMaster. What\'s your Name : ')
        while name.isspace() or name == '' :
            name = raw_input('What\'s your Name : ')
        self.username = name
        print '\nHi', self.username, '! Welcome to the Quiz Game. Here comes the place where your knowledge will be tested in a fair manner.'
        print ' [It is Recommended that you Play it in Full-Screen Mode]\n'
        time.sleep(1)
        try:
            source = open("./Questions.txt", 'r')     #Source Data File
        except IOError :
            print "\t[ ERROR : Unable to Load Default Source File! ]\n"
            source = open("./quiz_data.txt", 'w+')
            source.write("-"*50+" User Disclaimer "+"-"*50+"""\n
\*\ This is the Question Data for the Quiz App! Do Not Modify it simply without having any Knowledge or without keeping up with the correct format of data.
\n[*]Format of A Level : 
 [LEVEL<level_tag>]:<Level_Identity>
 Q<two-digit_question_number>. <question_(should_fit_in_a_single_line)>
 ; <option1>; <option2>; <option3>; <option4>
 A<two-digit_question_number(should_match_same_question_number)>. (<option_input(a, b, c, d)>, <option>)
 Q<two-digit_question_number>. <question_(should_fit_in_a_single_line)>
 ; <option1>; <option2>; <option3>; <option4>
 A<two-digit_question_number(should_match_same_question_number)>. (<option_input(a, b, c, d)>, <option>)
    ...\n"""+"-"*120+"""
\n[LEVEL1]:Literature
Q01. 'scrub' means to
; blot; dispose; drape; clean
A01. ('d', 'clean')
Q02. Which of the following is best compatibe with the word 'store'
; shop; habit; college; passage
A02. ('a', 'store')
Q03. The opposite of healthy is
; modest; suitable; sick; apt
A03. ('c', 'sick')
Q04. 'repeat' means to
; make or do or perform again; direct the taking of; make perfect, bring to perfection; gather into a teeming multitude
A04. ('a', 'make again', 'do again', 'perform again', 'make or do or perform again')
Q05. Which of the following would best fit for 'an embarassing or tactical situation'
; deja vu; jamais vu; faux pas; faux ami
A05. ('c', 'faux pas')
""")
            source.seek(0)
        except :
            print "\t[ Unknown ERROR : Unable to Load Default Source File! The GamePlay cannot continue.]"
        content = source.read()
        source.close()
        content_lines = content.split('\n')
        for number in range(len(content_lines)):
            if content_lines[number].startswith("[LEVEL"):
                level_id = content_lines[number][9:]
                level_set = []
                total_questions = 0
                level_set.append(level_id)
                for increase in range(1, len(content_lines[number+1:])+1):
                    if content_lines[number+increase].startswith("[LEVEL"):
                        break
                    question_details = []
                    if content_lines[number+increase].startswith("Q"):
                        total_questions += 1
                        question = content_lines[number+increase][5:]
                        question_details.append(question)
                        question_details.append(tuple(content_lines[number+increase+1][1:].split(';')))
                        question_details.append(content_lines[number+increase+2][5:])
                        level_set.append(question_details)
                self.question_set.append(level_set)
                Quiz.levels[level_id] = total_questions
        self.net_levels = len(Quiz.levels)
        show = raw_input("Do you want to have a look on the Rules before we start the Game(yes/no) : ").lower()
        if show in ('yes', 'y', 'ok'):
            print " [ Great Move! ]"
            time.sleep(1.1)
            self.Rules()
        ask = raw_input("\n You might be sure of moving ahead. If not, there's still a chance .. Do you want to Quit? (y/n) : ").lower()
        if ask in ('y', 'yes') :
            print 'Your Honesty is well-appericiated!', '\n\n\t', 'Never Mind, Maybe Some Other Day!'
            quit()      # This will terminate the program 
        elif ask in ('n', 'no') :
            print 'That\'s like a real Human!'
        else :
            print "This Time, I assume it to be a 'No'. But remember, it won't happen always."
            time.sleep(.75)
        print "\n\t[Let the Game Begin . . . ]"
    def Rules(self):
        """Displays the Rules for the Quiz line-by-line.\n Contains most of necessary Guidelines and User-Information which imply a better control for this Game Player."""
        print "\n", "\'"*55, "[ RULES ]", "'"*55
        time.sleep(1)
        print "Here are the Rules of this Quiz : \n"
        time.sleep(.5)
        print "1.   Read what is asked before you Answer. Once answered, your Answer cannot be modified under any case."
        time.sleep(.3)
        print " 2.  There are no Time Limits. So Relax and Play Calmly."
        time.sleep(.3)
        print "3.   There are Negative Markings in the Quiz! Play smartly, and try to score maximum."
        time.sleep(.3)
        print " 4.  For every correct answer, you will earn +10 points, and for every incorrect answer, you will have a loss of -5 points from your score"
        time.sleep(.3)
        print "5.   You can Answer by simply typing in your choice(after the question is displayed) after the \'>>\', and Press ENTER to submit the Answer. "
        time.sleep(.3)
        print " 6.  Once a game begins, you won't be able to Pause it in between. You must finish a Level or else you won't be allowed to Play Next Level."
        time.sleep(.3)
        print "7.   You can skip a Question, by typing \'s\', \'skip\' or \'next\',  if you don't know it's Answer. This will save you from any of the Negative Marking(s)."
        time.sleep(.3)
        print " 8.  You have the choice to play additional BONUS question(s) at the end of each level."
        time.sleep(.3)
        print "9.   If you answer them correctly, you'll get +5 points. There won't be any negative marking for the bonus questions."
        time.sleep(.3)
        print " 10. You can have a review on the Game only after you finish the Game. After that, you can even Replay the Game to try to improve your score!"
        time.sleep(.4)
        print "11.  You can Finish the GamePlay anytime by writing \"##GiveUp\" or \"#GiveUp#\" in place of answer. Type it the same way as displayed, else it won't work!\n\n"
        time.sleep(.3)
        print "\'"*119, "\n\n\t[ !! GOOD LUCK !! ] \n"
        time.sleep(1)
    def Refresh(self):
        """Updates the GamePlay, loads the next info ..."""
        self.quest_num += 1
        if self.quest_num > self.net_questions:
            time.sleep(.5)
            print "\n\t = { Level Finished! } = "
            time.sleep(.75)
            print " ::> Your Total Score is = ", self.score
            print "\n !:!{ Time Elapsed (from starting) : "+str(time.clock())+" seconds }!:!"
            self.Level_Up()
            self.Refresh()
        else :
            self.question = self.question_set[self.level_num-1][self.quest_num][0]
            if self.question[1:6].upper() == "BONUS":
                self.earning = 5
                self.penalty = 0
                choice = raw_input("\n ... Would you like to continue with a bonus/additional question from this level? (yes/no) : ").lower()
                print "  --> ",
                if choice in ('yes', 'y', '1'):
                    print "Bravo! Go for It!"
                elif choice in ('no', 'n', '0'):
                    print "No Problem!\n"
                    self.Level_Up()
                else :
                    print "Moving On! Quick-Quick!\n"
                    self.Level_Up()
            else :
                self.earning = 10
                self.penalty = 5
            self.options = self.question_set[self.level_num-1][self.quest_num][1]
            try :
                self.correct_ans = eval(self.question_set[self.level_num-1][self.quest_num][2])
            except :
                self.correct_ans = ()
                self.Refresh()
    def Level_Up(self):
        """Loads up the Next Level"""
        self.quest_num = 0
        self.level_num += 1
        if self.level_num > self.net_levels:
            self.END()
        else :
            self.level_name = self.question_set[self.level_num-1][0]
            self.net_questions = len(self.question_set[self.level_num-1])-1
            time.sleep(1.25)
            print "\n\t\t[LEVEL : "+str(self.level_num)+"]\n\t- = {"+str(self.level_name)+"} = -"
            time.sleep(.75)
            if self.level_num == 1 :
                print " (Game's On!)"
            else:
                print " (Game's still On!)"
    def Base(self):
        """The Base handles a basic syntax of the Question Display, and checks the user-answer with the correct one, and then proceeds accordingly."""
        self.Refresh()
        print "\nQ"+str(self.quest_num)+". "+str(self.question)+"?"
        time.sleep(.9)
        print "(a) "+str(self.options[0])+"\t\t\t(b) "+str(self.options[1])
        print "(c) "+str(self.options[2])+"\t\t\t(d) "+str(self.options[3])
        time.sleep(.75)
        print "Your Answer : ",
        user_entry = raw_input(">> ").lower()
        while user_entry.startswith(' ') or user_entry.startswith('\t') :
            user_entry = user_entry[1:]
        while user_entry.endswith(' ') or user_entry.endswith('\t') :
            user_entry = user_entry[:-1]
        if user_entry in ("##giveup", "##give up", "#giveup#", "#give up#"):
            self.END()
        if user_entry in self.correct_ans:
            print " --> Correct! <-- "
            self.right_attempts += 1
            self.score += self.earning
        elif user_entry in ('s', "skip", "next") :
            print " -- Skipping Up! --> "
            self.skips += 1
        else :
            print " --> Wrong! <-- "
            self.wrong_attempts += 1
            self.score -= self.penalty
        self.Base()     # Calling a function within itself is known as Recursion
    def END(self):
        """Marks the finishing of the Game!"""
        print "\n\n -- -- [ Quiz Completed! ] -- -- "
        time.sleep(.75)
        print "\nHave a review on the Game : "
        time.sleep(.75)
        print "[*]Total Questions : ", self.right_attempts + self.wrong_attempts + self.skips
        print "[*]Number of Favourable Questions (Correct Attempts) : ", self.right_attempts
        print "[*]Number of Unfavourable Questions (Wrong Attempts) : ", self.wrong_attempts
        print "[*]Number of Questions Skipped : ", self.skips
        print "[*] -- Score Attained -- : ", self.score
        time.sleep(1.5)
        self.Leaderboard()
        demand = raw_input("\nWould you like to Replay for a better score (yes/no) : ").lower()
        if demand in ('yes', 'y', '1'):
            self.RePlay()
        print '\n\t[Ended at : ', time.ctime(),"]\n\n"   # Marks the Ending time (Displays Date and Time at the time of execution)
        print "\n\t\t[ The Game Play has Ended Successfully! ]"
        print "\n\n -- -- -- Thanks For Playing! Please Visit Again! -- -- -- "
        # One Final Step - Press ENTER to EXIT  
        choice = raw_input("\n\t.. [PRESS ENTER TO EXIT] ..")
        exit()
    def Leaderboard(self, filename = 'quiz_leaderboard'):
        """Displays the Leaderboard and Updates the Entry"""
        reference = open(filename+".txt", 'a+')
        data = [self.username, Quiz.levels, self.right_attempts + self.wrong_attempts + self.skips, self.right_attempts, self.wrong_attempts, self.skips, self.score, "Play Turn : "+str(self.gameplay_num)]
        reference.write("\n"+str(data))
        reference.seek(0)
        details = reference.readlines()
        extract = []
        reference.close()
        choice = raw_input("\nWould you like to have a look at the High-Scores?(yes/no) : ").lower()
        if choice in ('yes', 'y', '1'):
            print "\nHere are the all-time High-Scorers with their rankings in this LeaderBoard:"
            print "\n", "- - "*16+"[ HIGH-SCORES ]"+" - -"*16
            print " Rank\tName\t\t\tScore\tLevels Played\tQuestions Played/Total Questions\tCorrect Answer(s)\tIncorrect Answer(s)"
            for info in details :
                try :
                    info = eval(info)
                except :
                    continue
                Name = info[0]
                num_levels = len(info[1])
                num_questions = sum(info[1].values())
                num_correct = info[3]
                num_incorrect = info[4]
                num_of_pass = info[5]
                num_attempts = info[2] #num_correct+num_incorrect+num_of_pass
                user_score = info[6]
                if Name.isspace() or num_levels == 0 :
                    continue
                extract.append([Name, user_score, num_levels, str(num_attempts)+"/"+str(num_questions), num_correct, num_incorrect])
            ## Selection Sorting !
            for sort in range(len(extract)):
                for item in range(sort+1, len(extract)):
                    if extract[item][1]>extract[sort][1]:
                        extract[item], extract[sort] = extract[sort], extract[item]
            # Deciding the Rank and displaying the contents of score-sorted list
            for flag in range(len(extract)) :
                if flag == 0 :
                    rank = 1
                else :
                    if extract[flag][1] < extract[flag-1][1] :
                        rank += 1
                while len(extract[flag][0]) < 4 :
                    extract[flag][0] += ' '
                if len(extract[flag][0]) >= 12 :
                    extract[flag][0] += '\t'
                name_print = extract[flag][0] + "\t"*(4-len(extract[flag][0])/4)
                print " "+str(rank)+"\t"+name_print+str(extract[flag][1])+"\t\t"+str(extract[flag][2])+"\t\t"+extract[flag][3]+"\t\t\t\t"+str(extract[flag][4])+"\t"*4+str(extract[flag][5])
            print "- - "*16+"[That's All]"+" - -"*16
        elif choice in ('no', 'n', '0'):
            print " [As You Wish!]\n"
        else :
            print "[I didn't Get That One! You're in a hurry, I suppose.]\n"
    def RePlay(self):
        """Restarts the Quiz from the Beginning"""
        print "\t\t[Please wait while the Game Reboots ... ] "
        print "_"*100
        print
        self.gameplay_num += 1
        print "\t\t >> [Consecutive Game Attempt Number : ", self.gameplay_num, "] <<"
        time.sleep(1.75)
        self.score = 0
        self.right_attempts = self.wrong_attempts = self.skips = 0
        self.level_num = self.quest_num = 0
        self.Level_Up()
        self.Base()

# __main__
session1 = Quiz()
session1.setup()
session1.Level_Up()
session1.Base()
