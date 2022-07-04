#
#
# Name:   examples.py - describing BPMN processes in Python
# Author: Gwen Salaun
# Start date: February 2022
################################################################################

#!/usr/bin/python3

from refbpmn import *

##
# A class defining instances of BPMN processes
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
        return (proc, 10)

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
        return (proc, 30)


    def proc3(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",10,{"r1", "r2"})
        t2 = Activity("t2","T2",10,{"r3"})
        t3 = Activity("t3","T3",20,{"r3"})
        t4 = Activity("t4","T4",20,{"r1", "r2"})
        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", g1, t3)
        f4 = Flow("f4", t1, t2)
        f5 = Flow("f5", t3, t4)
        f6 = Flow("f6", t2, g2)
        f7 = Flow("f7", t4, g2)
        f8 = Flow("f8", g2, e)

        # BPMN graph
        proc = BPMNGraph("p3", {s, t1, t2, t3, t4, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7, f8})
        return (proc, 30)

    def proc4(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"r1"})
        a2 = Activity("a2","A2",10,{"r2", "r3"})
        a3 = Activity("a3","A3",10,{"r4", "r5"})
        e = End("e")

        # flows
        f1 = Flow("f1", s, a1)
        f2 = Flow("f2", a1, a2)
        f3 = Flow("f3", a2, a3)
        f4 = Flow("f4", a3, e)

        # BPMN graph
        proc = BPMNGraph("p4", {s, a1, a2, a3, e}, {f1, f2, f3, f4})
        return (proc, 10)

    def proc5(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",10,{"r1"})
        t2 = Activity("t2","T2",10,{"r3"})
        t3 = Activity("t3","T3",20,{"r3"})
        t4 = Activity("t4","T4",20,{"r2"})
        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", g1, t3)
        f4 = Flow("f4", t1, t2)
        f5 = Flow("f5", t3, t4)
        f6 = Flow("f6", t2, g2)
        f7 = Flow("f7", t4, g2)
        f8 = Flow("f8", g2, e)

        # BPMN graph
        proc = BPMNGraph("p5", {s, t1, t2, t3, t4, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7, f8})
        return (proc, 30)

    def proc6(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",2,{"r1", "r2"})
        t2 = Activity("t2","T2",2,{"r3"})
        t3 = Activity("t3","T3",2,{"r3"})
        t4 = Activity("t4","T4",2,{"r1", "r2"})
        e = End("e")
        g1 = Split("g1", "exclusive")
        g2 = Join("g2", "exclusive")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", g1, t3)
        f4 = Flow("f4", t1, t2)
        f5 = Flow("f5", t3, t4)
        f6 = Flow("f6", t2, g2)
        f7 = Flow("f7", t4, g2)
        f8 = Flow("f8", g2, e)

        # BPMN graph
        proc = BPMNGraph("p6", {s, t1, t2, t3, t4, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7, f8})
        return (proc, 2)

    def proc7(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"r1"})
        a2 = Activity("a2","A2",10,{"r2", "r3"})
        a3 = Activity("a3","A3",10,{"r4", "r5"})
        e = End("e")

        # flows
        f1 = Flow("f1", s, a1)
        f2 = Flow("f2", a1, a2)
        f3 = Flow("f3", a2, a3)
        f4 = Flow("f4", a3, e)

        # BPMN graph
        proc = BPMNGraph("p7", {s, a1, a2, a3, e}, {f1, f2, f3, f4})
        return (proc, 10)

    def proc8(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"r1"})
        a2 = Activity("a2","A2",10,{"r2", "r3"})
        e = End("e")

        # flows
        f1 = Flow("f1", s, a1)
        f2 = Flow("f2", a1, a2)
        f3 = Flow("f3", a2, e)

        # BPMN graph
        proc = BPMNGraph("p8", {s, a1, a2, e}, {f1, f2, f3})
        return (proc, 10)

    def proc9(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",10,{"r2"})
        t3 = Activity("t3","T3",20,{"r3"})
        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", g1, t2)
        f4 = Flow("f4", t1, g2)
        f5 = Flow("f5", t2, g2)
        f6 = Flow("f6", g2, t3)
        f7 = Flow("f7", t3, e)

        # BPMN graph
        proc = BPMNGraph("p9", {s, t1, t2, t3, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7})
        return (proc, 20)

    def proc10(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",50,{"r2"})
        t3 = Activity("t3","T3",20,{"r1"})
        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f1 = Flow("f1", s, t1)
        f2 = Flow("f2", t1, g1)
        f3 = Flow("f3", g1, t2)
        f4 = Flow("f4", g1, t3)
        f5 = Flow("f5", t2, g2)
        f6 = Flow("f6", t3, g2)
        f7 = Flow("f7", g2, e)

        # BPMN graph
        proc = BPMNGraph("p10", {s, t1, t2, t3, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7})
        return (proc, 50)

    def proc11(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",50,{"r2"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",20,{"r1"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f1 = Flow("f1", s, t1)
        f2 = Flow("f2", t1, g1)
        f3 = Flow("f3", g1, t2)
        f4 = Flow("f4", g1, t3)
        f5 = Flow("f5", t2, g2)
        f6 = Flow("f6", t3, g2)
        f7 = Flow("f7", g2, t4)
        f8 = Flow("f8", t4, e)

        # BPMN graph
        proc = BPMNGraph("p11", {s, t1, t2, t3, t4, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7, f8})
        return (proc, 60)

    def proc12(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"r1"})
        a2 = Activity("a2","A2",10,{"r2", "r3"})
        a3 = Activity("a3","A3",10,{"r4", "r5"})
        a4 = Activity("a4","A4",10,{"r6"})
        e = End("e")

        # flows
        f1 = Flow("f1", s, a1)
        f2 = Flow("f2", a1, a2)
        f3 = Flow("f3", a2, a3)
        f4 = Flow("f4", a3, a4)
        f5 = Flow("f5", a4, e)

        # BPMN graph
        proc = BPMNGraph("p12", {s, a1, a2, a3, a4, e}, {f1, f2, f3, f4, f5})
        return (proc, 10)

    def proc13(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"r1"})
        a2 = Activity("a2","A2",10,{"r1", "r2"})
        a3 = Activity("a3","A3",10,{"r1", "r3"})
        a4 = Activity("a4","A4",40,{"r4"})
        e = End("e")

        # flows
        f1 = Flow("f1", s, a1)
        f2 = Flow("f2", a1, a2)
        f3 = Flow("f3", a2, a3)
        f4 = Flow("f4", a3, a4)
        f5 = Flow("f5", a4, e)

        # BPMN graph
        proc = BPMNGraph("p13", {s, a1, a2, a3, a4, e}, {f1, f2, f3, f4, f5})
        return (proc, 40)

    def proc14(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",50,{"r1"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",20,{"r2"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f1 = Flow("f1", s, t1)
        f2 = Flow("f2", t1, g1)
        f3 = Flow("f3", g1, t2)
        f4 = Flow("f4", g1, t3)
        f5 = Flow("f5", t2, g2)
        f6 = Flow("f6", t3, g2)
        f7 = Flow("f7", g2, t4)
        f8 = Flow("f8", t4, e)

        # BPMN graph
        proc = BPMNGraph("p14", {s, t1, t2, t3, t4, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7, f8})
        return (proc, 90)

    def proc15(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",50,{"r1"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",20,{"r2"})

        e = End("e")
        g1 = Split("g1", "exclusive")
        g2 = Join("g2", "exclusive")

        # flows
        f1 = Flow("f1", s, t1)
        f2 = Flow("f2", t1, g1)
        f3 = Flow("f3", g1, t2)
        f4 = Flow("f4", g1, t3)
        f5 = Flow("f5", t2, g2)
        f6 = Flow("f6", t3, g2)
        f7 = Flow("f7", g2, t4)
        f8 = Flow("f8", t4, e)

        # BPMN graph
        proc = BPMNGraph("p15", {s, t1, t2, t3, t4, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7, f8})
        return (proc, 55)

    def proc16(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",50,{"r1"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",20,{"r2"})

        e = End("e")
        g1 = Split("g1", "exclusive")
        g2 = Join("g2", "exclusive")

        # flows
        f1 = Flow("f1", s, t1)
        f2 = Flow("f2", t1, g1)
        f3 = Flow("f3", g1, t2)
        f4 = Flow("f4", g1, t3)
        f5 = Flow("f5", t2, g2)
        f6 = Flow("f6", t3, g2)
        f7 = Flow("f7", g2, t4)
        f8 = Flow("f8", t4, e)

        # BPMN graph
        proc = BPMNGraph("p16", {s, t1, t2, t3, t4, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7, f8})
        return (proc, 55)


    def proc17(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",30,{"r1"})
        t2 = Activity("t2","T2",40,{"r2"})
        t3 = Activity("t3","T3",10,{"r1"})

        e = End("e")
        g1 = Split("g1", "exclusive")
        g2 = Join("g2", "exclusive")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", g1, t2)
        f4 = Flow("f4", t1, g2)
        f5 = Flow("f5", t2, g2)
        f6 = Flow("f6", g2, t3)
        f7 = Flow("f7", t3, e)

        # BPMN graph
        proc = BPMNGraph("p17", {s, t1, t2, t3, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7})
        return (proc, 40)


    def proc18(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",30,{"r1"})
        t2 = Activity("t2","T2",40,{"r2"})
        t3 = Activity("t3","T3",10,{"r3"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", g1, t2)
        f4 = Flow("f4", t1, g2)
        f5 = Flow("f5", t2, g2)
        f6 = Flow("f6", g2, t3)
        f7 = Flow("f7", t3, e)

        # BPMN graph
        proc = BPMNGraph("p18", {s, t1, t2, t3, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7})
        return (proc, 40)


    def proc19(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",30,{"r1"})
        t2 = Activity("t2","T2",40,{"r2"})
        t3 = Activity("t3","T3",10,{"r3"})
        t01 = Activity("t01","T001",30,{"r1"})
        t02 = Activity("t02","T002",30,{"r2"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, t01)
        f22 = Flow("f22", t01, t1)
        f3 = Flow("f3", g1, t02)
        f33 = Flow("f33", t02, t2)
        f4 = Flow("f4", t1, g2)
        f5 = Flow("f5", t2, g2)
        f6 = Flow("f6", g2, t3)
        f7 = Flow("f7", t3, e)

        # BPMN graph
        proc = BPMNGraph("p19", {s, t1, t2, t3, t01, t02, e, g1, g2}, {f1, f2, f22, f3, f33, f4, f5, f6, f7})
        return (proc, 70)

    def proc20(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",40,{"r2"})
        t3 = Activity("t3","T3",10,{"r1"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", g1, t2)
        f4 = Flow("f4", t1, g2)
        f5 = Flow("f5", t2, g2)
        f6 = Flow("f6", g2, t3)
        f7 = Flow("f7", t3, e)

        # BPMN graph
        proc = BPMNGraph("p20", {s, t1, t2, t3, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7})
        return (proc, 40)

    def proc21(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r1"})
        t3 = Activity("t3","T3",20,{"r2"})
        t4 = Activity("t4","T4",40,{"r2"})
        tlast = Activity("tlast","TLAST",10,{"r1"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", g1, t2)
        f4 = Flow("f4", g1, t3)
        f5 = Flow("f5", t1, g2)
        f6 = Flow("f6", t2, g2)
        f7 = Flow("f7", t3, t4)
        f8 = Flow("f8", t4, g2)
        f9 = Flow("f9", g2, tlast)
        f10 = Flow("f10", tlast, e)

        # BPMN graph
        proc = BPMNGraph("p21", {s, t1, t2, t3, t4, tlast, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7, f8, f9, f10})
        return (proc, 60)

    def proc22(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r2"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",20,{"r2"})

        e = End("e")
        g1 = Split("g1", "exclusive")
        g2 = Split("g2", "exclusive")
        g3 = Join("g3", "exclusive")
        #g4 = Join("g4", "exclusive")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, g2)
        f3 = Flow("f3", g2, t1)
        f4 = Flow("f4", g2, t2)
        f5 = Flow("f5", t1, g3)
        f6 = Flow("f6", t2, g3)
        # f7 = Flow("f7", g3, g4)
        f8 = Flow("f8", g1, t3)
        f9 = Flow("f9", t3, g3)
        f10 = Flow("f10", g3, t4)
        f11 = Flow("f11", t4, e)

        # BPMN graph
        proc = BPMNGraph("p22", {s, t1, t2, t3, t4, e, g1, g2, g3}, {f1, f2, f3, f4, f5, f6, f8, f9, f10, f11})
        return (proc, 25)

    def proc23(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r2"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",20,{"r2"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Split("g2", "parallel")
        g3 = Join("g3", "parallel")
        #g4 = Join("g4", "exclusive")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, g2)
        f3 = Flow("f3", g2, t1)
        f4 = Flow("f4", g2, t2)
        f5 = Flow("f5", t1, g3)
        f6 = Flow("f6", t2, g3)
        # f7 = Flow("f7", g3, g4)
        f8 = Flow("f8", g1, t3)
        f9 = Flow("f9", t3, g3)
        f10 = Flow("f10", g3, t4)
        f11 = Flow("f11", t4, e)

        # BPMN graph
        proc = BPMNGraph("p23", {s, t1, t2, t3, t4, e, g1, g2, g3}, {f1, f2, f3, f4, f5, f6, f8, f9, f10, f11})
        return (proc, 40)

    def proc24(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r2"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",20,{"r2"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Split("g2", "exclusive")
        g3 = Join("g3", "exclusive")
        g4 = Join("g4", "parallel")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, g2)
        f3 = Flow("f3", g2, t1)
        f4 = Flow("f4", g2, t2)
        f5 = Flow("f5", t1, g3)
        f6 = Flow("f6", t2, g3)
        f7 = Flow("f7", g3, g4)
        f8 = Flow("f8", g1, t3)
        f9 = Flow("f9", t3, g4)
        f10 = Flow("f10", g4, t4)
        f11 = Flow("f11", t4, e)

        # BPMN graph
        proc = BPMNGraph("p24", {s, t1, t2, t3, t4, e, g1, g2, g3, g4}, {f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11})
        return (proc, 50)

    def proc25(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r2"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",20,{"r2"})

        e = End("e")
        g1 = Split("g1", "exclusive")
        g2 = Split("g2", "parallel")
        g3 = Join("g3", "parallel")
        g4 = Join("g4", "exclusive")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, g2)
        f3 = Flow("f3", g2, t1)
        f4 = Flow("f4", g2, t2)
        f5 = Flow("f5", t1, g3)
        f6 = Flow("f6", t2, g3)
        f7 = Flow("f7", g3, g4)
        f8 = Flow("f8", g1, t3)
        f9 = Flow("f9", t3, g4)
        f10 = Flow("f10", g4, t4)
        f11 = Flow("f11", t4, e)

        # BPMN graph
        proc = BPMNGraph("p25", {s, t1, t2, t3, t4, e, g1, g2, g3, g4}, {f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11})
        return (proc, 30)

    def proc26(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r2"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",20,{"r2"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Split("g2", "parallel")
        g3 = Join("g3", "parallel")
        g4 = Join("g4", "parallel")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, g2)
        f3 = Flow("f3", g2, t1)
        f4 = Flow("f4", g2, t2)
        f5 = Flow("f5", t1, g3)
        f6 = Flow("f6", t2, g3)
        f7 = Flow("f7", g3, g4)
        f8 = Flow("f8", g1, t3)
        f9 = Flow("f9", t3, g4)
        f10 = Flow("f10", g4, t4)
        f11 = Flow("f11", t4, e)

        # BPMN graph
        proc = BPMNGraph("p26", {s, t1, t2, t3, t4, e, g1, g2, g3, g4}, {f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11})
        return (proc, 40) # or 60 ??

    def proc27(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r2"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",20,{"r2"})

        e = End("e")
        g1 = Split("g1", "exclusive")
        g2 = Split("g2", "exclusive")
        g3 = Join("g3", "exclusive")
        g4 = Join("g4", "exclusive")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, g2)
        f3 = Flow("f3", g2, t1)
        f4 = Flow("f4", g2, t2)
        f5 = Flow("f5", t1, g3)
        f6 = Flow("f6", t2, g3)
        f7 = Flow("f7", g3, g4)
        f8 = Flow("f8", g1, t3)
        f9 = Flow("f9", t3, g4)
        f10 = Flow("f10", g4, t4)
        f11 = Flow("f11", t4, e)

        # BPMN graph
        proc = BPMNGraph("p27", {s, t1, t2, t3, t4, e, g1, g2, g3, g4}, {f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11})
        return (proc, 25)

    def proc28(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r2"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",20,{"r2"})
        t5 = Activity("t5","T5",20,{"r2"})

        e = End("e")
        g1 = Split("g1", "exclusive")
        g2 = Split("g2", "exclusive")
        g5 = Split("g5", "exclusive")
        g6 = Join("g6", "exclusive")
        g3 = Join("g3", "exclusive")
        g4 = Join("g4", "exclusive")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, g2)
        f3 = Flow("f3", g2, t1)
        f4 = Flow("f4", g2, g5)
        f5 = Flow("f5", t1, g3)
        f6 = Flow("f6", g6, g3)
        f7 = Flow("f7", g3, g4)
        f8 = Flow("f8", g1, t3)
        f9 = Flow("f9", t3, g4)
        f10 = Flow("f10", g4, t4)
        f11 = Flow("f11", t4, e)

        f21 = Flow("f21", g5, t2)
        f22 = Flow("f22", t2, g6)
        f23 = Flow("f23", g5, t5)
        f24 = Flow("f24", t5, g6)

        # BPMN graph
        proc = BPMNGraph("p28", {s, t1, t2, t3, t4, t5, e, g1, g2, g3, g4, g5, g6}, {f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f21, f22, f23, f24})
        return (proc, 25)

    def proc29(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r2"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",20,{"r2"})
        t5 = Activity("t5","T5",20,{"r2"})

        e = End("e")
        g1 = Split("g1", "exclusive")
        g2 = Split("g2", "exclusive")
        g5 = Split("g5", "parallel")
        g6 = Join("g6", "parallel")
        g3 = Join("g3", "exclusive")
        g4 = Join("g4", "exclusive")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, g2)
        f3 = Flow("f3", g2, t1)
        f4 = Flow("f4", g2, g5)
        f5 = Flow("f5", t1, g3)
        f6 = Flow("f6", g6, g3)
        f7 = Flow("f7", g3, g4)
        f8 = Flow("f8", g1, t3)
        f9 = Flow("f9", t3, g4)
        f10 = Flow("f10", g4, t4)
        f11 = Flow("f11", t4, e)

        f21 = Flow("f21", g5, t2)
        f22 = Flow("f22", t2, g6)
        f23 = Flow("f23", g5, t5)
        f24 = Flow("f24", t5, g6)

        # BPMN graph
        proc = BPMNGraph("p29", {s, t1, t2, t3, t4, t5, e, g1, g2, g3, g4, g5, g6}, {f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f21, f22, f23, f24})
        return (proc, 45)

    def proc30(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",30,{"r1"})
        t2 = Activity("t2","T2",40,{"r2"})
        t3 = Activity("t3","T3",10,{"r1"})

        e = End("e")
        g1 = Split("g1", "exclusive")
        g2 = Join("g2", "exclusive")

        # flows
        f1 = Flow("f1", s, t1)
        f2 = Flow("f2", t1, g1)
        f3 = Flow("f3", g1, t2)
        f4 = Flow("f4", g1, t3)
        f5 = Flow("f5", t2, g2)
        f6 = Flow("f6", t3, g2)
        f7 = Flow("f7", g2, e)

        # BPMN graph
        proc = BPMNGraph("p30", {s, t1, t2, t3, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7})
        return (proc, 55)

    def proc31(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",30,{"r1"})
        t2 = Activity("t2","T2",40,{"r2"})
        t3 = Activity("t3","T3",10,{"r1"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f1 = Flow("f1", s, t1)
        f2 = Flow("f2", t1, g1)
        f3 = Flow("f3", g1, t2)
        f4 = Flow("f4", g1, t3)
        f5 = Flow("f5", t2, g2)
        f6 = Flow("f6", t3, g2)
        f7 = Flow("f7", g2, e)

        # BPMN graph
        proc = BPMNGraph("p31", {s, t1, t2, t3, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7})
        return (proc, 40)

    def proc32(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",30,{"r1", "r3"})
        t2 = Activity("t2","T2",10,{"r2"})
        t3 = Activity("t3","T3",10,{"r1", "r3"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f1 = Flow("f1", s, t1)
        f2 = Flow("f2", t1, g1)
        f3 = Flow("f3", g1, t2)
        f4 = Flow("f4", g1, t3)
        f5 = Flow("f5", t2, g2)
        f6 = Flow("f6", t3, g2)
        f7 = Flow("f7", g2, e)

        # BPMN graph
        proc = BPMNGraph("p32", {s, t1, t2, t3, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7})
        return (proc, 40)

    def proc33(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r2"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",20,{"r2"})
        t = Activity("t","T",50,{"r3"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")
        g3 = Split("g3", "parallel")
        g4 = Join("g4", "parallel")

        # flows
        f0 = Flow("f0", s, g1)
        f1 = Flow("f1", g1, t1)
        f2 = Flow("f2", g1, t2)
        f3 = Flow("f3", t1, g2)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", g2, g3)
        f6 = Flow("f6", g3, t3)
        f7 = Flow("f7", g3, t)
        f8 = Flow("f8", g3, t4)
        f9 = Flow("f9", t3, g4)
        f10 = Flow("f10", t, g4)
        f11 = Flow("f11", t4, g4)
        f12 = Flow("f12", g4, e)

        # BPMN graph
        proc = BPMNGraph("p33", {s, t1, t2, t3, t4, t, e, g1, g2, g3, g4}, {f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12})
        return (proc, 50)

    def proc34(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r2"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",20,{"r2"})
        t = Activity("t","T",20,{"r3"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")
        g3 = Split("g3", "parallel")
        g4 = Join("g4", "parallel")

        # flows
        f0 = Flow("f0", s, g1)
        f1 = Flow("f1", g1, t1)
        f2 = Flow("f2", g1, t2)
        f3 = Flow("f3", t1, g2)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", g2, g3)
        f6 = Flow("f6", g3, t3)
        f7 = Flow("f7", g3, t)
        f8 = Flow("f8", g3, t4)
        f9 = Flow("f9", t3, g4)
        f10 = Flow("f10", t, g4)
        f11 = Flow("f11", t4, g4)
        f12 = Flow("f12", g4, e)

        # BPMN graph
        proc = BPMNGraph("p34", {s, t1, t2, t3, t4, t, e, g1, g2, g3, g4}, {f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12})
        return (proc, 40)

    def proc35(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"r1"})
        a2 = Activity("a2","A2",10,{"r2"})
        a3 = Activity("a3","A3",10,{"r3"})
        a4 = Activity("a4","A4",40,{"r4"})
        a5 = Activity("a5","A5",10,{"r5"})
        e = End("e")

        # flows
        f1 = Flow("f1", s, a1)
        f2 = Flow("f2", a1, a2)
        f3 = Flow("f3", a2, a3)
        f4 = Flow("f4", a3, a4)
        f5 = Flow("f5", a4, a5)
        f6 = Flow("f6", a5, e)

        # BPMN graph
        proc = BPMNGraph("p35", {s, a1, a2, a3, a4, a5, e}, {f1, f2, f3, f4, f5, f6})
        return (proc, 40)

    def proc36(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"r1"})
        a2 = Activity("a2","A2",10,{"r2"})
        a3 = Activity("a3","A3",10,{"r3"})
        a4 = Activity("a4","A4",40,{"r4"})
        e = End("e")

        # flows
        f1 = Flow("f1", s, a1)
        f2 = Flow("f2", a1, a2)
        f3 = Flow("f3", a2, a3)
        f4 = Flow("f4", a3, a4)
        f5 = Flow("f5", a4, e)

        # BPMN graph
        proc = BPMNGraph("p36", {s, a1, a2, a3, a4, e}, {f1, f2, f3, f4, f5})
        return (proc, 40)

    def proc37(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r2"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",20,{"r2"})
        t = Activity("t","T",50,{"r3"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")
        g3 = Split("g3", "parallel")
        g4 = Join("g4", "parallel")

        # flows
        f0 = Flow("f0", s, g1)
        f1 = Flow("f1", g1, t1)
        f2 = Flow("f2", g1, t2)
        f3 = Flow("f3", t1, g2)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", g2, g3)
        f6 = Flow("f6", g3, t3)
        f7 = Flow("f7", g4, t)
        f8 = Flow("f8", g3, t4)
        f9 = Flow("f9", t3, g4)
        f10 = Flow("f10", t, e)
        f11 = Flow("f11", t4, g4)
        #f12 = Flow("f12", g4, e)

        # BPMN graph
        proc = BPMNGraph("p37", {s, t1, t2, t3, t4, t, e, g1, g2, g3, g4}, {f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11})
        return (proc, 50)

    def proc38(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r2"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",20,{"r2"})
        t = Activity("t","T",50,{"r3"})
        t5 = Activity("t5","T5",20,{"r1","r2"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")
        g3 = Split("g3", "parallel")
        g4 = Join("g4", "parallel")

        # flows
        f0 = Flow("f0", s, g1)
        f1 = Flow("f1", g1, t1)
        f2 = Flow("f2", g1, t2)
        f3 = Flow("f3", t1, g2)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", g2, g3)
        f6 = Flow("f6", g3, t3)
        f7 = Flow("f7", g4, t5)
        f8 = Flow("f8", g3, t4)
        f9 = Flow("f9", t3, g4)
        f10 = Flow("f10", t5, t)
        f11 = Flow("f11", t4, g4)
        f12 = Flow("f12", t, e)

        # BPMN graph
        proc = BPMNGraph("p38", {s, t1, t2, t3, t4, t5, t, e, g1, g2, g3, g4}, {f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12})
        return (proc, 60)

    def proc39(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r1"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",20,{"r1"})
        t5 = Activity("t5","T5",20,{"r1"})
        t = Activity("t","T",50,{"r3"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f0 = Flow("f0", s, t1)
        f1 = Flow("f1", t1, t2)
        f2 = Flow("f2", t2, g1)
        f3 = Flow("f3", g1, t3)
        f4 = Flow("f4", g1, t4)
        f5 = Flow("f5", t3, g2)
        f6 = Flow("f6", t4, g2)
        f7 = Flow("f7", g2, t5)
        f8 = Flow("f8", t5, t)
        f9 = Flow("f9", t, e)

        # BPMN graph
        proc = BPMNGraph("p39", {s, t1, t2, t3, t4, t5, t, e, g1, g2}, {f0, f1, f2, f3, f4, f5, f6, f7, f8, f9})
        return (proc, 100)

    def proc40(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r1"})
        t3 = Activity("t3","T3",20,{"r1"})
        t = Activity("t","T",50,{"r3"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f0 = Flow("f0", s, t1)
        f1 = Flow("f1", t1, g1)
        f2 = Flow("f2", g1, t2)
        f3 = Flow("f3", g1, t3)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", t3, g2)
        f6 = Flow("f6", g2, t)
        f7 = Flow("f7", t, e)

        # BPMN graph
        proc = BPMNGraph("p40", {s, t1, t2, t3, t, e, g1, g2}, {f0, f1, f2, f3, f4, f5, f6, f7})
        return (proc, 60)


    def proc41(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",50,{"res"})
        t3 = Activity("t3","T3",20,{"r1"})
        t = Activity("t","T",50,{"r1"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f0 = Flow("f0", s, t1)
        f1 = Flow("f1", t1, g1)
        f2 = Flow("f2", g1, t2)
        f3 = Flow("f3", g1, t3)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", t3, g2)
        f6 = Flow("f6", g2, t)
        f7 = Flow("f7", t, e)

        # BPMN graph
        proc = BPMNGraph("p41", {s, t1, t2, t3, t, e, g1, g2}, {f0, f1, f2, f3, f4, f5, f6, f7})
        return (proc, 90)

    def proc42(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",50,{"res"})
        t3 = Activity("t3","T3",20,{"r1"})
        t = Activity("t","T",20,{"r1"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f0 = Flow("f0", s, t1)
        f1 = Flow("f1", t1, g1)
        f2 = Flow("f2", g1, t2)
        f3 = Flow("f3", g1, t3)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", t3, g2)
        f6 = Flow("f6", g2, t)
        f7 = Flow("f7", t, e)

        # BPMN graph
        proc = BPMNGraph("p42", {s, t1, t2, t3, t, e, g1, g2}, {f0, f1, f2, f3, f4, f5, f6, f7})
        return (proc, 60)

    def proc43(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",50,{"res"})
        t3 = Activity("t3","T3",20,{"r1"})
        t = Activity("t","T",20,{"r1"})
        task = Activity("task","Task",20,{"r1"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Split("g2", "parallel")

        # flows
        f0 = Flow("f0", s, t1)
        f1 = Flow("f1", t1, g1)
        f2 = Flow("f2", g1, t2)
        f3 = Flow("f3", g1, t3)
        f4 = Flow("f4", t2, e)
        f5 = Flow("f5", t3, g2)
        f6 = Flow("f6", g2, t)
        f7 = Flow("f7", t, e)
        f8 = Flow("f8", g2, task)
        f9 = Flow("f9", task, e)

        # BPMN graph
        proc = BPMNGraph("p43", {s, t1, t2, t3, t, task, e, g1, g2}, {f0, f1, f2, f3, f4, f5, f6, f7, f8, f9})
        return (proc, 80)

    def proc44(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",50,{"res"})
        t3 = Activity("t3","T3",20,{"r1"})
        t = Activity("t","T",10,{"r1"})
        task = Activity("task","Task",10,{"r1"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Split("g2", "parallel")

        # flows
        f0 = Flow("f0", s, t1)
        f1 = Flow("f1", t1, g1)
        f2 = Flow("f2", g1, t2)
        f3 = Flow("f3", g1, t3)
        f4 = Flow("f4", t2, e)
        f5 = Flow("f5", t3, g2)
        f6 = Flow("f6", g2, t)
        f7 = Flow("f7", t, e)
        f8 = Flow("f8", g2, task)
        f9 = Flow("f9", task, e)

        # BPMN graph
        proc = BPMNGraph("p44", {s, t1, t2, t3, t, task, e, g1, g2}, {f0, f1, f2, f3, f4, f5, f6, f7, f8, f9})
        return (proc, 60)

    # example with a loop
    def proc45(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"res1"})
        a2 = Activity("a2","A2",10,{"res2", "res3"})
        e = End("e")
        g1 = Join("g1", "exclusive")
        g2 = Split("g2", "exclusive")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, a1)
        f3 = Flow("f3", a1, a2)
        f4 = Flow("f4", a2, g2)
        f5 = Flow("f5", g2, g1)
        f6 = Flow("f6", g2, e)

        # BPMN graph
        proc = BPMNGraph("p45", {s, a1, a2, e, g1, g2}, {f1, f2, f3, f4, f5, f6})
        return (proc, 20)

    # another example with a loop
    def proc46(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"res1"})
        a2 = Activity("a2","A2",10,{"res2", "res3"})
        a3 = Activity("a3","A3",10,{"res4"})
        e = End("e")
        g1 = Join("g1", "exclusive")
        g2 = Split("g2", "exclusive")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, a1)
        f3 = Flow("f3", a1, a2)
        f4 = Flow("f4", a2, a3)
        fff = Flow("fff", a3, g2)
        f5 = Flow("f5", g2, g1)
        f6 = Flow("f6", g2, e)

        # BPMN graph
        proc = BPMNGraph("p46", {s, a1, a2, a3, e, g1, g2}, {f1, f2, f3, f4, f5, f6, fff})
        return (proc, 20)

    # another example with a loop
    def proc47(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"res1"})
        a2 = Activity("a2","A2",10,{"res2", "res3"})
        a3 = Activity("a3","A3",10,{"res4"})
        abef = Activity("abef","ABEF",10,{"ressource"})

        e = End("e")
        g1 = Join("g1", "exclusive")
        g2 = Split("g2", "exclusive")

        # flows
        f1 = Flow("f1", s, abef)
        newf = Flow("newf", abef, g1)
        f2 = Flow("f2", g1, a1)
        f3 = Flow("f3", a1, a2)
        f4 = Flow("f4", a2, a3)
        fff = Flow("fff", a3, g2)
        f5 = Flow("f5", g2, g1)
        f6 = Flow("f6", g2, e)

        # BPMN graph
        proc = BPMNGraph("p47", {s, a1, a2, a3, abef, e, g1, g2}, {f1, f2, f3, f4, f5, f6, fff, newf})
        return (proc, 30)

    # another example with a loop
    def proc48(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"res1"})
        a2 = Activity("a2","A2",10,{"res2", "res3"})
        a3 = Activity("a3","A3",10,{"res4"})
        abef = Activity("abef","ABEF",10,{"ressource"})

        e = End("e")
        g1 = Join("g1", "exclusive")
        g2 = Split("g2", "exclusive")

        # flows
        f1 = Flow("f1", s, abef)
        newf = Flow("newf", abef, g1)
        f2 = Flow("f2", g1, a1)
        f3 = Flow("f3", a1, a2)
        f4 = Flow("f4", a2, g2)
        fff = Flow("fff", g2, a3)
        f5 = Flow("f5", g2, g1)
        f6 = Flow("f6", a3, e)

        # BPMN graph
        proc = BPMNGraph("p48", {s, a1, a2, a3, abef, e, g1, g2}, {f1, f2, f3, f4, f5, f6, fff, newf})
        return (proc, 40)

    # another example with a loop
    def proc49(self):

        # nodes
        s = Start("s")
        a0 = Activity("a0","A0",10,{"res"})
        a1 = Activity("a1","A1",10,{"res1"})
        a2 = Activity("a2","A2",10,{"res2", "res3"})
        a3 = Activity("a3","A3",10,{"res4"})
        abef = Activity("abef","ABEF",10,{"ressource"})

        e = End("e")
        g1 = Join("g1", "exclusive")
        g2 = Split("g2", "exclusive")

        # flows
        f1 = Flow("f1", s, abef)
        newf = Flow("newf", abef, a0)
        newf2 = Flow("newf2", a0, g1)

        f2 = Flow("f2", g1, a1)
        f3 = Flow("f3", a1, g2)
        f4 = Flow("f4", g2, a2)
        fff = Flow("fff", a2, a3)
        f5 = Flow("f5", g2, g1)
        f6 = Flow("f6", a3, e)

        # BPMN graph
        proc = BPMNGraph("p49", {s, a0, a1, a2, a3, abef, e, g1, g2}, {f1, f2, f3, f4, f5, f6, fff, newf, newf2})
        return (proc, 40)

    def proc50(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",30,{"r1"})
        t2 = Activity("t2","T2",30,{"r2"})
        t3 = Activity("t3","T3",30,{"r3"})

        e = End("e")
        g1 = Split("g1", "exclusive")
        g2 = Join("g2", "exclusive")

        # flows
        f1 = Flow("f1", s, t1)
        f2 = Flow("f2", t1, g1)
        f3 = Flow("f3", g1, t2)
        f4 = Flow("f4", g1, t3)
        f5 = Flow("f5", t2, g2)
        f6 = Flow("f6", t3, g2)
        f7 = Flow("f7", g2, e)

        # BPMN graph
        proc = BPMNGraph("p50", {s, t1, t2, t3, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7})
        return (proc, 30)

    def proc51(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",30,{"r1"})
        t2 = Activity("t2","T2",30,{"r2"})
        t3 = Activity("t3","T3",30,{"r1"})

        e = End("e")
        g1 = Split("g1", "exclusive")
        g2 = Join("g2", "exclusive")

        # flows
        f1 = Flow("f1", s, t1)
        f2 = Flow("f2", t1, g1)
        f3 = Flow("f3", g1, t2)
        f4 = Flow("f4", g1, t3)
        f5 = Flow("f5", t2, g2)
        f6 = Flow("f6", t3, g2)
        f7 = Flow("f7", g2, e)

        # BPMN graph
        proc = BPMNGraph("p51", {s, t1, t2, t3, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7})
        return (proc, 60)

    def proc52(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",30,{"r1"})
        t2 = Activity("t2","T2",30,{"r2"})
        t3 = Activity("t3","T3",30,{"r3"})

        t4 = Activity("t4","T4",30,{"r1","r2","r3"})

        e = End("e")
        g1 = Split("g1", "exclusive")
        g2 = Join("g2", "exclusive")

        # flows
        f1 = Flow("f1", s, t1)
        f2 = Flow("f2", t1, g1)
        f3 = Flow("f3", g1, t2)
        f4 = Flow("f4", g1, t3)
        f5 = Flow("f5", t2, g2)
        f6 = Flow("f6", t3, g2)
        f7 = Flow("f7", g2, t4)
        f8 = Flow("f8", t4, e)

        # BPMN graph
        proc = BPMNGraph("p52", {s, t1, t2, t3, t4, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7, f8})
        return (proc, 60)

    def proc53(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",30,{"r1"})
        t2 = Activity("t2","T2",30,{"r2"})
        t3 = Activity("t3","T3",30,{"r3"})

        t4 = Activity("t4","T4",30,{"r4"})
        t5 = Activity("t5","T5",30,{"r5"})

        e = End("e")
        g1 = Split("g1", "exclusive")
        g2 = Join("g2", "exclusive")

        # flows
        f1 = Flow("f1", s, t1)
        f2 = Flow("f2", t1, g1)
        f3 = Flow("f3", g1, t2)
        f4 = Flow("f4", g1, t3)
        f5 = Flow("f5", t2, g2)
        f6 = Flow("f6", t3, g2)
        f7 = Flow("f7", g2, t4)
        f8 = Flow("f8", t4, t5)
        f9 = Flow("f9", t5, e)

        # BPMN graph
        proc = BPMNGraph("p53", {s, t1, t2, t3, t4, t5, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7, f8, f9})
        return (proc, 90)

    def proc54(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",30,{"r1"})
        t2 = Activity("t2","T2",30,{"r1"})
        t3 = Activity("t3","T3",30,{"r1"})

        t4 = Activity("t4","T4",30,{"r1"})
        t5 = Activity("t5","T5",30,{"r2"})

        e = End("e")
        g1 = Split("g1", "exclusive")
        g2 = Join("g2", "exclusive")

        # flows
        f1 = Flow("f1", s, t1)
        f2 = Flow("f2", t1, g1)
        f3 = Flow("f3", g1, t2)
        f4 = Flow("f4", g1, t3)
        f5 = Flow("f5", t2, g2)
        f6 = Flow("f6", t3, g2)
        f7 = Flow("f7", g2, t4)
        f8 = Flow("f8", t4, t5)
        f9 = Flow("f9", t5, e)

        # BPMN graph
        proc = BPMNGraph("p54", {s, t1, t2, t3, t4, t5, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7, f8, f9})
        return (proc, 90)


    # example taken from FOCLASA 2018
    def proc55(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","FillInForms",2,{})
        t2 = Activity("t2","MedicalCheckUp",3,{"doctor"})
        t3 = Activity("t3","Visa",10,{"visaofficer"})

        t4 = Activity("t4","Reject",1,{"HR"})
        t5 = Activity("t5","Validate",1,{"HR"})
        t6 = Activity("t6","ValidatePartial",1,{"HR"})
        t7 = Activity("t7","CheckAddDocuments",2,{"HR"})

        t8 = Activity("t8","UpdatePersonnelDB",1,{"TechnicalStaff"})

        t9 = Activity("t9","AnticipateWages",2,{"HR"})
        t10 = Activity("t10","PrepareWelcomeKit",3,{"Assistant"})
        t11 = Activity("t11","ArchiveAllDocuments",1,{"HR"})

        e = End("e")
        g1 = Join("g1", "exclusive")
        g2 = Split("g2", "exclusive")
        g3 = Join("g3", "exclusive")
        g4 = Split("g4", "exclusive")
        g5 = Join("g5", "exclusive")
        g6 = Split("g6", "parallel")
        g7 = Join("g7", "parallel")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", t1, t2)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", g2, g3)
        f6 = Flow("f6", g2, t3)
        f7 = Flow("f7", t3, g3)
        f8 = Flow("f8", g3, g4)
        f9 = Flow("f9", g4, t4)
        f10 = Flow("f10", t4, g1)
        f11 = Flow("f11", g4, t5)
        f12 = Flow("f12", g4, t6)
        f23 = Flow("f23", t6, t7)
        f13 = Flow("f13", t5, g5)
        f14 = Flow("f14", t7, g5)
        f15 = Flow("f15", g5, t8)
        f16 = Flow("f16", t8, g6)
        f17 = Flow("f17", g6, t9)
        f18 = Flow("f18", g6, t10)
        f19 = Flow("f19", t9, g7)
        f20 = Flow("f20", t10, g7)
        f21 = Flow("f21", g7, t11)
        f22 = Flow("f22", t11, e)

        # BPMN graph
        proc = BPMNGraph("p55", {s, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, e, g1, g2, g3, g4, g5, g6, g7}, {f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23})
        return (proc, 12)

    # example taken from FOCLASA 2018 (without loop)
    def proc56(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","FillInForms",2,{})
        t2 = Activity("t2","MedicalCheckUp",3,{"doctor"})
        t3 = Activity("t3","Visa",10,{"visaofficer"})

        #t4 = Activity("t4","Reject",1,{"HR"})
        t5 = Activity("t5","Validate",1,{"HR"})
        t6 = Activity("t6","ValidatePartial",1,{"HR"})
        t7 = Activity("t7","CheckAddDocuments",2,{"HR"})

        t8 = Activity("t8","UpdatePersonnelDB",1,{"TechnicalStaff"})

        t9 = Activity("t9","AnticipateWages",2,{"HR"})
        t10 = Activity("t10","PrepareWelcomeKit",3,{"Assistant"})
        t11 = Activity("t11","ArchiveAllDocuments",1,{"HR"})

        e = End("e")
        #g1 = Join("g1", "exclusive")
        g2 = Split("g2", "exclusive")
        g3 = Join("g3", "exclusive")
        g4 = Split("g4", "exclusive")
        g5 = Join("g5", "exclusive")
        g6 = Split("g6", "parallel")
        g7 = Join("g7", "parallel")

        # flows
        f1 = Flow("f1", s, t1)
        #f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", t1, t2)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", g2, g3)
        f6 = Flow("f6", g2, t3)
        f7 = Flow("f7", t3, g3)
        f8 = Flow("f8", g3, g4)
        #f9 = Flow("f9", g4, t4)
        #f10 = Flow("f10", t4, g1)
        f11 = Flow("f11", g4, t5)
        f12 = Flow("f12", g4, t6)
        f23 = Flow("f23", t6, t7)
        f13 = Flow("f13", t5, g5)
        f14 = Flow("f14", t7, g5)
        f15 = Flow("f15", g5, t8)
        f16 = Flow("f16", t8, g6)
        f17 = Flow("f17", g6, t9)
        f18 = Flow("f18", g6, t10)
        f19 = Flow("f19", t9, g7)
        f20 = Flow("f20", t10, g7)
        f21 = Flow("f21", g7, t11)
        f22 = Flow("f22", t11, e)

        # BPMN graph
        proc = BPMNGraph("p56", {s, t1, t2, t3, t5, t6, t7, t8, t9, t10, t11, e, g2, g3, g4, g5, g6, g7}, {f1, f3, f4, f5, f6, f7, f8, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23})
        return (proc, 8)


    # example taken from FOCLASA 2018 (without loop & with strong flows)
    def proc57(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","FillInForms",2,{})
        t2 = Activity("t2","MedicalCheckUp",3,{"doctor"})
        t3 = Activity("t3","Visa",10,{"visaofficer"})

        #t4 = Activity("t4","Reject",1,{"HR"})
        t5 = Activity("t5","Validate",1,{"HR"})
        t6 = Activity("t6","ValidatePartial",1,{"HR"})
        t7 = Activity("t7","CheckAddDocuments",2,{"HR"})

        t8 = Activity("t8","UpdatePersonnelDB",1,{"TechnicalStaff"})

        t9 = Activity("t9","AnticipateWages",2,{"HR"})
        t10 = Activity("t10","PrepareWelcomeKit",3,{"Assistant"})
        t11 = Activity("t11","ArchiveAllDocuments",1,{"HR"})

        e = End("e")
        #g1 = Join("g1", "exclusive")
        g2 = Split("g2", "exclusive")
        g3 = Join("g3", "exclusive")
        g4 = Split("g4", "exclusive")
        g5 = Join("g5", "exclusive")
        g6 = Split("g6", "parallel")
        g7 = Join("g7", "parallel")

        # flows
        f1 = Flow("f1", s, t1)
        #f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", t1, t2)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", g2, g3)
        f6 = Flow("f6", g2, t3)
        f7 = Flow("f7", t3, g3)
        f8 = Flow("f8", g3, g4)
        #f9 = Flow("f9", g4, t4)
        #f10 = Flow("f10", t4, g1)
        f11 = Flow("f11", g4, t5)
        f12 = Flow("f12", g4, t6)
        f23 = Flow("f23", t6, t7)
        f13 = Flow("f13", t5, g5)
        f14 = Flow("f14", t7, g5)
        f15 = Flow("f15", g5, t8)
        f16 = Flow("f16", t8, g6)
        f17 = Flow("f17", g6, t9)
        f18 = Flow("f18", g6, t10)
        f19 = Flow("f19", t9, g7)
        f20 = Flow("f20", t10, g7)
        f21 = Flow("f21", g7, t11)
        f22 = Flow("f22", t11, e)

        # BPMN graph
        proc = BPMNGraph("p57", {s, t1, t2, t3, t5, t6, t7, t8, t9, t10, t11, e, g2, g3, g4, g5, g6, g7}, {f1, f3, f4, f5, f6, f7, f8, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23})
        return (proc, 10)

    # example taken from FOCLASA 2018 (without loop & with strong flows & with employee res.)
    def proc58(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","FillInForms",2,{"employee"})
        t2 = Activity("t2","MedicalCheckUp",3,{"doctor", "employee"})
        t3 = Activity("t3","Visa",10,{"visaofficer", "employee"})

        #t4 = Activity("t4","Reject",1,{"HR"})
        t5 = Activity("t5","Validate",1,{"HR", "employee"})
        t6 = Activity("t6","ValidatePartial",1,{"HR", "employee"})
        t7 = Activity("t7","CheckAddDocuments",2,{"HR", "employee"})

        t8 = Activity("t8","UpdatePersonnelDB",1,{"TechnicalStaff", "employee"})

        t9 = Activity("t9","AnticipateWages",2,{"HR"})
        t10 = Activity("t10","PrepareWelcomeKit",3,{"Assistant", "employee"})
        t11 = Activity("t11","ArchiveAllDocuments",1,{"HR"})

        e = End("e")
        #g1 = Join("g1", "exclusive")
        g2 = Split("g2", "exclusive")
        g3 = Join("g3", "exclusive")
        g4 = Split("g4", "exclusive")
        g5 = Join("g5", "exclusive")
        g6 = Split("g6", "parallel")
        g7 = Join("g7", "parallel")

        # flows
        f1 = Flow("f1", s, t1)
        #f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", t1, t2)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", g2, g3)
        f6 = Flow("f6", g2, t3)
        f7 = Flow("f7", t3, g3)
        f8 = Flow("f8", g3, g4)
        #f9 = Flow("f9", g4, t4)
        #f10 = Flow("f10", t4, g1)
        f11 = Flow("f11", g4, t5)
        f12 = Flow("f12", g4, t6)
        f23 = Flow("f23", t6, t7)
        f13 = Flow("f13", t5, g5)
        f14 = Flow("f14", t7, g5)
        f15 = Flow("f15", g5, t8)
        f16 = Flow("f16", t8, g6)
        f17 = Flow("f17", g6, t9)
        f18 = Flow("f18", g6, t10)
        f19 = Flow("f19", t9, g7)
        f20 = Flow("f20", t10, g7)
        f21 = Flow("f21", g7, t11)
        f22 = Flow("f22", t11, e)

        # BPMN graph
        proc = BPMNGraph("p58", {s, t1, t2, t3, t5, t6, t7, t8, t9, t10, t11, e, g2, g3, g4, g5, g6, g7}, {f1, f3, f4, f5, f6, f7, f8, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23})
        return (proc, 11)

    # example taken from FOCLASA 2018 (without loop & with strong flows & with employee res.)
    # completing changing the resources (keeping the structure) to have the variability
    # at the beginning
    def proc59(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","FillInForms",2,{"employee"})
        t2 = Activity("t2","MedicalCheckUp",3,{"doctor"})
        t3 = Activity("t3","Visa",10,{"visaofficer", "employee"})

        #t4 = Activity("t4","Reject",1,{"HR"})
        t5 = Activity("t5","Validate",1,{"HR", "employee"})
        t6 = Activity("t6","ValidatePartial",1,{"HR", "employee"})
        t7 = Activity("t7","CheckAddDocuments",2,{"HR", "employee"})

        t8 = Activity("t8","UpdatePersonnelDB",1,{"TechnicalStaff", "employee"})

        t9 = Activity("t9","AnticipateWages",2,{"HR", "employee"})
        t10 = Activity("t10","PrepareWelcomeKit",3,{"Assistant", "employee"})
        t11 = Activity("t11","ArchiveAllDocuments",1,{"HR", "employee"})

        e = End("e")
        #g1 = Join("g1", "exclusive")
        g2 = Split("g2", "exclusive")
        g3 = Join("g3", "exclusive")
        g4 = Split("g4", "exclusive")
        g5 = Join("g5", "exclusive")
        g6 = Split("g6", "parallel")
        g7 = Join("g7", "parallel")

        # flows
        f1 = Flow("f1", s, t1)
        #f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", t1, t2)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", g2, g3)
        f6 = Flow("f6", g2, t3)
        f7 = Flow("f7", t3, g3)
        f8 = Flow("f8", g3, g4)
        #f9 = Flow("f9", g4, t4)
        #f10 = Flow("f10", t4, g1)
        f11 = Flow("f11", g4, t5)
        f12 = Flow("f12", g4, t6)
        f23 = Flow("f23", t6, t7, "strong")
        f13 = Flow("f13", t5, g5)
        f14 = Flow("f14", t7, g5, "strong")
        f15 = Flow("f15", g5, t8, "strong")
        f16 = Flow("f16", t8, g6)
        f17 = Flow("f17", g6, t9)
        f18 = Flow("f18", g6, t10)
        f19 = Flow("f19", t9, g7)
        f20 = Flow("f20", t10, g7)
        f21 = Flow("f21", g7, t11)
        f22 = Flow("f22", t11, e)

        # BPMN graph
        proc = BPMNGraph("p59", {s, t1, t2, t3, t5, t6, t7, t8, t9, t10, t11, e, g2, g3, g4, g5, g6, g7}, {f1, f3, f4, f5, f6, f7, f8, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23})
        return (proc, 13)

    # example taken from FOCLASA 2018 (without loop & with strong flows & with employee res.)
    # only parallel gateways
    def proc60(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","FillInForms",2,{"employee"})
        t2 = Activity("t2","MedicalCheckUp",3,{"doctor"})
        t3 = Activity("t3","Visa",10,{"visaofficer", "employee"})

        #t4 = Activity("t4","Reject",1,{"HR"})
        t5 = Activity("t5","Validate",1,{"HR", "employee"})
        t6 = Activity("t6","ValidatePartial",1,{"HR", "employee"})
        t7 = Activity("t7","CheckAddDocuments",2,{"HR", "employee"})

        t8 = Activity("t8","UpdatePersonnelDB",1,{"TechnicalStaff", "employee"})

        t9 = Activity("t9","AnticipateWages",2,{"HR", "employee"})
        t10 = Activity("t10","PrepareWelcomeKit",3,{"Assistant", "employee"})
        t11 = Activity("t11","ArchiveAllDocuments",1,{"HR", "employee"})

        e = End("e")
        #g1 = Join("g1", "exclusive")
        g2 = Split("g2", "parallel")
        g3 = Join("g3", "parallel")
        g4 = Split("g4", "parallel")
        g5 = Join("g5", "parallel")
        g6 = Split("g6", "parallel")
        g7 = Join("g7", "parallel")

        # flows
        f1 = Flow("f1", s, t1)
        #f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", t1, t2)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", g2, g3)
        f6 = Flow("f6", g2, t3)
        f7 = Flow("f7", t3, g3)
        f8 = Flow("f8", g3, g4)
        #f9 = Flow("f9", g4, t4)
        #f10 = Flow("f10", t4, g1)
        f11 = Flow("f11", g4, t5)
        f12 = Flow("f12", g4, t6)
        f23 = Flow("f23", t6, t7)
        f13 = Flow("f13", t5, g5)
        f14 = Flow("f14", t7, g5)
        f15 = Flow("f15", g5, t8)
        f16 = Flow("f16", t8, g6)
        f17 = Flow("f17", g6, t9)
        f18 = Flow("f18", g6, t10)
        f19 = Flow("f19", t9, g7)
        f20 = Flow("f20", t10, g7)
        f21 = Flow("f21", g7, t11)
        f22 = Flow("f22", t11, e)

        # BPMN graph
        proc = BPMNGraph("p60", {s, t1, t2, t3, t5, t6, t7, t8, t9, t10, t11, e, g2, g3, g4, g5, g6, g7}, {f1, f3, f4, f5, f6, f7, f8, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23})
        return (proc, 23)

    # example taken from FOCLASA 2018 (without loop & with strong flows & with employee res.)
    # only parallel gateways
    def proc61(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","FillInForms",2,{"employee"})
        t2 = Activity("t2","MedicalCheckUp",3,{"doctor"})
        t3 = Activity("t3","Visa",10,{"visaofficer", "employee"})

        #t4 = Activity("t4","Reject",1,{"HR"})
        t5 = Activity("t5","Validate",1,{"HR", "employee"})
        t6 = Activity("t6","ValidatePartial",1,{"HR", "employee"})
        t7 = Activity("t7","CheckAddDocuments",2,{"HR", "employee"})

        t8 = Activity("t8","UpdatePersonnelDB",1,{"TechnicalStaff", "employee"})

        #t9 = Activity("t9","AnticipateWages",2,{"HR", "employee"})
        #t10 = Activity("t10","PrepareWelcomeKit",3,{"Assistant", "employee"})
        #t11 = Activity("t11","ArchiveAllDocuments",1,{"HR", "employee"})

        e = End("e")
        #g1 = Join("g1", "exclusive")
        g2 = Split("g2", "parallel")
        g3 = Join("g3", "parallel")
        g4 = Split("g4", "parallel")
        g5 = Join("g5", "parallel")
        #g6 = Split("g6", "parallel")
        #g7 = Join("g7", "parallel")

        # flows
        f1 = Flow("f1", s, t1)
        #f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", t1, t2)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", g2, g3)
        f6 = Flow("f6", g2, t3)
        f7 = Flow("f7", t3, g3)
        f8 = Flow("f8", g3, g4)
        #f9 = Flow("f9", g4, t4)
        #f10 = Flow("f10", t4, g1)
        f11 = Flow("f11", g4, t5)
        f12 = Flow("f12", g4, t6)
        f23 = Flow("f23", t6, t7)
        f13 = Flow("f13", t5, g5)
        f14 = Flow("f14", t7, g5)
        f15 = Flow("f15", g5, t8)
        f16 = Flow("f16", t8, e)
        #f17 = Flow("f17", g6, t9)
        #f18 = Flow("f18", g6, t10)
        #f19 = Flow("f19", t9, g7)
        #f20 = Flow("f20", t10, g7)
        #f21 = Flow("f21", g7, t11)
        #f22 = Flow("f22", t11, e)

        # BPMN graph
        proc = BPMNGraph("p61", {s, t1, t2, t3, t5, t6, t7, t8, e, g2, g3, g4, g5}, {f1, f3, f4, f5, f6, f7, f8, f11, f12, f13, f14, f15, f16, f23})
        return (proc, 17)

    # example taken from FOCLASA 2018 (without loop & with strong flows & with employee res.)
    # only parallel gateways
    def proc62(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","FillInForms",2,{"employee"})
        t2 = Activity("t2","MedicalCheckUp",3,{"doctor"})
        t3 = Activity("t3","Visa",10,{"visaofficer", "employee"})

        #t4 = Activity("t4","Reject",1,{"HR"})
        t5 = Activity("t5","Validate",1,{"HR", "employee"})
        t6 = Activity("t6","ValidatePartial",1,{"employee"})
        t7 = Activity("t7","CheckAddDocuments",2,{"HR"})

        #t8 = Activity("t8","UpdatePersonnelDB",1,{"TechnicalStaff", "employee"})

        #t9 = Activity("t9","AnticipateWages",2,{"HR", "employee"})
        #t10 = Activity("t10","PrepareWelcomeKit",3,{"Assistant", "employee"})
        #t11 = Activity("t11","ArchiveAllDocuments",1,{"HR", "employee"})

        e = End("e")
        #g1 = Join("g1", "exclusive")
        g2 = Split("g2", "parallel")
        g3 = Join("g3", "parallel")
        g4 = Split("g4", "parallel")
        g5 = Join("g5", "parallel")
        #g6 = Split("g6", "parallel")
        #g7 = Join("g7", "parallel")

        # flows
        f1 = Flow("f1", s, t1)
        #f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", t1, t2)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", g2, g3)
        f6 = Flow("f6", g2, t3)
        f7 = Flow("f7", t3, g3)
        f8 = Flow("f8", g3, g4)
        #f9 = Flow("f9", g4, t4)
        #f10 = Flow("f10", t4, g1)
        f11 = Flow("f11", g4, t5)
        f12 = Flow("f12", g4, t6)
        f23 = Flow("f23", t6, t7)
        f13 = Flow("f13", t5, g5)
        f14 = Flow("f14", t7, g5)
        f15 = Flow("f15", g5, e)
        #f16 = Flow("f16", t8, e)
        #f17 = Flow("f17", g6, t9)
        #f18 = Flow("f18", g6, t10)
        #f19 = Flow("f19", t9, g7)
        #f20 = Flow("f20", t10, g7)
        #f21 = Flow("f21", g7, t11)
        #f22 = Flow("f22", t11, e)

        # BPMN graph
        proc = BPMNGraph("p62", {s, t1, t2, t3, t5, t6, t7, e, g2, g3, g4, g5}, {f1, f3, f4, f5, f6, f7, f8, f11, f12, f13, f14, f15, f23})
        return (proc, 14)

    # with some exclusive gateways
    def proc63(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","FillInForms",2,{"employee"})
        t2 = Activity("t2","MedicalCheckUp",3,{"doctor"})
        t3 = Activity("t3","Visa",10,{"visaofficer", "employee"})

        #t4 = Activity("t4","Reject",1,{"HR"})
        t5 = Activity("t5","Validate",1,{"HR", "employee"})
        t6 = Activity("t6","ValidatePartial",1,{"employee"})
        t7 = Activity("t7","CheckAddDocuments",2,{"HR"})

        #t8 = Activity("t8","UpdatePersonnelDB",1,{"TechnicalStaff", "employee"})

        #t9 = Activity("t9","AnticipateWages",2,{"HR", "employee"})
        #t10 = Activity("t10","PrepareWelcomeKit",3,{"Assistant", "employee"})
        #t11 = Activity("t11","ArchiveAllDocuments",1,{"HR", "employee"})

        e = End("e")
        #g1 = Join("g1", "exclusive")
        g2 = Split("g2", "exclusive")
        g3 = Join("g3", "exclusive")
        g4 = Split("g4", "parallel")
        g5 = Join("g5", "parallel")
        #g6 = Split("g6", "parallel")
        #g7 = Join("g7", "parallel")

        # flows
        f1 = Flow("f1", s, t1)
        #f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", t1, t2)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", g2, g3)
        f6 = Flow("f6", g2, t3)
        f7 = Flow("f7", t3, g3)
        f8 = Flow("f8", g3, g4)
        #f9 = Flow("f9", g4, t4)
        #f10 = Flow("f10", t4, g1)
        f11 = Flow("f11", g4, t5)
        f12 = Flow("f12", g4, t6)
        f23 = Flow("f23", t6, t7)
        f13 = Flow("f13", t5, g5)
        f14 = Flow("f14", t7, g5)
        f15 = Flow("f15", g5, e)
        #f16 = Flow("f16", t8, e)
        #f17 = Flow("f17", g6, t9)
        #f18 = Flow("f18", g6, t10)
        #f19 = Flow("f19", t9, g7)
        #f20 = Flow("f20", t10, g7)
        #f21 = Flow("f21", g7, t11)
        #f22 = Flow("f22", t11, e)

        # BPMN graph
        proc = BPMNGraph("p63", {s, t1, t2, t3, t5, t6, t7, e, g2, g3, g4, g5}, {f1, f3, f4, f5, f6, f7, f8, f11, f12, f13, f14, f15, f23})
        return (proc, 6)

    # home made, realistic, simple
    def proc64(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","FillInForms",2,{"employee"})
        t2 = Activity("t2","MedicalPaper",3,{"doctor"})
        t3 = Activity("t3","Visa",10,{"visaofficer", "employee"})

        #t4 = Activity("t4","Reject",1,{"HR"})
        t5 = Activity("t5","Validate",1,{"HR", "employee"})
        t6 = Activity("t6","PrepareWelcomeKit",3,{"Assistant"})
        t7 = Activity("t7","ArchiveDocuments",1,{"HR"})

        #t8 = Activity("t8","UpdatePersonnelDB",1,{"TechnicalStaff", "employee"})

        #t9 = Activity("t9","AnticipateWages",2,{"HR", "employee"})
        #t10 = Activity("t10","PrepareWelcomeKit",3,{"Assistant", "employee"})
        #t11 = Activity("t11","ArchiveAllDocuments",1,{"HR", "employee"})

        e = End("e")
        #g1 = Join("g1", "exclusive")
        #g2 = Split("g2", "parallel")
        #g3 = Join("g3", "parallel")
        g4 = Split("g4", "parallel")
        g5 = Join("g5", "parallel")
        #g6 = Split("g6", "parallel")
        #g7 = Join("g7", "parallel")

        # flows
        f1 = Flow("f1", s, t1)
        #f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", t1, t2)
        f4 = Flow("f4", t2, t3)
        # f5 = Flow("f5", g2, g3)
        #f6 = Flow("f6", g2, t3)
        f7 = Flow("f7", t3, g4)
        #f8 = Flow("f8", g3, g4)
        #f9 = Flow("f9", g4, t4)
        #f10 = Flow("f10", t4, g1)
        f11 = Flow("f11", g4, t5)
        f12 = Flow("f12", g4, t6)
        f23 = Flow("f23", t6, t7)
        f13 = Flow("f13", t5, g5)
        f14 = Flow("f14", t7, g5)
        f15 = Flow("f15", g5, e)
        #f16 = Flow("f16", t8, e)
        #f17 = Flow("f17", g6, t9)
        #f18 = Flow("f18", g6, t10)
        #f19 = Flow("f19", t9, g7)
        #f20 = Flow("f20", t10, g7)
        #f21 = Flow("f21", g7, t11)
        #f22 = Flow("f22", t11, e)

        # BPMN graph
        proc = BPMNGraph("p64", {s, t1, t2, t3, t5, t6, t7, e, g4, g5}, {f1, f3, f4, f7, f11, f12, f13, f14, f15, f23})
        return (proc, 13)

    # home made, realistic, simple
    def proc65(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","MedicalAuthorization",3,{"doctor"})
        t2 = Activity("t2","FillInForms",3,{"employee"})
        t3 = Activity("t3","Visa",10,{"visaofficer", "employee"})

        #t4 = Activity("t4","Reject",1,{"HR"})
        t5 = Activity("t5","Validate",1,{"HR", "employee"})
        t6 = Activity("t6","PrepareWelcomeKit",3,{"Assistant"})
        t7 = Activity("t7","ArchiveDocuments",1,{"HR"})

        #t8 = Activity("t8","UpdatePersonnelDB",1,{"TechnicalStaff", "employee"})

        #t9 = Activity("t9","AnticipateWages",2,{"HR", "employee"})
        #t10 = Activity("t10","PrepareWelcomeKit",3,{"Assistant", "employee"})
        #t11 = Activity("t11","ArchiveAllDocuments",1,{"HR", "employee"})

        e = End("e")
        #g1 = Join("g1", "exclusive")
        g2 = Split("g2", "parallel")
        g3 = Join("g3", "parallel")
        g4 = Split("g4", "parallel")
        g5 = Join("g5", "parallel")
        #g6 = Split("g6", "parallel")
        #g7 = Join("g7", "parallel")

        # flows
        f1 = Flow("f1", s, t1)
        #f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", t1, g2)
        f4 = Flow("f4", g2, t2)
        f5 = Flow("f5", t2, g3)
        f6 = Flow("f6", g2, t3)
        f7 = Flow("f7", t3, g3)
        f8 = Flow("f8", g3, g4)
        #f9 = Flow("f9", g4, t4)
        #f10 = Flow("f10", t4, g1)
        f11 = Flow("f11", g4, t5)
        f12 = Flow("f12", g4, t6)
        f23 = Flow("f23", t6, t7)
        f13 = Flow("f13", t5, g5)
        f14 = Flow("f14", t7, g5)
        f15 = Flow("f15", g5, e)
        #f16 = Flow("f16", t8, e)
        #f17 = Flow("f17", g6, t9)
        #f18 = Flow("f18", g6, t10)
        #f19 = Flow("f19", t9, g7)
        #f20 = Flow("f20", t10, g7)
        #f21 = Flow("f21", g7, t11)
        #f22 = Flow("f22", t11, e)

        # BPMN graph
        proc = BPMNGraph("p65", {s, t1, t2, t3, t5, t6, t7, e, g2, g3, g4, g5}, {f1, f3, f4, f5, f6, f7, f8, f11, f12, f13, f14, f15, f23})
        return (proc, 14)

    # example taken from FOCLASA 2018 (without loop & with strong flows & with employee res.)
    # only parallel gateways
    def proc66(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","FillInForms",2,{"employee"})
        t2 = Activity("t2","MedicalCheckUp",3,{"doctor"})
        t3 = Activity("t3","Visa",10,{"visaofficer", "employee"})

        #t4 = Activity("t4","Reject",1,{"HR"})
        t5 = Activity("t5","Validate",1,{"HR", "employee"})
        t6 = Activity("t6","ValidatePartial",1,{"HR" })
        t7 = Activity("t7","CheckAddDocuments",2,{"HR", "employee"})

        t8 = Activity("t8","UpdatePersonnelDB",1,{"TechnicalStaff", "employee"})

        t9 = Activity("t9","AnticipateWages",2,{"HR"})
        t10 = Activity("t10","PrepareWelcomeKit",3,{"Assistant" })
        t11 = Activity("t11","ArchiveAllDocuments",1,{"HR", "employee"})

        e = End("e")
        #g1 = Join("g1", "exclusive")
        g2 = Split("g2", "parallel")
        g3 = Join("g3", "parallel")
        g4 = Split("g4", "parallel")
        g5 = Join("g5", "parallel")
        g6 = Split("g6", "parallel")
        g7 = Join("g7", "parallel")

        # flows
        f1 = Flow("f1", s, t1)
        #f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", t1, t2)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", g2, g3)
        f6 = Flow("f6", g2, t3)
        f7 = Flow("f7", t3, g3)
        f8 = Flow("f8", g3, g4)
        #f9 = Flow("f9", g4, t4)
        #f10 = Flow("f10", t4, g1)
        f11 = Flow("f11", g4, t5)
        f12 = Flow("f12", g4, t6)
        f23 = Flow("f23", t6, t7)
        f13 = Flow("f13", t5, g5)
        f14 = Flow("f14", t7, g5)
        f15 = Flow("f15", g5, t8)
        f16 = Flow("f16", t8, g6)
        f17 = Flow("f17", g6, t9)
        f18 = Flow("f18", g6, t10)
        f19 = Flow("f19", t9, g7)
        f20 = Flow("f20", t10, g7)
        f21 = Flow("f21", g7, t11)
        f22 = Flow("f22", t11, e)

        # BPMN graph
        proc = BPMNGraph("p66", {s, t1, t2, t3, t5, t6, t7, t8, t9, t10, t11, e, g2, g3, g4, g5, g6, g7}, {f1, f3, f4, f5, f6, f7, f8, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23})
        return (proc, 18)

    def proc67(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"r1"})
        a2 = Activity("a2","A2",10,{"r2", "r3"})
        a3 = Activity("a3","A3",10,{"r4", "r5"})
        a4 = Activity("a4","A4",10,{"r6"})
        a5 = Activity("a5","A5",10,{"r7", "r8"})
        a6 = Activity("a6","A6",10,{"r11", "r12"})
        a7 = Activity("a7","A7",10,{"r14"})
        a8 = Activity("a8","A8",10,{"r222", "r33"})
        a9 = Activity("a9","A9",10,{"r444", "r555"})
        e = End("e")

        # flows
        f1 = Flow("f1", s, a1)
        f2 = Flow("f2", a1, a2)
        f3 = Flow("f3", a2, a3)
        f4 = Flow("f4", a3, a4)
        f5 = Flow("f5", a4, a5)
        f6 = Flow("f6", a5, a6)
        f7 = Flow("f7", a6, a7)
        f8 = Flow("f8", a7, a8)
        f9 = Flow("f9", a8, a9)
        f10 = Flow("f10", a9, e)

        # BPMN graph
        proc = BPMNGraph("p67", {s, a1, a2, a3, a4, a5, a6, a7, a8, a9, e}, {f1, f2, f3, f4, f5, f6, f7, f8, f9, f10})
        return (proc, 10)

    def proc68(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"r1"})
        a2 = Activity("a2","A2",10,{"r1"})
        a3 = Activity("a3","A3",10,{"r1"})
        a4 = Activity("a4","A4",10,{"r1"})
        a5 = Activity("a5","A5",10,{"r1"})
        a6 = Activity("a6","A6",10,{"r1"})
        a7 = Activity("a7","A7",10,{"r1"})
        a8 = Activity("a8","A8",70,{"r222", "r333"})
        a9 = Activity("a9","A9",70,{"r444", "r555"})
        e = End("e")

        # flows
        f1 = Flow("f1", s, a1)
        f2 = Flow("f2", a1, a2)
        f3 = Flow("f3", a2, a3)
        f4 = Flow("f4", a3, a4)
        f5 = Flow("f5", a4, a5)
        f6 = Flow("f6", a5, a6)
        f7 = Flow("f7", a6, a7)
        f8 = Flow("f8", a7, a8)
        f9 = Flow("f9", a8, a9)
        f10 = Flow("f10", a9, e)

        # BPMN graph
        proc = BPMNGraph("p68", {s, a1, a2, a3, a4, a5, a6, a7, a8, a9, e}, {f1, f2, f3, f4, f5, f6, f7, f8, f9, f10})
        return (proc, 70)

    def proc69(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"r1"})
        a2 = Activity("a2","A2",10,{"r2"})
        a3 = Activity("a3","A3",10,{"r3"})
        a4 = Activity("a4","A4",10,{"r1"})
        a5 = Activity("a5","A5",10,{"r1"})
        a6 = Activity("a6","A6",10,{"r1"})
        a7 = Activity("a7","A7",10,{"r1"})
        a8 = Activity("a8","A8",10,{"r1"})
        a9 = Activity("a9","A9",10,{"r1"})
        e = End("e")

        # flows
        f1 = Flow("f1", s, a1)
        f2 = Flow("f2", a1, a2)
        f3 = Flow("f3", a2, a3)
        f4 = Flow("f4", a3, a4)
        f5 = Flow("f5", a4, a5)
        f6 = Flow("f6", a5, a6)
        f7 = Flow("f7", a6, a7)
        f8 = Flow("f8", a7, a8)
        f9 = Flow("f9", a8, a9)
        f10 = Flow("f10", a9, e)

        # BPMN graph
        proc = BPMNGraph("p69", {s, a1, a2, a3, a4, a5, a6, a7, a8, a9, e}, {f1, f2, f3, f4, f5, f6, f7, f8, f9, f10})
        return (proc, 70)

    def proc70(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"r1"})
        a2 = Activity("a2","A2",10,{"r2"})
        a3 = Activity("a3","A3",10,{"r3"})
        e = End("e")

        # flows
        f1 = Flow("f1", s, a1)
        f2 = Flow("f2", a1, a2)
        f3 = Flow("f3", a2, a3, "strong")
        f4 = Flow("f4", a3, e)

        # BPMN graph
        proc = BPMNGraph("p70", {s, a1, a2, a3, e}, {f1, f2, f3, f4})
        return (proc, 20)

    def proc71(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"r1"})
        a2 = Activity("a2","A2",10,{"r2"})
        a3 = Activity("a3","A3",10,{"r3"})
        a4 = Activity("a4","A4",10,{"r4"})
        e = End("e")

        # flows
        f1 = Flow("f1", s, a1)
        f2 = Flow("f2", a1, a2)
        f3 = Flow("f3", a2, a3, "strong")
        f4 = Flow("f4", a3, a4)
        f5 = Flow("f5", a4, e)

        # BPMN graph
        proc = BPMNGraph("p71", {s, a1, a2, a3, a4, e}, {f1, f2, f3, f4, f5})
        return (proc, 20)

    def proc72(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"r1"})
        a2 = Activity("a2","A2",10,{"r2"})
        a3 = Activity("a3","A3",10,{"r3"})
        a4 = Activity("a4","A4",10,{"r4"})
        e = End("e")

        # flows
        f1 = Flow("f1", s, a1)
        f2 = Flow("f2", a1, a2, "strong")
        f3 = Flow("f3", a2, a3, "strong")
        f4 = Flow("f4", a3, a4)
        f5 = Flow("f5", a4, e)

        # BPMN graph
        proc = BPMNGraph("p72", {s, a1, a2, a3, a4, e}, {f1, f2, f3, f4, f5})
        return (proc, 30)

    def proc73(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r2"})
        t3 = Activity("t3","T3",40,{"r3"})
        t4 = Activity("t4","T4",40,{"r4"})
        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", g1, t3)
        f4 = Flow("f4", t1, t2, "strong")
        f5 = Flow("f5", t3, t4)
        f6 = Flow("f6", t2, g2)
        f7 = Flow("f7", t4, g2)
        f8 = Flow("f8", g2, e)

        # BPMN graph
        proc = BPMNGraph("p73", {s, t1, t2, t3, t4, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7, f8})
        return (proc, 40)

    def proc74(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"r1"})
        a2 = Activity("a2","A2",10,{"r2"})
        a3 = Activity("a3","A3",10,{"r3"})
        a4 = Activity("a4","A4",10,{"r4"})
        a5 = Activity("a5","A5",10,{"r5"})
        a6 = Activity("a6","A6",10,{"r6"})
        a7 = Activity("a7","A7",10,{"r7"})
        a8 = Activity("a8","A8",10,{"r8"})
        a9 = Activity("a9","A9",10,{"r9"})
        e = End("e")

        # flows
        f1 = Flow("f1", s, a1)
        f2 = Flow("f2", a1, a2, "strong")
        f3 = Flow("f3", a2, a3)
        f4 = Flow("f4", a3, a4)
        f5 = Flow("f5", a4, a5, "strong")
        f6 = Flow("f6", a5, a6)
        f7 = Flow("f7", a6, a7)
        f8 = Flow("f8", a7, a8, "strong")
        f9 = Flow("f9", a8, a9)
        f10 = Flow("f10", a9, e)

        # BPMN graph
        proc = BPMNGraph("p74", {s, a1, a2, a3, a4, a5, a6, a7, a8, a9, e}, {f1, f2, f3, f4, f5, f6, f7, f8, f9, f10})
        return (proc, 40)

    def proc75(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"r1"})
        a2 = Activity("a2","A2",10,{"r2"})
        a3 = Activity("a3","A3",10,{"r3"})
        a4 = Activity("a4","A4",10,{"r4"})
        a5 = Activity("a5","A5",10,{"r5"})
        a6 = Activity("a6","A6",10,{"r6"})
        a7 = Activity("a7","A7",10,{"r7"})
        a8 = Activity("a8","A8",10,{"r8"})
        a9 = Activity("a9","A9",10,{"r9"})
        e = End("e")

        # flows
        f1 = Flow("f1", s, a1)
        f2 = Flow("f2", a1, a2, "strong")
        f3 = Flow("f3", a2, a3)
        f4 = Flow("f4", a3, a4, "strong")
        f5 = Flow("f5", a4, a5, "strong")
        f6 = Flow("f6", a5, a6, "strong")
        f7 = Flow("f7", a6, a7)
        f8 = Flow("f8", a7, a8, "strong")
        f9 = Flow("f9", a8, a9, "strong")
        f10 = Flow("f10", a9, e)

        # BPMN graph
        proc = BPMNGraph("p75", {s, a1, a2, a3, a4, a5, a6, a7, a8, a9, e}, {f1, f2, f3, f4, f5, f6, f7, f8, f9, f10})
        return (proc, 50)

    def proc76(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r2"})
        t3 = Activity("t3","T3",40,{"r3"})
        t4 = Activity("t4","T4",40,{"r4"})
        t5 = Activity("t5","T5",20,{"r5"})
        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", g1, t3)
        f4 = Flow("f4", t1, t2, "strong")
        f5 = Flow("f5", t3, t4)
        f6 = Flow("f6", t2, g2)
        f7 = Flow("f7", t4, g2, "strong")
        f8 = Flow("f8", g2, t5, "strong")
        f9 = Flow("f9", t5, e)

        # BPMN graph
        proc = BPMNGraph("p76", {s, t1, t2, t3, t4, t5, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7, f8, f9})
        return (proc, 60)

    def proc77(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r2"})
        t3 = Activity("t3","T3",40,{"r3"})
        t4 = Activity("t4","T4",40,{"r4"})
        t5 = Activity("t5","T5",20,{"r5"})
        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", g1, t3)
        f4 = Flow("f4", t1, t2, "strong")
        f5 = Flow("f5", t3, t4, "strong")
        f6 = Flow("f6", t2, g2)
        f7 = Flow("f7", t4, g2)
        f8 = Flow("f8", g2, t5)
        f9 = Flow("f9", t5, e)

        # BPMN graph
        proc = BPMNGraph("p77", {s, t1, t2, t3, t4, t5, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7, f8, f9})
        return (proc, 80)

    def proc78(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r1"})
        t3 = Activity("t3","T3",40,{"r3"})
        t4 = Activity("t4","T4",40,{"r4"})
        t5 = Activity("t5","T5",20,{"r5"})
        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", g1, t3)
        f4 = Flow("f4", t1, t2)
        f5 = Flow("f5", t3, t4)
        f6 = Flow("f6", t2, g2)
        f7 = Flow("f7", t4, g2, "strong")
        f8 = Flow("f8", g2, t5, "strong")
        f9 = Flow("f9", t5, e)

        # BPMN graph
        proc = BPMNGraph("p78", {s, t1, t2, t3, t4, t5, e, g1, g2}, {f1, f2, f3, f4, f5, f6, f7, f8, f9})
        return (proc, 60)

    def proc79(self):

        # nodes
        s = Start("s")
        t0 = Activity("t0","T0",20,{"r0"})
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r1"})
        t3 = Activity("t3","T3",20,{"r3"})
        t4 = Activity("t4","T4",20,{"r4"})
        t5 = Activity("t5","T5",20,{"r5"})
        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f0 = Flow("f0", s, t0)
        f1 = Flow("f1", t0, g1)
        f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", g1, t3)
        f4 = Flow("f4", t1, t2)
        f5 = Flow("f5", t3, t4, "strong")
        f6 = Flow("f6", t2, g2)
        f7 = Flow("f7", t4, g2)
        f8 = Flow("f8", g2, t5)
        f9 = Flow("f9", t5, e)

        # BPMN graph
        proc = BPMNGraph("p79", {s, t0, t1, t2, t3, t4, t5, e, g1, g2}, {f0, f1, f2, f3, f4, f5, f6, f7, f8, f9})
        return (proc, 40)

    def proc80(self):

        # nodes
        s = Start("s")
        t0 = Activity("t0","T0",60,{"r0"})
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r1"})
        t3 = Activity("t3","T3",20,{"r3"})
        t4 = Activity("t4","T4",20,{"r3"})
        t5 = Activity("t5","T5",20,{"r5"})
        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f0 = Flow("f0", s, t0)
        f1 = Flow("f1", t0, g1)
        f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", g1, t3)
        f4 = Flow("f4", t1, t2)
        f5 = Flow("f5", t3, t4)
        f6 = Flow("f6", t2, g2, "strong")
        f7 = Flow("f7", t4, g2, "strong")
        f8 = Flow("f8", g2, t5, "strong")
        f9 = Flow("f9", t5, e)

        # BPMN graph
        proc = BPMNGraph("p80", {s, t0, t1, t2, t3, t4, t5, e, g1, g2}, {f0, f1, f2, f3, f4, f5, f6, f7, f8, f9})
        return (proc, 60)

    def proc81(self):

        # nodes
        s = Start("s")
        t0 = Activity("t0","T0",60,{"r0"})
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r1"})
        t3 = Activity("t3","T3",20,{"r3"})
        t4 = Activity("t4","T4",20,{"r3"})
        t5 = Activity("t5","T5",60,{"r5"})
        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", g1, t3)
        f4 = Flow("f4", t1, t2)
        f5 = Flow("f5", t3, t4)
        f6 = Flow("f6", t2, g2, "strong")
        f7 = Flow("f7", t4, g2, "strong")
        f8 = Flow("f8", g2, t5, "strong")
        f9 = Flow("f9", t5, t0)
        f0 = Flow("f0", t0, e)

        # BPMN graph
        proc = BPMNGraph("p81", {s, t0, t1, t2, t3, t4, t5, e, g1, g2}, {f0, f1, f2, f3, f4, f5, f6, f7, f8, f9})
        return (proc, 100)

    def proc82(self):

        # nodes
        s = Start("s")
        t0 = Activity("t0","T0",60,{"r0"})
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r1"})
        t9 = Activity("t9","T9",40,{"r9"})
        t3 = Activity("t3","T3",20,{"r3"})
        t4 = Activity("t4","T4",20,{"r3"})
        t5 = Activity("t5","T5",60,{"r5"})
        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", g1, t3)
        f4 = Flow("f4", t1, t9)
        f44 = Flow("f44", t9, t2)
        f5 = Flow("f5", t3, t4)
        f6 = Flow("f6", t2, g2, "strong")
        f7 = Flow("f7", t4, g2, "strong")
        f8 = Flow("f8", g2, t5, "strong")
        f9 = Flow("f9", t5, t0)
        f0 = Flow("f0", t0, e)

        # BPMN graph
        proc = BPMNGraph("p82", {s, t0, t1, t2, t3, t4, t5, t9, e, g1, g2}, {f0, f1, f2, f3, f4, f44, f5, f6, f7, f8, f9})
        return (proc, 100)

    def proc83(self):

        # nodes
        s = Start("s")
        t0 = Activity("t0","T0",80,{"r0"})
        t1 = Activity("t1","T1",30,{"r1"})
        t2 = Activity("t2","T2",30,{"r1"})
        t9 = Activity("t9","T9",40,{"r9"})
        t3 = Activity("t3","T3",40,{"r3"})
        t4 = Activity("t4","T4",40,{"r4"})
        t5 = Activity("t5","T5",80,{"r5"})
        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f1 = Flow("f1", s, g1)
        f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", g1, t3)
        f4 = Flow("f4", t1, t9)
        f44 = Flow("f44", t9, t2, "strong")
        f5 = Flow("f5", t3, t4, "strong")
        f6 = Flow("f6", t2, g2)
        f7 = Flow("f7", t4, g2)
        f8 = Flow("f8", g2, t5)
        f9 = Flow("f9", t5, t0)
        f0 = Flow("f0", t0, e)

        # BPMN graph
        proc = BPMNGraph("p83", {s, t0, t1, t2, t3, t4, t5, t9, e, g1, g2}, {f0, f1, f2, f3, f4, f44, f5, f6, f7, f8, f9})
        return (proc, 120)

    def proc84(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"r1"})
        a2 = Activity("a2","A2",10,{"r2"})
        a3 = Activity("a3","A3",10,{"r3"})
        a4 = Activity("a4","A4",10,{"r4"})
        a5 = Activity("a5","A5",10,{"r5"})
        a6 = Activity("a6","A6",10,{"r6"})
        a7 = Activity("a7","A7",10,{"r7"})
        a8 = Activity("a8","A8",10,{"r8"})
        a9 = Activity("a9","A9",10,{"r9"})
        e = End("e")

        # flows
        f1 = Flow("f1", s, a1)
        f2 = Flow("f2", a1, a2)
        f3 = Flow("f3", a2, a3)
        f4 = Flow("f4", a3, a4)
        f5 = Flow("f5", a4, a5, "strong")
        f6 = Flow("f6", a5, a6)
        f7 = Flow("f7", a6, a7)
        f8 = Flow("f8", a7, a8)
        f9 = Flow("f9", a8, a9)
        f10 = Flow("f10", a9, e)

        # BPMN graph
        proc = BPMNGraph("p84", {s, a1, a2, a3, a4, a5, a6, a7, a8, a9, e}, {f1, f2, f3, f4, f5, f6, f7, f8, f9, f10})
        return (proc, 20)

    # realistic example (travel organization) with strong flows
    def proc85(self):

        # nodes
        s = Start("s")
        t0 = Activity("MissionPaperwork","MissionPaperwork",3,{"assistant"})
        t1 = Activity("FlightBooking","FlightBooking",3,{"travelagency"})
        t2 = Activity("HotelReservation","HotelReservation",2,{"agent"})
        t3 = Activity("Visa","Visa",10,{"visaoffice"})
        t4 = Activity("Vaccination","Vaccination",7,{"agent", "doctor"})
        t5 = Activity("ReturnDocuments","ReturnDocuments",3,{"agent"})
        t6 = Activity("Reimbursement","Reimbursement",15,{"financialstaff"})
        t7 = Activity("ArchiveDocs","ArchiveDocs",7,{"assistant"})
        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")

        # flows
        f0 = Flow("f0", s, t0)
        f1 = Flow("f1", t0, t1)
        f2 = Flow("f2", t1, t2)
        f3 = Flow("f3", t2, g1)
        f4 = Flow("f4", g1, t3)
        f5 = Flow("f5", g1, t4)
        f6 = Flow("f6", t3, g2, "strong")
        f7 = Flow("f7", t4, g2, "strong")
        f8 = Flow("f8", g2, t5, "strong")
        f9 = Flow("f9", t5, t6, "strong")
        f10 = Flow("f10", t6, t7)
        f11 = Flow("f11", t7, e)

        # BPMN graph
        proc = BPMNGraph("p85", {s, t0, t1, t2, t3, t4, t5, t6, t7, e, g1, g2}, {f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11})
        return (proc, 28)

    # example taken from FOCLASA 2018 (without loop)
    def proc86(self):

        # nodes
        s = Start("s")
        t1 = Activity("FillInForms","FillInForms",2,{"employee"})
        t2 = Activity("MedicalCheckUp","MedicalCheckUp",3,{"doctor", "employee"})
        t3 = Activity("Visa","Visa",10,{"visaofficer"})

        #t4 = Activity("Reject","Reject",1,{"HR"})
        t5 = Activity("Validate","Validate",1,{"HR"})
        t6 = Activity("PartialValidate","PartialValidate",1,{"HR"})
        t7 = Activity("CheckAddDocuments","CheckAddDocuments",2,{"HR"})

        t8 = Activity("UpdatePersonnelDB","UpdatePersonnelDB",1,{"TechnicalStaff"})

        t9 = Activity("AnticipateWages","AnticipateWages",2,{"HR"})
        t10 = Activity("PrepareWelcomeKit","PrepareWelcomeKit",3,{"Assistant"})
        t11 = Activity("ArchiveAllDocuments","ArchiveAllDocuments",1,{"HR"})

        e = End("e")
        #g1 = Join("g1", "exclusive")
        g2 = Split("g2", "exclusive")
        g3 = Join("g3", "exclusive")
        g4 = Split("g4", "exclusive")
        g5 = Join("g5", "exclusive")
        g6 = Split("g6", "parallel")
        g7 = Join("g7", "parallel")

        # flows
        f1 = Flow("f1", s, t2)
        #f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", t2, g2)
        f4 = Flow("f4", g2, g3)
        f5 = Flow("f5", g2, t3)
        f6 = Flow("f6", t3, g3)
        f7 = Flow("f7", g3, t1)
        f8 = Flow("f8", t1, g4, "strong")
        # f9 = Flow("f9", g4, t4)
        # f10 = Flow("f10", t4, e)
        f11 = Flow("f11", g4, t5, "strong")
        f12 = Flow("f12", g4, t6, "strong")
        f23 = Flow("f23", t6, t7)
        f13 = Flow("f13", t5, g5)
        f14 = Flow("f14", t7, g5)
        f15 = Flow("f15", g5, t8)
        f16 = Flow("f16", t8, g6)
        f17 = Flow("f17", g6, t9)
        f18 = Flow("f18", g6, t10)
        f19 = Flow("f19", t9, g7)
        f20 = Flow("f20", t10, g7)
        f21 = Flow("f21", g7, t11)
        f22 = Flow("f22", t11, e)

        # BPMN graph
        proc = BPMNGraph("p86", {s, t1, t2, t3, t5, t6, t7, t8, t9, t10, t11, e, g2, g3, g4, g5, g6, g7}, {f1, f3, f4, f5, f6, f7, f8, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23})
        return (proc, 12) # ??

    # example taken from FOCLASA 2018 (without loop)
    def proc87(self):

        # nodes
        s = Start("s")
        t1 = Activity("FillInForms","FillInForms",2,{"employee"})
        t2 = Activity("MedicalCheckUp","MedicalCheckUp",3,{"doctor", "employee"})
        t3 = Activity("Visa","Visa",10,{"visaofficer"})

        #t4 = Activity("Reject","Reject",1,{"HR"})
        t5 = Activity("Validate","Validate",1,{"HR"})
        #t6 = Activity("PartialValidate","PartialValidate",1,{"HR"})
        #t7 = Activity("CheckAddDocuments","CheckAddDocuments",2,{"HR"})

        t8 = Activity("UpdatePersonnelDB","UpdatePersonnelDB",1,{"TechnicalStaff"})

        t9 = Activity("AnticipateWages","AnticipateWages",2,{"HR"})
        t10 = Activity("PrepareWelcomeKit","PrepareWelcomeKit",3,{"Assistant"})
        t11 = Activity("ArchiveAllDocuments","ArchiveAllDocuments",1,{"HR"})

        e = End("e")
        #g1 = Join("g1", "exclusive")
        # g2 = Split("g2", "exclusive")
        # g3 = Join("g3", "exclusive")
        # g4 = Split("g4", "exclusive")
        # g5 = Join("g5", "exclusive")
        g6 = Split("g6", "parallel")
        g7 = Join("g7", "parallel")

        # flows
        f1 = Flow("f1", s, t2)
        #f2 = Flow("f2", g1, t1)
        f3 = Flow("f3", t2, t3)
        #f4 = Flow("f4", g2, g3)
        #f5 = Flow("f5", g2, t3)
        #f6 = Flow("f6", t3, g3)
        f7 = Flow("f7", t3, t1)
        f8 = Flow("f8", t1, t5, "strong")
        # f9 = Flow("f9", g4, t4)
        # f10 = Flow("f10", t4, e)
        f11 = Flow("f11", t5, t8, "strong")
        #f12 = Flow("f12", g4, t6, "strong")
        #f23 = Flow("f23", t6, t7)
        #f13 = Flow("f13", t5, g5)
        #f14 = Flow("f14", t7, g5)
        #f15 = Flow("f15", g5, t8)
        f16 = Flow("f16", t8, g6)
        f17 = Flow("f17", g6, t9)
        f18 = Flow("f18", g6, t10)
        f19 = Flow("f19", t9, g7)
        f20 = Flow("f20", t10, g7)
        f21 = Flow("f21", g7, t11)
        f22 = Flow("f22", t11, e)

        # BPMN graph
        proc = BPMNGraph("p87", {s, t1, t2, t3, t5, t8, t9, t10, t11, e, g6, g7}, {f1, f3, f7, f8, f11, f16, f17, f18, f19, f20, f21, f22})
        return (proc, 14)

    def proc88(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r2"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",20,{"r2"})
        t = Activity("t","T",100,{"r3"})
        t10 = Activity("t10","T10",20,{"r8"})
        t20 = Activity("t20","T20",20,{"r4"})
        t30 = Activity("t30","T30",20,{"r5"})
        t40 = Activity("t40","T40",20,{"r6"})
        t50 = Activity("t50","T50",50,{"r7"})

        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")
        g3 = Split("g3", "parallel")
        g4 = Join("g4", "parallel")

        # flows
        f0 = Flow("f0", s, g1)
        f1 = Flow("f1", g1, t1)
        f2 = Flow("f2", g1, t2)
        f3 = Flow("f3", t1, g2)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", g2, g3)
        f6 = Flow("f6", g3, t3)
        f7 = Flow("f7", g3, t)
        f8 = Flow("f8", g3, t4)
        f9 = Flow("f9", t3, g4)
        f10 = Flow("f10", t, g4)
        f11 = Flow("f11", t4, g4)
        f12 = Flow("f12", g4, e)

        f21 = Flow("f21", g1, t10)
        f22 = Flow("f22", t10, g2)
        f23 = Flow("f23", g1, t20)
        f24 = Flow("f24", t20, g2)
        f25 = Flow("f25", g1, t30)
        f26 = Flow("f26", t30, g2)
        f27 = Flow("f27", g1, t40)
        f28 = Flow("f28", t40, g2)
        f29 = Flow("f29", g1, t50)
        f30 = Flow("f30", t50, g2)

        # BPMN graph
        proc = BPMNGraph("p88", {s, t1, t2, t3, t4, t, t10, t20, t30, t40, t50, e, g1, g2, g3, g4}, {f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30})
        return (proc, 100)

    def proc89(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r2"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",20,{"r2"})
        t = Activity("t","T",100,{"r4"})
        t10 = Activity("t10","T10",40,{"r1"})
        t20 = Activity("t20","T20",40,{"r2"})
        t30 = Activity("t30","T30",20,{"r1"})
        t40 = Activity("t40","T40",20,{"r2"})
        t50 = Activity("t50","T50",20,{"r1"})

        t60 = Activity("t60","T60",20,{"r3"})
        t70 = Activity("t70","T70",20,{"r4"})


        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")
        g3 = Split("g3", "parallel")
        g4 = Join("g4", "parallel")

        g5 = Split("g5", "parallel")
        g6 = Join("g6", "parallel")
        g7 = Split("g7", "parallel")
        g8 = Join("g8", "parallel")


        # flows
        f0 = Flow("f0", s, g1)
        f1 = Flow("f1", g1, t1)
        f2 = Flow("f2", g1, t2)
        f3 = Flow("f3", t1, g2)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", g2, g3)
        f6 = Flow("f6", g3, t3)
        f7 = Flow("f7", g3, t)
        f8 = Flow("f8", g3, t4)
        f9 = Flow("f9", t3, g4)
        f10 = Flow("f10", t, g4)
        f11 = Flow("f11", t4, g4)
        f12 = Flow("f12", g8, e)
        f55 = Flow("f55", g4, g5)
        f56 = Flow("f56", g6, g7)

        f21 = Flow("f21", g5, t10)
        f22 = Flow("f22", t10, g6)
        f23 = Flow("f23", g5, t20)
        f24 = Flow("f24", t20, g6)
        f25 = Flow("f25", g7, t30)
        f26 = Flow("f26", t30, g8)
        f27 = Flow("f27", g7, t40)
        f28 = Flow("f28", t40, g8)
        f29 = Flow("f29", g7, t50)
        f30 = Flow("f30", t50, g8)

        f31 = Flow("f31", g1, t60)
        f32 = Flow("f32", t60, g2)
        f33 = Flow("f33", g1, t70)
        f34 = Flow("f34", t70, g2)

        # BPMN graph
        proc = BPMNGraph("p89", {s, t1, t2, t3, t4, t, t10, t20, t30, t40, t50, t60, t70, e, g1, g2, g3, g4, g5, g6, g7, g8}, {f55, f56, f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34})
        return (proc, 120)


    def proc90(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r2"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",40,{"r2"})
        t = Activity("t","T",20,{"r1"})
        t10 = Activity("t10","T10",40,{"r1"})
        t20 = Activity("t20","T20",40,{"r2"})
        t30 = Activity("t30","T30",20,{"r1"})
        t40 = Activity("t40","T40",20,{"r2"})
        t50 = Activity("t50","T50",20,{"r1"})

        t60 = Activity("t60","T60",20,{"r1"})
        t70 = Activity("t70","T70",20,{"r2"})

        t80 = Activity("t80","T80",100,{"r3"})
        t90 = Activity("t90","T90",20,{"r1"})
        t100 = Activity("t100","T100",20,{"r2"})



        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")
        g3 = Split("g3", "parallel")
        g4 = Join("g4", "parallel")

        g5 = Split("g5", "parallel")
        g6 = Join("g6", "parallel")
        g7 = Split("g7", "parallel")
        g8 = Join("g8", "parallel")

        g9 = Split("g9", "parallel")
        g10 = Join("g10", "parallel")


        # flows
        f0 = Flow("f0", s, g1)
        f1 = Flow("f1", g1, t1)
        f2 = Flow("f2", g1, t2)
        f3 = Flow("f3", t1, g2)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", g2, g3)
        f6 = Flow("f6", g3, t3)
        f7 = Flow("f7", g3, t)
        f8 = Flow("f8", g3, t4)
        f9 = Flow("f9", t3, g4)
        f10 = Flow("f10", t, g4)
        f11 = Flow("f11", t4, g4)
        f12 = Flow("f12", g10, e)
        f55 = Flow("f55", g4, g5)
        f56 = Flow("f56", g6, g7)

        f21 = Flow("f21", g5, t10)
        f22 = Flow("f22", t10, g6)
        f23 = Flow("f23", g5, t20)
        f24 = Flow("f24", t20, g6)
        f25 = Flow("f25", g7, t30)
        f26 = Flow("f26", t30, g8)
        f27 = Flow("f27", g7, t40)
        f28 = Flow("f28", t40, g8)
        f29 = Flow("f29", g7, t50)
        f30 = Flow("f30", t50, g8)

        f31 = Flow("f31", g1, t60)
        f32 = Flow("f32", t60, g2)
        f33 = Flow("f33", g1, t70)
        f34 = Flow("f34", t70, g2)

        f41 = Flow("f41", g9, t80)
        f42 = Flow("f42", t80, g10)
        f43 = Flow("f43", g9, t90)
        f44 = Flow("f44", t90, g10)
        f45 = Flow("f45", g9, t100)
        f46 = Flow("f46", t100, g10)
        f47 = Flow("f47", g8, g9)

        # BPMN graph
        proc = BPMNGraph("p90", {s, t1, t2, t3, t4, t, t10, t20, t30, t40, t50, t60, t70, t80, t90, t100, e, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10}, {f55, f56, f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34, f41, f42, f43, f44, f45, f46, f47})
        return (proc, 180)



    def proc91(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r2"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",40,{"r2"})
        t = Activity("t","T",20,{"r1"})
        t10 = Activity("t10","T10",40,{"r1"})
        t20 = Activity("t20","T20",40,{"r2"})
        t30 = Activity("t30","T30",20,{"r1"})
        t40 = Activity("t40","T40",20,{"r2"})
        t50 = Activity("t50","T50",20,{"r1"})

        t60 = Activity("t60","T60",20,{"r1"})
        t70 = Activity("t70","T70",20,{"r2"})

        t80 = Activity("t80","T80",100,{"r3"})
        t90 = Activity("t90","T90",100,{"r4"})
        t100 = Activity("t100","T100",20,{"r2"})



        e = End("e")
        g1 = Split("g1", "parallel")
        g2 = Join("g2", "parallel")
        g3 = Split("g3", "parallel")
        g4 = Join("g4", "parallel")

        g5 = Split("g5", "parallel")
        g6 = Join("g6", "parallel")
        g7 = Split("g7", "parallel")
        g8 = Join("g8", "parallel")

        g9 = Split("g9", "parallel")
        g10 = Join("g10", "parallel")


        # flows
        f0 = Flow("f0", s, g1)
        f1 = Flow("f1", g1, t1)
        f2 = Flow("f2", g1, t2)
        f3 = Flow("f3", t1, g2)
        f4 = Flow("f4", t2, g2)
        f5 = Flow("f5", g2, g3)
        f6 = Flow("f6", g3, t3)
        f7 = Flow("f7", g3, t)
        f8 = Flow("f8", g3, t4)
        f9 = Flow("f9", t3, g4)
        f10 = Flow("f10", t, g4)
        f11 = Flow("f11", t4, g4)
        f12 = Flow("f12", g10, e)
        f55 = Flow("f55", g4, g5)
        f56 = Flow("f56", g6, g7)

        f21 = Flow("f21", g5, t10)
        f22 = Flow("f22", t10, g6)
        f23 = Flow("f23", g5, t20)
        f24 = Flow("f24", t20, g6)
        f25 = Flow("f25", g7, t30)
        f26 = Flow("f26", t30, g8)
        f27 = Flow("f27", g7, t40)
        f28 = Flow("f28", t40, g8)
        f29 = Flow("f29", g7, t50)
        f30 = Flow("f30", t50, g8)

        f31 = Flow("f31", g1, t60)
        f32 = Flow("f32", t60, g2)
        f33 = Flow("f33", g1, t70)
        f34 = Flow("f34", t70, g2)

        f41 = Flow("f41", g9, t80)
        f42 = Flow("f42", t80, g10)
        f43 = Flow("f43", g9, t90)
        f44 = Flow("f44", t90, g10)
        f45 = Flow("f45", g9, t100)
        f46 = Flow("f46", t100, g10)
        f47 = Flow("f47", g8, g9)

        # BPMN graph
        proc = BPMNGraph("p91", {s, t1, t2, t3, t4, t, t10, t20, t30, t40, t50, t60, t70, t80, t90, t100, e, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10}, {f55, f56, f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34, f41, f42, f43, f44, f45, f46, f47})
        return (proc, 180)

    def proc92(self):

        # nodes
        s = Start("s")
        a1 = Activity("a1","A1",10,{"r1"})
        a2 = Activity("a2","A2",10,{"r2"})
        a3 = Activity("a3","A3",10,{"r2"})
        e = End("e")

        # flows
        f1 = Flow("f1", s, a1)
        f2 = Flow("f2", a1, a2)
        f3 = Flow("f3", a2, a3)
        f4 = Flow("f4", a3, e)

        # BPMN graph
        proc = BPMNGraph("p92", {s, a1, a2, a3, e}, {f1, f2, f3, f4})
        return (proc, 20)

    def proc93(self):

        # nodes
        s = Start("s")
        t1 = Activity("t1","T1",20,{"r1"})
        t2 = Activity("t2","T2",20,{"r2"})
        t3 = Activity("t3","T3",20,{"r1"})
        t4 = Activity("t4","T4",20,{"r2"})
        t5 = Activity("t5","T5",20,{"r2"})
        t6 = Activity("t6","T6",20,{"r2"})
        t7 = Activity("t7","T7",20,{"r1"})

        e = End("e")
        g1 = Split("g1", "exclusive")
        g2 = Split("g2", "exclusive")
        g5 = Split("g5", "exclusive")
        g6 = Join("g6", "exclusive")
        g3 = Join("g3", "exclusive")
        g4 = Join("g4", "exclusive")

        # flows
        f1 = Flow("f1", s, t6)
        f111 = Flow("f111", t6, g1)
        f2 = Flow("f2", g1, g2)
        f3 = Flow("f3", g2, t1)
        f4 = Flow("f4", g2, g5)
        f5 = Flow("f5", t1, t7)
        f555 = Flow("f555", t7, g3)
        f6 = Flow("f6", g6, g3)
        f7 = Flow("f7", g3, g4)
        f8 = Flow("f8", g1, t3)
        f9 = Flow("f9", t3, t4)
        f10 = Flow("f10", t4, g4)
        f11 = Flow("f11", g4, e)

        f21 = Flow("f21", g5, t2)
        f22 = Flow("f22", t2, g6)
        f23 = Flow("f23", g5, t5)
        f24 = Flow("f24", t5, g6)

        # BPMN graph
        proc = BPMNGraph("p93", {s, t1, t2, t3, t4, t5, t6, t7, e, g1, g2, g3, g4, g5, g6}, {f555, f111, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f21, f22, f23, f24})
        return (proc, 25)



    def getAllProcesses(self):
        allp=[]

        p1=self.proc1()
        allp.append(p1)
        p2=self.proc2()
        allp.append(p2)
        p3=self.proc3()
        allp.append(p3)
        p4=self.proc4()
        allp.append(p4)
        p5=self.proc5()
        allp.append(p5)
        p6=self.proc6()
        allp.append(p6)
        p7=self.proc7()
        allp.append(p7)
        p8=self.proc8()
        allp.append(p8)
        p9=self.proc9()
        allp.append(p9)
        p10=self.proc10()
        allp.append(p10)

        p11=self.proc11()
        allp.append(p11)
        p12=self.proc12()
        allp.append(p12)
        p13=self.proc13()
        allp.append(p13)
        p14=self.proc14()
        allp.append(p14)
        p15=self.proc15()
        allp.append(p15)
        p16=self.proc16()
        allp.append(p16)
        p17=self.proc17()
        allp.append(p17)
        p18=self.proc18()
        allp.append(p18)
        p19=self.proc19()
        allp.append(p19)
        p20=self.proc20()
        allp.append(p20)

        p21=self.proc21()
        allp.append(p21)
        p22=self.proc22()
        allp.append(p22)
        p23=self.proc23()
        allp.append(p23)
        p24=self.proc24()
        allp.append(p24)
        p25=self.proc25()
        allp.append(p25)
        p26=self.proc26()
        allp.append(p26)
        p27=self.proc27()
        allp.append(p27)
        p28=self.proc28()
        allp.append(p28)
        p29=self.proc29()
        allp.append(p29)
        p30=self.proc30()
        allp.append(p30)

        p31=self.proc31()
        allp.append(p31)
        p32=self.proc32()
        allp.append(p32)
        p33=self.proc33()
        allp.append(p33)
        p34=self.proc34()
        allp.append(p34)
        p35=self.proc35()
        allp.append(p35)
        p36=self.proc36()
        allp.append(p36)
        p37=self.proc37()
        allp.append(p37)
        p38=self.proc38()
        allp.append(p38)
        p39=self.proc39()
        allp.append(p39)
        p40=self.proc40()
        allp.append(p40)
        p41=self.proc41()
        allp.append(p41)
        p42=self.proc42()
        allp.append(p42)
        p43=self.proc43()
        allp.append(p43)
        p44=self.proc44()
        allp.append(p44)
        p45=self.proc45()
        allp.append(p45)
        p46=self.proc46()
        allp.append(p46)
        p47=self.proc47()
        allp.append(p47)
        p48=self.proc48()
        allp.append(p48)
        p49=self.proc49()
        allp.append(p49)
        p50=self.proc50()
        allp.append(p50)
        p51=self.proc51()
        allp.append(p51)
        p52=self.proc52()
        allp.append(p52)
        p53=self.proc53()
        allp.append(p53)
        p54=self.proc54()
        allp.append(p54)
        p55=self.proc55()
        allp.append(p55)
        p56=self.proc56()
        allp.append(p56)
        p57=self.proc57()
        allp.append(p57)
        p58=self.proc58()
        allp.append(p58)
        p59=self.proc59()
        allp.append(p59)
        p60=self.proc60()
        allp.append(p60)
        p61=self.proc61()
        allp.append(p61)
        p62=self.proc62()
        allp.append(p62)
        p63=self.proc63()
        allp.append(p63)
        p64=self.proc64()
        allp.append(p64)
        p65=self.proc65()
        allp.append(p65)
        p66=self.proc66()
        allp.append(p66)
        p67=self.proc67()
        allp.append(p67)
        p68=self.proc68()  # not the optimal solution for this ex.
        allp.append(p68)
        p69=self.proc69()
        allp.append(p69)
        p70=self.proc70()
        allp.append(p70)
        p71=self.proc71()
        allp.append(p71)
        p72=self.proc72()
        allp.append(p72)
        p73=self.proc73()
        allp.append(p73)
        p74=self.proc74()
        allp.append(p74)
        p75=self.proc75()
        allp.append(p75)
        p76=self.proc76()
        allp.append(p76)
        p77=self.proc77()
        allp.append(p77)
        p78=self.proc78()
        allp.append(p78)
        p79=self.proc79()
        allp.append(p79)
        p80=self.proc80()
        allp.append(p80)
        p81=self.proc81()
        allp.append(p81)
        p82=self.proc82()
        allp.append(p82)
        p83=self.proc83()
        allp.append(p83)
        p84=self.proc84()
        allp.append(p84)
        p85=self.proc85()
        allp.append(p85)
        p86=self.proc86()
        allp.append(p86)
        p87=self.proc87()
        allp.append(p87)
        p88=self.proc88()
        allp.append(p88)
        p89=self.proc89()
        allp.append(p89)
        p90=self.proc90()
        allp.append(p90)
        p91=self.proc91()
        allp.append(p91)
        p92=self.proc92()
        allp.append(p92)

        return allp
