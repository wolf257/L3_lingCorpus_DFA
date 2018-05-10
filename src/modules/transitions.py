#!/usr/bin/env python3

import pprint , io , os

import modules.l3_pos as pos_file
import modules.l3_table as table

# Lien vers les dossiers de la racine ############################################
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from settings import PROJECT_ROOT, CORPUS_PHRASES, TREETAGGER_ROOT
###################################################################################

table_de_transition = table.table_de_transition

def analyse_phrase_from_dico(dico_phrase_with_tags) :
    
    # VAR
    i = 0
    etat_courant = 'r_init'

    dico_phrase = dico_phrase_with_tags
    longueur = len(dico_phrase_with_tags)

    ###############
    while (etat_courant != 'etat_final') and (etat_courant != 'etat_erreur') and (i < longueur) :

        pos_tree = dico_phrase[i]['pos']
        lemme_tree = dico_phrase[i]['lemme']
        pos_to_use = pos_file.POS_finder(pos_tree , lemme_tree)

        # TEST    
        print('\nOn est au mot \'{}\' de pos \'{}\' '.format(dico_phrase[i]['mot_forme'] , str(pos_to_use)))
        partie_gauche_table = (etat_courant , pos_to_use)
        # TEST
        print("Le couple a chercher est : {}".format(partie_gauche_table))

        if partie_gauche_table in table_de_transition.keys() :

            fonction_to_use = table_de_transition[(etat_courant , pos_to_use)][1]
            fonction_to_use()

            etat_courant = table_de_transition[(etat_courant , pos_to_use)][0]
            i += 1

        else :
            etat_courant = 'etat_erreur'
            # print('+++ J\'ai rencontré une erreur.+++ ')

    ###############
    if etat_courant != 'etat_erreur' :
        etat_courant = 'etat_final'
        # print('\nC\'est bon. La reconnaissance a reussi.') # etat_courant = ' + str(etat_courant))
        return "YES"
    else :
        return "NO"
