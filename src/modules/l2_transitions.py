#!/usr/bin/env python3

import pprint , io , os
import codecs

import modules.l3_pos as pos_file
import modules.l3_table as table

# Lien vers les dossiers de la racine ############################################
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from settings import PROJECT_ROOT, CORPUS_PHRASES, TREETAGGER_ROOT
###################################################################################

########################################################
# LIST FUNCTIONS IN MODULES
#
#     + analyse_phrase_from_dico()
#
########################################################

table_de_transition = table.table_de_transition

def analyse_phrase_from_dico(dico_phrase_with_tags, langue_analyse, lien_f_analyse_detaillee='') :
    
    # VAR
    i = 0
    etat_courant = 'r_init'

    dico_phrase = dico_phrase_with_tags
    langue = langue_analyse
    longueur = len(dico_phrase_with_tags)
    f_analyse_detaillee = lien_f_analyse_detaillee
    
    ###############
    while (etat_courant != 'etat_final') and (etat_courant != 'etat_erreur') and (i < longueur) :

        #file opening
        if f_analyse_detaillee :
            file_details = codecs.open(f_analyse_detaillee, mode='a', encoding='utf8')

        pos_tree = dico_phrase[i]['pos']
        lemme_tree = dico_phrase[i]['lemme']
        if langue == 'fr' :
            pos_to_use = pos_file.POS_finder_fr(pos_tree , lemme_tree)
        elif langue == 'en' :
            pos_to_use = pos_file.POS_finder_en(pos_tree , lemme_tree)
        
        suivi = "\n\nOn est au mot \'{}\' de pos \'{}\' ".format(dico_phrase[i]['mot_forme'] , str(pos_to_use))
        
        partie_gauche_table = (etat_courant , pos_to_use)

        couple_a_chercher = "\n\tLe couple a chercher est : {}".format(str(partie_gauche_table))
        
        if f_analyse_detaillee :
            file_details.write(str(suivi))
        
            file_details.write(str(couple_a_chercher))
        else : 
            print(str(suivi))
        
            print(str(couple_a_chercher))

        if partie_gauche_table in table_de_transition.keys() :
            
            if f_analyse_detaillee :
                fonction_to_use = table_de_transition[(etat_courant , pos_to_use)][1]
                fonction_to_use(file_details)
            else :
                fonction_to_use = table_de_transition[(etat_courant , pos_to_use)][2]
                fonction_to_use()
                
            etat_courant = table_de_transition[(etat_courant , pos_to_use)][0]
            i += 1

        else :
            etat_courant = 'etat_erreur'
            
        if f_analyse_detaillee :
            file_details.close()
        
    ###############
    if etat_courant != 'etat_erreur' :
        etat_courant = 'etat_final'
        phrase_conclusion = "OUI : Reconnaissance réussie." +\
        "\n\t Je pense que c'est une structure de comparaison."

    else :
        phrase_conclusion = "NON : Reconnaissance non-réussie. " +\
        "\n\tDans l'état actuel de mes connaissances, je ne la considère pas comme une structure de comparaison."

    return phrase_conclusion