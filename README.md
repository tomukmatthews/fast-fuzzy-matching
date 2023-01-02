# fuzzy-lightning

fuzzy-lightning is a fast and customizable package for finding the closest matches in a list of target strings (documents) using fuzzy string matching. It is particularly effective for short string matching against large document sets, and includes the fastest implementation of the Damerau-Levenshtein and longest common substring algorithms in its class.

## Introduction
This package provides a fuzzy string matching algorithm for finding the closest matches in a list of target strings (documents). It converts strings to vectors using a sklearn TF-IDF vectorizer on character n-grams and then generates a shortlist of match candidates from the top N nearest neighbors (cosine similarity) of dictionary key vectors for each string (ordered from best match to worst). This list of candidates is then pruned to select the best match using the longest common substring to length ratio.

Installation
To install the package, run the following command:

`pip install fuzzy-lightning`

### Quick Start
Here is an example of how to use the FuzzyMatch class to find the closest matches in a list of documents for a list of input strings:

```
from fuzzy_lightning import FuzzyMatch

documents = ["SMARTEST ENERGY", "SMARTPIG"]
fuzzy_matcher = FuzzyMatch(documents=documents)
strings = ['Smart Piggie', 'the smartest energy']
matches = fuzzy_matcher.get_document_matches(strings=strings)
print(matches)
>>> [
    DocumentMatch(match='SMARTPIG', confidence=1.0),
    DocumentMatch(match='SMARTEST ENERGY', confidence=1.0)
]
```

The output is a list of DocumentMatch objects, each with a match attribute that contains the closest matching document and a confidence attribute that represents the confidence of the match (a value between 0 and 1):

If you want to find the closest match for a single string, you can use the get_lookup_match method:

```
match = fuzzy_matcher.get_lookup_match('SMART PIGGIE')
print(match)
>>> DocumentMatch(match='SMARTPIG', confidence=1.0)
```

The FuzzyMatch class has a number of configurable parameters that you can set using the `FuzzyMatchConfig` class. 

- **n_gram_range** (Tuple[int, int]): Range of lengths of n-grams to use with the TF-IDF vectorizer. For example,
    n_gram_range = (2, 3) will use bi-grams and tri-grams.
- **min_document_freq** (int, optional): Minimum number of documents a term must appear in to be considered.
    Defaults to 1.
- **tfidf_similarity_threshold** (float, optional): Minimum cosine similarity to a viable candidate for LCS.
    Defaults to 0.1.
- **n_top_candidates** (int, optional): Maximum number of candidates to return that exceed the
    similarity_threshold. Defaults to 40.
- **lcs_min_characters** (int): Minimum length of the string to qualify for matching to the target strings.
- **lcs_min_length_ratio** (float): Minimum ratio of string length to target string length for an string <> target
    string match to qualify.
- **lcs_similarity_threshold** (float, optional): Minimum LCS match ratio to accept classification.
use_threads** (bool): Whether to use threads to parallelise the work to find the n_top_candidates for each
    string.
- **n_threads** (int): Number of threads to use when finding the n_top_candidates. Increasing the number of threads
    reduces the run time, but there becomes a trade off in production where there may be 'thread congestion'.
- **string_preprocessor** (Optional[Callable[[str], str]]): A callable that takes in a string and returns a processed
    string. This can be used to perform any preprocessing steps on the input strings before they are compared.

For example, to change the range of n-grams used by the TF-IDF vectorizer, you can do the following:

```
from fuzzy_match import FuzzyMatch, FuzzyMatchConfig

config = FuzzyMatchConfig(n_gram_range=(1, 2))
fuzzy_matcher = FuzzyMatch(documents=documents, config=config)
```

## Appendix

### Why is this super fast?

1. C++
2. Dynamic Programming
3. Cache locality benefits of using a 1D array to mimic the behaviour of a 2D array