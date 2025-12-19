from astroquery.jplhorizons import Horizons

AU_TO_KM = 149_597_870.7

obj = Horizons(id="Voyager 1", location='500@10', epochs={'start':'2010-05-05', 'stop':'2010-05-06', 'step':'1d'})
distance_FE = obj.ephemerides()
distance_FE['delta_km'] = distance_FE['delta'] * AU_TO_KM
print(distance_FE['delta_km'])