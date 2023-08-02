import random
import cyrtranslit
import nltk
from nltk.corpus import names

from genderdefiner.enums import Gender
from genderdefiner.types import SubjectGender


class GenderDefiner:

    def __init__(self):
        self.__labeled_names = self.__get_labeled_names()
        random.shuffle(self.__labeled_names)

        self.__set = self.__get_train_set()
        self.__classifier = self.__get_classifier()

    @staticmethod
    def __gender_features(word: str):
        return {'last_letter': word[-1]}

    @staticmethod
    def __get_labeled_names():
        return (
            [(name, 'male') for name in names.words('male.txt')]
            +
            [(name, 'female') for name in names.words('female.txt')]
        )

    def __feature_sets(self):
        return [(self.__gender_features(n), gender) for (n, gender) in self.__labeled_names]

    def __get_train_set(self):
        return self.__feature_sets()[500:]

    def __get_test_set(self):
        return self.__feature_sets()[:500]

    def __get_classifier(self):
        return nltk.NaiveBayesClassifier.train(self.__set)

    @staticmethod
    def to_latin(name: str) -> str:
        return cyrtranslit.to_latin(name, 'ru')

    def define(self, name: str) -> SubjectGender:
        name_on_latin = self.to_latin(name)

        gender: Gender = self.__classifier.classify(self.__gender_features(name_on_latin))
        probability: float = nltk.classify.accuracy(self.__classifier, self.__set)

        return SubjectGender(
            gender=gender,
            probability=probability
        )
