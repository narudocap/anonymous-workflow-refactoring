#
#
# Name:   bpmn.py - describing BPMN processes in Python
# Author: Gwen Salaun
# Start date: February 2022
################################################################################

#!/usr/bin/python3

import time
import random
import copy

# from subprocess import call


##
# A Node is an identifier
class Node:

    def __init__(self, ident):
        self.id=ident

    def getIdent(self):
        return self.id

    def print(self):
        print(self.id)

    def isGateway(self):
        return False


##
# A start node
class Start(Node):

    def __init__(self, ident):
        self.id=ident
        self.name=ident

    def getClass(self):
        return "Start"

    def print(self):
        print("start", self.id)

    def isGateway(self):
        return False

##
# An end node
class End(Node):

    def __init__(self, ident):
        self.id=ident
        self.name=ident

    def getClass(self):
        return "End"

    def print(self):
        print("end", self.id)

    def isGateway(self):
        return False



##
# An activity
class Activity(Node):

    def __init__(self, ident, name, time, res):
        self.ident=ident
        self.name=name
        self.time=time
        self.res=res

    def getIdent(self):
        return self.ident

    def getName(self):
        return self.name

    def print(self):
        print("activity", self.ident, self.name, self.time, self.res)

    def getClass(self):
        return "Activity"

    #def setTime(self, time):
    #    self.time=time

    def getRes(self):
        return self.res

    def getTime(self):
        return self.time

    def setIdent(self, ident):
        self.ident=ident

    def setName(self, name):
        self.name=name

    def isGateway(self):
        return False

##
# A split node
class Split(Node):

    def __init__(self, ident, type):
        self.id=ident
        self.name=type  # this can be: exclusive, inclusive, parallel

    def getType(self):
        return self.name

    def print(self):
        print("split", self.name, self.id)

    def getClass(self):
        return "Split"

    def isGateway(self):
        return True

##
# A join node
class Join(Node):

    def __init__(self, ident, type):
        self.id=ident
        self.name=type  # this can be: exclusive, inclusive, parallel

    def getType(self):
        return self.name

    def print(self):
        print("join", self.name, self.id)

    def getClass(self):
        return "Join"

    def isGateway(self):
        return True

##
# A flow
class Flow:

    def __init__(self, ident, source, target, prop="weak"):
        self.id=ident
        self.source=source  # source node
        self.target=target  # target node
        self.prop=prop

    def getIdent(self):
        return self.id

    def getSource(self):
        return self.source

    def getTarget(self):
        return self.target

    def setTarget(self, node):
        self.target=node

    def getProp(self):
        return self.prop

    def print(self):
        print("flow", self.id,":", self.source.getIdent(), "->", self.target.getIdent())

##
# A BPMN graph is defined by a set of nodes and a set of flows.
class BPMNGraph:
    def __init__(self, name, nodes, flows):
        self.name=name
        self.nodes = nodes
        self.flows = flows

    def addNode(self, node):
        # if not node.getIdent() in [n.getIdent() for n in self._nodes]:
        self.nodes.add(node)

    def addFlow(self, flow):
        #print("ADD FLOW")
        #flow.print()
        self.flows.add(flow)

    def getNodes(self):
        return self.nodes

    def getFlows(self):
        return self.flows

    def getName(self):
        return self.name

    def getNode(self, ident):
        for n in self.nodes:
            if (n.getIdent()==ident):
                return n

    def getNodePrefix(self, ident):
        for n in self.nodes:
            if (n.getIdent().startswith(ident)):
                return n

    def removeNode(self, ident):
        nds=set()
        for n in self.nodes:
            if (n.getIdent()!=ident):
                nds.add(n)
        self.nodes=nds

    def getFlow(self, ident):
        for f in self.flows:
            if (f.getIdent()==ident):
                return f

    def removeFlow(self, ident):
        fls=set()
        for f in self.flows:
            if (f.getIdent()!=ident):
                fls.add(f)
        self.flows=fls

    # returns the flows outgoing of a given node
    def getOutgoingFlows(self, ident):
        fls=set()
        for f in self.flows:
            if (f.getSource().getIdent()==ident):
                fls.add(f)
        return fls

    # returns the flows incoming to a given node
    def getIncomingFlows(self, ident):
        fls=set()
        for f in self.flows:
            if (f.getTarget().getIdent()==ident):
                fls.add(f)
        return fls

    # returns the flows incoming to a given node, but only if the source node is a task
    def getIncomingFlowsActivityOnly(self, ident):
        fls=set()
        for f in self.flows:
            if (f.getTarget().getIdent()==ident):
                if (f.getSource().getClass()=="Activity"):
                    fls.add(f)
        return fls

    def getActivity(self, name):
        for n in self.nodes:
            if (n.getClass()=="Activity") and (n.getName()==name):
                return n

    # returns the start node of the process
    def getStartNode(self):
        for n in self.nodes:
            if (n.getClass()=="Start"):
                return n

    # returns the end nodes of the process
    def getEndNodes(self):
        res=set()
        for n in self.nodes:
            if (n.getClass()=="End"):
                res.add(n)
        return res

    # returns all the tasks of the process
    def getTasks(self):
        res=set()
        for n in self.nodes:
            if (n.getClass()=="Activity"):
                res.add(n)
        return res

    # returns all the splits of the process
    def getSplits(self):
        res=set()
        for n in self.nodes:
            if (n.getClass()=="Split"):
                res.add(n)
        return res

    # returns all the joins of the process
    def getJoins(self):
        res=set()
        for n in self.nodes:
            if (n.getClass()=="Join"):
                res.add(n)
        return res

    # returns all parallel gateways of the process
    def getParallelGateways(self):
        res=set()
        for n in self.nodes:
            if ((n.getClass()=="Split") or (n.getClass()=="Join")) and (n.getType()=="parallel"):
                res.add(n)
        return res

    # returns all exclusive gateways of the process
    def getExclusiveGateways(self):
        res=set()
        for n in self.nodes:
            if ((n.getClass()=="Split") or (n.getClass()=="Join")) and (n.getType()=="exclusive"):
                res.add(n)
        return res

    # This function returns the successor nodes of a given node
    def getSucc(self, node):
        flows=self.getFlows()
        succ=[]
        for f in flows:
            if (f.getSource().getIdent()==node.getIdent()):
                # f.print()
                succ.append(f.getTarget())
        return succ

    # This function returns the predecessor nodes of a given node
    def getPred(self, node):
        flows=self.getFlows()
        pred=[]
        for f in flows:
            if (f.getTarget().getIdent()==node.getIdent()):
                pred.append(f.getSource())
        return pred

    # computes the alphabet of the process
    def computeAlphabet(self):
        tasks=self.getTasks()
        alpha=set()
        for t in tasks:
            alpha.add(t.getIdent())
        return alpha

    # Prints a BPMN graph
    def print(self):
        print("START OF THE PROCESS PRETTY PRINT")
        print(self.name)
        for n in self.nodes:
            n.print()
        for f in self.flows:
            f.print()
        print("END OF THE PROCESS PRETTY PRINT")

    # sums the time of all tasks
    def getSumTimeTasks(self):
        sum=0
        for t in self.getTasks():
            sum=sum+t.getTime()
        return sum


    # checks if there is at least one token/ident with time zero
    def oneTokenToZero(self, queue):
        res=False
        for c in queue:
            if (c[1]==0):
                res=True
        return res

    # checks if a given id is in the queue with time zero
    def oneGivenTokenToZero(self, queue, ident):
        res=False
        for c in queue:
            if (c[0]==ident) and (c[1]==0):
                res=True
        return res

    # computes available resources in the process
    # we assume one replica per resource type so far
    # TODO: provide the option to give a different number per resource
    def computeResources(self, nb):
        tasks=self.getTasks()
        res=set()
        for t in tasks:
            rset=t.getRes()
            for r in rset:
                res.add(r)
        # we finally transform this set into a dictionary with 1 replica by default
        finalres={}
        for r in res:
            finalres[r]=nb
        return finalres

    # checks whether the resources associated to a task are all available
    # first parameter is a set of strings
    # second parameter is a set of couples (res, nbreplicas)
    def resAvailable (self, res, resources):
        available=True
        for r in res:
            for key in resources:
                if (r==key) and (resources[key]<=0):
                    available=False
        return available

    # updates resources
    # first parameter is a set of strings
    # second parameter is a set of couples (res, nbreplicas)
    def updateResources (self, res, resources):
        for r in res:
            for key in resources:
                if (r==key):
                    resources[key]=resources[key]-1
        return resources

    # release resources
    # first parameter is a set of strings (resources of a task)
    # second parameter is a set of couples (res, nbreplicas)
    def releaseResources (self, res, resources):
        for r in res:
            for key in resources:
                if (r==key):
                    resources[key]=resources[key]+1
        return resources

    # checks whether a ident corresponds to a task
    def isTask(self, ident):
        tasks=self.getTasks()
        res=False
        for t in tasks:
            if (t.getIdent()==ident):
                res=True
        return res

    # removes a token from the queue of tokens
    def removeToken(self, ident, queue):
        rqueue=[]
        for c in queue:
            if (c[0]!=ident):
                rqueue.append(c)
        return rqueue

    # checks whether there is token with time zero in the queue for each incoming flow
    def allTokensReadyJoinPar(self, targetnode, queue):
        flows=self.getIncomingFlows(targetnode.getIdent())
        res=True
        for f in flows:
            if not(self.oneGivenTokenToZero(queue, f.getIdent())):
                res=False
        return res

    # decreases all times by one
    def updateQueue(self, queue):
        rqueue=[]
        for c in queue:
            if (c[1]>0):
                rqueue.append((c[0],c[1]-1))
            else:
                rqueue.append(c)
        return rqueue

    # extracts one token with zero time from the queue (any one)
    # pre-condition: there is one token with zero time at least
    def getOneTokenToZero(self, queue):
        for c in queue:
            if (c[1]==0):
                return c

    # extracts all tokens to zero
    def getAllTokensToZero(self, queue):
        queuezero=[]
        for c in queue:
            if (c[1]==0):
                queuezero.append(c)
        return queuezero

    # build a dictionary storing task status (waiting/executing/completed)
    def buildTaskStatus(self):
        tasks=self.getTasks()
        finalres={}
        for t in tasks:
            finalres[t.getIdent()]="waiting"
            # print(t.getIdent())
        return finalres

    # simulation of the process ONCE
    # takes as input the list of resources and available amout (same for all resources now)
    # the verbose parameter is a boolean indicating to print (or not) details about the simulation
    def simulate(self, nbreplicas, verbose):

        gtime=0
        flows=list(self.getOutgoingFlows(self.getStartNode().getIdent()))
        # keeps track of active tokens
        queue=[(flows[0].getIdent(),0)]
        # keeps track of resource usage
        resources=self.computeResources(nbreplicas)
        # keeps track of task status
        taskstatus=self.buildTaskStatus()

        # logs all information regarding resource usage and task status
        log=[]

        while (queue!=[]):

            if verbose:
                # print gtime + status of resources
                print("TIME =",gtime)
                print ("RESOURCES = {", end = ' ')
                for key in resources:
                    print(key, "->", resources[key], end = ' '),
                print("}")
                print ("TOKENS = {", end = ' ')
                for c in queue:
                    print(c[0], "->", c[1], end = ' ')
                print("}")
                print ("TASK STATUS = {", end = ' ')
                for key in taskstatus:
                    print(key, "(", end = ' ')
                    task=self.getNode(key)
                    for resource in task.getRes():
                        print(resource, end = ' ')
                    print(")", end = ' ')
                    print("->", taskstatus[key], end = ' ')
                print("}\n")

            log.append((gtime, copy.deepcopy(resources), copy.deepcopy(taskstatus)))

            # if there is identifiers with time 0, move tokens forward
            queuezero=self.getAllTokensToZero(queue)

            # this queue is used to keep track of tokens in queuezero that are
            # not triggered when analysed below.
            queuenottriggered=[]

            while (queuezero!=[]):
                c = queuezero[0]
                queuezero.pop(0)

                donesomething=False # this is useful to check whether one of the following cases
                                    # has been triggered

                # print("HERE",c[0])

                if (c[1]==0):
                    # check if the token is in a task (end of a task execution)
                    if self.isTask(c[0]):
                        queue=self.removeToken(c[0], queue)
                        flows=list(self.getOutgoingFlows(c[0])) # set of flows, but just one in that case
                        queue.append((flows[0].getIdent(),0))
                        queuezero.append((flows[0].getIdent(),0))
                        task=self.getNode(c[0])
                        res=task.getRes()
                        resources=self.releaseResources(res, resources)
                        taskstatus[c[0]]="completed"
                        donesomething=True

                    # otherwise, the token is in a flow
                    else:
                    # get target node
                        #print(c[0])
                        flow=self.getFlow(c[0])
                        targetnode=flow.getTarget()
                        if (targetnode.getClass()=="Activity"):
                            time=targetnode.getTime()
                            res=targetnode.getRes()
                            # check resource availability
                            if self.resAvailable(res, resources):
                                # update resources
                                resources=self.updateResources(res, resources)
                                # updates tokens
                                queue=self.removeToken(c[0], queue)
                                queue.append((targetnode.getIdent(),targetnode.getTime()))
                                if (targetnode.getTime()==0):
                                    queuezero.append((targetnode.getIdent(),targetnode.getTime()))
                                # update status of that task
                                taskstatus[targetnode.getIdent()]="running"
                                donesomething=True
                        if (targetnode.getClass()=="End"):
                            # removes the token, the process terminates
                            queue=self.removeToken(c[0], queue)
                            donesomething=True
                        if (targetnode.getClass()=="Split"):
                            tgw=targetnode.getType()
                            if (tgw=="exclusive"):
                                queue=self.removeToken(c[0], queue)
                                flows=list(self.getOutgoingFlows(targetnode.getIdent())) # set of flows
                                # print("LEN",len(flows)-1, flows)
                                randflow=random.randint(0,len(flows)-1)
                                queue.append((flows[randflow].getIdent(),0)) # add randomly a token on one flow
                                queuezero.append((flows[randflow].getIdent(),0))
                                donesomething=True
                            if (tgw=="parallel"):
                                queue=self.removeToken(c[0], queue)
                                flows=self.getOutgoingFlows(targetnode.getIdent()) # set of flows
                                for f in flows:
                                    queue.append((f.getIdent(),0)) # add a token to each flow
                                    queuezero.append((f.getIdent(),0))
                                donesomething=True
                        if (targetnode.getClass()=="Join"):
                            tgw=targetnode.getType()
                            if (tgw=="exclusive"):
                                queue=self.removeToken(c[0], queue)
                                flows=list(self.getOutgoingFlows(targetnode.getIdent())) # set of flows, but just one in that case
                                queue.append((flows[0].getIdent(),0)) # puts a token on the outgoing flow
                                queuezero.append((flows[0].getIdent(),0))
                                donesomething=True
                            if (tgw=="parallel"):
                                if self.allTokensReadyJoinPar(targetnode, queue):
                                    flows=self.getIncomingFlows(targetnode.getIdent())
                                    for f in flows:
                                        queue=self.removeToken(f.getIdent(), queue)
                                        queuezero=self.removeToken(f.getIdent(), queuezero)
                                    flows=list(self.getOutgoingFlows(targetnode.getIdent())) # set of flows, but just one in that case
                                    queue.append((flows[0].getIdent(),0)) # puts a token on the outgoing flow
                                    queuezero.append((flows[0].getIdent(),0))
                                    donesomething=True

                # if something has changed, this couple (ident,time) is added to the
                # queue of elements that have not been triggered when analysed
                if not(donesomething):
                    queuenottriggered.append(c)
                # otherwise (something has been triggered), all the couples in queuenottriggered
                # are added back to queuezero because they could be triggered now
                else:
                    queuezero=queuezero+queuenottriggered

            #time.sleep(1)
            gtime=gtime+1
            queue=self.updateQueue(queue)

        if verbose:
            print("PROCESS COMPLETED!")

        return log

    # checks if a tuple (time, ident, resources) is in a log
    def isTupleInLog(self, c, log):
        gt=c[0]
        ident=c[1]
        #res=c[2]
        res=False
        for entry in log:
            if (entry[0]==gt) and (entry[1]==ident):
                res=True
        return res

    # combines 2 logs, the first one is the final result, the second one is the new one
    # we add a tuple from the second one to the new one, if not already present
    def combine(self, l1, l2):
        flog=l1
        for c in l2:
            if not(self.isTupleInLog(c, l1)):
                flog.append(c)
        return flog

    # simulation of the process several times and computes the AET
    def simulateANDanalyse(self, nbreplicas, snumber):
        ind=snumber
        cumulatedtime=0
        while (ind>0):
            log=self.simulate(nbreplicas, False)
            print(log)
            # print(log[len(log)-1][0])
            # this is the global time of the last entry in the log
            cumulatedtime=cumulatedtime+log[len(log)-1][0]
            ind=ind-1
        tres=cumulatedtime/snumber
        # print("AVERAGE EXECUTION TIME =", tres)
        return tres



class Examples:

    def proc1(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"employee"})
        a2 = Activity("a2","A2",10,{"employee", "drone"})
        e = End("e")
        g1 = Split("g1", "exclusive")
        g2 = Join("g2", "exclusive")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, a1)
        f3 = Flow("f3", g1, a2)
        f4 = Flow("f4", a1, g2)
        f5 = Flow("f5", a2, g2)
        f6 = Flow("f6", g2, e)

        # BPMN graph
        proc = BPMNGraph("p1", {s, a1, a2, e, g1, g2}, {f1, f2, f3, f4, f5, f6})
        return proc

    def proc2(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"employee", "drone"})
        a3 = Activity("a3","A3",20,{"employee", "drone"})
        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, a1)
        f3 = Flow("f3", g1, a3)
        f4 = Flow("f4", a1, g2)
        f5 = Flow("f5", a3, g2)
        f6 = Flow("f6", g2, e)

        # BPMN graph
        proc = BPMNGraph("p2", {s, a1, a3, e, g1, g2}, {f1, f2, f3, f4, f5, f6})
        return proc




if __name__ == '__main__':

    #import sys
    #from subprocess import call

    ex=Examples().proc2()
    ex.print()
    t=ex.simulateANDanalyse(1, 1) # it takes as input the nb of each res and the nb of simulation
    print(t) # it returns the average execution time
