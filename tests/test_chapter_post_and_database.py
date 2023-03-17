#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from book_tester import (
    ChapterTest,
    CodeListing,
    Command,
    Output,
)

class Chapter5Test(ChapterTest):
    chapter_name = 'chapter_post_and_database'
    previous_chapter = 'chapter_philosophy_and_refactoring'

    def test_listings_and_commands_and_output(self):
        self.parse_listings()

        # sanity checks
        self.assertEqual(type(self.listings[0]), CodeListing)
        self.assertEqual(type(self.listings[1]), Command)
        self.assertEqual(type(self.listings[2]), Output)

        views_pos = 16
        assert "request.POST.get" in self.listings[views_pos].contents

        nutemplate_pos = 77
        assert '{"items": items}' in self.listings[nutemplate_pos].contents

        migrate_pos = 81
        assert 'migrate' in self.listings[migrate_pos]
        assert self.listings[migrate_pos].type == 'interactive manage.py'

        # skips
        self.skip_with_check(86, "3: Buy peacock feathers")

        self.start_with_checkout()
        self.start_dev_server()
        self.unset_PYTHONDONTWRITEBYTECODE()

        restarted_after_views = False
        restarted_after_migrate = False
        restarted_after_nutemplate = False
        while self.pos < len(self.listings):
            print(self.pos)
            if self.pos > views_pos and not restarted_after_views:
                self.restart_dev_server()
                restarted_after_views = True
            if self.pos > migrate_pos and not restarted_after_migrate:
                self.restart_dev_server()
                restarted_after_migrate = True
            if self.pos > nutemplate_pos and not restarted_after_nutemplate:
                self.restart_dev_server()
                restarted_after_nutemplate = True
            self.recognise_listing_and_process_it()

        self.assert_all_listings_checked(self.listings)
        self.check_final_diff(ignore=[
            "moves",
            "Generated by Django 4.1",
        ])


if __name__ == '__main__':
    unittest.main()
