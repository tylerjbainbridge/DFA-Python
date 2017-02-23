## Usage examples

```bash
> python dfa.py -d m1.dfa 10100
10100 ----> NOT ACCEPT
```

```bash
> python dfa.py -d m1.json 10100
10100 ----> NOT ACCEPT
```


```bash
> python dfa.py -d m1.json < m1.in
10100 ----> NOT ACCEPT
```

```bash
> python dfa.py -d m1.dfa < m1.in
010101 ----> ACCEPT
0101010 ----> ACCEPT
0000 ----> NOT ACCEPT
1010101 ----> ACCEPT
```

```bash
> python dfa.py -d m1.dfa < m1.in > m1.out
```

```bash
> python dfa.py -d m1.dfa < m1.in -v

---­­­BEGIN DFA definition­­­---
{ 'alphabet': ['0', '1'],
  'finalstate': 'q3',
  'startstate': 'q0',
  'states': ['q0', 'q1', 'q2', 'q3'],
  'transition': { ('q0', '0'): 'q0',
                  ('q0', '1'): 'q1',
                  ('q1', '0'): 'q1',
                  ('q1', '1'): 'q2',
                  ('q2', '0'): 'q2',
                  ('q2', '1'): 'q3',
                  ('q3', '0'): 'q3',
                  ('q3', '1'): 'q3'}}
---END DFA definition­­­---

Current State: q0 -> New State: q0
Current State: q0 -> New State: q1
Current State: q1 -> New State: q1
Current State: q1 -> New State: q2
Current State: q2 -> New State: q2
Current State: q2 -> New State: q3
010101 ----> ACCEPT
Current State: q0 -> New State: q0
Current State: q0 -> New State: q1
Current State: q1 -> New State: q1
Current State: q1 -> New State: q2
Current State: q2 -> New State: q2
Current State: q2 -> New State: q3
Current State: q3 -> New State: q3
0101010 ----> ACCEPT
Current State: q0 -> New State: q0
Current State: q0 -> New State: q0
Current State: q0 -> New State: q0
Current State: q0 -> New State: q0
0000 ----> NOT ACCEPT
Current State: q0 -> New State: q1
Current State: q1 -> New State: q1
Current State: q1 -> New State: q2
Current State: q2 -> New State: q2
Current State: q2 -> New State: q3
Current State: q3 -> New State: q3
Current State: q3 -> New State: q3
1010101 ----> ACCEPT
```

```bash
> python dfa.py -d m1.dfa -interactive
interactive mode
type exit to leave

> 100101
100101 ----> ACCEPT
> 10000111100
10000111100 ----> ACCEPT
> 10000
10000 ----> NOT ACCEPT
>
```

```bash
python dfa.py -d m1.dfa -i m1.in
010101 ----> ACCEPT
0101010 ----> ACCEPT
0000 ----> NOT ACCEPT
1010101 ----> ACCEPT
```