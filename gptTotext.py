import re
import json
import g4f
from typing import Tuple, List  
from termcolor import colored


def generate_script(video_subject: str) -> list[str]:
    """
    Generate a script for a video, depending on the subject of the video.

    Args:
        video_subject (str): The subject of the video.

    Returns:
        str: The script for the video.
    """

    # Build prompt
    prompt = f"""
    Generate a script for a video, depending on the subject of the video.
    Subject: {video_subject}


    Do not under any circumstance reference this prompt in your response.

    Get straight to the point, don't start with unnecessary things like, "welcome to this video".

    Obviously, the script should be related to the subject of the video.

    The length of the script should be strictly under 30 words. At any cost it should not go above the word limit. And it must be above 10 words.

    Give the title also and the title is not included in the word count.

    It should be some random fact obviously about the topic.
    
    No markup language must be used. everyting should return in plain text.

    Title should also be the plain text. Nothing should be marked bold.

    STRICTLY Do NOT USE ANY THINGS LIKE "TITLE: " or "SCRIPT: ".
    Follow this format strictly => In first line give the title and in second like give the script.

    ONLY RETURN THE RAW CONTENT OF THE SCRIPT. DO NOT INCLUDE "VOICEOVER", "NARRATOR" OR SIMILAR INDICATORS OF WHAT SHOULD BE SPOKEN AT THE BEGINNING OF EACH PARAGRAPH OR LINE.
    """

    # Generate script
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo_16k_0613,
        messages=[{"role": "user", "content": prompt}],
    )
    if not response.find("\n"):
        response = response.replace(':','\n')

    print(colored(response, "cyan"))
    ans = response.split("\n")

    for i in range(len(ans)):
        ans[i] = ans[i].strip()

    resp = []
    for i in ans:
        if(i):
            resp.append(i)

    # Return the generated script
    if response:
        # Clean the script
        # Remove asterisks, hashes
        response = response.replace("*", "")
        response = response.replace("#", "")
        

        # Remove markdown syntax
        response = re.sub(r'\[.*\]', '', response)
        response = re.sub(r'\(.*\)', '', response)
        return resp
    print(colored("[-] GPT returned an empty response.", "red"))


def get_search_terms(video_subject: str, amount: int, script: str) -> List[str]:
    """
    Generate a JSON-Array of search terms for stock videos,
    depending on the subject of a video.

    Args:
        video_subject (str): The subject of the video.
        amount (int): The amount of search terms to generate.
        script (str): The script of the video.

    Returns:
        List[str]: The search terms for the video subject.
    """

    # Build prompt
    prompt = f"""
    Generate {amount} search terms for stock videos,
    depending on the subject of a video.
    Subject: {video_subject}

    The search terms are to be returned as
    a JSON-Array of strings.

    Each search term should consist of 1-3 words,
    always add the main subject of the video.
    
    YOU MUST ONLY RETURN THE JSON-ARRAY OF STRINGS.
    YOU MUST NOT RETURN ANYTHING ELSE. 
    YOU MUST NOT RETURN THE SCRIPT.
    
    The search terms must be related to the subject of the video.
    Here is an example of a JSON-Array of strings:
    ["search term 1", "search term 2", "search term 3"]

    For context, here is the full text:
    {script}
    """

    # Generate search terms
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo_16k_0613,
        messages=[{"role": "user", "content": prompt}],
    )

    # Load response into JSON-Array
    try:
        search_terms = json.loads(response)
    except Exception:
        print(colored("[*] GPT returned an unformatted response. Attempting to clean...", "yellow"))

        # Use Regex to extract the array from the markdown
        search_terms = re.findall(r'\[.*\]', str(response))

        if not search_terms:
            print(colored("[-] Could not parse response.", "red"))

        # Load the array into a JSON-Array
        search_terms = json.loads(search_terms)

    # Let user know
    print(colored(f"\nGenerated {amount} search terms: {', '.join(search_terms)}", "cyan"))

    # Return search terms
    return search_terms

def generate_metadata(video_subject: str, script: str) -> Tuple[str, str, List[str]]:  
    """  
    Generate metadata for a YouTube video, including the title, description, and keywords.  
  
    Args:  
        video_subject (str): The subject of the video.  
        script (str): The script of the video.  
  
    Returns:  
        Tuple[str, str, List[str]]: The title, description, and keywords for the video.  
    """  
  
    # Build prompt for title  
    title_prompt = f"""  
    Generate a catchy and SEO-friendly title for a YouTube shorts video about {video_subject}.  
    """  
  
    # Generate title  
    title_response = g4f.ChatCompletion.create(  
        model=g4f.models.gpt_35_turbo_16k_0613,  
        messages=[{"role": "user", "content": title_prompt}],  
    )  
  
    # Extract title from response  
    title = title_response.strip()  # Assuming title_response is a string  
  
    # Build prompt for description  
    description_prompt = f"""  
    Write a brief and engaging description for a YouTube shorts video about {video_subject}.  
    The video is based on the following script:  
    {script}  
    """  
  
    # Generate description  
    description_response = g4f.ChatCompletion.create(  
        model=g4f.models.gpt_35_turbo_16k_0613,  
        messages=[{"role": "user", "content": description_prompt}],  
    )  
  
    # Extract description from response  
    description = description_response.strip()  # Assuming description_response is a string  
  
    # Generate keywords  
    keywords = get_search_terms(video_subject, 6, script)  # Assuming you want 6 keywords  
  
    return title, description, keywords  