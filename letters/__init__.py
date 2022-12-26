from .create import create


def write(background=None, job=None, save=None):
    """
    Generate a cover letter using GPT-3 and the user's background and the job posting.

    Parameters
    ----------
    background : str
        The name of the YAML file containing the user's background.
        This file should contain a list of lists, one for 'Education' and one for 'Experience'
    job : str
        The name of the text file containing the job posting.
    save : Optional[str], optional
        The name of the file to save the output to. If not provided, the output will be printed to the console.

    Returns
    -------
    str
        The generated cover letter.
    """
    return create(background=background, job=job, save=save)
