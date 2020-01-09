import numpy as np
counter = 0
class NeuralNetwork():
	


	def __init__(self):
		np.random.seed()

		self.synaptic_weights = 2 * np.random.random((5, 1)) - 1

	def sigmoid(self, x):
		return 1/(1 + np.exp(-x))

	def sigmoid_derivative(self, x):
		return x * (1 - x)

 
	def train(self, training_inputs, training_outputs, acceptable_error):
		keep_iterating = True
		while keep_iterating:
			output = self.think(training_inputs)
			error = training_outputs - output
			adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))
			self.synaptic_weights += adjustments
			
			global counter 
			counter = counter + 1
			# if counter > 1000:#if abs(error*100) < acceptable_error: #True:
			# 	keep_iterating = False
			if (all(abs(each*10) < acceptable_error for each in error)):
				keep_iterating = False

	
	
	def think(self, inputs):

		inputs = inputs.astype(float)
		output = self.sigmoid(np.dot(inputs, self.synaptic_weights))

		return output

if __name__ == "__main__":
	neural_network = NeuralNetwork()

	print('Random synaptic weights: ')
	print(neural_network.synaptic_weights)
	training_inputs = np.array([[0,0,1,0,1],
								[1,1,1,0,0],
								[1,0,1,1,1],
								[0,1,1,0,0]])

	training_outputs = np.array([[0,1,1,0]]).T

	neural_network.train(training_inputs, training_outputs, .005)

	print('Symnaptic weights after training: ')
	print(neural_network.synaptic_weights)

	# A = str(input('Input 1: '))
	# B = str(input('Input 2: '))
	# C = str(input('Input 3: '))
	A = str(1)
	B = str(0)
	C = str(1)
	D = str(1)
	E = str(1)

	print('New situation: input data -', A, B, C, D, E)
	print('Output data: ')
	print(neural_network.think(np.array([A, B, C, D, E])))




