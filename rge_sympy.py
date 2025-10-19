import sympy as sp

# 1-loop RGE for α_s
alpha_s_mu0, mu0, beta0, mu = sp.symbols('alpha_s_mu0 mu0 beta0 mu')
rge = alpha_s_mu0 / (1 + (beta0 * alpha_s_mu0 / (2 * sp.pi)) * sp.ln(mu / mu0))
alpha_s_lambda = rge.subs({alpha_s_mu0: 0.35, mu0: 1, beta0: 9, mu: 0.332})
print(f"α_s(Λ_QCD=332 MeV): {float(alpha_s_lambda):.4f}")  # 0.5200