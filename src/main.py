#!/usr/bin/env python3
#-*- coding : utf8 -*-

import os
import re
import random
import treetaggerwrapper
import pprint
import io
import codecs
import time

from settings import PROJECT_ROOT
from collections import defaultdict

# import modules.others as others
import modules.big_process as bp

# Lien vers les dossiers de la racine ############################################
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from settings import PROJECT_ROOT, CORPUS_PHRASES, TREETAGGER_ROOT
###################################################################################

# dossier_base_projet = PROJECT_ROOT
# dossier_corpus_litterature = CORPUS_LITTERATURE
# dossier_corpus_professeur = CORPUS_PROFESSEUR

def main():
    print("\nNote de version : ")
    print("\t - v1.0 : pour l'instant, je ne peux faire que des analyses interactives et l'option 2.")
    
    while 1 :
        a = input("\nBonjour, et bienvenue." + \
            "\n Que voulez-vous faire :" +\
            "\n 1 : Une analyse interactive " + \
            "\n 2 : Une analyse sur les phrases de corpus_phrases/phrases_test.txt " + \
            "\n 3 : Une analyse sur corpus " + \
            "\n (enter) - Exit" + \

            "\n\nQuel est votre choix : ")

        #==================================
        if a.strip() == '1' :
            
            b = input("\nEst-ce une phrase en : " + \
            "\n 1 : français " + \
            "\n 2 : anglais " + \
            "\n (enter) - Exit" + \
            "\n -- par défaut : français --" + \

            "\n\nQuel est votre choix : ")
            
            if b.strip() == '2' :
                langue_analyse = 'en'
                print("\n\t Analyse sur de l'anglais.")
            elif b.strip() == '' :
                print("\n-------------------------------------------------------------------")
                print("Peut être voulez-vous changer de mode d'analyse. Retournons au menu.")
                print("-------------------------------------------------------------------\n")
                continue
            else :
                print("\n\t Analyse sur du français.")
                langue_analyse = 'fr'
                
            phrase_a_analyser = (input("\nVeuillez entrer votre phrase : ")).strip().lower()
            print('')
            
            bp.traitement_phrase(phrase_a_analyser , langue_analyse)
            
            break

        #==================================
        elif a.strip() == '2' :
            print("\n-----------------------------------")
            bp.traitement_phrases_dans_texte(CORPUS_PHRASES)

            break
       
        #==================================
        elif a.strip() == '3' :
            print("\n-----------------------------------")
            print("Je ne sais pas encore le faire. Désolé.")
            print("-----------------------------------\n")

            #break

        #==================================
        elif a.strip() == '' :
            print("\n-----------------------------------")
            print("Vous nous quittez déjà ! Au revoir.")
            print("-----------------------------------\n")

            break

        #==================================
        else :
            print("\n---------------------------------------------------------------------")
            print("Désolé, je n'ai pas compris votre instruction. (Retournons au début.)")
            print("-----------------------------------------------------------------------")


if __name__ == '__main__':
    main()
