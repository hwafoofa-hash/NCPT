import numpy as np

# Constants (PDG 2024)
lambda_qcd = 213  # MeV
e_ryd = 13.6 / 1e6  # MeV
ratio = lambda_qcd / e_ryd
print(f"Ratio: {ratio:.2e}")

# Alpha_s running (1-loop)
alpha_s_1gev = 0.3
b = 9  # n_f=3
mu0 = 1  # GeV
mu = lambda_qcd /1000  # GeV
ln_ratio = np.log(mu / mu0)
alpha_s_mu = alpha_s_1gev / (1 + (b * alpha_s_1gev / (2 * np.pi)) * ln_ratio)
print(f"Alpha_s at Λ_QCD: {alpha_s_mu:.4f}")

n_q = 3
four_pi = 4 * np.pi
f = four_pi * alpha_s_mu * (n_q / 2)
gamma_h_base = ratio / f
print(f"Base Γ_h: {gamma_h_base:.2e}")

# Chiral vacuum scale χ_v ≈ 2.0 (m_π / Λ_QCD inverse approx)
chi_v = 2.0  # (140/213)^-2 ≈ 2.06, approx 2.0
gamma_h = gamma_h_base * chi_v
print(f"Final Γ_h: {gamma_h:.2e}")

# Verification: Neutron μ_n = Γ_h * S0 / m_n^2, S0=0.001, m_n=939 MeV
s0 = 0.001
m_n = 939
mu_n = gamma_h * s0 / m_n**2
print(f"μ_n prediction: {mu_n:.4f} μ_N (exp 1.913)")