import re
import praw
import subprocess
import time


r = praw.Reddit(user_agent='pep8_enforcer 0.001')
r.login('PEP8_enforcer', 'Redditete11463')

subreddit = r.get_subreddit('shittyarcheology')

while True:
    for submission in subreddit.get_new(limit=20):

        if any(comment.author.name == 'PEP8_enforcer' for comment in submission.comments):
            continue

        code_lines = re.findall(r'    .*\n', submission.selftext)

        if not code_lines:
            continue

        code_lines = [line[4:] for line in code_lines]
        code = ''.join(code_lines)

        with open('temp.py', 'w') as tempfile:
            tempfile.write(code)

        output = subprocess.run('pep8 temp.py', stdout=subprocess.PIPE)
        result_text = output.stdout.decode('ascii')

        post_lines = []
        for line in result_text.split('\n'):
            if line != '':
                line_number = line[8]
                line_text = line.split(' ', 2)[-1]
                post_lines.append('line {}: {}'.format(line_number, line_text))

        if not post_lines:
            continue

        post_text = '\n\n'.join(post_lines)
        submission.add_comment(post_text)

    time.sleep(1)
