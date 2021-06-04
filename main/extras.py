from django.template.defaultfilters import slugify

MAX_UPLOAD_SIZE = 5242880

def get_pic_name(instance, pic_name):
    title = instance.property_title
    slug = slugify(title)
    return "properties/%s/%s-%s" % (title, slug, pic_name)

def validate_image(image):
        file_size = image.file.size
        if file_size > MAX_UPLOAD_SIZE:
            raise forms.ValidationError('Max size of file is 5 megabytes!')

def blog_pictures(instance, picture_title):
    title = instance.article_title
    slug = slugify(title)
    return "blogs/%s/%s-%s" % (title, slug, picture_title)