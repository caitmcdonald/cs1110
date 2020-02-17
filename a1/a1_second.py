# a1.py
# cam435
# Sources/people consulted: "NONE"
# 2/16/20
# Skeleton by Prof. Lee (cs1110-prof@cornell.edu), Feb 6 2020
# UPDATE 2/10, 7pm: added 3rd precondition to first_between()

"""
Functions for finding which lectures/sections of a class are open according to
a class roster webpage.

"""


def after(text, tag):
    """Returns: the part of `text` starting just after the 1st `tag`.

    Preconditions:
        `text` [str]: contains at least one instance of `tag`
        `tag`  [str]: length > 0

    Examples:
        after('start <a id="c111"> this that', '<a id="c111">')
            --> ' this that'
            (Note the single space at the beginning.)

        after('start <a id="c111"> this that the other', 'other')
            --> ''
    """
    tag_start = text.find(tag)
    tag_len = len(tag)
    after_tag = text[tag_start+tag_len:]
    return after_tag


def first_between(text, start_str, end_str):
    """Returns substring of `text` occurring between the 1st occurrence of
    `start_str` and the first following occurrence of `end_str`.
    Preconditions:
        `text` [str]: length > 0.
        `start_str` and `end_str` [str]: both non-empty and occur in `text`.
         At least one `end_str` appears after a `start_str` in `text`.


    Examples:
        first_between('A1A2A3bA4ccccA5', 'A', 'b') ---> '1A2A3'
        first_between('hi)bye(x)(a+b)', '(', ')')  --> 'x'
            (Note that there was an end_str before start_str.)

        first_between('<a href="x">yes</a><span>toodles</span>', '<span>', '<')
            --> 'toodles'
    """
    after_start = after(text, start_str)
    end_pos = after_start.find(end_str)
    between = after_start[:end_pos]
    return between
    # STUDENTS: your implementation MUST call your `after` function (in a
    # useful way).

def after_last(text, tag):
    """Returns: the part of `text` starting just after the last instance of `tag`.

    Preconditions:
        `text` [str]: contains at least one instance of `tag`
        `tag`  [str]: length > 0

    Examples:
        after_last('before before before i go', 'before')
            --> ' i go'
    """
    last_start = text.rfind(tag)
    last_len = len(tag)
    to_end = text[last_start+last_len:]
    return to_end


def report_section(s):
    """Returns string '<component> <meeting day(s)> <time> <status>'.

    Preconditions:
    `s` corresponds to a single class component (=lecture/section)
    that isn't TBA, having a pattern like this
        '<ul class="section ... aria-label="Class Section DIS 202"
         ... class="pattern-only"><span ...>T</span>
         ... class="time">11:15am - 12:05pm</time>
         ... <li class="open-status"> ... data-content="Open"...'
    where the following substrings occur exactly once:
        '<ul class="section'
        'class="pattern-only"><span'
        'class="time">'
        <li class="open-status">

    For this example, this function returns 'DIS 202 T 11:15am - 12:05pm Open'.
    """
    # get <component>
    component = first_between(s, 'Section ', '"')

    # get <time>
    time = first_between(s, '"time">', '</time>')

    # get <day>
    pat_to_time = first_between(s, 'pattern-only">', time)
    to_day = first_between(pat_to_time,'>','</span>')

    # get <status>
    time_pos = s.find(time)
    time_to_end = s[time_pos:]
    status = after_last(time_to_end, 'data-content')
    status_stripped = first_between(status, '="','"')

    # return all information
    return component + ' ' + to_day + ' ' + time  + ' ' + status_stripped

    # STUDENTS: YOUR IMPLEMENTATION MUST CALL first_between() in a useful way.
    # Use of other helpers is fine, too.
