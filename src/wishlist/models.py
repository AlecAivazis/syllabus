from django.db import models


User = 'core.SyllUser'
ClassProfile = 'academia.ClassProfile'
Term = 'academia.Term'

# this schema handles a wishlists - user specified priority lists that get handled
# in a specified manner 

# the funcdamental unit of the wishlist application
# the {user} wants to get {profile} asap when it becomes {term}
class WishList(models.Model):
    user = models.ForeignKey(User)
    profile = models.ForeignKey(ClassProfile)
    term = models.ForeignKey(Term)
