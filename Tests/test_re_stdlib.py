# Licensed to the .NET Foundation under one or more agreements.
# The .NET Foundation licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information.

##
## Run selected tests from test_re from StdLib
##

import unittest
import sys

from iptest import run_test

import test.test_re

def load_tests(loader, standard_tests, pattern):
    if sys.implementation.name == 'ironpython':
        suite = unittest.TestSuite()
        suite.addTest(test.test_re.ExternalTests('test_re_benchmarks'))
        suite.addTest(unittest.expectedFailure(test.test_re.ExternalTests('test_re_tests')))
        suite.addTest(test.test_re.ImplementationTest('test_overlap_table'))
        suite.addTest(unittest.expectedFailure(test.test_re.PatternReprTests('test_bytes')))
        suite.addTest(unittest.expectedFailure(test.test_re.PatternReprTests('test_inline_flags')))
        suite.addTest(unittest.expectedFailure(test.test_re.PatternReprTests('test_long_pattern')))
        suite.addTest(unittest.expectedFailure(test.test_re.PatternReprTests('test_multiple_flags')))
        suite.addTest(unittest.expectedFailure(test.test_re.PatternReprTests('test_quotes')))
        suite.addTest(unittest.expectedFailure(test.test_re.PatternReprTests('test_single_flag')))
        suite.addTest(unittest.expectedFailure(test.test_re.PatternReprTests('test_unicode_flag')))
        suite.addTest(unittest.expectedFailure(test.test_re.PatternReprTests('test_unknown_flags')))
        suite.addTest(unittest.expectedFailure(test.test_re.PatternReprTests('test_without_flags')))
        suite.addTest(test.test_re.ReTests('test_anyall'))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_ascii_and_unicode_flag')))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_backref_group_name_in_exception')))
        suite.addTest(test.test_re.ReTests('test_basic_re_sub'))
        suite.addTest(test.test_re.ReTests('test_big_codesize'))
        suite.addTest(test.test_re.ReTests('test_bigcharset'))
        suite.addTest(test.test_re.ReTests('test_bug_113254'))
        suite.addTest(test.test_re.ReTests('test_bug_114660'))
        suite.addTest(test.test_re.ReTests('test_bug_117612'))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_bug_13899')))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_bug_1661')))
        suite.addTest(test.test_re.ReTests('test_bug_16688'))
        suite.addTest(test.test_re.ReTests('test_bug_20998'))
        suite.addTest(test.test_re.ReTests('test_bug_2537'))
        suite.addTest(test.test_re.ReTests('test_bug_3629'))
        suite.addTest(test.test_re.ReTests('test_bug_418626'))
        suite.addTest(test.test_re.ReTests('test_bug_448951'))
        suite.addTest(test.test_re.ReTests('test_bug_449000'))
        suite.addTest(test.test_re.ReTests('test_bug_449964'))
        suite.addTest(test.test_re.ReTests('test_bug_462270'))
        suite.addTest(test.test_re.ReTests('test_bug_527371'))
        suite.addTest(test.test_re.ReTests('test_bug_545855'))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_bug_581080')))
        suite.addTest(test.test_re.ReTests('test_bug_612074'))
        suite.addTest(test.test_re.ReTests('test_bug_6509'))
        suite.addTest(test.test_re.ReTests('test_bug_6561'))
        suite.addTest(test.test_re.ReTests('test_bug_725106'))
        suite.addTest(test.test_re.ReTests('test_bug_725149'))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_bug_764548')))
        suite.addTest(test.test_re.ReTests('test_bug_817234'))
        suite.addTest(test.test_re.ReTests('test_bug_926075'))
        suite.addTest(test.test_re.ReTests('test_bug_931848'))
        suite.addTest(test.test_re.ReTests('test_bytes_str_mixing'))
        suite.addTest(test.test_re.ReTests('test_category'))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_compile')))
        suite.addTest(test.test_re.ReTests('test_constants'))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_dealloc')))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_debug_flag')))
        suite.addTest(test.test_re.ReTests('test_dollar_matches_twice'))
        suite.addTest(test.test_re.ReTests('test_empty_array'))
        suite.addTest(test.test_re.ReTests('test_expand'))
        suite.addTest(test.test_re.ReTests('test_finditer'))
        suite.addTest(test.test_re.ReTests('test_flags'))
        suite.addTest(test.test_re.ReTests('test_getattr'))
        suite.addTest(test.test_re.ReTests('test_getlower'))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_group_name_in_exception')))
        suite.addTest(test.test_re.ReTests('test_groupdict'))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_ignore_case')))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_ignore_case_range')))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_ignore_case_set')))
        suite.addTest(test.test_re.ReTests('test_inline_flags'))
        suite.addTest(test.test_re.ReTests('test_issue17998'))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_keep_buffer')))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_keyword_parameters')))
        suite.addTest(test.test_re.ReTests('test_large_search'))
        suite.addTest(test.test_re.ReTests('test_large_subn'))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_locale_caching'))) # fails on .NET Core linux/macos
        suite.addTest(test.test_re.ReTests('test_lookahead'))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_lookbehind')))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_match_repr')))
        suite.addTest(test.test_re.ReTests('test_not_literal'))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_pickling')))
        suite.addTest(test.test_re.ReTests('test_qualified_re_split'))
        suite.addTest(test.test_re.ReTests('test_qualified_re_sub'))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_re_escape')))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_re_escape_byte')))
        suite.addTest(test.test_re.ReTests('test_re_escape_non_ascii'))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_re_escape_non_ascii_bytes')))
        suite.addTest(test.test_re.ReTests('test_re_findall'))
        suite.addTest(test.test_re.ReTests('test_re_fullmatch'))
        suite.addTest(test.test_re.ReTests('test_re_groupref'))
        suite.addTest(test.test_re.ReTests('test_re_groupref_exists'))
        suite.addTest(test.test_re.ReTests('test_re_match'))
        suite.addTest(test.test_re.ReTests('test_re_split'))
        suite.addTest(test.test_re.ReTests('test_re_subn'))
        suite.addTest(test.test_re.ReTests('test_repeat_minmax'))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_repeat_minmax_overflow')))
        suite.addTest(test.test_re.ReTests('test_repeat_minmax_overflow_maxrepeat'))
        suite.addTest(test.test_re.ReTests('test_scanner'))
        suite.addTest(test.test_re.ReTests('test_search_coverage'))
        suite.addTest(test.test_re.ReTests('test_search_dot_unicode'))
        suite.addTest(test.test_re.ReTests('test_search_star_plus'))
        suite.addTest(test.test_re.ReTests('test_special_escapes'))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_sre_byte_class_literals')))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_sre_byte_literals')))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_sre_character_class_literals')))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_sre_character_literals')))
        suite.addTest(test.test_re.ReTests('test_stack_overflow'))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_string_boundaries')))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_sub_template_numeric_escape')))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_symbolic_groups')))
        suite.addTest(unittest.expectedFailure(test.test_re.ReTests('test_symbolic_refs')))
        suite.addTest(test.test_re.ReTests('test_unlimited_zero_width_repeat'))
        suite.addTest(test.test_re.ReTests('test_weakref'))
        return suite

    else:
        return loader.loadTestsFromModule(test.test_re, pattern)

run_test(__name__)
