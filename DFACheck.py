class DFA:
    currentState = None;

    def __init__(self, states, alphabet, transition, startstate, finalstate, verbose):
        self.states = states;
        self.alphabet = alphabet;
        self.transition = transition;
        self.startstate = startstate;
        self.finalstate = finalstate;
        self.currentState = startstate;
        self.verbose = verbose;
        return;

    def transitionTo(self, inputValue):
        thisTransition = (self.currentState, inputValue);
        transitions = self.transition.keys();
        if (thisTransition not in transitions):
            self.currentState = None;
            print "Invalid state transition";
            exit(1);
        else:
            newState = self.transition[thisTransition];
            if self.verbose:
                print "Current State: " + self.currentState + " -> New State: " + newState;
            self.currentState = newState;
        return;

    def inAcceptedState(self):
        isValidEndState = self.currentState in self.finalstate;
        return 'ACCEPT' if isValidEndState else 'NOT ACCEPT';

    def start(self):
        self.currentState = self.startstate;
        return;

    def runWithInput(self, inputList):
        self.start();
        for step in inputList:
            self.transitionTo(step);
            continue;
        return self.inAcceptedState();
    pass;
