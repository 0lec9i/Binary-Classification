from pyAudioAnalysis import audioTrainTest as aT
from sys import argv


models = ["knn", "svm", "gradientboosting", "extratrees", "randomforest"]
overall_score = 0.0

for arg in argv[1:]:
	for current_model in models:
		overall_score += aT.fileClassification(arg, current_model+"Model",current_model)[1][0]

	overall_score /= 5
	# print(good_prob)
	print()
	print(arg)
	if overall_score > 0.5:
		print("This is good file!")
	else:
		print("Bad file")
	print("Avg score: ", overall_score)
