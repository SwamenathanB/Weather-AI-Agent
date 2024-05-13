"""
.__tip_selection
identify_weather

"""

from crewai import Task
from textwrap import dedent


class WeatherTasks:
    def __tip_selection(self):
        return "If you do your BEST WORK, I'll give you a $100 commission! "

    def identify_weather(self, city, agent):
        return Task(
            description=dedent(
                f"""

        **Task**: Get me the WEATHER REPORT OF TODAY.

        **Description**: Give me a detailed description of the weather report of the current day. 
                         You MUST give a detailed Weather Report of the city for the current day precautions that has to be taken if there's a bad weather. For example carry an umberella when its rainy. 
                         You MUST give me the actual weather report.

        **Parameters**:
        - City: {city}

        **Note**: {self.__tip_selection()}

                """
            ), agent=agent
        )

    def identify_forecast(self, city, agent):
        return Task(
            description=(
                f"""

        **Task**: Get me the WEATHER FORECAST FOR NEXT 3 DAYS.

        **Description**: Give me a detailed description of the weather forecast of the city for the next 3 days. 
                         You MUST give a detailed WEATHER FORECAST of the city for the next 3 days along with any precautions that has to be taken if there's a bad weather. For example carry an umberella when forecast rainy. 
                         You MUST give me the actual weather forecast.

        **Parameters**:
        - City: {city}

        **Note**: {self.__tip_selection()}

                """
            ), agent=agent
        )
