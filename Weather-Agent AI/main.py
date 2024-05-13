from crewai import Crew
from textwrap import dedent
from agents import WeatherAgents
from tasks import WeatherTasks

from dotenv import load_dotenv
load_dotenv()


class WeatherCrew:
    def __init__(self, city):
        self.city = city

    def run(self):

        # Defining custom weather agents and tasks
        agents = WeatherAgents()
        tasks = WeatherTasks()

        # Defining custom agents
        weather_report_agent = agents.weather_report_agent()
        weather_forecast_agent = agents.weather_forecast_agent()

        # Custom Tasks

        weather_report_task = tasks.identify_weather(
            agent=weather_report_agent,
            city=self.city
        )

        weather_forecast_task = tasks.identify_forecast(
            agent=weather_forecast_agent,
            city=self.city
        )

        # Defining crew
        crew = Crew(
            agents=[
                weather_report_agent,
                weather_forecast_agent
            ],
            tasks=[
                weather_report_task,
                weather_forecast_task
            ]
        )

        result = crew.kickoff()
        return result

# Main Function


if __name__ == "__main__":
    print("## Welcome to Weather Crew ##")
    print('-------------------------------')
    city = input(
        dedent("""
                Please provide the name of the city for which you'd like a weather report.
               """)
    )

    weather_crew = WeatherCrew(city=city)
    result = weather_crew.run()
    print("\n\n########################")
    print("## Here is your Detailed Weather Report and Forecast")
    print("########################\n")
    print(result)