from abc import ABC, abstractmethod


class FuzzyNumber(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def addition(self, FuzzyNumber):
        """
        This method is used to perform the addition of two fuzzy numbers of the same class

        Parameter:
        This method receives a fuzzy number of the same class

        Return:
            This method returns a fuzzy number of the same class. This fuzzy number is the result of the addition of the
            two fuzzy numbers

        """

        pass

    @abstractmethod
    def subtraction(self, FuzzyNumber):
        """
        This method is used to perform the subtraction of two fuzzy numbers of the same class

        Parameter:
        This method receives a fuzzy number of the same class

        Return:
            This method returns a fuzzy number of the same class. This fuzzy number is the result of the subtraction of
            the two fuzzy numbers

        """

        pass

    @abstractmethod
    def multiplication(self, FuzzyNumber):
        """
        This method is used to perform the multiplication of two fuzzy numbers of the same class

        Parameter:
        This method receives a fuzzy number of the same class

        Return:
            This method returns a fuzzy number of the same class. This fuzzy number is the result of the multiplication
            of the two fuzzy numbers

        """

        pass

    @abstractmethod
    def output(self):
        """
        This method is used to perform the multiplication of two fuzzy numbers of the same class

        Parameter:
        This method receives a fuzzy number of the same class

        Return:
            This method returns a fuzzy number of the same class. This fuzzy number is the result of the multiplication
            of the two fuzzy numbers

        """

        pass

    @abstractmethod
    def representation(self):
        """
        This method is used to show the representation of the fuzzy number

        Return: This method returns a string with the representation of the fuzzy number: triangular; trapezoidal;
        L-R; gaussian.

        """
        pass

    @abstractmethod
    def toCartesian(self):
        """
        This method is used to show the cartesian values of the fuzzy number

        Return:
            This method returns a list of the cartesian values of the fuzzy number

        """
        pass
