"""This is the HelloWorld challenge to teach the usage of the library by a
minimal example.

This challenge takes a number and a word and composes a new word based
on the input.

The class fully focuses on the "business logic" by overwriting just two
methods of parent class challenge.challenge.Challenge:

    * build: This sets up the data model from the given input lines.
    * calc: This is the core algorithm of the challenge.

This is called the Template Method Pattern. While the parent class handles the
common parts of the challenge flow, the child class just encapsulates what is
special.

The two methods above is just the bare minimum to implement. For more complex
challenges you will overwrite or extend other parts of the parent class.

Have a look into the parent class especially into the main function that
controls the execution of the challenge. Also have a look into the parents
__init__ method to see what instance variables are already prepared to simplify
the communication of the methods.

By the class variable sample a minimal example of the possible input is given.
This is recommended for every challenge. This is useful during development or
for smoke tests.
"""

from challenge.challenge import Challenge

class  HelloWorld(Challenge):
    """This is the HelloWorld Challenge class.

    This challenge takes a word as input and a number at which position
    to split the word. It returns a new word composed of the switched parts
    with a blank in between.
    """

    sample = '''
        5
        WorldHello
    '''
    """This is the input sample. It can be overwritten by injection.

        * first line: integer
        * second line: word
    """

    def build(self):
        """Parse the input lines and set up the model."""
        self.model.splitAt = self.lineToIntegers(0)[0]
        self.model.word = self.line(1)

    def calc(self):
        """Swap head and tail of the model and store to result."""
        first = self.model.word[self.model.splitAt:]
        second = self.model.word[:self.model.splitAt]
        self.result = first + ' ' + second

