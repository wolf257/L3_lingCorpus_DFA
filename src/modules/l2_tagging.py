#!/usr/bin/env python3

########################################################
# LIST FUNCTIONS IN MODULES
#
#	+ 
#
########################################################

import os, re, random

import treetaggerwrapper
import pprint , io

from collections import defaultdict

#import modules.others as others

# Lien vers les dossiers de la racine ############################################
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from settings import PROJECT_ROOT, CORPUS_PHRASES, TREETAGGER_ROOT
###################################################################################

folder_treetagger = TREETAGGER_ROOT

# Construction et configuration du wrapper
tagger_fr = treetaggerwrapper.TreeTagger(TAGLANG='fr', TAGINENC='utf-8' , TAGOUTENC='utf-8' , TAGDIR=folder_treetagger)
tagger_en = treetaggerwrapper.TreeTagger(TAGLANG='en', TAGINENC='utf-8' , TAGOUTENC='utf-8' , TAGDIR=folder_treetagger)

##############################################################
# Fonction : tagger_phrase_show_dict()
##############################################################
def tagger_phrase_return_dict(dico_a_remplir, phrase_a_analyser, langue_analyse='fr') :

    #var
    langue = langue_analyse
    compteur_mot = 0
    
    
    #TAGGER LA PHRASE
    tags_fr = tagger_fr.TagText(phrase_a_analyser)
    tags_en = tagger_en.TagText(phrase_a_analyser)
    
    if langue == 'en' :
        tags_to_use = tags_en
    else :
        tags_to_use = tags_fr
        
    tags_wrapper = treetaggerwrapper.make_tags(tags_to_use)

    # VAR
    nb_mots_dans_phrase = len(tags_wrapper)

    while compteur_mot < nb_mots_dans_phrase :
        num_mot = compteur_mot

        # RECUPERATION DES INFOS
            # FORME
        try :
            mot_forme = tags_wrapper[num_mot][0]
        except :
            mot_forme = 'forme_NR'

        dico_a_remplir[num_mot]["mot_forme"] = mot_forme
        
            # POS
        try :
            mot_pos_treetagger = tags_wrapper[num_mot][1]
        except :
            mot_pos_treetagger = 'POS_NR'

        dico_a_remplir[num_mot]["pos"] = mot_pos_treetagger

            # LEMME
        try :
            mot_lemme_treetagger = tags_wrapper[num_mot][2]
        except :
            mot_lemme_treetagger = 'POS_NR'

        dico_a_remplir[num_mot]["lemme"] = mot_lemme_treetagger

        compteur_mot += 1

    return dico_a_remplir
