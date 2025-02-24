import numpy as np
import ctrl   # NEED TO INSTALL IF NOT AVAILABLE USING PIP INSTALL 

# MAKE A NOTE THAT SYSTEMS ARE FIRST ORDER AND VARY AS PER REQUIREMENT
systems = {
    "G1(s)": ([1], [1, 0.1]),
    "G2(s)": ([1], [1, 1]),
    "G3(s)": ([1], [1, 10]),
    "G4(s)": ([1], [1, -1]),
    "G5(s)": ([1], [1, 0]),
    "G6(s)": ([10], [1, 1]),
}

poles_list = []

for label, (num, den) in systems.items():
    system = ctrl.TransferFunction(num, den)
    
    poles = np.roots(den)
    poles_list.extend(poles)
    pole = poles[0]
    
    if pole != 0:
        tau = -1 / pole
        settling_time = 5 * tau
        steady_state_response = num[0] / den[-1]
        stability = "Stable" if pole < 0 else "Unstable"
    else:
        tau = np.inf
        settling_time = np.inf
        steady_state_response = np.inf
        stability = "Marginally Stable"
    
    print(f"{label}:")
    print(f"  Pole: {pole}")
    print(f"  Time Constant (τ): {tau}")
    print(f"  Settling Time (Ts): {settling_time}")
    print(f"  Steady-State Response: {steady_state_response}")
    print(f"  Stability: {stability}\n")
