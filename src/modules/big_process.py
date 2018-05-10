#!/usr/bin/env python3
#-*- coding : utf-8 -*-

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#     PRESENTATION DU MODULE :
#          Ce modules rassemble les fonctions de fonctions
#          Dans le souci de ne pas surcharger le fichier main.py
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

########################################################
# LIST FUNCTIONS IN MODULES
#
#     + generation_dico_corpus_pr_xml()
#     + creer_et_remplir_fichier_synthese_xml()
#
########################################################

import os
import re
import random
import codecs
#import subprocess

from collections import defaultdict

import pprint , io

import modules.tagging as tagging
import modules.transitions as transitions

# Lien vers les dossiers de la racine ############################################
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from settings import PROJECT_ROOT, CORPUS_PHRASES, TREETAGGER_ROOT
###################################################################################

##############################################################
# Fonction : traitement_phrase_fr(phrase)
# Input :
##############################################################

def traitement_phrase(phrase , langue='fr'):
    
    #VAR
    phrase_a_analyser = phrase
    langue_analyse = langue
    dico_a_remplir = defaultdict(lambda: defaultdict(dict))

    # TAGGING
    dico_tags = tagging.tagger_phrase_return_dict(dico_a_remplir, phrase_a_analyser, langue_analyse)

    # TEST
    print("\n======================================")
    print("======================================")
    
    for key in dico_tags :
        print("Key : {} +++ forme : {} +++ pos : {} +++ lemme : {}".format(key, 
        dico_tags[key]["mot_forme"], dico_tags[key]["pos"], dico_tags[key]["lemme"]))

    # ANALYSE
    issue_analyse = transitions.analyse_phrase_from_dico(dico_tags) # YES or NO

    print("\n L'analyse a donnée : {}".format(str(issue_analyse)))
    
    return issue_analyse
    
def traitement_phrases_dans_texte(lien_dossier):
    
    fichiers_phrases = ["phrases_fr" , "phrases_en"]
    
    for fichier in fichiers_phrases :
        # choix langue
        if "fr" in fichier :
            langue = 'fr'
        elif "en" in fichier :
            langue = 'en'
        # constitution des liens
        lien_phrases_test = lien_dossier+fichier+".txt"
        lien_results_analyse = lien_dossier+fichier+"_results.txt"
        # analyse et remplissage fichier
        with codecs.open(lien_phrases_test, mode='r', encoding='utf8') as file_in :
            with codecs.open(lien_results_analyse, mode='w', encoding='utf8') as file_out :
        
                for line in file_in :
                    if line.strip() == '' or line.startswith('#'):
                        file_out.write(str(line))
                    else :
                        result = traitement_phrase(line, langue)
                        file_out.write("\n" + str(line) + "\t ---> " + str(result) + "\n")
  