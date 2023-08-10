import pickle

from textblob.classifiers import NaiveBayesClassifier

classifier = NaiveBayesClassifier([('__sentence__', '__category__'), ...])

classifier.update([('__sentence__', '__category__'), ...])

with open('classifier.pickle', 'wb') as f:
    pickle.dump(classifier, f)

with open('classifier.pickle', 'rb') as f:
    classifier = pickle.load(f)

classifier.classify(...)
