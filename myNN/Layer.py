import numpy as np
from utils import activations


class NNLayer:
    def __init__(self, no_input, no_output):
        self._w = np.random.rand(no_output, no_input)
        self._b = np.random.rand(no_output, 1)

    def forward_prop(self, input, af):
        self._lastInput = input

        sum = self._w.dot(input) + self._b
        self._lastOutput = sum

        if af == 0:
            return activations.ReLU(sum)
        elif af == 1:
            return activations.sigmoid(sum)
                
    def input_err(self, output_err):
        wT = self._w.T
        return wT.dot(output_err)

    def backward_prop(self, err, lr, af):
        gradient = []

        if af == 0:
            dO = activations.dReLU(self._lastOutput)
        elif af == 1:
            dO = activations.dSigmoid(self._lastOutput)

        gradient = lr * err * dO
        iT = self._lastInput.T
        dW = gradient.dot(iT)

        self._w += dW
        self._b += gradient

        return self.input_err(err)


    def getW(self):
        return self._w

    def getB(self):
        return self._b
