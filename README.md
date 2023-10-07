# donor_finder
Django code for automatic finding blood donor based on geo location
1) Donor registration " Donor_add_form.html" here first time donor have to register themself, after filling the form ..will get the message " Registration done successfully " redirect to "donor_finder.html page"
2) Donor finder " Donor_finder.html"  where donor seeker will select the required blood group , appliocation will take the Geo-location automatically and then will selecect the donor finder based on two criteria
          a) Donor has donoated blood atleast 50 days before. ( difference between current and blood donated added atleast 50 days or more)
          b) Donor should be in with in predefine of range radius
                 i) 30Km Range Radius    ii) 50Km Range Radius   iii) 70Km Radius
     
