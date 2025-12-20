from fastapi import FastAPI
from astroquery.jplhorizons import Horizons
from astropy.time import Time

AU_TO_KM = 149_597_870.7

app = FastAPI()

@app.get("/distance_to_voyager1")
def voyager_distance():
    # Get current time
    now = Time.now().jd

    obj = Horizons(
        id="Voyager 1",
        location="399",  # Earth
        epochs=now
    )

    eph = obj.ephemerides()

    distance_km = eph["delta"][0] * AU_TO_KM

    return f"{distance_km:,.0f} km from Earth to Voyager 1"