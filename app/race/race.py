from app.race.models.race_model import RaceModel
from app.race.services.race_service import RaceService
from app.utils.date import Date


class Race:
    @staticmethod
    def start(race: RaceModel):
        if RaceService.check_conditions_to_start_race():
            race.update(started_at=Date.get_current_datetime())
