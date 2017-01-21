#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from book_tester import ChapterTest

class Chapter11Test(ChapterTest):
    chapter_no = 11

    def test_listings_and_commands_and_output(self):
        self.parse_listings()

        # sanity checks
        self.assertEqual(self.listings[0].type, 'code listing with git ref')
        self.assertEqual(self.listings[1].type, 'code listing with git ref')
        self.assertEqual(self.listings[2].type, 'test')

        # other prep
        self.sourcetree.start_with_checkout(self.chapter_no)
        self.prep_database()

        # hack fast-forward
        skip = True
        if skip:
            self.pos = 27
            self.sourcetree.run_command('git checkout {}'.format(
                self.sourcetree.get_commit_spec('ch11l011')
            ))

        while self.pos < len(self.listings):
            print(self.pos, self.listings[self.pos].type)
            self.recognise_listing_and_process_it()

        self.assert_all_listings_checked(self.listings)
        self.check_final_diff()


if __name__ == '__main__':
    unittest.main()
