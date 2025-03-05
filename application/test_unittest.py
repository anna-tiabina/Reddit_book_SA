"""
The unittest module allows a developer to test the module app_Reddit, namely, if its functions dowload and process the data correctly. It contains the following functions:
    *test_get_review tests wheather a review is dowloaded from Reddit
    *test_get_sentiment tests whether the sentiment model works properly. The testing review is positive and the function get_sentiment should return the prediction equal to torch.Tensor([1])

"""
import unittest
import numpy as np
from app_Reddit import get_review, get_sentiment 


review = "I love the book. The mook is amazing and interesting"

class TestRedditApp(unittest.TestCase):
    def test_get_review(self):
        """
        The function to test wheather a review is dowloaded from Reddit 
        """
        self.assertTrue(get_review())

    def test_get_sentiment(self):
        """
        The function to test whether the sentiment model works properly. The testing review is positive and the function get_sentiment should return the prediction equal to array([1]), the function return numpy.ndarray)
        """
        self.assertEqual(get_sentiment(review), array([1]))


if __name__ == "__main__":
    unittest.main()
    