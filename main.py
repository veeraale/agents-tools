import os
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile

load_dotenv()
openAI_key = os.getenv("OPENAI_KEY")

if __name__ == "__main__":
    summary_template = """
    Given the information {information} about a person, I wish you to create:
    1. A 50-word summary that highlights the person's expertise. Use a casual tone.
    2. Two bullets with facts about the person. Use a funny tone.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_profile_url = linkedin_lookup_agent(name="Nate Bachmeier from AWS")

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url)

    print(chain.run(information=linkedin_data))
