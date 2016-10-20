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
        courses_taken   = taken
        schedule        = []
        #visited       = []
        allclasses      = copy.deepcopy(courses)
        print allclasses
        term = copy.deepcopy(start)
        initial = state(courses_taken, [], allclasses, term)
        options = self.getSuccessors(initial)
        cls_cntr = 0
        #search loop  - while options have not been exhausted
        while(len(options) != 0):
            current = options.pop(0)
            cls_cntr += 1
            if self.isGoal(current, credits):
                return current
            else:
                if cls_cntr == rate:#number of classes for term has been acheived
                    cls_cntr = 0
                    term = term + 1 #set new term
                    if term == 4: term = 1
            options += self.getSuccessors(current)
                
        return [] # loop has failed         
                    
         
            
   
    def isGoal(self, opt, degreecredits):#return true if schedule is satisfied
        if (len(opt.schedule)*4 >= degreecredits):
            return True
        else:
            return False
    
    def getSuccessors(self, plnr):
        options = []
        
        i = 0
        for course in plnr.available:
            if self.validPrereq(course, plnr.taken) and  self.offered(course,plnr.currterm): #course is valid insert to options
                #check if 
                #estimate    = self.getEstimate(course, courses_taken, courses)
                t = copy.deepcopy(plnr.taken)
                a = copy.deepcopy(plnr.available)
                s = copy.deepcopy(plnr.schedule)
                trm = copy.deepcopy(plnr.currterm)
                s.append(course)
                a = list(a)
                a.pop(i)
                
                new_state = state(t, a, s,trm)
                print new_state
                options.append(new_state)
                #options = self.insertOption(options, courses_taken, course,current_total + estimate)
            i += 1 
        print options
        return options
                
    
    
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
        return True
       # if crse in taken: return False
        #for required in crse.prereqs:
         #   if required not in taken:
          #      return False
        #return True
        
    
    #returns True if class offered this term
    def offered(self, crse, trm):
        return True
#        if trm == 1:
 #           return crse.fall
#        elif trm == 2:
 #           return crse.winter
  #      elif trm == 3:
   #         return crse.spring
    #    else: 
   #         return False
        
class state:
    #course list
    #current term
    #current estimate
    def __init__(self, tkn, sched, avail, trm):
        self.taken      = tkn
        self.schedule   = sched
        self.available  = avail
        self.currterm   = trm