import yaml
import os
import logging
import openai

KEY = os.getenv('OPENAI_API_KEY')

if KEY is None:
    logging.error('Can not find API key; please set the "OPENAI_API_KEY" environment variable and restart.')
    breakpoint()

openai.api_key = KEY
logging.basicConfig(format='%(asctime)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)


def create(background=None, job=None, save=None):
    if background is None or job is None:
        print('Please set yaml to the input file.')
        return

    # Open the YAML file
    with open(background, 'r') as f:
        background_data = yaml.safe_load(f)

    with open(job, 'r') as f:
        job_data = f.read()

    prompt = """My background: 
    Education: """ + '\n'.join(background_data['Education']) + '\n\n' + """
    Experience: """ + '\n'.join(background_data['Experience']) + '\n\n' + """
    Job posting:
    """ + job_data + """
    Cover letter:
    """

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=int(1024),
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        best_of=3
    )

    output = response['choices'][0]['text']

    if save is None:
        with open(save, 'w') as f:
            f.write(output)

    return output
