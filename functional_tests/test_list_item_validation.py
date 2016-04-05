from unittest import skip

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_item(self):
        # User accidentally hits enter without entering task text
        # User is warned and given the chance to enter text
        self.fail('Write test!')
