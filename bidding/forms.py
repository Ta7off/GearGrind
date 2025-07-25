from django import forms

from bidding.models import Bid


class BidBaseForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']

class CreateBidForm(BidBaseForm):
    pass

class UpdateBidForm(BidBaseForm):
    pass