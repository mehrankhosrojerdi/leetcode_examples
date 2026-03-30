import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.primitives import StatevectorEstimator as Estimator
from qiskit.circuit import Parameter
from qiskit_algorithms.optimizers import SPSA
from qiskit.quantum_info import Pauli

# make dataset
X = np.linspace(0,np.pi, 5)
Y = np.sin(x)

# make a trainable variable
theta = Parameter('t') 

# build parametrized circuit
def creat_circuit(x_value):
  qc = QuantumCircuit(1)
  qc.ry(x_value, 0) # angle encoding 
  qc.ry(theta, 0) # weight
  return qc

# loss Function
estimator = Estimator() # <psi|o|psi>


def cost_finction(theta_value):
    total_loss = 0
    for x, y in zip(X, Y):
        qc = creat_circuit(x)
        bound_qc = qc.assign_parameters({theta: theta_value})
        observable = Pauli("Z")
        result = estimator.run([(bound_qc, observable)]).result()
        expectation = result[0].data.evs
        total_loss += (expectation - y) ** 2
    return total_loss  

# train block
optimizer = SPSA(maxiter=50) #simultaneous perturbation stochastic approximation

initial_theta = np.random.random() #random value for theta
result = optimizer.minimize(
    fun = cost_finction,
    x0=np.array([initial_theta])
)

print('optimal theta:', result.x)