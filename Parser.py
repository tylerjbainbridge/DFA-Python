# -*- coding: utf-8 -*-
import pprint;
import json;

pp = pprint.PrettyPrinter(indent=2);

class Parser:
    def __init__(self, fileName, verbose):
        self.fileName = fileName;
        self.fileContents = None;
        self.machineDefinition = {
            "states": [],
            "alphabet": [],
            "startstate": [],
            "finalstate": [],
            "transition": {}
        };
        self.verbose = verbose;
        return;

    def getFileContents(self):
        return self.fileContents;

    def getDefinition(self):
        try:
            self.fileContents = open(self.fileName, "r").read();
        except:
            print "File doesn't exist.";

        if self.fileName.find("json") > 0:
            self.parseJson();
        elif self.fileName.find("dfa") > 0:
            self.parseDFA();
        else:
            print "Invalid input file type";
            exit(1);

        return self.machineDefinition;

    def parseJson(self):
        fileContentsInJson = json.loads(self.fileContents);
        for k, v in fileContentsInJson.items():
            if k == "transition":
                for trans in v:
                    transition = list(trans.split(" "));
                    (state1, alpha, state2) = map(str, transition);
                    self.machineDefinition[k][(state1, alpha)] = state2;
            elif k == "startstate" or k == "finalstate":
                self.machineDefinition[k] = str(v);
            else:
                try:
                    self.machineDefinition[k] = list(map(str, v));
                except:
                    print "Incorrect formatting in DFA file";
        if self.verbose:
            print "---­­­BEGIN DFA definition­­­---"
            pp.pprint(self.machineDefinition);
            print "---END DFA definition­­­---"
        return;

    def parseDFA(self):
        for line in self.fileContents.splitlines():
            (k, v) = line.split(': ');
            if k == "transition":
                transition = list(v.split(" "));
                (state1, alpha, state2) = transition;
                self.machineDefinition[k][(state1, alpha)] = state2;
            elif k == "startstate" or k == "finalstate":
                self.machineDefinition[k] = str(v);
            else:
                try:
                    self.machineDefinition[k] = list(v.split(" "));
                except:
                    print "Incorrect formatting in DFA file";
        if self.verbose:
            print "\n---­­­BEGIN DFA definition­­­---"
            pp.pprint(self.machineDefinition);
            print "---END DFA definition­­­---\n"
        return;
