# a1_first.py
# cam435
# Sources/people consulted: "NONE"
# 2/16/20
# Skeleton by Prof. Lee (cs1110-prof@cornell.edu), Feb 6 2020
# UPDATED Feb 9, 6:30pm to fix missing line for test_after()'s test case 5
# UPDATED Feb 11, 9:30am: add 2nd arg, test_after()'s testcase 10 assert_equals()
# UPDATED Feb 12, 7:30pm: correct test_first_between docstring

""" (Skeleton for) test cases for CS1110 A1, Spring 2020.

    STUDENTS: be sure to read the assignment writeup before proceeding!

"""

import testcase
import a1_second


def test_after():
    """Test function a1_second.after"""
    print("Testing a1_second.after")

    ### STUDENTS: see instructions in assignment writeup!!!

    # 1. tag at beginning
    result = a1_second.after('start', 'st')
    testcase.assert_equals('art', result)

    # 2. (given, guaranteed ok) tag in middle (and tag like one expects in html)
    result = a1_second.after('start <a id="c111"> this that', '<a id="c111">')
    testcase.assert_equals(' this that', result)

    # 3. (given, guaranteed ok) tag at end
    result = a1_second.after('start <a id="c111"> this that the other', 'other')
    testcase.assert_equals('', result)

    # 4. tag not in text
    # ... STUDENT-DELETED CASE ...
    # ... REASON: violates precondition
    #result = a1_second.after('start', 'x')
    #testcase.assert_equals(None, result)

    # 5. tag in twice
    # ... STUDENT-FIXED ERROR ...
    result = a1_second.after('start A start B', 'start')
    #testcase.assert_equals(' A ', result)
    testcase.assert_equals(' A start B', result)

    # 6. text and tag are the same
    result = a1_second.after('start', 'start')
    testcase.assert_equals('', result)

    # 7. tag contains punctuation
    result = a1_second.after("Hi! How's it going?", "'")
    testcase.assert_equals('s it going?', result)

    # 8. parts of tag show up before actual tag
    result = a1_second.after('aaa1aaaa2', 'aaaa')
    testcase.assert_equals('2', result)

    # 9. tag contains space(s)
    result = a1_second.after("Hi! How's it going?", "it going")
    testcase.assert_equals('?', result)

    # 10. empty tag
    # ... STUDENT-DELETED CASE ...
    # ... REASON: violates precondition
    #result = a1_second.after('aaa1aaaa2', '')
    #testcase.assert_equals('aaa1aaaa2', result)

    # 11. tag is case-sensitive
    result = a1_second.after("UPPER upper", "up")
    testcase.assert_equals('per', result)

    # 12. tag is space (probably redundant with #9?)
    result = a1_second.after("Hello, world", " ")
    testcase.assert_equals('world', result)

    # 13. tag and text are single character
    result = a1_second.after("a","a")
    testcase.assert_equals('', result)

    # 14. tag contains a number (redundant with #2 and #3)
    result = a1_second.after("0100","1")
    testcase.assert_equals('00', result)

    print("finished test\n")


def test_first_between():
    """Test function a1_second.first_between"""

    print("Testing a1_second.first_between")

    # simple markers, typical case (given, guaranteed correct)
    result = a1_second.first_between('A1A2A3bA4ccccA5', 'A', 'b')
    testcase.assert_equals('1A2A3', result)

    # end_str before start_str (given, guaranteed correct)
    result = a1_second.first_between('hello and hi) bye(x) shoo', '(', ')')
    testcase.assert_equals("x", result)

    # start_str and end_str are like real html (given, guaranteed correct)
    t = '<a href="x">yes</a><span>toodles</span>'
    result = a1_second.first_between(t, '<span>', '<')
    testcase.assert_equals("toodles", result)

    # text has no string between start_str and end_str
    result = a1_second.first_between('coursework', 'course', 'work')
    testcase.assert_equals('', result)

    # end_str same as start_str
    result = a1_second.first_between('banana', 'n', 'n')
    testcase.assert_equals('a', result)

    # end_str same as start_str same as text
    result = a1_second.first_between('N','N','N')
    testcase.assert_equals('', result)

    # multiple start_str
    result = a1_second.first_between('hello hello world', 'hello', 'world')
    testcase.assert_equals(' hello ', result)

    # start_str contains space
    result = a1_second.first_between('hello world',' ', 'd')
    testcase.assert_equals('worl', result)

    # end_str contains space
    result = a1_second.first_between('hello world','h', ' ')
    testcase.assert_equals('ello', result)

    # start_str contains punctuation
    result = a1_second.first_between('Please! No more testing.','!', 'i')
    testcase.assert_equals(' No more test', result)

    # end_str contains punctuation
    result = a1_second.first_between('Please no more testing!','Please ', '!')
    testcase.assert_equals('no more testing', result)

    # start_str and end_str are case-sensitive
    result = a1_second.first_between('Bonobo', 'Bo', 'bo')
    testcase.assert_equals('no', result)

    print("finished test\n")


def test_report_section():
    """Test function a1_second.report_section"""

    print("Testing a1_second.report_section")

    # simple version of template
    s0 = '<ul class="section section-last aria-label="Class Section DIS 202"'
    s0 = s0 + 'class="pattern-only"><span filler>T</span>As you set out for '
    s0 = s0 + 'Ithaka <class="time">11:15am - 12:05pm</time>hope your road i'
    s0 = s0 + 's a long one<li class="open-status"> full of adventure, full '
    s0 = s0 + 'data-content="Open" of discovery.'
    result = a1_second.report_section(s0)
    testcase.assert_equals('DIS 202 T 11:15am - 12:05pm Open', result)

    # another simple version of template
    s1 = '<ul class="section Laistrygonians, aria-label="Class Section AB 2"'
    s1 = s1 + 'class="pattern-only"><span aria-label="Class Section EVL 666">R'
    s1 = s1 + '</span> <class="time">9:05am - 12:05pm</time>aria-label="NO"'
    s1 = s1 + 'Cyclops, angry <li class="open-status">Poseidon --- don\'t be'
    s1 = s1 + 'afraid data-content="Closed" of them:'
    result = a1_second.report_section(s1)
    testcase.assert_equals('AB 2 R 9:05am - 12:05pm Closed', result)

    # real example
    s2 = '<ul class="section  "  aria-label="Class Section LEC 001">'
    s2 = s2 + '<li class="class-numbers"><h5 class="hidden">Class Number &amp; '
    s2 = s2 + '<Section Details</h5><p><strong class="tooltip-iws" '
    s2 = s2 + 'data-toggle="popover" data-content="14442" title="Class Number">'
    s2 = s2 + '14442</strong><span class="course-repeater">CS 1132&nbsp;&nbsp;'
    s2 = s2 + '</span><em class="tooltip-iws" data-toggle="popover" '
    s2 = s2 + 'data-content="Lecture" title="Component">LEC</em> 001\n'
    s2 = s2 + '<span class="favorite fav-14442"><a class="tooltip-iws" '
    s2 = s2 + 'data-toggle="popover" data-content="Add to Favorites" aria-'
    s2 = s2 + 'label="Add to Favorites" href="#" data-class-nbr="14442" data-s'
    s2 = s2 + 'sr-component="LEC" data-section="001"></a></span></p></li><li c'
    s2 = s2 + 'lass="consent">&nbsp;\n</li><li class="meeting-pattern"><h5 cla'
    s2 = s2 + 'ss="hidden">Meeting Pattern</h5><ul class="meetings  meetings-f'
    s2 = s2 + 'irst"><li class="dates"><span class="pattern"><span class="patt'
    s2 = s2 + 'ern-only"><span class="tooltip-iws" data-toggle="popover" data-'
    s2 = s2 + 'content="Mon &amp; Wed">MW</span></span><time class="time">3:35'
    s2 = s2 + 'pm - 4:25pm</time></span><a class="facility-search" href="http:'
    s2 = s2 + '//www.cornell.edu/about/maps/?q=Thurston%20Hall#CUmap" target="'
    s2 = s2 + '_blank" rel="nofollow">Thurston Hall 203</a></li><li class="dat'
    s2 = s2 + 'e-range">\nJan 21 - Mar 10, 2020\n</li><li class="instructors">'
    s2 = s2 + '<h5 class="hidden">Instructors</h5><p><span class="tooltip-iws"'
    s2 = s2 + ' data-toggle="popover" data-content="Nate Veldt (lnv22)">Veldt,'
    s2 = s2 + ' N</span></p></li></ul></li><li class="open-status"><span class'
    s2 = s2 + '="tooltip-iws" data-toggle="popover" data-content="Open"><span '
    s2 = s2 + 'class="'
    result = a1_second.report_section(s2)
    testcase.assert_equals('LEC 001 MW 3:35pm - 4:25pm Open', result)
    print("finished test\n")


###########
# Calls to testing functions
###########

test_after()

test_first_between()

test_report_section()

print('Passed all test functions for a1_second. Hurrah!')
