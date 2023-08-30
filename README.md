# SSVQE
This repo contains an implementation of the SSVQE algorithm (see https://arxiv.org/abs/1810.09434) in Qiskit. SSVQE is a generalization of VQE which takes a set of mutually orthogonal states, applies the same parameterized ansatz circuit to all of them, then minimizes a weighted sum of the expectation values of the operator with respect to these states. Because inner products of states are invariant under unitary transformations, the set of states remains orthogonal under ideal conditions and thus the global minimum corresponds to the low-lying eigenstates. This implementation may be installed by cloning the repo and installing with pip. Here is a simple example of how one may use this implementation:

```
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.primitives import Estimator
from qiskit.circuit.library import RealAmplitudes
from qiskit.algorithms.optimizers import SPSA
from qiskit.algorithms.eigensolvers import SSVQE

operator = SparsePauliOp(['ZZ'])
input_states = [QuantumCircuit(2), QuantumCircuit(2)]
input_states[0].x(0)
input_states[1].x(1)

ssvqe_instance = SSVQE(k=2,
                            estimator=Estimator(),
                            optimizer=SPSA(),
                            ansatz=RealAmplitudes(2),
                            initial_states=input_states)

result = ssvqe_instance.compute_eigenvalues(operator)
```

This will find the lowest eigenvalues of the `ZZ` operator and the resulting optimized parameters will encode the corresponding eigenstates.


