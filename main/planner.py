#AI Script that finds the optimal plan for the student

#notes
#Suggested Algorithm  A* - using the number of prereqs the class fulfills and whether it's a requirement or not be a heuristic for the search
#store the visited course paths as integers or strings of integers
#successor method that finds all possible classes you can take 
class Planner:
    
    def __init__(self, st, mjr, rt):
        self.start  = st
        self.major  = mjr
        self.rt     = rt
        
    quarters = ["Fall","Winter","Spring"]
    #test comment
    #takes list of possible courses, start date, end date, class taking rate, number of credits needed 
    def plan(self, courses, start, rate,credits):
        courses_taken = []
        schedule      = []
        visited       = []
        term = start
        options = self.getSuccessors(courses, courses_taken, rate, term,0)
        cls_cntr = 0
        #search loop  - while options have not been exhausted
        while(len(options != 0)):
            current = options.pop(0)
            cls_cntr += 1
            if self.isGoal(current, credits):
                return current
            else:
                if cls_cntr == rate:#number of classes for term has been acheived
                    cls_cntr = 0
                    term = (term + 1) % 3 #set new term
                
                options = self.getSuccessors(courses,current[0], rate,term,current[1])
                
        return [] # loop has failed         
                    
         
            
   
    def isGoal(self, opt, credits):#return true if schedule is satisfied
        if (len(opt[0])*4 >= credits):
            return True
        else:
            return False
    
    def getSuccessors(self, courses,courses_taken, rate, term,current_total):
        for course in courses:
            if self.validPrereq(course,courses, courses_taken) and  self.offered(course,term): #course is valid insert to options
                #check if 
                estimate    = self.getEstimate(course, courses_taken, courses)
                options     = [] 
                #options = self.insertOption(options, courses_taken, course,current_total + estimate)
                
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
    def validPrereq(self, crse,crselst, taken):
        if crse in taken: return False
        for required in crse.prereqs:
            if required not in taken:
                return False
        return True
        
    
    #returns True if class offered this term
    def offered(self, crse, trm):
        if trm in crse.avaialble: return True
        else: return False
        
class schedule_state:
    #course list
    #current term
    #current estimate
    def ex1(self):
        pass