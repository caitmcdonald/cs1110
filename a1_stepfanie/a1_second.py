# a1_second.py
# PUT YOUR NETID(S) HERE
# Sources/people consulted: FILL IN OR WRITE "NONE"
# PUT DATE YOU COMPLETED THIS HERE
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
    #pass

    first_tag = text.index(tag) #finds the first instance of `tag` in the text string
    length = len(tag) #gets length of tag!
    text_after_tag = text[first_tag+length:] #outputs everything in the `text` string after the `tag`

    return text_after_tag
### after function passed the test!
### only needed to fix the indexing of the final text_after_tag
### need to figure out the length of the tag first to get the correct place to start the outputting


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
    #pass

    sub_text = after(text,start_str) #uses after function to subset the text string to after the start_str `tag`
    end_tag = sub_text.index(end_str) #identifies the index of the end_str
    between_text = sub_text[:end_tag] #outputs string between start_str and end_str

    return between_text

    # STUDENTS: your implementation MUST call your `after` function (in a
    # useful way).



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
    #pass

    time = first_between(s, 'class="time">', '</time>') #uses find between to ID the times
    #time is consistently listed in this way

    component1 = first_between(s, '<ul class="section', '><')
    #first needed to pull this unique string
    component2 = first_between(component1, 'Class Section ', '"')
    #then need to further subdivide the string to get the course name
    #sometimes there's more info in between the original subset

    day1 = first_between(s, 'class="pattern-only"><span', '/span>')
    #first need to pull this unique string
    day2 = first_between(day1, '>', '<')
    #there's sometimes additional information included in day1, so need to then grab only what's between > <

    status1 = after(s, '<li class="open-status">')
    #this one was annoying
    #needed to first use the after function with the unique string
    status2 = first_between(status1,'data-content="','"')
    #then was able to use first_between because the open status is always started with 'data-content="'


    #component_text = after(s,'<ul class="section')
    #component = first_between(component_text, 'aria_label="Class Section ','">')

    #day = first_between(s, 'class="pattern-only"><span','</span>')

    #status_text = after(s,'<li class="open-status">')
    #status = first_between(status_text, 'data-content="','"')

    return component2 + ' ' + day2 + ' ' + time + ' ' + status2

    # STUDENTS: YOUR IMPLEMENTATION MUST CALL first_between() in a useful way.
    # Use of other helpers is fine, too.
