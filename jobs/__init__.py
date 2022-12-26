from .create import create


def write(background=None,
          job=None,
          save=None,
          what='cover',
          temperature=0,
          max_tokens=1024,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0,
          best_of=3):
    """
    Generate a cover letter and resume using GPT-3 and the user's background and the job posting.

    Parameters
    ----------
    background : str
        The name of the YAML file containing the user's background.
        This file should contain a list of lists, one for 'Education' and one for 'Experience'
    job : str
        The name of the text file containing the job posting.
    what : str
        'cover' for cover letter, 'resume' for resume
    save : Optional[str], optional
        The name of the file to save the output to. If not provided, the output will be printed to the console.

    Returns
    -------
    str
        The generated cover letter.
    """
    return create(background=background,
                  job=job,
                  save=save,
                  what=what,
                  temperature=temperature,
                  max_tokens=max_tokens,
                  top_p=top_p,
                  frequency_penalty=frequency_penalty,
                  presence_penalty=presence_penalty,
                  best_of=best_of
                  )
