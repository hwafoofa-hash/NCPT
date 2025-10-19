# NCPT Hadron Derivation: Γ_h Origin

## Overview
Zero-parameter derivation of hadron enhancement Γ_h ≈ 1.86 × 10^6 via QCD scale separation and field-theory corrections. Integrates with NCPT triad (h-c coupling, ρ_empty, velocity weave).

## Setup
- Python 3.12+
- Dependencies: numpy, sympy, scipy (pip install)

## Run
python gamma_h_numeric.py  # Numerical Γ_h computation
python rge_sympy.py  # Symbolic RGE

## Results
- Γ_h = 1.8602 × 10^6 (error 0.17% vs PDG target)
- Convergence with Math Path A: <0.1%

## Figures
Run `plot_convergence.py` for α_s running and A/B plot (Matplotlib output).