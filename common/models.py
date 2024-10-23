from django.db import models 
from django.utils.translation import gettext_lazy as _


from django.db import models
# from account.models import CustomUser

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import datetime

class PlasticCart(models.Model):
    
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)  # 16-digit card number
    expiration_date = models.CharField(max_length=5)  # Format: MM/YY
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("PlasticCart")
        verbose_name_plural = _("PlasticCarts")

    def __str__(self):
        return str(self.card_number)

    # Custom validation for card number length
    def clean(self):
        if not self.card_number.isdigit() or len(self.card_number) != 16:
            raise ValidationError(_("Card number must be a valid 16-digit number."))

        # Checking expiration date format MM/YY and validity
        try:
            expiration = datetime.strptime(self.expiration_date, "%m/%y")
        except ValueError:
            raise ValidationError(_("Expiration date must be in MM/YY format."))

        # Deactivate the card if the expiration date has passed
        if expiration < datetime.now():
            self.is_active = False

    def save(self, *args, **kwargs):
        # Perform custom validation before saving
        self.clean()
        super().save(*args, **kwargs)

    


class Address(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    long = models.DecimalField(max_digits=8, decimal_places=3)
    lat = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    city = models.CharField(max_length=35, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    street_address = models.CharField(max_length=150, blank=True, null=True)
    postal_code = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addreses")
    
    def __str__(self):
        return f"{self.user} from {self.city}"
