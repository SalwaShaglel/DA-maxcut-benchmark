# DA-MaxCut-Benchmark

This repository contains the dataset and code for our paper:

### **"A Comprehensive Benchmark of an Ising Machine on the Max-Cut Problem"**

**Authors:**  
Salwa Shaglel, Markus Kirsch, Marten Winkler, Christian Münch, Stefan Walter, Fritz Schinkel, Martin Kliesch  
**Published:** 2025  
**[arXiv Link](https://arxiv.org/abs/00000000000)** [CITE]

---

## Benchmarks Overview

This repository includes data and results from our benchmarking of Digital Annealer versions (DAv2 and DAv3) against various heuristics on the Max-Cut problem.

### File Formats

- **CSV files**: In general contain instance specifications, obtained cut values, baseline time limits, corresponding bitstring solutions. For the DA also contain it parameters and a breakdown of DA time components (including total duration).
- **JSON files**: Record the progress of DAv3 solutions over time.
- **TXT files**: Store terminal run outputs.

---

##  DAv3 and Comparison with MQLib Heuristics [CITE]

- **Instances:** 3,506 MQLib Max-Cut problem instances
- **Runs per instance:** 5
- **Included methods:**
  - **DAv2:** 5 runs per instance for 3,319 instances
  - **DAv3:** 5 runs per instance for all 3,400 instances  
    Includes multiple 5-run batches per instance with different time limit offsets
    **Total:** ~25,781 files (CSV, TXT, JSON)
  - **38 MQLib heuristics:** 5 runs per instance on a large subset of the 3,400 instances

---

## DAv3 vs. D-Wave Hybrid Solver (HS) [CITE]

- **Instances:** 45 selected by D-Wave
- **DAv3 runs:** 5 runs per instance
- **Files per instance:** CSV, TXT, and JSON

---

## DAv2 and DAv3 vs. QIS3 [CITE]

- **Instances:** Selected from the G-set
- **Runs:**
  - **DAv2:**  
    - 14 instances  
    - 5 runs per instance  
    - 10 time configurations per run (1s to 10s)  
    - Output: CSV and TXT files
  - **DAv3:**  
    - 16 instances  
    - 5 runs per instance  
    - 10 time configurations per run (1s to 10s)  
    - Output: CSV, TXT, and JSON files

---

Let us know if you need help navigating the dataset or reproducing results.

