import praw
import json


class RedditSubmission(praw.reddit.models.Submission):
    def __init__(self, reddit, submission_id=None, url=None, _data=None):
        super().__init__(reddit, id=submission_id, url=url, _data=_data)

    def to_json(self):
        # Convert the submission to a dictionary
        submission_dict = self.to_dict()

        # Use the JSON encoder provided by the praw library to convert the dictionary to a JSON string
        return json.dumps(submission_dict)

    def to_dict(self):
        return {
            # 'author': self.author, # Redditor
            'author_flair_text': self.author_flair_text,
            'clicked': self.clicked,
            # 'comments': self.comments, # CommentForest
            'created_utc': self.created_utc,
            'distinguished': self.distinguished,
            'edited': self.edited,
            'id': self.id,
            'is_original_content': self.is_original_content,
            'is_self': self.is_self,
            'link_flair_text': self.link_flair_text,
            'locked': self.locked,
            'name': self.name,
            'num_comments': self.num_comments,
            'over_18': self.over_18,
            'permalink': self.permalink,
            'saved': self.saved,
            'score': self.score,
            'selftext': self.selftext,
            'spoil': self.spoiler,
            # 'subreddit': self.subreddit, # Subreddit
            'title': self.title,
            'upvote_ratio': self.upvote_ratio,
            'url': self.url,
        }
