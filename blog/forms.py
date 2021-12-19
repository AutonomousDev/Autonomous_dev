from django import forms


class UploadFileForm(forms.Form):
    """This class is needed to make image uploads work on create views. Image
    fields are a sub type of file forms.

    When I have this bug again remember,
    1) HTML Template needs <form method="post" enctype="multipart/form-data">
    2) copy past this class into the relevant app
    """
    title = forms.CharField(max_length=50)
    file = forms.FileField()
