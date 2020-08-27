import numpy
import pandas


def get_main_dataset():
    """
    Download and clean main dataset.
    """
    # Download csv
    dataset = pandas.read_csv(
        'https://object.cato.org/sites/cato.org/files/'
        'human-freedom-index-files/human-freedom-index-2019.csv'
    )

    # Select important columns
    pf_identity_cols = [col for col in dataset.columns if 'pf_identity' in col]
    score_cols = pf_identity_cols + [
        'pf_score',  # Personal Freedom (score)
        'pf_rank',  # Personal Freedom (rank)
        'ef_score',  # Economic Freedom (score)
        'ef_rank',  # Economic Freedom (rank)
        'hf_score',  # Human Freedom (score)
        'hf_rank',  # Human Freedom (rank)
    ]
    num_cols = ['year'] + score_cols
    cat_cols = ['ISO_code', 'countries', 'region']
    important_cols = cat_cols + num_cols

    # Clean dataset
    dataset = dataset[important_cols].replace('-', numpy.nan)
    for score_col in score_cols:
        dataset[score_col] = pandas.to_numeric(dataset[score_col])

    return dataset


dataset = get_main_dataset()
