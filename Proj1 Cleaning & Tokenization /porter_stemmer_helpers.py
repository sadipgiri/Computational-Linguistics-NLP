#!/usr/bin/env python3
"""
    Python3 program to stemmize using Porter's algorithm with important helper functions
        Paper - https://tartarus.org/martin/PorterStemmer/def.txt
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Date: 03/04/2019
"""

def is_consonant(word, index):
    '''
        normalize word to lowercase
        According to consonant definition: define is consonant function
            A \consonant\ in a word is a letter other than A, E, I, O or U, and other
            than Y preceded by a consonant. (The fact that the term `consonant' is
            defined to some extent in terms of itself does not make it ambiguous.) So in
            TOY the consonants are T and Y, and in SYZYGY they are S, Z and G. If a
            letter is not a consonant it is a \vowel\.
    '''
    word = word.lower()
    if word[index] in 'aeiou':
        return False
    if word[index] == 'y':
        if index == len(word) - 1:
            return True
        elif word[index+1] in 'aeiou':
            return True
        else:
            return False
    return True

def measure_word(word,word_format=False):
    '''
        normalize lowercase word in the form of c's and v's according to definition from the paper as follows:
        count vc's from the represented string -> defined as {m} the measure.

            A consonant will be denoted by c, a vowel by v. A list ccc... of length
            greater than 0 will be denoted by C, and a list vvv... of length greater
            than 0 will be denoted by V. Any word, or part of a word, therefore has one
            of the four forms:
                CVCV ... C
                CVCV ... V
                VCVC ... C
                VCVC ... V
            These may all be represented by the single form
                [C]VCVC ... [V]
            where the square brackets denote arbitrary presence of their contents.
            Using (VC){m} to denote VC repeated m times, this may again be written as
                [C](VC){m}[V].
            m will be called the \measure\ of any word or word part when represented in
            this form. The case m = 0 covers the null word. Here are some examples:
                m=0    TR,  EE,  TREE,  Y,  BY.
                m=1    TROUBLE,  OATS,  TREES,  IVY.
                m=2    TROUBLES,  PRIVATE,  OATEN,  ORRERY.
    '''
    word_in_cv = ''
    for i in range(len(word)):
        if is_consonant(word.lower(),i):
            word_in_cv += 'c'
        else:
            word_in_cv += 'v'
    if word_format == True:
        return [word_in_cv.count('vc'), word_in_cv]
    return word_in_cv.count('vc')

def helper_replace_suffix(word, suffix, replacement):
    '''
        get the stem of word after splitting suffix 
        return stem attached with replacement
    '''
    return word[:-len(suffix)] + replacement

def step1a(word):
    '''
        stemming according to given step1a rule as follows from the paper:
            Step 1a
                SSES -> SS                         caresses  ->  caress
                IES  -> I                          ponies    ->  poni
                                                   ties      ->  ti
                SS   -> SS                         caress    ->  caress
                S    ->                            cats      ->  cat
    '''
    word = word.lower()
    if word.endswith('sses'):
        return helper_replace_suffix(word, 'sses', 'ss')
    if word.endswith('ies'):
        return helper_replace_suffix(word, 'ies', 'i')
    if word.endswith('ss'):
        return helper_replace_suffix(word, 'ss', 'ss')
    if word.endswith('s'):
        return helper_replace_suffix(word, 's', '')
    return word

def step1b(word):
    '''
        Step 1b:
            (m>0) EED -> EE                 feed      ->  feed
                                            agreed    ->  agree
            (*v*) ED  ->                    plastered ->  plaster
                                            bled      ->  bled
            (*v*) ING ->                    motoring  ->  motor
                                            sing      ->  sing
        If the second or third of the rules in Step 1b is successful, the following
        is done:
            AT -> ATE                       conflat(ed)  ->  conflate
            BL -> BLE                       troubl(ed)   ->  trouble
            IZ -> IZE                       siz(ed)      ->  size
            (*d and not (*L or *S or *Z))
            -> single letter
                                            hopp(ing)    ->  hop
                                            tann(ed)     ->  tan
                                            fall(ing)    ->  fall
                                            hiss(ing)    ->  hiss
                                            fizz(ed)     ->  fizz
            (m=1 and *o) -> E               fail(ing)    ->  fail
                                            fil(ing)     ->  file
        The rule to map to a single letter causes the removal of one of the double
        letter pair. The -E is put back on -AT, -BL and -IZ, so that the suffixes
        -ATE, -BLE and -IZE can be recognised later. This E may be removed in step

    NOTE: 
        return word -> if m == 0 and endswith('eed') e.g. feed -> fee if we don't define this way!!
    '''
    cond1_or_2_success = False
    word = word.lower()
    if word.endswith('eed') and measure_word(word[:-len('eed')])>0:
        return helper_replace_suffix(word, 'eed', 'ee')
    if word.endswith('eed') and measure_word(word[:-len('eed')]) == 0:
        return word 
    if word.endswith('ed') and 'v' in measure_word(word[:-len('ed')], word_format=True)[1]:
        word = helper_replace_suffix(word, 'ed', '')
        cond1_or_2_success = True
    if word.endswith('ing') and 'v' in measure_word(word[:-len('ing')], word_format=True)[1]:
        word = helper_replace_suffix(word, 'ing', '')
        cond1_or_2_success = True
    if cond1_or_2_success:
        if word.endswith('at'):
            return helper_replace_suffix(word, 'at', 'ate')
        if word.endswith('bl'):
            return helper_replace_suffix(word, 'bl', 'ble')
        if word.endswith('iz'):
            return helper_replace_suffix(word, 'iz', 'ize')
        if measure_word(word,word_format=True)[1].endswith('cc') and not (word.endswith('l') or word.endswith('s') or word.endswith('z')):
            return helper_replace_suffix(word, word[len(word)-2:], word[len(word)-1])
        lst_measure_and_cv_form = measure_word(word, word_format=True)
        if lst_measure_and_cv_form[0] == 1 and lst_measure_and_cv_form[1].endswith('cvc') and not (word.endswith('w') or word.endswith('x') or word.endswith('y')):
            return word + 'e'
    return word

def step1c(word):
    '''
        Step 1c
            (*v*) Y -> I                    happy        ->  happi
                                            sky          ->  sky
            Step 1 deals with plurals and past participles. The subsequent steps are
            much more straightforward.
    '''
    word = word.lower()
    if word.endswith('y') and 'v' in measure_word(word,word_format=True)[1]:
        return helper_replace_suffix(word, 'y', 'i')
    return word

def step2(word):
    '''
        Step 2
            (m>0) ATIONAL ->  ATE           relational     ->  relate
            (m>0) TIONAL  ->  TION          conditional    ->  condition
                                            rational       ->  rational
            (m>0) ENCI    ->  ENCE          valenci        ->  valence
            (m>0) ANCI    ->  ANCE          hesitanci      ->  hesitance
            (m>0) IZER    ->  IZE           digitizer      ->  digitize
            (m>0) ABLI    ->  ABLE          conformabli    ->  conformable
            (m>0) ALLI    ->  AL            radicalli      ->  radical
            (m>0) ENTLI   ->  ENT           differentli    ->  different
            (m>0) ELI     ->  E             vileli        - >  vile
            (m>0) OUSLI   ->  OUS           analogousli    ->  analogous
            (m>0) IZATION ->  IZE           vietnamization ->  vietnamize
            (m>0) ATION   ->  ATE           predication    ->  predicate
            (m>0) ATOR    ->  ATE           operator       ->  operate
            (m>0) ALISM   ->  AL            feudalism      ->  feudal
            (m>0) IVENESS ->  IVE           decisiveness   ->  decisive
            (m>0) FULNESS ->  FUL           hopefulness    ->  hopeful
            (m>0) OUSNESS ->  OUS           callousness    ->  callous
            (m>0) ALITI   ->  AL            formaliti      ->  formal
            (m>0) IVITI   ->  IVE           sensitiviti    ->  sensitive
            (m>0) BILITI  ->  BLE           sensibiliti    ->  sensible
        The test for the string S1 can be made fast by doing a program switch on
        the penultimate letter of the word being tested. This gives a fairly even
        breakdown of the possible values of the string S1. It will be seen in fact
        that the S1-strings in step 2 are presented here in the alphabetical order
        of their penultimate letter. Similar techniques may be applied in the other
        steps.
    '''
    word = word.lower()
    suffixes_dct = {
        'ational': 'ate',
        'tional': 'tion',
        'enci': 'ence',
        'anci': 'ance',
        'izer': 'ize',
        'abli': 'able',
        'alli': 'al',
        'entli': 'ent',
        'eli': 'e',
        'ousli': 'ous',
        'ization': 'ize',
        'ation': 'ate',
        'ator': 'ate',
        'alism': 'al',
        'iveness': 'ive',
        'fulness': 'ful',
        'ousness': 'ous',
        'aliti': 'al',
        'iviti': 'ive',
        'biliti': 'ble'
    }
    for i in suffixes_dct.keys():
        if word.endswith(i) and measure_word(word[:-len(i)]) > 0:
            return helper_replace_suffix(word, i, suffixes_dct[i])
    return word

def step3(word):
    '''
        Step 3
            (m>0) ICATE ->  IC              triplicate     ->  triplic
            (m>0) ATIVE ->                  formative      ->  form
            (m>0) ALIZE ->  AL              formalize      ->  formal
            (m>0) ICITI ->  IC              electriciti    ->  electric
            (m>0) ICAL  ->  IC              electrical     ->  electric
            (m>0) FUL   ->                  hopeful        ->  hope
            (m>0) NESS  ->                  goodness       ->  good
    '''
    suffixes_dct = {
        'icate': 'ic',
        'ative': '',
        'alize': 'al',
        'iciti': 'ic',
        'ical': 'ic',
        'ful': '',
        'ness': ''
    }
    for i in suffixes_dct.keys():
        if word.endswith(i) and measure_word(word[:-len(i)]) > 0:
            return helper_replace_suffix(word, i, suffixes_dct[i])
    return word

def step4(word):
    '''
        Step 4
            (m>1) AL    ->                  revival        ->  reviv
            (m>1) ANCE  ->                  allowance      ->  allow
            (m>1) ENCE  ->                  inference      ->  infer
            (m>1) ER    ->                  airliner       ->  airlin
            (m>1) IC    ->                  gyroscopic     ->  gyroscop
            (m>1) ABLE  ->                  adjustable     ->  adjust
            (m>1) IBLE  ->                  defensible     ->  defens
            (m>1) ANT   ->                  irritant       ->  irrit
            (m>1) EMENT ->                  replacement    ->  replac
            (m>1) MENT  ->                  adjustment     ->  adjust
            (m>1) ENT   ->                  dependent      ->  depend
            (m>1 and (*S or *T)) ION ->     adoption       ->  adopt
            (m>1) OU    ->                  homologou      ->  homolog
            (m>1) ISM   ->                  communism      ->  commun
            (m>1) ATE   ->                  activate       ->  activ
            (m>1) ITI   ->                  angulariti     ->  angular
            (m>1) OUS   ->                  homologous     ->  homolog
            (m>1) IVE   ->                  effective      ->  effect
            (m>1) IZE   ->                  bowdlerize     ->  bowdler
    '''
    word = word.lower()
    suffixes_list = ['al','ance','ence','er','ic','able','ible','ant','ement','ment','ent','ou','ism','ate','iti','ous','ive','ize']
    # only condition: (m>1 and (*S or *T)) ION ->     adoption       ->  adopt 
    if word.endswith('ion') and measure_word(word[:-len('ion')]) > 1 and (word[:-len('ion')].endswith('s') or word[:-len('ion')].endswith('t')):
        return helper_replace_suffix(word, 'ion', '')
    for i in suffixes_list:
        if word.endswith(i) and measure_word(word[:-len(i)]) > 1:
            return helper_replace_suffix(word, i, '')
    return word

def step5a(word):
    '''
        Step 5a
            (m>1) E     ->                  probate        ->  probat
                                            rate           ->  rate
            (m=1 and not *o) E ->           cease          ->  ceas
    '''
    word = word.lower()
    stem = word[:-len('e')]
    lst_measure_and_cv_form = measure_word(word, word_format=True)
    if lst_measure_and_cv_form[0] > 1 and word.endswith('e'):
        return helper_replace_suffix(word, 'e', '')
    if lst_measure_and_cv_form[0] > 1 and word.endswith('e') and not (lst_measure_and_cv_form[1].endswith('cvc') and not (stem.endswith('w') or stem.endswith('x') or stem.endswith('y'))):
        return helper_replace_suffix(word, 'e', '')
    return word

def step5b(word):
    '''
        Step 5b
            (m > 1 and *d and *L) -> single letter      controll       ->  control
                                                        roll           ->  roll
    '''
    word = word.lower()
    if measure_word(word) > 1 and word[-2] == word[-1] and word.endswith('l'):
        return helper_replace_suffix(word, word[len(word)-2:], word[len(word)-1])
    return word

'''
    NOTEs from the paper:
        The algorithm is careful not to remove a suffix when the stem is too short,
        the length of the stem being given by its measure, m. There is no linguistic
        basis for this approach. It was merely observed that m could be used quite
        effectively to help decide whether or not it was wise to take off a suffix.
        For example, in the following two lists:

                        list A        list B
                        ------        ------
                        RELATE        DERIVATE
                        PROBATE       ACTIVATE
                        CONFLATE      DEMONSTRATE
                        PIRATE        NECESSITATE
                        PRELATE       RENOVATE
        -ATE is removed from the list B words, but not from the list A words. This
        means that the pairs DERIVATE/DERIVE, ACTIVATE/ACTIVE, DEMONSTRATE/DEMONS-
        TRABLE, NECESSITATE/NECESSITOUS, will conflate together. The fact that no
        attempt is made to identify prefixes can make the results look rather
        inconsistent. Thus PRELATE does not lose the -ATE, but ARCHPRELATE becomes
        ARCHPREL. In practice this does not matter too much, because the presence of
        the prefix decreases the probability of an erroneous conflation.

        Complex suffixes are removed bit by bit in the different steps. Thus
        GENERALIZATIONS is stripped to GENERALIZATION (Step 1), then to GENERALIZE
        (Step 2), then to GENERAL (Step 3), and then to GENER (Step 4). OSCILLATORS
        is stripped to OSCILLATOR (Step 1), then to OSCILLATE (Step 2), then to
        OSCILL (Step 4), and then to OSCIL (Step 5). In a vocabulary of 10,000
        words, the reduction in size of the stem was distributed among the steps as
        follows:
            Suffix stripping of a vocabulary of 10,000 words
            ------------------------------------------------
            Number of words reduced in step 1:   3597
                        "                 2:    766
                        "                 3:    327
                        "                 4:   2424
                        "                 5:   1373
            Number of words not reduced:         3650
        The resulting vocabulary of stems contained 6370 distinct entries. Thus the
        suffix stripping process reduced the size of the vocabulary by about one
        third.
'''

if __name__ == '__main__':
    # print('-----Measure Words-----')
    # for i in ['TR',  'EE',  'TREE',  'Y',  'BY','TROUBLE',  'OATS',  'TREES',  'IVY','TROUBLES',  'PRIVATE',  'OATEN',  'ORRERY']:
    #     print(measure_word(i))
    print('-----STEP1A-----')
    for i in ['caresses', 'ponies', 'ties', 'caress', 'cats']:
        print(step1a(i))
    print('-----STEP1B-----')
    for i in ['feed', 'agreed', 'plastered', 'bled', 'motoring', 'sing', 'conflated', 'troubled', 'sized', 'hopping', 'tanned', 'falling', 'hissing', 'fizzed', 'failing', 'filing']:
        print(step1b(i))
    print('-----STEP1C-----')
    for i in ['happy', 'sky']:
        print(step1c(i))
    print('-----STEP2-----')
    for i in ['relational','conditional','rational','valenci','hesitanci','digitizer','conformabli','radicalli','differentli','sensibiliti']:
        print(step2(i))
    print('-----STEP3-----')
    for i in ['triplicate', 'formative', 'electrical', 'electriciti', 'goodness', 'hopeful', 'formalize']:
        print(step3(i))
    print('-----STEP4-----')
    for i in ['revival', 'allowance', 'inference', 'airliner', 'gyroscopic', 'adjustable','defensible','irritant','replacement','adjustment','dependent','adoption','homologou','communism']:
        print(step4(i))
    print('-----STEP5a-----')
    for i in ['probate', 'rate', 'cease']:
        print(step5a(i))
    print('-----STEP5b-----')
    for i in ['controll','roll']:
        print(step5b(i))
    print('-----Running All At Once-----')
    words = ['oscillators','GENERALIZATIONS']
    lst = []
    for i in words:
        i = step1a(i)
        i = step1b(i)
        i = step1c(i)
        i = step2(i)
        i = step3(i)
        i = step4(i)
        i = step5a(i)
        i = step5b(i)
        lst.append(i)
    print(lst)

