from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm): 
    """ Post Form """

    title = StringField( 
        'Title', 
        [DataRequired()]
    )

    subreddit = StringField( 
        'Subreddit', 
        [DataRequired()]
    )

    username = StringField( 
        'Username', 
        [DataRequired()]
    )

    body = TextField( 
        'Body', 
        [
            DataRequired(), 
            Length(max=255, 
            message=('Body length too long.'))
        ]
    )

    numUpvotes = IntegerField( 
        'numUpvotes', 
        [DataRequired()]
    )

    submit = SubmitField('Submit')

