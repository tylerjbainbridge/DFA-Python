import json;
from DFAClass import DFA;
from Parser import Parser;

def runDFA(dfaFileName, inputFileName, stdInInputs, verbose, interactive):
    parser = Parser(dfaFileName, verbose);
    machineDefinition = parser.getDefinition();

    dfa = DFA(
        machineDefinition["states"],
        machineDefinition["alphabet"],
        machineDefinition["transition"],
        machineDefinition["startstate"],
        machineDefinition["finalstate"],
        verbose
    );

    if inputFileName != None:
        inputFile = open(inputFileName, "r").read();
        for inputString in inputFile.splitlines():
            sanitizedInput = inputString.strip();
            print sanitizedInput + ' ----> ' + dfa.runWithInput(list(sanitizedInput));

    elif interactive:
        print "interactive mode";
        print "type exit to leave\n";
        while True:
            inputString = raw_input("> ");
            if inputString == "exit":
                break;
            else:
                print inputString + ' ----> ' + dfa.runWithInput(list(inputString));

    elif stdInInputs != None:
        for inputString in stdInInputs:
            sanitizedInput = inputString.strip();
            print sanitizedInput + ' ----> ' + dfa.runWithInput(list(sanitizedInput));
