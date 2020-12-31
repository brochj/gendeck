# -*- coding: utf-8 -*-

from .context import sample

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(sample.hmm())


if __name__ == '__main__':
    unittest.main()


# # -*- coding: utf-8 -*-
# """
# Created on Tue Dec 29 23:16:19 2020

# @author: broch
# """

# import unittest

# # from web-scraping import Oxford

# # from faker import Faker


# # class TestUser(unittest.TestCase):
# #     def setUp(self):
# #         self.fake = Faker()
# #         self.user = User(
# #             first_name = self.fake.first_name(),
# #             last_name = self.fake.last_name(),
# #             job = self.fake.job(),
# #             address = self.fake.address()
# #         )

# #     def test_user_creation(self):
# #         self.assertIsInstance(self.user, User)

# #     def test_user_name(self):
# #         expected_username = self.user.first_name + " " + self.user.last_name
# #         self.assertEqual(expected_username, self.user.user_name)

# # if __name__ == '__main__':
# #     unittest.main()