import re

from bs4 import BeautifulSoup
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from etc.config import settings as app_settings
from email.MIMEImage import MIMEImage


class HTMLEmailMessage(EmailMessage):
    """
    A HTML-only email massage with images as inline attachments.
    """
    content_subtype = 'html'
    mixed_subtype = 'related'

    def __init__(self, subject='', from_email=None, to=None,
                 template=None, template_context=None, cc=None, bcc=None):

        super(HTMLEmailMessage, self).__init__(subject, '', from_email, to,
                                               bcc=bcc, connection=None,
                                               attachments=None, headers=None,
                                               cc=cc)

        if template:
            self.load_template(template, template_context)

    def load_template(self, template, context):
        """
        Loads template and sets it as a message body. If template contains images
        they will be added to messsage as inline attachments.

        :param string template: the name of the template to load
        :param dict context: variables that should be available in the context
            of the template
        """
        template_context = self.get_default_template_context()
        template_context.update(context)
        html = render_to_string(template, template_context)

        images = []
        soup = BeautifulSoup(html)
        IMAGE_MATCH_PATTERN = r'url\(([^)]+)\)'

        def image_finder(tag):
            return tag.name == 'img' or (tag.get('style') and re.findall(IMAGE_MATCH_PATTERN, tag['style']))

        for index, tag in enumerate(soup.findAll(image_finder)):
            cid = 'img{0}'.format(index)

            if tag.name == 'img':
                filename = tag['src']
                tag['src'] = 'cid:' + cid
            else:
                filename = re.findall(IMAGE_MATCH_PATTERN, tag['style'])[0]
                tag['style'] = re.sub(IMAGE_MATCH_PATTERN, 'url(cid:{0})'.format(cid), tag['style'])

            images.append((filename, cid))
        self.body = str(soup)

        for filename, cid in images:
            self.attach_inline_image(filename, cid)

    def attach_inline_image(self, filename, cid):
        """
        Attaches an image as inline attachment.

        :param string filename: the name of image to attach
        :param string cid: identifier of the attachment
        """
        with open(settings.MAILING_STATIC_DIR / filename, 'rb') as img_file:
            img = MIMEImage(img_file.read())
        img.add_header('Content-ID', '<%s>' % cid)
        img.add_header('Content-Disposition', 'inline', filename=filename)
        self.attach(img)

    def get_default_template_context(self):
        """ Returns dict of common variables used in mailing templates """
        return dict(
            kanary_url=app_settings.ui_frontend_url
        )
