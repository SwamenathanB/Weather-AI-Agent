"""
weather_report agent
weather_forecast agent
"""
from crewai import Agent
from langchain.llms import OpenAI, ollama
from tools.weather_tool import WeatherTool
from tools.weather_forecast import WeatherForecastTool
from textwrap import dedent
from langchain_openai import ChatOpenAI


class WeatherAgents:

    def __init__(self):
        self.gpt35 = ChatOpenAI(
            model_name="gpt-3.5-turbo", temperature=0.7
        )
        self.gpt4 = ChatOpenAI(model_name='gpt-4', temperature=0.7)

    def weather_report_agent(self):
        return Agent(
            role="Expert Weather Report Agent",
            backstory=dedent(
                f"""
                    Expert in giving weather report.
                    I've decades of experience in giving weather report.
                """
            ),
            goal=dedent(
                f"""
                    Create a detailed weather report for the the particular date of the given city. 
                    Check for any weather alerts. Give weather alerts if any and the precautions to be taken if any alert exists.
                """),

            tools=[WeatherTool.get_weather_report],
            verbose=True,
            llm=self.gpt35,

        )

    def weather_forecast_agent(self):
        return Agent(
            role="Expert Weather Forecast Agent",
            backstory=dedent(
                f"""
                    Expert in giving weather forecast.
                    I've decades of exprience in giving weather forecast.
                """
            ),
            goal=dedent(
                f"""
                        Create a detailed weather forecast for the given city for the next few days. Check if there're any weather alerts. If any give safety precautions to be taken. 
                    """),
            tools=[WeatherForecastTool.get_weather_forecast],
            verbose=True,
            llm=self.gpt35,
        )
