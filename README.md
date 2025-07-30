# DA-MaxCut-Benchmark

This repository contains the dataset and code for our paper:

### **"A Comprehensive Benchmark of an Ising Machine on the Max-Cut Problem"**

**Authors:**  
Salwa Shaglel, Markus Kirsch, Marten Winkler, Christian Münch, Stefan Walter, Fritz Schinkel, Martin Kliesch  
**Published:** 2025  
**[arXiv Link](https://arxiv.org/6660338/)**

@misc{SalwaDAMB2025,
  author    = {Salwa Shaglel, Markus Kirsch, Marten Winkler, Christian Münch, Stefan Walter, Fritz Schinkel, Martin Kliesch},
  title     = {A Comprehensive Benchmark of an Ising Machine on the Max-Cut Problem},
  year      = {2025},
  archivePrefix = {arXiv},
  eprint={},
  primaryClass={quant-ph},
  url={}}

---

## Benchmarks Overview

This repository includes data and results from our benchmarking of Digital Annealer versions (DAv2 and DAv3) against various heuristics on the Max-Cut problem.

### File Formats

- **CSV files**: In general, contain instance specifications, obtained cut values, baseline time limits, and corresponding bitstring solutions. For the DA, it also contains its parameters and a breakdown of DA time components (including total duration).
- **JSON files**: Record the progress of DAv3 solutions over time.
- **TXT files**: Store terminal run outputs.

---

##  DA vs. [MQLib Heuristics](https://github.com/MQLib/MQLib)

- **Instances:** 3,506 MQLib Max-Cut problem instances (as of 2025)
- **Runs per instance:** 5
- **Time-limit:** Instance-specific time limits available in **BASELINE** directory, determined by a local search algorithm (5 runs per instance).
- **Included methods:**
  - **DAv2:** 5 runs per instance for 3,319 instances
  - **DAv3:** 5 runs per instance for all 3,400 instances  
    Includes multiple 5-run batches per instance with different time limit offsets from 0 (no offset) to 5 seconds
    **Total:** ~17,331 files (CSV, TXT, JSON)
  - ** MQLib heuristics:** 5 runs per instance on a large subset of the 3,506 instances: MERZ1999GLS, PALUBECKIS2004bMST2, and BURER2002
 

    -**NOTE:** We removed the disconnected vertices and fixed a vertex to one side of the cut. Therefore, the number of vertices of instances may differ by 1 vertex or a bit more than those provided in MQLib.
    -**NOTE:** For instances with float weights, it is encouraged to calculate the obtained objective value from the available bit string solution to avoid rounding issues.

---

## DAv3 vs. [D-Wave Hybrid Solver (HS) ](https://www.dwavequantum.com/resources/white-paper/d-wave-hybrid-solver-service-an-overview/)

- **Instances:** 45 selected by D-Wave
- **DAv3 runs:** 5 runs per instance
- **Time limit:** 20 minutes
- **Files per instance:** CSV, TXT, and JSON

---

## DAv2 and DAv3 vs. [QIS3](https://arxiv.org/abs/2506.04596)

- **Instances:** Selection from [The G-set](https://web.stanford.edu/~yyye/yyye/Gset/)
- **Runs:**
  - **DAv2:**  
    - 14 instances  
    - 5 runs per instance  
    - 10 time configurations per instance (1s to 10s)  
    - Output: CSV and TXT files
  - **DAv3:**  
    - 16 instances  
    - 5 runs per instance  
    - 10 time configurations per instance (1s to 10s)  
    - Output: CSV, TXT, and JSON files

---

Contact the first author of the paper if you need help navigating the dataset or reproducing the results, or if you find any issues.

