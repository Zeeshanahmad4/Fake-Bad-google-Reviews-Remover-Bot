import unittest
from src.review_parser import is_valid_review_url, extract_review_id

class TestReviewParser(unittest.TestCase):
    def test_is_valid_review_url(self):
        """Test URL validation for both valid and invalid URLs."""
        self.assertTrue(is_valid_review_url("https://www.example.com/reviews/123"), "Valid URL should return True")
        self.assertFalse(is_valid_review_url("https://www.example.com/notreviews/123"), "Invalid URL should return False")
        self.assertFalse(is_valid_review_url("Just a string"), "Non-URL string should return False")

    def test_extract_review_id_valid_url(self):
        """Test ID extraction from a valid review URL."""
        self.assertEqual(extract_review_id("https://www.example.com/reviews/123"), "123", "Should extract the ID '123'")

    def test_extract_review_id_invalid_url(self):
        """Test ID extraction behavior with an invalid review URL."""
        self.assertIsNone(extract_review_id("https://www.example.com/notreviews/123"), "Should return None for invalid URLs")
        self.assertIsNone(extract_review_id("Just a string"), "Should return None for non-URL strings")

if __name__ == '__main__':
    unittest.main()
# Tests for the review parser module
