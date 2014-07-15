FROM dockerfile/ubuntu

RUN apt-get install git -y

RUN git clone http://github.com/wcmckee/pyatakl.git /wcmckee/pytakl

ADD https://reddit.com/r/redditgetsdrawn.json /wcmckee/reddit
