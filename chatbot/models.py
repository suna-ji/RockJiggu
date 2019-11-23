from django.db import models

class ReturnInfo(models.Model):
    is_received = models.CharField(null = True, max_length = 30)
    is_agency = models.CharField(null = True, max_length = 30)
    agency_name = models.CharField(null = True, max_length = 100) #is_agency가 False인 경우 angency_name은 null
    mall_name = models.CharField(null = True, max_length = 100)
    is_clearance = models.CharField(null = True,max_length = 30)
    shipping_state_agency = models.CharField(null = True, max_length = 100)
    shipping_state_direct = models.CharField(null = True, max_length = 100)
    is_clearanceimpossible = models.BooleanField(default = False, max_length = 30)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.agency_name)



