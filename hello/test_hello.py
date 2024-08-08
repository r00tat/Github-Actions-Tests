"""Sample tests."""

import logging
import unittest

log = logging.getLogger("test")


class TestHello(unittest.IsolatedAsyncioTestCase):
    """test hello."""

    def setUp(self) -> None:
        """Set up tests."""
        if len(logging.getLogger().handlers) <= 0:
            logging.basicConfig(level=logging.INFO)
        return super().setUp()

    def test_ok(self):
        """Everything is good."""
        self.assertEqual(1, 1)
