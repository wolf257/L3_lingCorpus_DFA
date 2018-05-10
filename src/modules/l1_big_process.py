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
#     + traitement_phrase_interactif()
#     + traitement_phrase()
#     + traitement_phrases_dans_texte()
#
########################################################

import os , io
import re
import random
import codecs

from collections import defaultdict

import pprint

import modules.l2_tagging as tagging
import modules.l2_transitions as transitions
import modules.l2_others as others

# Lien vers les dossiers de la racine ############################################
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from settings import PROJECT_ROOT, CORPUS_PHRASES, TREETAGGER_ROOT
###################################################################################

##############################################################
# Fonction : traitement_phrase_interactif(phrase, langue)
# Input :
##############################################################
def traitement_phrase_interactif(phrase , langue='fr'):
    ''' Analyse et écrit le détails'''
    
    #VAR
    phrase_a_analyser = phrase
    langue_analyse = langue
    dico_a_remplir = defaultdict(lambda: defaultdict(dict))
    # TAGGING
    dico_tags = tagging.tagger_phrase_return_dict(dico_a_remplir, phrase_a_analyser, langue_analyse)

    print("\n\n======================================")

    for key in dico_tags :
        print("\nKey : {} +++ forme : {} +++ pos : {} +++ lemme : {}".format(key, 
        dico_tags[key]["mot_forme"], dico_tags[key]["pos"], dico_tags[key]["lemme"]))
    
    # ANALYSE (phrase contenant la conclusion)
    issue_analyse = transitions.analyse_phrase_from_dico(dico_tags, langue_analyse)

    print("\n\n!!! {}".format(str(issue_analyse)))
    
    return issue_analyse

##############################################################
# Fonction : traitement_phrase(phrase , lien_f_analyse_detaillee, num_phrase, langue='fr)
# Input :
##############################################################
def traitement_phrase(phrase , lien_f_analyse_detaillee, num_phrase, langue='fr'):
    ''' Analyse et écrit le détails'''
    
    #VAR
    phrase_a_analyser = phrase
    langue_analyse = langue
    dico_a_remplir = defaultdict(lambda: defaultdict(dict))
    f_a_detaillee = lien_f_analyse_detaillee
    # TAGGING
    dico_tags = tagging.tagger_phrase_return_dict(dico_a_remplir, phrase_a_analyser, langue_analyse)

    with codecs.open(f_a_detaillee, mode='a', encoding='utf8') as file_details :
        file_details.write("\n\n======================================")
        file_details.write("======================================")
        file_details.write("\n\tPhrase numéro {} : {} \n".format(num_phrase, phrase_a_analyser))

        for key in dico_tags :
            file_details.write("\nKey : {} +++ forme : {} +++ pos : {} +++ lemme : {}".format(key, 
            dico_tags[key]["mot_forme"], dico_tags[key]["pos"], dico_tags[key]["lemme"]))
    
    # ANALYSE (phrase contenant la conclusion)
    issue_analyse = transitions.analyse_phrase_from_dico(dico_tags, langue_analyse, f_a_detaillee)

    with codecs.open(f_a_detaillee, mode='a', encoding='utf8') as file_details :
        file_details.write("\n\n !!! {}".format(str(issue_analyse)))
    
    return issue_analyse

##############################################################
# Fonction : traitement_phrases_dans_texte(lien_dossier)
# Input :
##############################################################
def traitement_phrases_dans_texte(lien_dossier):
    
    fichiers_phrases = ["phrases_fr" , "phrases_en"]
    
    for fichier in fichiers_phrases :
        num_phrase = 1
        
        # choix langue
        if "fr" in fichier :
            langue = 'fr'
        elif "en" in fichier :
            langue = 'en'
            
        # constitution des liens
        others.creation_folder(lien_dossier, 'resultats')
        
        lien_phrases_test = lien_dossier+fichier+".txt"
        lien_results_analyse = lien_dossier+'resultats/'+fichier+"_results.txt"
        lien_f_analyse_detaillee = lien_dossier+'resultats/'+fichier+'_analyse_detaillee.txt'

        # analyse et remplissage fichier
        with codecs.open(lien_phrases_test, mode='r', encoding='utf8') as file_in :
            with codecs.open(lien_results_analyse, mode='w', encoding='utf8') as file_out :
                
                for line in file_in :
                    if line.strip() == '' or line.startswith('#'):
                        file_out.write(str(line))
                    else :
                        result = traitement_phrase(line, lien_f_analyse_detaillee, num_phrase, langue)
                        file_out.write("\n{} : {} ----> {} \n".format(str(num_phrase), str(line) , \
                        str(result)))
                        num_phrase += 1
                        

                        
                        
                        
                        