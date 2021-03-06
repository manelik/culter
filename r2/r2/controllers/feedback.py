# The contents of this file are subject to the Common Public Attribution
# License Version 1.0. (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://code.reddit.com/LICENSE. The License is based on the Mozilla Public
# License Version 1.1, but Sections 14 and 15 have been added to cover use of
# software over a computer network and provide for limited attribution for the
# Original Developer. In addition, Exhibit A has been modified to be consistent
# with Exhibit B.
# 
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for
# the specific language governing rights and limitations under the License.
# 
# The Original Code is Reddit.
# 
# The Original Developer is the Initial Developer.  The Initial Developer of the
# Original Code is CondeNet, Inc.
# 
# All portions of the code written by CondeNet are Copyright (c) 2006-2009
# CondeNet, Inc. All Rights Reserved.
################################################################################
from reddit_base import RedditController
from pylons import c, request
from pylons.i18n import _
from r2.lib.pages import FormPage, Feedback, Captcha, PaneStack, SelfServeBlurb

class FeedbackController(RedditController):

    def GET_ad_inq(self):
        title = _("inquire about advertising on reddit")
        return FormPage('advertise',
                        content = PaneStack([SelfServeBlurb(),
                                             Feedback(title=title,
                                                      action='ad_inq')]),
                        loginbox = False).render()

    def GET_feedback(self):
        title = _("send reddit feedback")
        return FormPage('feedback',
                        content = Feedback(title=title, action='feedback'),
                        loginbox = False).render()

    def GET_i18n(self):
        title = _("help translate reddit into your language")
        return FormPage('help translate',
                        content = Feedback(title=title, action='i18n'),
                        loginbox = False).render()
