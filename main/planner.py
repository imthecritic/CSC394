import copy
#AI Script that finds the optimal plan for the student

#notes
#Suggested Algorithm  A* - using the number of prereqs the class fulfills and whether it's a requirement or not be a heuristic for the search
#store the visited course paths as integers or strings of integers
#successor method that finds all possible classes you can take 
class Planner:
    
    def __init__(self, st, mjr, rt, rq):
        self.start  = st
        self.major  = mjr
        self.rt     = rt
        self.reqs   = rq
        
    quarters = ["Fall","Winter","Spring"]
    #test comment
    #takes list of possible courses, start date, end date, class taking rate, number of credits needed 
    def plan(self, courses, taken, start, rate,credits):
        print("  \n\n\n")
        courses_taken   = list(taken)
        courses_taken    = [cls.courseID.course_id.lower() for cls in taken]
        print courses_taken
        schedule    = []
        tsched      = []
        allclasses      = list(copy.deepcopy(courses))
        for c in allclasses: print(c.name)
        term = int(copy.deepcopy(start))
        rate = int(rate)
        initial = state(courses_taken,tsched, [],allclasses, term,rate,rate)
        options = self.getSuccessors(initial)
        cls_cntr = 0
        maxsize = 0
        #search loop  - while options have not been exhausted
        while(len(options) != 0):
            cls_cntr += 1
            current = options.pop(0)
            # if cls_cntr == 3:
            #     return current
            if  len(current.schedule) > maxsize:
                print(len(current.schedule))
                for c in current.schedule: print c.name, c.course_id
                print("  ")
                maxsize = len(current.schedule)
            if self.isGoal(current, credits):
                print (current.schedule)
                print ("finished")
                print (current.termsched)
                return self.beautify_planner(current.schedule + current.termsched, start, rate)
            else:
                if cls_cntr == rate:#number of classes for term has been acheived
                    cls_cntr = 0
                    term = term + 1 #set new term
                    if term == 4: term = 1
            options = self.getSuccessors(current) + options
        
        print ("done")       
        return [] # loop has failed         
                    
         
            
    def isGoal(self, opt, degreecredits):#return true if schedule is satisfied
        if ((len(opt.taken) + len(opt.termsched)) *4 >= degreecredits):
            return True
        else:
            return False
    
    def getSuccessors(self, plnr):
        options = []
        
        i = 0
        for course in plnr.available:
            if self.validPrereq(course, plnr.taken) and  self.offered(course,plnr.currterm): #course is valid insert to options
                #print course.name, course.course_id, "GOOD"
                #check if 
                #estimate    = self.getEstimate(course, courses_taken, courses)
                t = copy.deepcopy(plnr.taken)
                ts = copy.deepcopy(plnr.termsched)
                a = copy.deepcopy(plnr.available)
                s = copy.deepcopy(plnr.schedule)
                trm = copy.deepcopy(plnr.currterm)
                rt = copy.deepcopy(plnr.rate_avail)
                class_rate = copy.deepcopy(plnr.rate)
                
                ts.append(course)
                rt = rt - 1 
                if rt == 0:     #term is full of classes
                    rt = class_rate
                    trm += 1    #increase term
                    t += [c.course_id.lower() for c in ts]     #add term courses to taken
                    ts = []
                if trm > 4:
                    trm = 1
                    
                s.append(course) #append course to schedule
                #t.append(course.course_id.lower()) #append course to taken
                a = list(a)
                a.pop(i)
                new_state = state(t, ts, s, a,trm,class_rate,rt)
                options.append(new_state)
                #options = self.insertOption(options, courses_taken, course,current_total + estimate)
            i += 1 
        return options
                
    def beautify_planner(self, planner, start, rate):
        term_names = ['Fall:','Winter:','Spring:','Summer:']
        i = 0
        new_plan = []
        curr = []
        st = int(start) - 1
        curr.append(term_names[st])
        for cls in planner:
            curr.append(cls.course_id + ": " + cls.name)
            i += 1
            if i % (rate) == 0:
                st += 1
                st = st % len(term_names)
                new_plan.append(curr)
                curr = []
                curr.append(term_names[st])
        return new_plan
    
    #insert course into option list according to estimate            
    def insertOption(self,options,crse_taken, crse,est):
        if len(options == 0):
            return [([crse],est)]
        else:
            lst = [crse_taken] + [crse]
            for i in range(len(options)):
                if options[i][1] <= est:
                    options.insert(i,(lst,est)) #insert option 
                    return options
        options.append((lst,est))
        return options
            
    #calculates a heuristic value for the class   
    #requirement for degree and number of prereqs the class satisfies as a heuristic.
    def getEstimate(self, crse, crs_tkn, crselst):
        pass
     
    #returns True if class prereqs have been met      
    #returns false otherwise or if course is in taken
    def validPrereq(self, crse, taken):
        #return True
        tkn_names = taken
        #tkn_names = [cls.course_id.lower() for cls in taken]
        if crse.course_id.lower() in tkn_names: 
            return False
        elif crse.prereq.lower() == "none":
            return True
        elif crse.prereq[0] == "*": #special cases - need help with this
            return False
        else:
            #print crse.name
            pre = crse.prereq.lower()
            pre = pre.split(" ")
            #print (pre, taken)
            valid = self.helper(pre,tkn_names)
            #print crse.name, valid
            return valid
        return False
        
        #return True
    def helper(self, pre, tkn_names):
        i = 0
        lst_len = len(pre)
        bracket = False
        while i < lst_len:
            if pre[i] == "(": #enter bracket condition
                bracket = True
            elif pre[i] == ")":
                bracket = False
            elif pre[i] in tkn_names: # if class has been taken
                if i + 1 < lst_len: #if next element is valid index
                    if pre[i+1] == "or":
                        if not bracket: # no bracket prereqs have been met
                            return True
                        else:
                            while i < lst_len:
                                if pre[i] == ")" : #bracket is satisfied increase i until out of bracket
                                    bracket = False
                                    break
                                i += 1
                            i += 1
                            if i >= lst_len -1: return True #if end of list return True
                    elif pre[i+1] == "and": #prereq not met, increment i 
                        i += 1
                    elif i + 1 == lst_len -1: #end of list reqs met
                        return True
                else: #all reqs met
                    return True
            elif pre[i] == "or" or pre[i] == "and": #continue if condition statement
                pass
            else: # not in taken
                if i + 1 < lst_len: #if next element is valid index
                    if pre[i+1] != "or": #return false unless an or is next
                        if not bracket:
                            return False
                        else:
                            while i < lst_len -1:
                                if pre[i] == ")" : #bracket is satisfied increase i until out of bracket
                                    bracket == False
                                    if pre[i+1] == "and": #if next is and - you've failed 
                                        return False
                                    else:
                                        #i += 1 # increament pre[i] == "or"
                                        break
                                i += 1 
                    else:
                        i += 1 #increment pre[i] ==  "or"
    
            i += 1
    
        return False
                
    
    #returns True if class offered this term
    def offered(self, crse, trm):
        if trm == 1:
            return crse.fall
        elif trm == 2:
            return crse.winter
        elif trm == 3:
            return crse.spring
        elif trm == 4:
            return crse.summer
        else:
            return False
        
class state:
    #course list
    #current term
    #current 
    def __init__(self, tkn, tsched, sched, avail, trm, rat,rt):
        self.taken      = tkn
        self.termsched  = tsched
        self.schedule   = sched
        self.available  = avail
        self.currterm   = trm
        self.rate       = rat
        self.rate_avail = rt
        