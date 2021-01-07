import pickle

from textblob.classifiers import NaiveBayesClassifier

classifier = NaiveBayesClassifier([('???', '???'), ...])

classifier.update([('???', '???'), ...])

with open('...', 'wb') as f:
    pickle.dump(classifier, f)

with open('...', 'rb') as f:
    classifier = pickle.load(f)

classifier.classify(...)
