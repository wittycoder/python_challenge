from html.parser import HTMLParser

class CommentHTMLParser(HTMLParser):
    def __init__(self):
        super(CommentHTMLParser, self).__init__()
        self.data = ''

    def handle_comment(self, comment):
        self.data = comment.strip().rstrip()  # Just save the last comment which contains the data
