from pyAudioAnalysis import audioTrainTest as aT

models = ["knn", "svm", "gradientboosting", "extratrees", "randomforest"]

for current_model in models:
	aT.featureAndTrain(["speechrec/Good", "speechrec/Bad"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, current_model, current_model+"Model", True)