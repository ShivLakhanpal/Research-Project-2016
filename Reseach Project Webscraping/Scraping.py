#API Reddit Wrapper
import praw


#All Reddit Websites have a key to distinguish each thread
sub_id = "4n6imx"


def comment_scraper(comment, output_data):

    output_data.append({"id": user_comment.id, "comment": user_comment.body})

    if len(user_comment._replies) > 0:

        for c in user_comment._replies:

            comment_scraper(c, reply_list)

    return reply_list


#state your purpose for conducting the comment scrape
#Had to get this part from another user on Github or else Reddit would ban me
c = praw.Reddit('get comments from reddit for NYU Research by User: Shiv')

submission = c.get_submission(submission_id=sub_id)



submission.replace_more_comments(limit=None, threshold=0)


#Final Output

output = []


for comment in submission.comments:

    f_data = []  #This array holds comments

    #Get all comments

    output.append(comment_scraper(comment, f_data))

with open('RedditComments2.csv', 'a') as outf:

    for item in output:

        for item_2 in item:

            # write to file in the proper comma delimited format, one per line

            outf.write(u"{0},{1}\n".format(ele2['id'], ele2['comment']).encode('utf-8'))
