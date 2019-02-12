#creating function to scrap from subreddits, multiple subreddit can be entered, 'redditdev+learnpython'
def scrapper(name_of_subreddit, search_term):
    
    #import relevant libraries
    import praw
    
    #enter authentications for reddit acct
    reddit = praw.Reddit(client_id = 'DL5VSD1vjS8LUg',
                         client_secret = 'G9zhV9uK2aIqP7KlStRPYVUb2K8',
                         username = 'biaproject',
                         password = '123qweasd',
                         user_agent = 'BIA_project')
    
    #creating empty dict to store relevant submissions, comments
    #relevant_submissions = {submission id: [title, body]}
    #relevant_comments = {comment id: [submission id, up votes, body, {reply id: [up votes, body]} ] }
    #raw_comments = [comment id, submission id, body, parent id]
    relevant_submissions = {}
    relevant_comments = {}
    raw_comments = []
    
    #creating instance of subreddit
    subreddit = reddit.subreddit(name_of_subreddit)
    
    #searching for relevant submissions
    for submission in subreddit.search(search_term):
        #defining the id, title and body text
        submission_id = submission.id
        submission_title = submission.title
        submission_body = submission.selftext
        
        #input into relevant submission dict
        relevant_submissions[submission.id]=[submission_title,submission_body]
        
        #replacing "more comments" with actual comment
        submission.comments.replace_more(limit=0)
        
        #list() is to print out comments, starting with lvl 1 comments, then lvl 2 and these are not sorted (e.g. this reply is for this comment)
        for comment in submission.comments.list():
            #creating new entry within dict if new comment, i.e. not found in dict
            if comment.id not in relevant_comments:
                relevant_comments[comment.id] = [submission.id, comment.ups, comment.body, {}]
                raw_comments.append([comment.id, submission.id, comment.body, str(comment.parent())])
                #this is to filter out for replies(lvl 2) onwards
                if comment.parent() != submission.id:
                    parent = str(comment.parent())
                    relevant_comments[parent][3][comment.id] = [comment.ups, comment.body]
    
    results = {'sub':relevant_submissions, 'comm':relevant_comments, 'raw':raw_comments}
                
    return results



