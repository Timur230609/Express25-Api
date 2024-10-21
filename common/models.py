from django.db import models 

# Create your models here.


# class BaseModel(models.Model):
#     created_at = models.DateTimeField("created at", auto_now_add=True)
#     updated_at = models.DateTimeField("updated at", auto_now=True)
#     created_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.SET_NULL,
#         null=True,
#         related_name="%(class)s_createdby",
#         editable=False,
#     )
#     modified_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.SET_NULL,
#         related_name="%(class)s_modifiedby",
#         null=True,
#         blank=True,
#         editable=False,
#     )

#     class Meta:
#         abstract = True

#     def save(self, *args, **kwargs):
#         if hasattr(self, "slug") and hasattr(self, "title"):
#             if not self.slug:
#                 self.slug = generate_unique_slug(self.__class__, self.title)

#         if hasattr(self, "slug") and hasattr(self, "name"):
#             if not self.slug:
#                 self.slug = generate_unique_slug(self.__class__, self.name)
#         super().save(*args, **kwargs)


# Muhammadjon, Boborahim, Norbek

class PlasticCard(models.Model):
    pass


class Address(models.Model):
    pass