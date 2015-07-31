#!/usr/bin/env python

import smtplib
import time
import uuid
import sys
import getopt

from_addr = "nobody@localhost"
to_addr = "nobody@localhost"
smtp_server = "localhost"
num_msgs = 1
delay = 2

def usage():
    print "./smtptest -f '<from address>' -t '<to address>' -s '<smtp server>' -n '<number of messages>' -d '<delay>'\n"

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'f:t:s:n:d:h', [])
    except getopt.GetoptError as e:
        usage()
        print str(e)
        sys.exit(1)

    for o, a in opts:
        if o == '-f':
            from_addr = a
        elif o == '-t':
            to_addr = a
        elif o == '-s':
            smtp_server = a
        elif o == '-n':
            num_msgs = int(a)
        elif o == '-d':
            delay = float(a)
        elif o == '-h':
            usage()
            sys.exit(0)
        else:
            assert False, 'unhandled option'
            
    for i in xrange(num_msgs):
        str_uuid = str(uuid.uuid4())
        try:
            s = smtplib.SMTP(smtp_server)
            s.starttls()

            body = "From: <%s>\nTo: <%s>\nSubject: Test %s\n\nMail test.\n\n" % (from_addr, to_addr, str_uuid)
            s.sendmail(from_addr, to_addr, body)
            s.quit()
            time.sleep(delay)
        except smtplib.SMTPException, e:
            print str(e)
