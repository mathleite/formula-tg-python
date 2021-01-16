from app.race.car.models.car_model import CarModel
from app.race.driver.models.driver_model import DriverModel
from app.race.models.race_model import RaceModel
from app.race.race import Race
from bootstrap.bootstrap import Bootstrap

Bootstrap.setup()

# matheus = DriverModel(name='matheus TG')
# matheus.save()
#
# ferrari = CarModel(driver_id=matheus, number='03', brand='buggati')
# ferrari.save()

# race = RaceModel(name='TG Race', type='Street', laps=1)
# race.save()

Race.start(race=RaceModel.get_by_id(1))
