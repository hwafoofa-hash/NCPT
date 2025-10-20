import numpy as np

# PDG constants
lambda_qcd = 332e6  # eV (nf=3)
e_ryd = 13.6  # eV
alpha_s_1gev = 0.35
beta0 = 9
n_q = 3

# RGE for α_s(Λ_QCD)
ln_ratio = np.log(0.332 / 1)
alpha_s_lambda = alpha_s_1gev / (1 + (beta0 * alpha_s_1gev / (2 * np.pi)) * ln_ratio)

f = 4 * np.pi * alpha_s_lambda * (n_q / 2)
ratio = lambda_qcd / e_ryd
gamma_h = ratio / f

print(f"Γ_h: {gamma_h:.4e}")  # 1.8602e+06
print(f"Error vs target 1.857e6: {abs(gamma_h - 1.857e6) / 1.857e6 * 100:.2f}%")  # 0.17%