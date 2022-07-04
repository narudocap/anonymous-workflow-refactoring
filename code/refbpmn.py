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

import requests as req
from xml.etree import ElementTree as ET
from xml.dom import minidom
from enum import Enum

from subprocess import call

from examples import *

counter=1

class NodeType(Enum):
    START = "startEvent"
    END = "endEvent"
    TASK = "userTask"
    FLOW = "sequenceFlow"
    EXC = "exclusiveGateway"
    PAR = "parallelGateway"
    INC = "inclusiveGateway"

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

    # write a method to generate a BPMN process (XML) from one workflow object
    # this method also checks the MCL property in the propfile if propfile != ""
    def generate_bpmnxml(self, outfile):

        # outfile=outfile+"_"+workflowname

        xmlns = "http://www.omg.org/spec/BPMN/20100524/MODEL" # BPMN model namespaces
        xsi = "http://www.w3.org/2001/XMLSchema-instance"
        xsd = "http://www.w3.org/2001/XMLSchema"
        namespace_map = {"xmlns": xmlns,
                    "xmlns:xsi": xsi,
                    "xmlns:xsd" : xsd}

        procdata = {'id': outfile, 'name': outfile, 'isExecutable':'false'}

        definitions = ET.Element('definitions', namespace_map)
        processelem = ET.SubElement(definitions, 'process', procdata)

        #start event
        startnode = self.getStartNode()
        # startdata = {'id': 'start', 'name': 'start event'}
        startdata = vars(startnode)
        processelem.append(ET.Element(NodeType.START.value, startdata))

        #end events
        endnodes = self.getEndNodes()
        #enddata = {'id': 'end1', 'name': 'end event'}
        for endnode in endnodes:
            enddata = vars(endnode)
            processelem.append(ET.Element(NodeType.END.value, enddata))

        # tasks
        tasks = self.getTasks()
        for task in tasks:
            # taskdata = vars(task)
            #taskdata = dict(id=task.getIdent(), name=task.getName()+" ("+task.getIdent().upper()+")")
            #taskdata = dict(id=task.getIdent(), name=task.getName())
            taskdata = dict(id=task.getIdent(), name=task.getIdent())
            processelem.append(ET.Element(NodeType.TASK.value, taskdata))

        # parallel gateways (reminder: no exclusive or inclusive gateways in Tosca workflows)
        pars = self.getParallelGateways()
        for par in pars:
            #pardata = vars(par)
            pardata = dict(id=par.getIdent(), name=par.getIdent())
            processelem.append(ET.Element(NodeType.PAR.value, pardata))

        # useful for the BPMN corresponding to the node lifecycle
        excs = self.getExclusiveGateways()
        for exc in excs:
            #excdata = vars(exc)
            excdata = dict(id=exc.getIdent(), name=exc.getIdent())
            processelem.append(ET.Element(NodeType.EXC.value, excdata))

        #flows
        # flowdata = {'id': 'flow1', 'sourceRef': 'start', 'targetRef': 'end1'}
        flows = self.getFlows()
        for flow in flows:
            flowdata = dict(id=flow.getIdent(), sourceRef=flow.getSource().getIdent(), targetRef=flow.getTarget().getIdent())
            processelem.append(ET.Element(NodeType.FLOW.value, flowdata))

        prettyxmlstring = self.prettyprint(definitions)

        #print("BEFORE ADDING LAYOUT")
        #print(prettyxmlstring)

        # we call VBPMN ("bpmn" method) to add the BPMN layout to the XML file
        transform_api_url = "http://localhost:8080/transformation/vbpmn/transform/bpmn"
        response = req.post(url=transform_api_url, data=prettyxmlstring)
        layoutxml = response.text

        #print("AFTER ADDING LAYOUT")
        #print(layoutxml)

        with open(outfile+'.bpmn', 'w') as bpmnxml:
            bpmnxml.write(layoutxml)
            bpmnxml.close()


    def prettyprint(self, xmlelement):
        xml_string = ET.tostring(xmlelement, 'utf-8')
        minidom_xml = minidom.parseString(xml_string)
        return minidom_xml.toprettyxml(indent="  ")


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

    # simulation of the process ONCE
    # takes as input the list of resources and available amout (same for all resources now)
    # the verbose parameter is a boolean indicating to print (or not) details about the simulation
    # takes a last parameter corresponding to the number of simulations
    # We also compute and print the average execution time (if verbose) !
    def simulateANDanalyse(self, nbreplicas, verbose, snumber):
        ind=snumber
        fres=[]
        cumulatedtime=0
        while (ind>0):
            log=self.simulate(nbreplicas, verbose)
            # print(log[len(log)-1][0])
            # this is the global time of the last entry in the log
            cumulatedtime=cumulatedtime+log[len(log)-1][0]
            res=self.analyse(log)
            ind=ind-1
            fres=self.combine(fres, res)
            # print(res)
        tres=cumulatedtime/snumber
        if verbose:
            print("RESULTING LOG =", fres)
            print("AVERAGE EXECUTION TIME =", tres)
        return (fres, tres)


    # checks whether all resources in a list of resources (lres) appear as available in
    #  a given dictionary of resources
    def resAvailable (self, lres, dicres):
        res=True
        for r in lres:
            if (dicres[r]<=0):
                res=False
        return res

    # this method removes from the log all tasks that are not executed during
    # the simulation, because they may make erroneous the results
    def purge(self, log):
        lasttaskstatus=log[len(log)-1][2]
        #print(lasttuple)
        nonexectasks=[]
        for key in lasttaskstatus:
            if (lasttaskstatus[key]=="waiting"):
                nonexectasks.append(key)
        # print(nonexectasks)
        newlog=[]
        for entry in log:
            gt=entry[0]
            r=entry[1]
            t=entry[2]
            newt={}
            for k in t:
                if not(k in nonexectasks):
                    newt[k]=t[k]
            newlog.append((gt,r,newt))
        #print("NEWLOG",newlog)
        return newlog


    # analyses the execution log to identify all tasks that can be executed earlier
    # a task can be executed earlier if a task is in the "waiting" state and
    #  all required resources for this task are available
    def analyse(self, log):
        restasks=[]
        # print("LOG",log)

        # the log needs to be purged, because all tasks appearing as "waiting"
        # at the end of the simulation must be removed from the log, otherwise
        # they will make the results erroneous

        log=self.purge(log)
        # self.purge(log)

        for entry in log[1:len(log)-1]: # we skip gtime 0 where all resources are still available
            time=entry[0]
            resources=entry[1]
            tasks=entry[2]
            for key in tasks:
                if (tasks[key]=="waiting"):
                    res=self.getNode(key).getRes()
                    if self.resAvailable(res, resources):
                        restasks.append((time, key, res))
        return restasks


    # This method returns the split node corresponding to the given merge/join node
    # Assumption: workflow is balanced
    def getSplitNode(self, mergenode):
        res=self.getSplitNodeAux(mergenode, mergenode, [], -1)
        return res

    def getSplitNodeAux(self, mergenode, current, visited, depth):
        if not (current.getIdent() in visited):
            # print("CURRENT", current.getIdent(), depth)
            if (current.getClass()=="Split") and (current.getType()==mergenode.getType()) and (len(self.getOutgoingFlows(current))==len(self.getIncomingFlows(mergenode))) and (depth==0):
                # print("FOUND", current.getIdent())
                return current
            else:
                res=[]
                r=None
                visited.append(current)
                incf=self.getIncomingFlows(current.getIdent())
                for f in incf:
                    source=f.getSource()
                    # print(source.getIdent())
                    if (source.getClass()=="Activity"):
                        r=self.getSplitNodeAux(mergenode, source, visited, depth)
                    elif (source.getClass()=="Split"):
                        r=self.getSplitNodeAux(mergenode, source, visited, depth+1)
                    elif (source.getClass()=="Join"):
                        r=self.getSplitNodeAux(mergenode, source, visited, depth-1)
                    if (r!=None):
                        res.append(r)
                return res[0]


    # This method returns the merge node corresponding to the given split node
    # Assumption: workflow is balanced
    def getMergeNode(self, splitnode):
        res=self.getMergeNodeAux(splitnode, splitnode, [], 1)
        return res

    def getMergeNodeAux(self, splitnode, current, visited, depth):
        if not (current.getIdent() in visited):
            # print("CURRENT", current.getIdent(), depth)
            if (current.getClass()=="Join") and (current.getType()==splitnode.getType()) and (len(self.getIncomingFlows(current))==len(self.getOutgoingFlows(splitnode))) and (depth==0):
                # print("FOUND", current.getIdent())
                return current
            else:
                res=[]
                r=None
                visited.append(current)
                incf=self.getOutgoingFlows(current.getIdent())
                for f in incf:
                    target=f.getTarget()
                    # print(target.getIdent())
                    if (target.getClass()=="Activity"):
                        r=self.getMergeNodeAux(splitnode, target, visited, depth)
                    elif (target.getClass()=="Split"):
                        r=self.getMergeNodeAux(splitnode, target, visited, depth+1)
                    elif (target.getClass()=="Join"):
                        r=self.getMergeNodeAux(splitnode, target, visited, depth-1)
                    if (r!=None):
                        res.append(r)
                return res[0]

    # This method returns the sets of resources used by tasks two nodes
    # Assumption: workflow is balanced
    def getResourcesBetweenTwoNodes(self, node1, node2):
        res=self.getResourcesBetweenTwoNodesAux(node1, node2, [])
        return res

    def getResourcesBetweenTwoNodesAux(self, current, final, visited):
        if current.getIdent() in visited:
            return set()
        else:
            # print("CURRENT", current.getIdent(), depth)
            if (current.getIdent()==final.getIdent()):
                # print("FOUND", current.getIdent())
                return set()
            else:
                res=set()
                visited.append(current.getIdent())
                incf=self.getOutgoingFlows(current.getIdent())
                for f in incf:
                    target=f.getTarget()
                    # print(target.getIdent())
                    if (target.getClass()=="Activity"):
                        # print("WE ADD RESSOURCES!")
                        res=res.union(target.getRes())
                    r2=self.getResourcesBetweenTwoNodesAux(target, final, visited)
                    res=res.union(r2)

                # print ("RES=", res)
                return res


    # takes as input one process and one task that can be executed earlier
    # and modifies the process into another one (with shorter execution time)
    # counter is useful to generate freash identifiers
    def refactor(self, currentp, newp, t, counter):

        # refactoring
        # counter=1   # useful for generating new identifiers

        # to keep track of supported patterns
        refactoringdone=True

        tnode=newp.getNode(t)
        # a task has a single preceding node
        pred=newp.getPred(newp.getNode(t))[0]
        # 3 options: task, merge or join

        if (pred.getClass()=="Activity"):
            # print("SEQUENCE ACTIV.")
            # remove the flow between task t and pred
            f2=list(currentp.getIncomingFlows(t))[0] # one single incoming flow for a task
            newp.removeFlow(f2.getIdent())
            # add one parallel split and one parallel join
            ident1="gref"+str(counter)
            counter=counter+1
            g1=Split(ident1, "parallel")
            newp.addNode(g1)
            ident2="gref"+str(counter)
            counter=counter+1
            g2=Join(ident2, "parallel")
            newp.addNode(g2)
            # add four flows going from gateways to tasks
            newp.addFlow(Flow("fref"+str(counter), g1, tnode))
            counter=counter+1
            newp.addFlow(Flow("fref"+str(counter), g1, pred))
            counter=counter+1
            newp.addFlow(Flow("fref"+str(counter), tnode, g2))
            counter=counter+1
            newp.addFlow(Flow("fref"+str(counter), pred, g2))
            counter=counter+1
            # update incoming flow of pred (it should go to g1)
            f1=list(currentp.getIncomingFlows(pred.getIdent()))[0]
            newp.addFlow(Flow("fref"+str(counter), f1.getSource(), g1))
            counter=counter+1
            newp.removeFlow(f1.getIdent())
            # update outgoing flow of t (it should go out from g2)
            f3=list(currentp.getOutgoingFlows(t))[0]
            newp.addFlow(Flow("fref"+str(counter), g2, f3.getTarget()))
            counter=counter+1
            newp.removeFlow(f3.getIdent())
        if (pred.getClass()=="Join"):
            splitnode=newp.getSplitNode(pred) # DIFFERENT !
            # print("SPLIT NODE", splitnode.getIdent())
            # remove the flow between task t and pred
            f2=list(currentp.getIncomingFlows(t))[0] # one single incoming flow for a task
            newp.removeFlow(f2.getIdent())
            # add one parallel split and one parallel join
            ident1="gref"+str(counter)
            counter=counter+1
            g1=Split(ident1, "parallel")
            newp.addNode(g1)
            ident2="gref"+str(counter)
            counter=counter+1
            g2=Join(ident2, "parallel")
            newp.addNode(g2)
            # add four flows going from gateways to tasks
            newp.addFlow(Flow("fref"+str(counter), g1, tnode))
            counter=counter+1
            newp.addFlow(Flow("fref"+str(counter), g1, splitnode)) # DIFFERENT !
            counter=counter+1
            newp.addFlow(Flow("fref"+str(counter), tnode, g2))
            counter=counter+1
            newp.addFlow(Flow("fref"+str(counter), pred, g2)) # DIFFERENT !
            counter=counter+1
            # update incoming flow of pred (it should go to g1)
            f1=list(currentp.getIncomingFlows(splitnode.getIdent()))[0]  # DIFFERENT !
            newp.addFlow(Flow("fref"+str(counter), f1.getSource(), g1))
            counter=counter+1
            newp.removeFlow(f1.getIdent())
            # update outgoing flow of t (it should go out from g2)
            f3=list(currentp.getOutgoingFlows(t))[0]
            newp.addFlow(Flow("fref"+str(counter), g2, f3.getTarget()))
            counter=counter+1
            newp.removeFlow(f3.getIdent())

        if (pred.getClass()=="Split"):
            # we check if there is one task preceding that split node (assumption of this pattern)
            flowbeforesplit=list(currentp.getIncomingFlows(pred.getIdent()))[0] # DIFFERENT !
            predtask=flowbeforesplit.getSource()   # DIFFERENT !
            if (predtask.getClass()=="Activity"):

                mergenode=newp.getMergeNode(pred) # DIFFERENT !
                # print("MERGE NODE", mergenode.getIdent())

                # remove the flow between preceding task and pred
                f2=list(currentp.getIncomingFlows(pred.getIdent()))[0] # DIFFERENT !
                newp.removeFlow(f2.getIdent())
                # add one parallel split and one parallel join
                ident1="gref"+str(counter)
                counter=counter+1
                g1=Split(ident1, "parallel")
                newp.addNode(g1)
                ident2="gref"+str(counter)
                counter=counter+1
                g2=Join(ident2, "parallel")
                newp.addNode(g2)
                # add four flows going from gateways to tasks
                newp.addFlow(Flow("fref"+str(counter), g1, pred))
                counter=counter+1
                newp.addFlow(Flow("fref"+str(counter), g1, predtask)) # DIFFERENT !
                counter=counter+1
                newp.addFlow(Flow("fref"+str(counter), mergenode, g2)) # DIFFERENT !
                counter=counter+1
                newp.addFlow(Flow("fref"+str(counter), predtask, g2)) # DIFFERENT !
                counter=counter+1
                # update incoming flow of pred (it should go to g1)
                f1=list(currentp.getIncomingFlows(predtask.getIdent()))[0]  # DIFFERENT !
                newp.addFlow(Flow("fref"+str(counter), f1.getSource(), g1))
                counter=counter+1
                newp.removeFlow(f1.getIdent())
                # update outgoing flow of mergenode (it should go out from g2)
                f3=list(currentp.getOutgoingFlows(mergenode.getIdent()))[0]   # DIFFERENT !
                newp.addFlow(Flow("fref"+str(counter), g2, f3.getTarget()))
                counter=counter+1
                newp.removeFlow(f3.getIdent())
            else:
                refactoringdone=False

        return (newp, refactoringdone)

    # checks if all predecesors of a node are tasks for a given process
    def onlyTasksBeforeNode(self, proc, node):
        res=True
        incf=proc.getIncomingFlows(node.getIdent())
        for f in incf:
            source=f.getSource()
            if (source.getClass()!="Activity"):
                res=False
        return res

    # checks whether all tasks preceding 'node' are different than those of node2
    #  (empty intersection)
    # caution: a node is taken into account only if it is a task
    def noSharedResources(self, proc, node, node2):

        allres=set()
        incf=proc.getIncomingFlows(node.getIdent())
        for f in incf:
            source=f.getSource()
            #print(source.getIdent())
            #print(source.getRes())
            if (source.getClass()=="Activity"):
                allres=allres.union(source.getRes())
        # print (allres)
        return (len(node2.getRes().intersection(allres))==0)

    # computes the set of tasks preceding 'node' with resources shared with node2
    # if a node is not a task, it is not considered
    def computeTasksWithSharedResources(self, proc, node, node2):

        res=set()
        incf=proc.getIncomingFlows(node.getIdent())
        for f in incf:
            source=f.getSource()
            if (source.getClass()=="Activity"):
                if (len(source.getRes().intersection(node2.getRes()))>0):
                    res.add(source)
        return res


    # takes as input one process and one task that can be executed earlier
    # and modifies the process into another one (with shorter execution time)
    # counter is useful to generate freash identifiers
    # This second "refactor" method improves the original one by relying on
    #  more precise refactoring patterns.
    def refactor2(self, currentp, newp, t, counter):

        # CAUTION GENERAL TO THE WHOLE METHOD: I GUESS THAT SOME currentp SHOULD
        # BE newp... EVERYTHING TO BE CHECKED !


        # refactoring
        # counter=1   # useful for generating new identifiers

        # to keep track of supported patterns
        refactoringdone=True

        tnode=newp.getNode(t)
        # a task has a single preceding node
        pred=newp.getPred(newp.getNode(t))[0]
        # 3 options: task, merge or join

        if (pred.getClass()=="Activity"):
            # print("SEQUENCE ACTIV.")
            # remove the flow between task t and pred
            f2=list(currentp.getIncomingFlows(t))[0] # one single incoming flow for a task
            newp.removeFlow(f2.getIdent())
            # add one parallel split and one parallel join
            ident1="gref"+str(counter)
            counter=counter+1
            g1=Split(ident1, "parallel")
            newp.addNode(g1)
            ident2="gref"+str(counter)
            counter=counter+1
            g2=Join(ident2, "parallel")
            newp.addNode(g2)
            # add four flows going from gateways to tasks
            newp.addFlow(Flow("fref"+str(counter), g1, tnode))
            counter=counter+1
            newp.addFlow(Flow("fref"+str(counter), g1, pred))
            counter=counter+1
            newp.addFlow(Flow("fref"+str(counter), tnode, g2))
            counter=counter+1
            newp.addFlow(Flow("fref"+str(counter), pred, g2))
            counter=counter+1
            # update incoming flow of pred (it should go to g1)
            f1=list(currentp.getIncomingFlows(pred.getIdent()))[0]
            newp.addFlow(Flow("fref"+str(counter), f1.getSource(), g1))
            counter=counter+1
            newp.removeFlow(f1.getIdent())
            # update outgoing flow of t (it should go out from g2)
            f3=list(currentp.getOutgoingFlows(t))[0]
            newp.addFlow(Flow("fref"+str(counter), g2, f3.getTarget()))
            counter=counter+1
            newp.removeFlow(f3.getIdent())

        if (pred.getClass()=="Join"):
            # 3 cases (exclusive with only tasks, parallel with only tasks,
            #  exclusive or parallel with at least another merge before)

            # case 1 (exclusive with only tasks before the merge)
            if (pred.getType()=="exclusive") and (self.onlyTasksBeforeNode(currentp, pred)):
                incf=newp.getIncomingFlows(pred.getIdent())
                for f in incf:
                    source=f.getSource()
                    #ident, name, time, res):
                    tnodeCOPY=Activity(tnode.getIdent()+"_"+str(counter), tnode.getName(), tnode.getTime(), tnode.getRes())
                    newp.addNode(tnodeCOPY)
                    counter=counter+1

                    # the preceding task has not shared resources
                    if (len(tnode.getRes().intersection(source.getRes()))==0):
                        # we move tnode in parallel with source

                        # we add two gateways and connect them to source and tnode
                        ident1="gref"+str(counter)
                        counter=counter+1
                        g1=Split(ident1, "parallel")
                        newp.addNode(g1)
                        ident2="gref"+str(counter)
                        counter=counter+1
                        g2=Join(ident2, "parallel")
                        newp.addNode(g2)
                        newp.addFlow(Flow("fref"+str(counter), g1, source))
                        counter=counter+1
                        newp.addFlow(Flow("fref"+str(counter), g1, tnodeCOPY))
                        counter=counter+1
                        newp.addFlow(Flow("fref"+str(counter), source, g2))
                        counter=counter+1
                        newp.addFlow(Flow("fref"+str(counter), tnodeCOPY, g2))
                        counter=counter+1
                        # update incoming flow of source (it should go to g1)
                        f1=list(currentp.getIncomingFlows(source.getIdent()))[0]  ## currentp and not newp (but why?)
                        newp.addFlow(Flow("fref"+str(counter), f1.getSource(), g1))
                        counter=counter+1
                        newp.removeFlow(f1.getIdent())
                        # update outgoing flow of source (it should go out from g2)
                        newp.addFlow(Flow("fref"+str(counter), g2, f.getTarget()))
                        counter=counter+1
                        newp.removeFlow(f.getIdent())

                    # the preceding task shares at least one resource
                    else:

                        # we move tnode after source and before pred
                        newp.removeFlow(f.getIdent())
                        newp.addFlow(Flow("fref"+str(counter), source, tnodeCOPY))
                        counter=counter+1
                        newp.addFlow(Flow("fref"+str(counter), tnodeCOPY, pred))
                        counter=counter+1

                # we suppress tnode only once at the end !
                # 1. we suppress the flow before tnode
                f3=list(currentp.getIncomingFlows(tnode.getIdent()))[0]
                newp.removeFlow(f3.getIdent())
                # 2. we change the source node of the flow after tnode
                f4=list(currentp.getOutgoingFlows(tnode.getIdent()))[0]
                newp.removeFlow(f4.getIdent())
                newp.addFlow(Flow("fref"+str(counter), pred, f4.getTarget()))
                counter=counter+1
                # 3. we remove tnode
                newp.removeNode(tnode.getIdent())

            # case 2 (parallel with only tasks before the merge)
            if (pred.getType()=="parallel") and (self.onlyTasksBeforeNode(currentp, pred)):

                # subcase 1: no shared resources
                if (self.noSharedResources(currentp, pred, tnode)):

                    print("No shared resources.")

                    # we need this set of incoming flow before changing are done
                    incf=newp.getIncomingFlows(pred.getIdent())

                    # remove flow going from merge to node
                    f3=list(currentp.getIncomingFlows(tnode.getIdent()))[0]
                    newp.removeFlow(f3.getIdent())
                    # we change the source node of the flow after tnode
                    f4=list(currentp.getOutgoingFlows(tnode.getIdent()))[0]
                    newp.removeFlow(f4.getIdent())
                    newp.addFlow(Flow("fref"+str(counter), pred, f4.getTarget()))
                    counter=counter+1

                    # move tnode before the parallel merge, that is, add flow from node to merge
                    newp.addFlow(Flow("fref"+str(counter), tnode, pred))
                    counter=counter+1
                    # add a parallel split gateway and add flow going from split to tnode
                    ident1="gref"+str(counter)
                    counter=counter+1
                    g1=Split(ident1, "parallel")
                    newp.addNode(g1)
                    newp.addFlow(Flow("fref"+str(counter), g1, tnode))
                    # add parallel merge gateway and connect it to new parallel split
                    ident2="gref"+str(counter)
                    counter=counter+1
                    g2=Join(ident2, "parallel")
                    newp.addNode(g2)
                    newp.addFlow(Flow("fref"+str(counter), g2, g1))
                    counter=counter+1
                    # we update incoming flows for all tasks preceding the merge (pred)
                    # and connect all flows preceding tasks preceding original merge
                    # to this new parallel merge gateway

                    for f in incf:
                        source=f.getSource()
                        newf=list(newp.getIncomingFlows(source.getIdent()))[0]
                        newp.addFlow(Flow("fref"+str(counter), g1, source))
                        counter=counter+1

                        source2=newf.getSource()
                        # print("III", source2.getIdent(), newf.getIdent())
                        newp.addFlow(Flow("fref"+str(counter), source2, g2))
                        counter=counter+1
                        newp.removeFlow(newf.getIdent())

                # subcase 2: shared resources (one task only, several but not all, all)
                else:
                    print("Shared resources.")

                    # compute the list of tasks with shared resources
                    ltasks=self.computeTasksWithSharedResources(currentp, pred, tnode)
                    incf=newp.getIncomingFlows(pred.getIdent())
                    # all incoming flows (preceding tasks) are concerned
                    if (len(ltasks)==len(incf)):
                        # no simple refactoring, we do not change anything
                        pass
                    # one single task is concerned
                    elif (len(ltasks)<len(incf)) and (len(ltasks)==1):
                        # we move the task after that task before the merge
                        # first, we suppress the flow before tnode
                        f3=list(newp.getIncomingFlows(tnode.getIdent()))[0]
                        newp.removeFlow(f3.getIdent())
                        # we change the source node of the flow after tnode
                        f4=list(newp.getOutgoingFlows(tnode.getIdent()))[0]
                        newp.removeFlow(f4.getIdent())
                        newp.addFlow(Flow("fref"+str(counter), pred, f4.getTarget()))
                        counter=counter+1
                        # a single task to be handled
                        task=list(ltasks)[0]
                        outf=list(newp.getOutgoingFlows(task.getIdent()))[0]
                        newp.removeFlow(outf.getIdent())
                        newp.addFlow(Flow("fref"+str(counter), task, tnode))
                        counter=counter+1
                        newp.addFlow(Flow("fref"+str(counter), tnode, pred))
                        counter=counter+1

                    # several tasks are concerned but not all
                    else:

                        # we move the task before the merge but after a new merge for all these tasks
                        # first, we suppress the flow before tnode
                        f3=list(newp.getIncomingFlows(tnode.getIdent()))[0]
                        newp.removeFlow(f3.getIdent())
                        # we change the source node of the flow after tnode
                        f4=list(newp.getOutgoingFlows(tnode.getIdent()))[0]
                        newp.removeFlow(f4.getIdent())
                        newp.addFlow(Flow("fref"+str(counter), pred, f4.getTarget()))
                        counter=counter+1
                        # add an additional parallel merge gateway, and connects it to node and pred
                        gident="gref"+str(counter)
                        counter=counter+1
                        gw=Join(gident, "parallel")
                        newp.addNode(gw)
                        newp.addFlow(Flow("fref"+str(counter), gw, tnode))
                        counter=counter+1
                        newp.addFlow(Flow("fref"+str(counter), tnode, pred))
                        counter=counter+1
                        # for each task in ltasks, remove the outgoing flow, and add a new one going to gw
                        for t in ltasks:
                            outf=list(newp.getOutgoingFlows(t.getIdent()))[0]
                            newp.removeFlow(outf.getIdent())
                            newp.addFlow(Flow("fref"+str(counter), t, gw))
                            counter=counter+1

            # case 3 (exclusive or parallel with at least another merge before)
            # not done in this version

        if (pred.getClass()=="Split"):

            # SAME AS IN THE "refactor" METHOD (NOT CHANGED YET)

            # we check if there is one task preceding that split node (assumption of this pattern)
            flowbeforesplit=list(currentp.getIncomingFlows(pred.getIdent()))[0] # DIFFERENT !
            predtask=flowbeforesplit.getSource()   # DIFFERENT !
            if (predtask.getClass()=="Activity"):

                mergenode=newp.getMergeNode(pred) # DIFFERENT !
                # print("MERGE NODE", mergenode.getIdent())

                # remove the flow between preceding task and pred
                f2=list(currentp.getIncomingFlows(pred.getIdent()))[0] # DIFFERENT !
                newp.removeFlow(f2.getIdent())
                # add one parallel split and one parallel join
                ident1="gref"+str(counter)
                counter=counter+1
                g1=Split(ident1, "parallel")
                newp.addNode(g1)
                ident2="gref"+str(counter)
                counter=counter+1
                g2=Join(ident2, "parallel")
                newp.addNode(g2)
                # add four flows going from gateways to tasks
                newp.addFlow(Flow("fref"+str(counter), g1, pred))
                counter=counter+1
                newp.addFlow(Flow("fref"+str(counter), g1, predtask)) # DIFFERENT !
                counter=counter+1
                newp.addFlow(Flow("fref"+str(counter), mergenode, g2)) # DIFFERENT !
                counter=counter+1
                newp.addFlow(Flow("fref"+str(counter), predtask, g2)) # DIFFERENT !
                counter=counter+1
                # update incoming flow of pred (it should go to g1)
                f1=list(currentp.getIncomingFlows(predtask.getIdent()))[0]  # DIFFERENT !
                newp.addFlow(Flow("fref"+str(counter), f1.getSource(), g1))
                counter=counter+1
                newp.removeFlow(f1.getIdent())
                # update outgoing flow of mergenode (it should go out from g2)
                f3=list(currentp.getOutgoingFlows(mergenode.getIdent()))[0]   # DIFFERENT !
                newp.addFlow(Flow("fref"+str(counter), g2, f3.getTarget()))
                counter=counter+1
                newp.removeFlow(f3.getIdent())
            else:
                refactoringdone=False

        return (newp, refactoringdone)

    # computes the set of merges preceding a given merge and a process, and
    # checks whether there is another merge before a parallel merge
    def computePrecedingMerges(self, merge, proc):
        res=[]
        res.append(merge)
        nodesToBeTraversed=[]
        nodesToBeTraversed.append(merge)
        mergeBeforeParMerge=False
        while (len(nodesToBeTraversed)!=0):
            mergenode=nodesToBeTraversed.pop(0)
            incf=proc.getIncomingFlows(mergenode.getIdent())
            for f in incf:
                source=f.getSource()
                if (source.getClass()=="Join"):
                    res.append(source)
                    nodesToBeTraversed.append(source)
                    if (mergenode.getType()=="parallel"):
                        mergeBeforeParMerge=True
        return (mergeBeforeParMerge, res)

    # checks if an exclusive split corresponds to a loop
    def isLoopSplit(self, splitnode, proc):
        res=False
        outf=proc.getOutgoingFlows(splitnode.getIdent())
        for f in outf:
            target=f.getTarget()
            if (target.getClass()=="Join") and (target.getType()=="exclusive"):
                res=True
        return res


    # checks if an exclusive merge corresponds to a loop
    def isLoop(self, mergenode, proc):
        res=False
        incf=proc.getIncomingFlows(mergenode.getIdent())
        for f in incf:
            source=f.getSource()
            if (source.getClass()=="Split") and (source.getType()=="exclusive"):
                res=True
        return res

    # checks if there is one merge in a list of merge corresponding to a loop
    def anyLoop(self, lmerges, proc):
        res=False
        for merge in lmerges:
            if self.isLoop(merge, proc):
                res=True
        return res

    # takes as input one process and one task that can be executed earlier
    # and modifies the process into another one (with shorter execution time)
    # counter is useful to generate freash identifiers
    # This third "refactor" method improves the second refactoring by including
    #  refactoring patterns for cascading merges (still very basic patterns for splits, to be done...)
    def refactor3(self, currentp, newp, t, verbose):

        global counter

        # CAUTION GENERAL TO THE WHOLE METHOD: I GUESS THAT SOME currentp SHOULD
        # BE newp... EVERYTHING TO BE CHECKED !

        # refactoring
        # counter=1   # useful for generating new identifiers

        # to keep track of supported patterns
        refactoringdone=False

        tnode=newp.getNode(t)
        # a task has a single preceding node
        pred=newp.getPred(newp.getNode(t))[0]
        # 3 options: task, merge or join

        # we also return the pattern applied (NONE by default)
        tpattern="NONE"

        if (pred.getClass()=="Activity"):
            # we put these 2 tasks in // only if no shared resources
            if (len(tnode.getRes().intersection(pred.getRes()))==0):
                refactoringdone=True
                tpattern="SEQ"
                if verbose:
                    print("SEQUENCE ACTIV.")
                # remove the flow between task t and pred
                f2=list(currentp.getIncomingFlows(t))[0] # one single incoming flow for a task
                newp.removeFlow(f2.getIdent())
                # add one parallel split and one parallel join
                ident1="gref"+str(counter)
                counter=counter+1
                g1=Split(ident1, "parallel")
                newp.addNode(g1)
                ident2="gref"+str(counter)
                counter=counter+1
                g2=Join(ident2, "parallel")
                newp.addNode(g2)
                # add four flows going from gateways to tasks
                newp.addFlow(Flow("fref"+str(counter), g1, tnode))
                counter=counter+1
                newp.addFlow(Flow("fref"+str(counter), g1, pred))
                counter=counter+1
                newp.addFlow(Flow("fref"+str(counter), tnode, g2))
                counter=counter+1
                newp.addFlow(Flow("fref"+str(counter), pred, g2))
                counter=counter+1
                # update incoming flow of pred (it should go to g1)
                f1=list(currentp.getIncomingFlows(pred.getIdent()))[0]
                newp.addFlow(Flow("fref"+str(counter), f1.getSource(), g1))
                counter=counter+1
                newp.removeFlow(f1.getIdent())
                # update outgoing flow of t (it should go out from g2)
                f3=list(currentp.getOutgoingFlows(t))[0]
                newp.addFlow(Flow("fref"+str(counter), g2, f3.getTarget()))
                counter=counter+1
                newp.removeFlow(f3.getIdent())

        if (pred.getClass()=="Join"):
            # 3 cases (exclusive with only tasks, parallel with only tasks,
            #  exclusive or parallel with at least another merge before)

            if verbose:
                print("JOIN.")

            # we first compute the list of all (cascading) merge gateways (including the current merge)
            # this method also checks if there is no additional merge before a parallel merge (too difficult pattern)
            result=self.computePrecedingMerges(pred, newp)
            mergeBeforeParMerge=result[0]
            lmerges=result[1]

            # print("MERGES", lmerges)
            if mergeBeforeParMerge:
                if verbose:
                    print("Warning: merge before parallel merge.")
                return (newp, False)

            if self.anyLoop(lmerges, newp):
                if verbose:
                    print("Warning: there is a loop.")
                # we do not want to change the process, so we put lmerges back to empty
                lmerges=[]

            removetnode=False

            while (len(lmerges)!=0):
                # use random, otherwise application of patterns in loop (non-converging process) -> NOT SURE...
                # index=random.randint(0,len(lmerges)-1)
                # onemerge=lmerges.pop(index)
                onemerge=lmerges.pop(0)

                # print("IDENT", onemerge.getIdent())

                # boolean indicating whether the tnode should be removed at the end of the while loop
                removetnode=False
                tpattern="MERGE" # possibly several ones....

                # case 1 (exclusive gateway)
                if (onemerge.getType()=="exclusive") and not(self.isLoop(onemerge, newp)): # and (self.onlyTasksBeforeNode(currentp, pred)):
                # Si c'est le cas, on ne fait rien !


                    incf=newp.getIncomingFlows(onemerge.getIdent())

                    for f in incf:
                        source=f.getSource()

                        # we proceed only if source is not a merge gateway (or a SPLIT in case of loops !)
                        # otherwise we do nothing now
                        if (source.getClass()!="Join"): # and (source.getClass()!="Split"):

                            removetnode=True

                            tnodeCOPY=Activity(tnode.getIdent()+"_"+str(counter), tnode.getName(), tnode.getTime(), tnode.getRes())
                            newp.addNode(tnodeCOPY)
                            counter=counter+1

                            refactoringdone=True
                            tpattern="MERGE" # possibly several ones....

                            # the preceding task has not shared resources
                            if (len(tnode.getRes().intersection(source.getRes()))==0):
                                # we move tnode in parallel with source

                                # we add two gateways and connect them to source and tnode
                                ident1="gref"+str(counter)
                                counter=counter+1
                                g1=Split(ident1, "parallel")
                                newp.addNode(g1)
                                ident2="gref"+str(counter)
                                counter=counter+1
                                g2=Join(ident2, "parallel")
                                newp.addNode(g2)
                                newp.addFlow(Flow("fref"+str(counter), g1, source))
                                counter=counter+1
                                newp.addFlow(Flow("fref"+str(counter), g1, tnodeCOPY))
                                counter=counter+1
                                newp.addFlow(Flow("fref"+str(counter), source, g2))
                                counter=counter+1
                                newp.addFlow(Flow("fref"+str(counter), tnodeCOPY, g2))
                                counter=counter+1
                                # update incoming flow of source (it should go to g1)
                                f1=list(currentp.getIncomingFlows(source.getIdent()))[0]  ## currentp and not newp (but why?)
                                newp.addFlow(Flow("fref"+str(counter), f1.getSource(), g1))
                                counter=counter+1
                                newp.removeFlow(f1.getIdent())
                                # update outgoing flow of source (it should go out from g2)
                                newp.addFlow(Flow("fref"+str(counter), g2, f.getTarget()))
                                counter=counter+1
                                newp.removeFlow(f.getIdent())

                            # the preceding task shares at least one resource
                            else:

                                # we move tnode after source and before pred
                                newp.removeFlow(f.getIdent())
                                newp.addFlow(Flow("fref"+str(counter), source, tnodeCOPY))
                                counter=counter+1
                                newp.addFlow(Flow("fref"+str(counter), tnodeCOPY, onemerge))
                                counter=counter+1


                # case 2 (parallel gateway)
                if (onemerge.getType()=="parallel"): # and (self.onlyTasksBeforeNode(currentp, pred)):

                    # subcase 1: no shared resources
                    if (self.noSharedResources(currentp, onemerge, tnode)):

                        removetnode=True
                        refactoringdone=True
                        tpattern="MERGE"

                        if verbose:
                            print("No shared resources.")

                        tnodeCOPY=Activity(tnode.getIdent()+"_"+str(counter), tnode.getName(), tnode.getTime(), tnode.getRes())
                        newp.addNode(tnodeCOPY)
                        counter=counter+1

                        # we need this set of incoming flow before changing are done
                        incf=newp.getIncomingFlows(onemerge.getIdent())

                        # remove flow going from merge to node
                        #f3=list(currentp.getIncomingFlows(tnode.getIdent()))[0]
                        #newp.removeFlow(f3.getIdent())
                        # we change the source node of the flow after tnode
                        #f4=list(currentp.getOutgoingFlows(tnode.getIdent()))[0]
                        #newp.removeFlow(f4.getIdent())
                        #newp.addFlow(Flow("fref"+str(counter), pred, f4.getTarget()))
                        #counter=counter+1

                        # move tnode before the parallel merge, that is, add flow from node to merge
                        newp.addFlow(Flow("fref"+str(counter), tnodeCOPY, onemerge))
                        counter=counter+1
                        # add a parallel split gateway and add flow going from split to tnode
                        ident1="gref"+str(counter)
                        counter=counter+1
                        g1=Split(ident1, "parallel")
                        newp.addNode(g1)
                        newp.addFlow(Flow("fref"+str(counter), g1, tnodeCOPY))
                        # add parallel merge gateway and connect it to new parallel split
                        ident2="gref"+str(counter)
                        counter=counter+1
                        g2=Join(ident2, "parallel")
                        newp.addNode(g2)
                        newp.addFlow(Flow("fref"+str(counter), g2, g1))
                        counter=counter+1
                        # we update incoming flows for all tasks preceding the merge (pred)
                        # and connect all flows preceding tasks preceding original merge
                        # to this new parallel merge gateway

                        for f in incf:
                            source=f.getSource()
                            if (source.getClass()=="Activity"):
                                newf=list(newp.getIncomingFlows(source.getIdent()))[0]
                                newp.addFlow(Flow("fref"+str(counter), g1, source))
                                counter=counter+1

                                source2=newf.getSource()
                                # print("III", source2.getIdent(), newf.getIdent())
                                newp.addFlow(Flow("fref"+str(counter), source2, g2))
                                counter=counter+1
                                newp.removeFlow(newf.getIdent())

                    # subcase 2: shared resources (one task only, several but not all, all)
                    else:

                        if verbose:
                            print("Shared resources.")

                        # compute the list of tasks with shared resources
                        tnodeCOPY=Activity(tnode.getIdent()+"_"+str(counter), tnode.getName(), tnode.getTime(), tnode.getRes())
                        ltasks=self.computeTasksWithSharedResources(currentp, onemerge, tnodeCOPY)
                        incf=newp.getIncomingFlowsActivityOnly(onemerge.getIdent())

                        # all incoming flows (with tasks) are concerned
                        if (len(ltasks)==len(incf)):

                            # no simple refactoring, we keep the task after the merge
                            pass

                            # OLD BUGGY CODE
                            # outf=list(newp.getOutgoingFlows(onemerge.getIdent()))[0]
                            # target=outf.getTarget()
                            # newp.removeFlow(outf.getIdent())
                            # newp.addFlow(Flow("fref"+str(counter), onemerge, tnodeCOPY))
                            # counter=counter+1
                            # newp.addFlow(Flow("fref"+str(counter), tnodeCOPY, target))
                            # counter=counter+1

                        # one single task is concerned
                        elif (len(ltasks)<len(incf)) and (len(ltasks)==1):

                            refactoringdone=True

                            removetnode=True

                            newp.addNode(tnodeCOPY)
                            counter=counter+1

                            # we move the task after that task before the merge
                            # first, we suppress the flow before tnode
                            #f3=list(newp.getIncomingFlows(tnode.getIdent()))[0]
                            #newp.removeFlow(f3.getIdent())
                            # we change the source node of the flow after tnode
                            #f4=list(newp.getOutgoingFlows(tnode.getIdent()))[0]
                            #newp.removeFlow(f4.getIdent())
                            #newp.addFlow(Flow("fref"+str(counter), pred, f4.getTarget()))
                            #counter=counter+1
                            # a single task to be handled
                            task=list(ltasks)[0]
                            outf=list(newp.getOutgoingFlows(task.getIdent()))[0]
                            newp.removeFlow(outf.getIdent())
                            newp.addFlow(Flow("fref"+str(counter), task, tnodeCOPY))
                            counter=counter+1
                            newp.addFlow(Flow("fref"+str(counter), tnodeCOPY, onemerge))
                            counter=counter+1

                        # several tasks are concerned but not all
                        else:

                            refactoringdone=True
                            tpattern="MERGE"

                            removetnode=True

                            tnodeCOPY=Activity(tnode.getIdent()+"_"+str(counter), tnode.getName(), tnode.getTime(), tnode.getRes())
                            newp.addNode(tnodeCOPY)
                            counter=counter+1

                            # we move the task before the merge but after a new merge for all these tasks
                            # first, we suppress the flow before tnode
                            #f3=list(newp.getIncomingFlows(tnode.getIdent()))[0]
                            #newp.removeFlow(f3.getIdent())
                            # we change the source node of the flow after tnode
                            #f4=list(newp.getOutgoingFlows(tnode.getIdent()))[0]
                            #newp.removeFlow(f4.getIdent())
                            #newp.addFlow(Flow("fref"+str(counter), pred, f4.getTarget()))
                            #counter=counter+1
                            # add an additional parallel merge gateway, and connects it to node and pred
                            gident="gref"+str(counter)
                            counter=counter+1
                            gw=Join(gident, "parallel")
                            newp.addNode(gw)
                            newp.addFlow(Flow("fref"+str(counter), gw, tnodeCOPY))
                            counter=counter+1
                            newp.addFlow(Flow("fref"+str(counter), tnodeCOPY, onemerge))
                            counter=counter+1
                            # for each task in ltasks, remove the outgoing flow, and add a new one going to gw
                            for t in ltasks:
                                outf=list(newp.getOutgoingFlows(t.getIdent()))[0]
                                newp.removeFlow(outf.getIdent())
                                newp.addFlow(Flow("fref"+str(counter), t, gw))
                                counter=counter+1


            if removetnode:
                # we suppress tnode only once at the end of the while loop !
                # 1. we suppress the flow before tnode
                f3=list(currentp.getIncomingFlows(tnode.getIdent()))[0]
                newp.removeFlow(f3.getIdent())
                # 2. we change the source node of the flow after tnode
                f4=list(currentp.getOutgoingFlows(tnode.getIdent()))[0]
                newp.removeFlow(f4.getIdent())
                newp.addFlow(Flow("fref"+str(counter), pred, f4.getTarget()))
                counter=counter+1
                # 3. we remove tnode
                newp.removeNode(tnode.getIdent())

        if (pred.getClass()=="Split"):

            if verbose:
                print("SPLIT.")

            if (pred.getType()=="parallel"):
                refactoringdone=True
                tpattern="PSPLIT"

                # we update the flow appearing after the parallel split
                f3=list(newp.getIncomingFlows(tnode.getIdent()))[0]
                newp.removeFlow(f3.getIdent())
                # 2. we change the source node of the flow after tnode
                f4=list(newp.getOutgoingFlows(tnode.getIdent()))[0]
                newp.removeFlow(f4.getIdent())
                newp.addFlow(Flow("fref"+str(counter), pred, f4.getTarget()))
                counter=counter+1
                # we move the node before the parallel split
                flowbeforesplit=list(newp.getIncomingFlows(pred.getIdent()))[0]
                source=flowbeforesplit.getSource()
                newp.removeFlow(flowbeforesplit.getIdent())
                newp.addFlow(Flow("fref"+str(counter), source, tnode))
                counter=counter+1
                newp.addFlow(Flow("fref"+str(counter), tnode, pred))
                counter=counter+1

            # this is an exclusive split gateway (but not a loop !)
            elif (pred.getType()=="exclusive") and not(self.isLoopSplit(pred, currentp)):

                #if verbose:
                #    print("Warning: exclusive split not supported yet.")
                refactoringdone=False

                # we check if there is one task preceding that split node (assumption of this pattern)
                flowbeforesplit=list(currentp.getIncomingFlows(pred.getIdent()))[0]
                predtask=flowbeforesplit.getSource()
                if (predtask.getClass()=="Activity"):

                    mergenode=newp.getMergeNode(pred)
                    # print("MERGE NODE", mergenode.getIdent())
                    # if a merge node was found, it means this part of the wf is balanced
                    if (mergenode.getClass()=="Join"):

                        # check resources that resources between the prev. task and the choice are different
                        #if (True):
                        usedres=self.getResourcesBetweenTwoNodes(pred, mergenode)
                        # print(usedres)
                        # print(predtask.getRes())
                        if (len(predtask.getRes().intersection(usedres))==0):

                            refactoringdone=True
                            tpattern="ESPLIT"

                            # remove the flow between preceding task and pred
                            f2=list(currentp.getIncomingFlows(pred.getIdent()))[0]
                            newp.removeFlow(f2.getIdent())
                            # add one parallel split and one parallel join
                            ident1="gref"+str(counter)
                            counter=counter+1
                            g1=Split(ident1, "parallel")
                            newp.addNode(g1)
                            ident2="gref"+str(counter)
                            counter=counter+1
                            g2=Join(ident2, "parallel")
                            newp.addNode(g2)
                            # add four flows going from gateways to tasks
                            newp.addFlow(Flow("fref"+str(counter), g1, pred))
                            counter=counter+1
                            newp.addFlow(Flow("fref"+str(counter), g1, predtask))
                            counter=counter+1
                            newp.addFlow(Flow("fref"+str(counter), mergenode, g2))
                            counter=counter+1
                            newp.addFlow(Flow("fref"+str(counter), predtask, g2))
                            counter=counter+1
                            # update incoming flow of pred (it should go to g1)
                            f1=list(currentp.getIncomingFlows(predtask.getIdent()))[0]
                            newp.addFlow(Flow("fref"+str(counter), f1.getSource(), g1))
                            counter=counter+1
                            newp.removeFlow(f1.getIdent())
                            # update outgoing flow of mergenode (it should go out from g2)
                            f3=list(currentp.getOutgoingFlows(mergenode.getIdent()))[0]
                            newp.addFlow(Flow("fref"+str(counter), g2, f3.getTarget()))
                            counter=counter+1
                            newp.removeFlow(f3.getIdent())

        return (newp, refactoringdone, tpattern)


    # This function searches in a list of couples (bool, dist) whether
    #  one of the booleans is set to True
    def isFoundNode(self,cbooldist):
        for c in cbooldist:
            if c[0]:
                return True
        return False

    # This function searches in a list of couples (bool, dist) the shortest
    #  distance for booleans set to True
    def getMinDistance(self,cbooldist):
        res=100000000  # beurk
        for c in cbooldist:
            if c[0]: # true means node found
                if (c[1]<res):
                    res=c[1]
        return res

    # This function measures the distance from the start node to a given node
    def distanceFromStartNode(self,node,proc):
        # We rely on a depth-first search algorithm with visited nodes
        #  and min computation when moving back up
        res=self.distanceAUX(proc.getStartNode(),node,proc,[])
        return res[1]

    # This function measures the distance from the start node to a given node
    #  in a BPMN graph, using a list of visited states
    def distanceAUX(self,current,node,proc,visited):
        if (current.getIdent() in visited):
            return (False,0)
        if (current.getIdent()==node.getIdent()):  # we have reached the searched node
            return (True,0)
        else:
            visited.append(current.getIdent())
            succ=proc.getSucc(current)
            res=[] # a list of couples (bool, dist)
            for node2 in succ:
                res.append(self.distanceAUX(node2,node,proc,visited))
            if self.isFoundNode(res):
                return (True,self.getMinDistance(res)+1)
            else:
                return (False,0)

    def chooseTaskStrategyLeftFirst(self, tasks, proc):
        # we first compute the min distance for each task from start node
        res=[]
        mindist=10000 # beurk
        for t in tasks:
            tnode=proc.getNode(t)
            dist=self.distanceFromStartNode(tnode, proc)
            if (dist<mindist):
                mindist=dist
            res.append((t,dist))
        # we then filter to keep only tasks with the smallest distance
        # print(res)
        res2=[]
        for c in res:
            if (c[1]==mindist):
                res2.append(c[0])
        # we return one of the tasks with the smallest distance randomly
        index=random.randint(0,len(res2)-1)
        task=res2[index]
        return task


    # counts the number of flows between two nodes
    def countFlowsBetweenTwoNodes(self, proc, node1, node2):
        nb=0
        flows=proc.getFlows()
        for f in flows:
            if (f.getSource().getIdent()==node1.getIdent()) and (f.getTarget().getIdent()==node2.getIdent()):
                nb=nb+1
        return nb

    # returns a Boolean indicating whether a node is reachable from another node
    def isNodeReachable(self, source, target):
        return self.isNodeReachableAUX(source, target, [])

    def isNodeReachableAUX(self, current, target, visited):
        if (current.getIdent() in visited):
            return False
        else:
            visited.append(current.getIdent())
            res=False
            allsucc=self.getSucc(current)
            for succ in allsucc:
                if (succ.getIdent()==target.getIdent()):
                    res=True
                else:
                    res=res or self.isNodeReachableAUX(succ, target, visited)
            return res

    # simplifies a process by removing unnecessary nodes
    def simplify(self, proc):
        newp=copy.deepcopy(proc)
        # newp.print()

        # we remove multiple flows between gateways
        flows=newp.getFlows()
        for f in flows:
            source=f.getSource()
            target=f.getTarget()
            nb=self.countFlowsBetweenTwoNodes(newp, source, target)
            outf=newp.getOutgoingFlows(source.getIdent())
            # we check if there are several flows between two gateways
            if (source.isGateway()) and (target.isGateway()) and (nb>1): # (len(outf)>1):
                newp.removeFlow(f.getIdent())
            # we check if there is another path between two gateways (A VERIFIER SUR EXAMPLES)
            # this makes sense only for parallel gateways
            ptmp=copy.deepcopy(newp)
            ptmp.removeFlow(f.getIdent())
            if (ptmp.isNodeReachable(source, target)) and (source.isGateway()) and (target.isGateway()):
                if (source.getType()=="parallel") and (target.getType()=="parallel"):
                    newp.removeFlow(f.getIdent())

        # we remove gateway with one incoming and one outgoing flow
        nodes=newp.getNodes()
        for n in nodes:
            incf=newp.getIncomingFlows(n.getIdent())
            outf=newp.getOutgoingFlows(n.getIdent())
            #print(n.getIdent(), len(incf), len(outf))
            if (n.isGateway()) and (len(incf)==1) and (len(outf)==1):
                incflow=list(incf)[0]
                outflow=list(outf)[0]
                source=incflow.getSource()
                target=outflow.getTarget()
                name=incflow.getIdent()
                newp.removeFlow(incflow.getIdent())
                newp.removeFlow(outflow.getIdent())
                newp.removeNode(n.getIdent())
                newp.addFlow(Flow(name, source, target))

        return newp

    # remove a task from a set of tasks
    def removeTaskFromTasks (self, task, tasks):
        res=set()
        for t in tasks:
            if (t!=task):
                res.add(t)
        return res

    # compares two nodes syntactically
    def matchNode(self, n1, n2, proc1, proc2):
        res=True
        if (n1.getClass()!=n2.getClass()):
            res=False
        elif (n1.getClass()=="Split") or (n1.getClass()=="Join"):
            # same type + same nb of incoming flows + same number of outgoingflows
            incf1=proc1.getIncomingFlows(n1)
            incf2=proc2.getIncomingFlows(n2)
            outf1=proc1.getOutgoingFlows(n1)
            outf2=proc2.getOutgoingFlows(n2)
            res=(n1.getType()==n2.getType()) and (len(incf1)==len(incf2)) and (len(outf1)==len(outf2))
        elif (n1.getClass()=="Activity"):
            res=(n1.getName()==n2.getName()) and (n1.getTime()==n2.getTime()) and (n1.getRes()==n2.getRes())

        return res

    # checks if two processes are synctactically the same
    def compareWorkflows(self, proc1, proc2):
        # we first check that they have the same numbers of elements
        #  (flows, nodes, tasks, splits, merges, exclusive, parallel)
        nodes1=proc1.getNodes()
        flows1=proc1.getFlows()
        tasks1=proc1.getTasks()
        splits1=proc1.getSplits()
        merges1=proc1.getJoins()
        par1=proc1.getParallelGateways()
        exc1=proc1.getExclusiveGateways()
        nodes2=proc2.getNodes()
        flows2=proc2.getFlows()
        tasks2=proc2.getTasks()
        splits2=proc2.getSplits()
        merges2=proc2.getJoins()
        par2=proc2.getParallelGateways()
        exc2=proc2.getExclusiveGateways()
        if (len(nodes1)==len(nodes2)) and (len(flows1)==len(flows2)) and (len(splits1)==len(splits2)) and (len(merges1)==len(merges2)) and (len(par1)==len(par2)) and (len(exc1)==len(exc2)):
            return self.compareWorkflowsAUX(proc1.getStartNode(), proc2.getStartNode(), proc1, proc2, []) # and self.compareWorkflowsAUX(proc2.getStartNode(), proc1.getStartNode(), proc2, proc1, [])
        else:
            return False

    def compareWorkflowsAUX(self, current1, current2, proc1, proc2, visited):
        if (current1.getIdent() in visited):
            return True
        elif (current1.getClass()=="End") and (current2.getClass()=="End"):
            return True
        else:
            # print("CURRENT",current1.getIdent())
            visited.append(current1.getIdent())
            allsucc1=proc1.getSucc(current1)
            res=True
            for succ1 in allsucc1:
                # print("SUCC1",succ1.getIdent())
                # look for a matching node among the succesor of current2 in proc2
                matchfound=False
                allsucc2=proc2.getSucc(current2)
                for succ2 in allsucc2:
                    # CAUTION: here we can choose twice the same succ2 for two different succ1 !!
                    if (self.matchNode(succ1, succ2, proc1, proc2)) and self.compareWorkflowsAUX(succ1, succ2, proc1, proc2, visited):
                        # print("found match:", succ2.getIdent())
                        matchfound=True
                        target=succ2
                if not(matchfound):
                    res=False
                #if matchfound:
                #    res=res and self.compareWorkflowsAUX(succ1, target, proc1, proc2, visited)
                #else:
                #    res=False
            return res

    # checks whether two nodes have the same succesors
    def matchSucc(self, n1, n2, proc1, proc2):
        succ1=proc1.getSucc(n1)
        succ2=proc2.getSucc(n2)
        res=True
        for s1 in succ1:
            res2=False
            for s2 in succ2:
                if self.matchNodeV2(s1, s2, proc1, proc2):
                    res2=True
            res=res and res2
        return res

    # compares two nodes syntactically (also checks both node have the same succesors)
    def matchNodeV2(self, n1, n2, proc1, proc2):
        res=True
        if (n1.getClass()!=n2.getClass()):
            res=False
        elif (n1.getClass()=="Split") or (n1.getClass()=="Join"):
            # same type + same nb of incoming flows + same number of outgoingflows
            incf1=proc1.getIncomingFlows(n1)
            incf2=proc2.getIncomingFlows(n2)
            outf1=proc1.getOutgoingFlows(n1)
            outf2=proc2.getOutgoingFlows(n2)
            samesucc=self.matchSucc(n1, n2, proc1, proc2)
            res=(n1.getType()==n2.getType()) and (len(incf1)==len(incf2)) and (len(outf1)==len(outf2)) and samesucc
        elif (n1.getClass()=="Activity"):
            samesucc=self.matchSucc(n1, n2, proc1, proc2)
            res=(n1.getName()==n2.getName()) and (n1.getTime()==n2.getTime()) and (n1.getRes()==n2.getRes()) and samesucc
        else:
            return self.matchSucc(n1, n2, proc1, proc2)

        return res

    # another simpler way to compare processes without traversing the graph structure
    def compareWorkflowsV3(self, proc1, proc2):
        return self.matchNodeV2(proc1.getStartNode(), proc2.getStartNode(), proc1, proc2)

    # another simpler way to compare processes without traversing the graph structure
    def compareWorkflowsV2(self, proc1, proc2):
        nodes1=proc1.getNodes()
        nodes2=proc2.getNodes()
        res=True
        for n1 in nodes1:
            res2=False
            for n2 in nodes2:
                if self.matchNodeV2(n1, n2, proc1, proc2):
                    res2=True
            res=res and res2
        return res

    # checks if a process/workflow is in a list of processes
    def procInProcesses(self, proc, processes):
        res=False
        for p in processes:
            if (self.compareWorkflows(proc, p)):
            # if (self.compareWorkflowsV3(proc, p)):
                # print("SAME PROCESSES !!! ")
                # proc.print()
                # p.print()
                res=True
        return res

    # checks if a process/workflow is in a dictionary of processes
    def procInProcessesDIC(self, hash, proc, processes):
        if not(hash in processes.keys()):
            return False
        else:
            return self.procInProcesses(proc, processes[hash])

    # counts the nb of occurrences of a process in a list of proc
    def countAppearances(self, proc, processes):
        res=0
        for p in processes:
            if (self.compareWorkflows(proc, p)):
                res=res+1
        return res

    # computes a hash value for a process
    def computeHashValue(self, proc):
        nodes=proc.getNodes()
        sumdist=0
        dict = {}
        for n in nodes:
            dist=self.distanceFromStartNode(n, proc)
            if dist in dict.keys():
                dict[dist]=dict[dist]+1
            else:
                dict[dist]=1
            # sumdist=sumdist+self.distanceFromStartNode(n, proc)
        #val = sumdist+11*len(proc.getNodes())+17*len(proc.getFlows())+37*(len(proc.getExclusiveGateways())+1)+23*(len(proc.getParallelGateways())+1)+29*(len(proc.getSplits())+1)+31*(len(proc.getJoins())+1)+7*(proc.getSumTimeTasks()+1)
        r=""
        for k in sorted(dict.keys()):
            #print(k,"->",dict[k])
            r=r+str(dict[k])
        return int(r) # + val

    # checks if a process/workflow is in a list of processes
    # this 2nd version relies on hash codes and a dictionary storing all (existing) processes
    def procInProcessesV2(self, proc, processes):
        res=False
        newhash=self.computeHashValue(proc)
        if newhask in processes.keys():
            # TODO: check if proc is equal to one of the processes stored at that key
            pass
        return res
    # NOTE: This solution has not been completed because the generation of hash value
    #  corresponding to a process is not satisfactory (too many collisions)

    # simulation of the process given a precise strategy (one arbitrary succession of refactoring steps ONLY)
    # takes as input the list of resources and available amout (same for all resources now)
    # the verbose parameter is a boolean indicating to print (or not) details about the simulation
    # takes a last parameter corresponding to the number of simulations
    # CAUTION: this method applies refactoring one by one starting with
    #  the one inducing the highest reduction in execution time
    # the nbsteps parameter allows to apply a given number of refactoring steps
    def simulateANDanalyseANDrefactor(self, nbreplicas, verbose, snumber, nbsteps):

        currentp=copy.deepcopy(self)
        newp=copy.deepcopy(self)

        loopagain=True

        # max number of steps
        ind=nbsteps

        proclog=[]

        while (loopagain) and (ind>0):

            # print("BIG LOOP")

            ind=ind-1

            # newp.print()

            # simulates
            log=currentp.simulateANDanalyse(nbreplicas, False, snumber)

            # computes from the log tasks to be updated in the process
            # CAUTION: if the task is preceded by a "strong" flow, we cannot update
            #   the workflow for this task !!
            tasks=set()
            for entry in log[0]:
                t=entry[1]
                incf=list(currentp.getIncomingFlows(t))
                if (incf[0].getProp()=="weak"):
                    tasks.add(t)

            if (len(tasks)>0):
                print("TASKS THAT CAN BE EXECUTED EARLIER =", tasks)
                # BASIC STRATEGY -> take the first one in the set of tasks !
                # CAUTION: this strategy leads to infinite loops by applying infinitely patterns for sequence and splits !!
                # OTHER STRATEGY -> take one task randomly
                newp=copy.deepcopy(currentp)

                # old version to choose a task randomly
                # index=random.randint(0,len(tasks)-1)
                # task=list(tasks)[index]

                if (len(tasks)==1):
                    task=list(tasks)[0]
                else: # more than one tasks to be moved
                    task=self.chooseTaskStrategyLeftFirst(tasks, newp)

                p=self.refactor3(currentp, newp, task, False)
                if (p[1]): # refactoring IS possible
                    newp=self.simplify(p[0])
                else:
                    print("REFACTORING PATTERN IS NOT SUPPORTED YET !")
                    loopagain=False

            else:
                loopagain=False

            currentp=copy.deepcopy(newp)

            proclog.append(copy.deepcopy(newp))

        if (ind==0):
            print("Warning: the program stops because of infinite loop of refactorings.")

        # newp.print()
        # newp.simulateANDanalyse(nbreplicas, False, snumber)

        return proclog
        # return newp

    # computes the set of tasks to be moved by refactoring
    # we do NOT keep all the tasks identified during the simulation, but only
    # those we smallest highest time in the log (it means this task is waiting less than
    # the others to be executed). If there are several ones with the smallest time, we keep all these ones.
    def computeSetTasks(self, log):
        rdic={}
        # we compute the highest time for each task in the log
        for entry in log[0]:
            t=entry[1]
            if not(t in rdic.keys()):
                rdic[t]=entry[0]
            else:
                if (rdic[t]<entry[0]):
                    rdic[t]=entry[0]

        # we compute the smallest time in the dictionary
        tmin=10000000
        for k in rdic.keys():
            if rdic[k]<tmin:
                tmin=rdic[k]
        # we put in the resulting set all the tasks with that time
        tasks=set()
        for k in rdic.keys():
            if (rdic[k]==tmin):
                tasks.add(k)
        return tasks

    # This method returns the set of following tasks given a task node
    # but only returns the tasks reachable following strong flows
    def getSuccStrongTasks(self, tasknode):
        res=self.getSuccStrongTasksAux(tasknode, [])
        return res

    def getSuccStrongTasksAux(self, current, visited):
        if not (current.getIdent() in visited):
            res=set()
            visited.append(current)
            incf=self.getOutgoingFlows(current.getIdent())
            for f in incf:
                if (f.getProp()=="strong"):
                    target=f.getTarget()
                    if (target.getClass()=="Activity"):
                        res.add(target)
                    else:
                        res=res.union(self.getSuccStrongTasksAux(target, visited))
            return res

    # returns a set of couples, one couple consisting of two tasks, and
    # corresponding to a (strong) causal dependency
    def computeDependProc(self, proc):
        tasks=proc.getTasks()
        res=set()
        for t in tasks:
            succnodes=proc.getSuccStrongTasks(t)
            if (len(succnodes)!=0):
                #print(t.getIdent(), "->", end = ' ')
                for succ in succnodes:
                    res.add((t.getIdent(), succ.getIdent()))
                    #print(succ.getIdent())
            #else:
                #print(t.getIdent(), "-> no succesors")
        return res

    def preserveDependencies(self, proc, depend):
        res=True
        for c in depend:
            t1=c[0]
            t2=c[1]
            # print (t1, proc.getNodePrefix(t1).getIdent())
            # print (t2, proc.getNodePrefix(t2).getIdent())
            if not(proc.isNodeReachable(proc.getNodePrefix(t1), proc.getNodePrefix(t2))):
                res=False
        return res

    # this function computes the best refactoring (wrt. execution time as optimization criterion)
    # inputs: - nb of replicas of each resource (currently works for one replica only, duplicate names if several replicas)
    #         - verbose if dumps text messages during simulation
    #         - snumber is the number of simulations
    #         - strategy indicates how to choose tasks to be moved
    #           ("exploration" = brute force approach with full exploration of all possibilities)
    #           ("heuristic" = keep to tasks to be applied first in terms of time)
    #         - the final parameter (optional, default value=1000) corresponds to the max number of explored processes
    #           (it is used to stop the exploration when there are too many processes)
    #           (if it stops, the best current one is returned)
    def computeOptimalRefactoring(self, nbreplicas, verbose, snumber, strategy, bound=1000):
        tobeexplored=[]     # list of processes to be explored
        alreadyexplored=[]  # list of already explored processes

        initialp=copy.deepcopy(self)
        tobeexplored.append(initialp)

        tmin=1000000 # beurk
        bestproc=None

        # we compute the time of the original process
        proctmp=copy.deepcopy(self)
        initlog=proctmp.simulateANDanalyse(nbreplicas, False, snumber)
        inittime=initlog[1]

        # we compute the (strong) causal dependencies on the initial process
        depend=self.computeDependProc(initialp)
        # print(depend)

        ind=0
        shash=set()

        while (len(tobeexplored)>0) and (ind<bound):

            print("Nb of explored processes =", len(alreadyexplored), "(original time =", inittime, "best time =", tmin,")")
            print("Nb of processes to be explored =", len(tobeexplored))
            # print("Nb of hash values =", len(shash))

            ind=ind+1

            currentp=tobeexplored.pop(0)
            alreadyexplored.append(copy.deepcopy(currentp))

            # currentp.generate_bpmnxml(currentp.getName()+"_"+str(ind))
            # currentp.print()

            # TEMPORARY EXPERIMENTS ON HASH FUNCTIONS
            newhash=currentp.computeHashValue(currentp)
            # print ("HASH =", newhash)
            shash.add(newhash)

            # simulates
            log=currentp.simulateANDanalyse(nbreplicas, False, snumber)

            # print(log[0])

            if (log[1]<tmin):
                tmin=log[1]
                bestproc=currentp

                # currentp.generate_bpmnxml(currentp.getName()+"_"+str(ind))

            # computes from the log all tasks that can be executed earlier in the process
            if (strategy=="exploration"):
                tasks=set()
                for entry in log[0]:
                    tasks.add(entry[1])
            # (strategy=="heuristic")
            # we keep only tasks that are waiting the less before being executed
            # if there are several ones with the same time, we keep all of them
            else:
                tasks=self.computeSetTasks(log)
                tasks2=list(tasks)
                if (len(tasks2)!=0):
                    tasks=set()
                    tasks.add(tasks2[0])
                else:
                    tasks=set()

            #t=list(tasks)[0]
            for t in tasks:
                #print("Moved task=",t)
                newp=copy.deepcopy(currentp)
                p=self.refactor3(currentp, newp, t, False)
                newp=self.simplify(copy.deepcopy(p[0]))
                if (p[1]): # important !
                    # we check if the new process respects the strong dependencies defined in the initial process
                    if (self.preserveDependencies(newp, depend)):
                        # we check if the process is not in one of the two queues
                        if not(self.procInProcesses(newp, alreadyexplored)) and not(self.procInProcesses(newp, tobeexplored)):
                            tobeexplored.append(copy.deepcopy(newp))
                            #print("PATTERN =",p[2])

        if (ind>=bound):
            print("Warning: exploration was stopped because max bound was reached.")

        # print("New AET =", tmin, "( AET of the initial process =", inittime,")")
        # print("Nb of explored processes =", len(alreadyexplored))

        # TEMPORARY EXPERIMENTS ON HASH FUNCTIONS
        # print("Nb of explored processes =", len(alreadyexplored))
        # print("Nb of hash values =", len(shash))

        return (bestproc, inittime, tmin, alreadyexplored)


    # second version, using dictionaries for performance purposes
    def computeOptimalRefactoringV2(self, nbreplicas, verbose, snumber, strategy, bound=1000):
        tobeexplored=[]     # list of processes to be explored
        tobeexploredDIC={}  # dictionary of processes to be explored
        alreadyexplored={}  # dictionary of already explored processes

        initialp=copy.deepcopy(self)
        tobeexplored.append(initialp)
        tobeexploredDIC[initialp.computeHashValue(initialp)]=[initialp]

        tmin=1000000 # beurk
        bestproc=None

        # we compute the time of the original process
        proctmp=copy.deepcopy(self)
        initlog=proctmp.simulateANDanalyse(nbreplicas, False, snumber)
        inittime=initlog[1]

        # we compute the (strong) causal dependencies on the initial process
        depend=self.computeDependProc(initialp)
        # print(depend)

        ind=0
        shash=set()

        while (len(tobeexplored)>0) and (ind<bound):

            isbest=False

            print("Nb of explored processes =", ind, "(original time =", inittime, "best time =", tmin,")")
            print("Nb of processes to be explored =", len(tobeexplored))
            print("Nb of hash values =", len(shash))

            ind=ind+1

            currentp=tobeexplored.pop(0)

            # currentp.generate_bpmnxml(currentp.getName()+"_"+str(ind))

            newhash=currentp.computeHashValue(currentp)
            shash.add(newhash)
            if (newhash in alreadyexplored.keys()):
                alreadyexplored[newhash].append(copy.deepcopy(currentp))
            else:
                alreadyexplored[newhash]=[copy.deepcopy(currentp)]

            # simulates
            log=currentp.simulateANDanalyse(nbreplicas, False, snumber)

            if (log[1]<tmin):
                tmin=log[1]
                bestproc=currentp
                isbest=True

            # computes from the log all tasks that can be executed earlier in the process
            if (strategy=="exploration"):
                tasks=set()
                for entry in log[0]:
                    tasks.add(entry[1])
            # (strategy=="heuristic")
            # we keep only tasks that are waiting the less before being executed
            # if there are several ones with the same time, we keep all of them
            else:
                tasks=self.computeSetTasks(log)
                tasks2=list(tasks)
                if (len(tasks2)!=0):
                    tasks=set()
                    tasks.add(tasks2[0])
                else:
                    tasks=set()

            for t in tasks:
                newp=copy.deepcopy(currentp)
                p=self.refactor3(currentp, newp, t, False)
                newp=self.simplify(copy.deepcopy(p[0]))
                if (p[1]):
                    # we check if the new process respects the strong dependencies defined in the initial process
                    if (self.preserveDependencies(newp, depend)):
                        # we check if the process is not in one of the two queues
                        # TODO: write 'procInProcessesDIC'
                        newhash=newp.computeHashValue(newp)
                        if not(self.procInProcessesDIC(newhash, newp, alreadyexplored)) and not(self.procInProcessesDIC(newhash, newp, tobeexploredDIC)):

                            #if isbest:
                                # we put at the beginning of the queue / list
                            #    tobeexplored.insert(0,copy.deepcopy(newp))
                            #else:
                            tobeexplored.append(copy.deepcopy(newp))

                            if (newhash in tobeexploredDIC.keys()):
                                tobeexploredDIC[newhash].append(copy.deepcopy(newp))
                            else:
                                tobeexploredDIC[newhash]=[copy.deepcopy(newp)]

        if (ind>=bound):
            print("Warning: exploration was stopped because max bound was reached.")

        return (bestproc, inittime, tmin, alreadyexplored)




if __name__ == '__main__':

    import sys
    from subprocess import call

    oneex=True

    # TO TEST ONE SINGLE EXAMPLE
    if oneex:
        ex=Examples().proc93()
        p=ex[0]
        p.generate_bpmnxml(p.getName()+"_before")
        res=p.computeOptimalRefactoringV2(1, False, 10, "exploration", 10)
        res[0].generate_bpmnxml(p.getName()+"_after")
        print(p.getName(), end = ' ')
        print(" -->  New AET =", res[2], "( AET of the initial process =", res[1],")")

    # TO TEST ALL EXAMPLES
    else:
        bestfound=0
        toolow=0
        toohigh=0
        allp=Examples().getAllProcesses()
        for proc in allp:
            p=proc[0]
            expectedbesttime=proc[1]
            p.generate_bpmnxml(p.getName()+"_before")
            res=p.computeOptimalRefactoringV2(1, False, 5, "exploration", 100)
            res[0].generate_bpmnxml(p.getName()+"_after")
            if (res[2]==expectedbesttime):
                bestfound=bestfound+1
            if (res[2]<expectedbesttime):
                toolow=toolow+1
            if (res[2]>expectedbesttime):
                toohigh=toohigh+1
            print(p.getName(), end = ' ')
            print(" -->  New AET =", res[2], "( AET of the initial process =", res[1],")")
        print("")
        print("Best time found =", bestfound)
        print("Time found is too low =", toolow)
        print("Time found is too high =", toohigh)
