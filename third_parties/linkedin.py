import os
import requests


def scrape_linkedin_profile(linkedin_profile_url):
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    api_key = os.getenv("PROXYCURL_API_KEY")
    header_dic = {"Authorization": "Bearer " + api_key}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    if response.status_code == 200:
        data = response.json()
        data = {
            k: v
            for k, v in data.items()
            if v not in ([], "", "", None)
            and k
            not in [
                "people_also_viewed",
                "certifications",
                "skills",
                "groups",
                "follower_count",
                "experiences",
                "certifications",
                "recommendations",
                "activities",
            ]
        }
        if data.get("groups"):
            for group_dict in data.get("groups"):
                group_dict.pop("profile_pic_url")
        return data
    else:
        return None
