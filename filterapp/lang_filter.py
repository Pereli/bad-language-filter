from spanlp.palabrota import Palabrota
from spanlp.domain.countries import Country
from spanlp.palabrota import Palabrota
from spanlp.domain.countries import Country
from spanlp.domain.strategies import JaccardIndex
from spanlp.domain.strategies import Preprocessing, TextToLower, RemoveAccents, NumbersToVowelsInLowerCase

text= 'bla'
strategies = [TextToLower(), RemoveAccents(), NumbersToVowelsInLowerCase()]
jaccard = JaccardIndex(threshold=0.7, normalize=True, n_gram=2, clean_strategies=strategies)
palabrota = Palabrota(censor_char="*", countries=[Country.ESPANA, Country.VENEZUELA], distance_metric=jaccard)
print(palabrota.censor(text))




# !pip install spanlp

# TextToLower

# RemoveAccents

# NumbersToVowelsInLowerCase