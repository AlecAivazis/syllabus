from django.db import models

# this schema handles a wishlists - user specified priority lists that get handled
# in a specified manner 

# the funcdamental unit of the wishlist application
# the {user} wants to get {profile} asap when it becomes {term}
class WishList(models.Model):
    user = models.ForeignKey(SyllUser)
    profile = models.ForeignKey(ClassProfile)
    term = models.ForeignKey(Term)
